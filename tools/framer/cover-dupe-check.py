#!/usr/bin/env python3
"""Flag ISSUE11 covers that reuse the same photo (Megan, Nov 19: keep every cover image unique).
Usage: python3 tools/framer/cover-dupe-check.py [new-cover.jpg]
Compares every drafts/issue11-blog/images/cover-*.jpg (skipping old *-v1 files that are no longer live)
with a small grayscale fingerprint of the center. Also look at a contact sheet: different crops of the
same photo can slip past the fingerprint."""
import glob, itertools, subprocess, sys, os
D = 'drafts/issue11-blog/images/'
SKIP = {'cover-gratitude-journal-prompts.jpg'}  # replaced by -v2, not live
def fp(f):
    out = subprocess.run(['convert', f, '-resize', '1600x1067!', '-crop', '1200x800+300+200', '+repage',
                          '-resize', '16x10!', '-colorspace', 'Gray', '-depth', '8', 'gray:-'],
                         capture_output=True).stdout
    return list(out)
files = [f for f in sorted(glob.glob(D + 'cover-*.jpg')) if os.path.basename(f) not in SKIP]
# a -v2 file replaces the file without the suffix
files = [f for f in files if not os.path.exists(f.replace('.jpg', '-v2.jpg'))]
files += sys.argv[1:]
sig = {f: fp(f) for f in files}
bad = 0
for a, b in itertools.combinations(files, 2):
    d = sum(abs(x - y) for x, y in zip(sig[a], sig[b])) / len(sig[a])
    if d < 25:
        bad += 1
        print(f'POSSIBLE REPEAT ({d:.1f}): {os.path.basename(a)} <-> {os.path.basename(b)}')
print('checked', len(files), 'covers,', bad, 'possible repeats')
