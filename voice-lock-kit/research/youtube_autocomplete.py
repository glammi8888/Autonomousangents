#!/usr/bin/env python3
"""Pull YouTube search autocomplete suggestions for a seed keyword.

Runs the "alphabet soup" method: the seed alone, then seed + a..z, plus
question prefixes (how to / why / best ...). Output is a deduplicated,
frequency-ranked list you can paste straight into Claude.

Usage:
    python3 youtube_autocomplete.py "content creator"
    python3 youtube_autocomplete.py "repurpose content" --csv out.csv

Needs network access to suggestqueries.google.com (no API key).
"""
import argparse
import csv
import json
import string
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter

ENDPOINT = "https://suggestqueries.google.com/complete/search"
PREFIXES = ["how to", "why", "best", "what is", "how do i", "is it worth", "tips"]


def suggest(query):
    params = urllib.parse.urlencode({"client": "firefox", "ds": "yt", "q": query})
    req = urllib.request.Request(f"{ENDPOINT}?{params}", headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8", "replace"))[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("seed")
    ap.add_argument("--csv", help="also write results to this CSV file")
    ap.add_argument("--delay", type=float, default=0.3, help="seconds between requests")
    args = ap.parse_args()

    queries = [args.seed]
    queries += [f"{args.seed} {c}" for c in string.ascii_lowercase]
    queries += [f"{p} {args.seed}" for p in PREFIXES]

    counts = Counter()
    for q in queries:
        try:
            counts.update(suggest(q))
        except Exception as e:  # keep going if one query fails
            print(f"! {q}: {e}", file=sys.stderr)
        time.sleep(args.delay)

    ranked = counts.most_common()
    for phrase, n in ranked:
        print(f"{n}\t{phrase}")

    if args.csv:
        with open(args.csv, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["phrase", "times_suggested"])
            w.writerows(ranked)
    print(f"\n{len(ranked)} unique suggestions from {len(queries)} queries", file=sys.stderr)


if __name__ == "__main__":
    main()
