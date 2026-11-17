"""Knowledge maps (graphify pieces). Megan, Nov 17: "keep doing /graphify in all chats please" + "and for all agents".
Usage (run from repo root, after: export GRAPHIFY_BACKEND=none GRAPHIFY_NO_CTA=1):
  python3 tools/graphs/graphs.py status            # which pieces have new/changed/deleted docs or code
  python3 tools/graphs/graphs.py todo <piece>      # writes graphs/<piece>/todo.txt + prints the subagent brief
  python3 tools/graphs/graphs.py build <piece|all> # rebuild graph.json + GRAPH_REPORT.md (code part is free)
Python: use graphify's interpreter: $(head -1 $(which graphify) | tr -d '#!')
"""
import sys, json, glob, hashlib, datetime
from pathlib import Path
REPO = Path(__file__).resolve().parents[2]; G = REPO / 'graphs'
PIECES = json.loads((G / 'pieces.json').read_text())
SPEC = REPO / '.claude/skills/graphify/references/extraction-spec.md'

def files(piece, kind):
    out = set()
    for g in PIECES[piece].get(kind, []):
        for p in glob.glob(str(REPO / g), recursive=True):
            pp = Path(p)
            if pp.is_file() and 'node_modules' not in pp.parts and 'graphify-out' not in pp.parts:
                if kind == 'code' and pp.suffix.lower() in ('.md', '.png', '.jpg', '.jpeg', '.json', '.lock', '.svg', '.ico', '.webp'):
                    continue
                out.add(str(pp.relative_to(REPO)))
    return sorted(out)

def sha(rel): return hashlib.sha1((REPO / rel).read_bytes()).hexdigest()
def manifest(piece):
    m = G / piece / 'manifest.json'
    return json.loads(m.read_text()) if m.exists() else {}

def diff(piece):
    m = manifest(piece); cur = {f: sha(f) for f in files(piece, 'docs') + files(piece, 'code')}
    changed = [f for f in cur if m.get(f) != cur[f]]; deleted = [f for f in m if f not in cur]
    return cur, changed, deleted

def rel(sf):
    sf = sf or ''
    return sf.split(str(REPO) + '/', 1)[1] if sf.startswith(str(REPO) + '/') else sf

def status():
    for p in PIECES:
        _, ch, de = diff(p)
        docs = [f for f in ch if f.endswith('.md')]
        print(f"{p}: {len(docs)} docs to re-extract, {len(ch)-len(docs)} code files (free), {len(de)} deleted" + ("" if ch or de else "  ✓ fresh"))
        for f in docs[:15]: print('   ~', f)

def todo(piece):
    _, ch, _ = diff(piece); docs = [f for f in ch if f.endswith('.md')]
    (G / piece / 'todo.txt').write_text('\n'.join(str(REPO / f) for f in docs))
    stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    print(f"{len(docs)} docs. Brief one general-purpose agent per <=25 docs:\n"
          f"  Skill: graphify. Follow the prompt inside the ``` block of {SPEC} exactly. FILE_LIST = paths in {G/piece/'todo.txt'}; "
          f"CHUNK_NUM 1, TOTAL_CHUNKS 1, DEEP_MODE false, CHUNK_PATH = {G/piece/'chunks'/(stamp+'.json')}. Write only that file.\n"
          f"Then: python3 tools/graphs/graphs.py build {piece}")

def build(piece):
    from graphify.extract import extract
    from graphify.build import build_from_json
    from graphify.cluster import cluster, score_all
    from graphify.analyze import god_nodes, surprising_connections, suggest_questions
    from graphify.report import generate
    from graphify.export import to_json
    cur, _, _ = diff(piece)
    live_docs = set(f for f in cur if f.endswith('.md'))
    # newest chunk wins per source file
    owner = {}; chunks = sorted((G / piece / 'chunks').glob('*.json'))
    data = [json.loads(c.read_text()) for c in chunks]
    for i, d in enumerate(data):
        for f, n in (d.get('coverage') or {}).items():
            if n: owner[rel(f)] = i
    nodes, edges, hyper = [], [], []
    for i, d in enumerate(data):
        keep = lambda x: owner.get(rel(x.get('source_file'))) == i and rel(x.get('source_file')) in live_docs
        for n in d.get('nodes', []):
            if keep(n): n['source_file'] = rel(n['source_file']); n.setdefault('_origin', 'semantic'); nodes.append(n)
        for e in d.get('edges', []):
            if keep(e): e['source_file'] = rel(e['source_file']); e.setdefault('_origin', 'semantic'); edges.append(e)
        for h in d.get('hyperedges', []):
            if keep(h): h['source_file'] = rel(h['source_file']); hyper.append(h)
    code = [REPO / f for f in files(piece, 'code')]
    ast = extract(code, cache_root=REPO, root=REPO) if code else {'nodes': [], 'edges': []}
    seen = {n['id'] for n in ast['nodes']}; alln = list(ast['nodes'])
    for n in nodes:
        if n['id'] not in seen: alln.append(n); seen.add(n['id'])
    ext = {'nodes': alln, 'edges': ast['edges'] + edges, 'hyperedges': hyper, 'input_tokens': 0, 'output_tokens': 0}
    Gr = build_from_json(ext, root=str(REPO), directed=False)
    if Gr.number_of_nodes() == 0: print(piece, 'EMPTY, not written'); return
    com = cluster(Gr); coh = score_all(Gr, com)
    labels = {c: Gr.nodes[max(m, key=Gr.degree)].get('label', '')[:40] for c, m in com.items()}
    det = {'files': {'code': [str(p) for p in code], 'document': sorted(live_docs)}, 'total_files': len(cur), 'total_words': 0, 'scan_root': str(REPO)}
    to_json(Gr, com, str(G / piece / 'graph.json'), force=True, community_labels=labels)
    rep = generate(Gr, com, coh, labels, god_nodes(Gr), surprising_connections(Gr, com), det, {'input': 0, 'output': 0}, str(REPO),
                   suggested_questions=suggest_questions(Gr, com, labels))
    (G / piece / 'GRAPH_REPORT.md').write_text(rep)
    missing = sorted(live_docs - set(owner))
    (G / piece / 'manifest.json').write_text(json.dumps({f: h for f, h in cur.items() if f not in missing}, indent=0))
    print(f"{piece}: {Gr.number_of_nodes()} nodes, {Gr.number_of_edges()} edges, {len(com)} clusters" + (f" · {len(missing)} docs not extracted yet (run todo)" if missing else ""))

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    if cmd == 'status': status()
    elif cmd == 'todo': todo(sys.argv[2])
    elif cmd == 'build':
        for p in (PIECES if sys.argv[2] == 'all' else [sys.argv[2]]): build(p)
