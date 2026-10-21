"""Find open class-action settlements you can claim without proof of purchase.

The agent searches the web for currently open "no proof required" settlements,
checks each one against your profile, and writes a report with the claim link,
deadline and estimated payout. It never files claims: you review each match and
file only the ones that are true for you (claims are signed under penalty of perjury).

Usage:
    pip install -r requirements.txt
    export ANTHROPIC_API_KEY=...
    python find_settlements.py profile.json [-o report.md]
"""

import argparse
import datetime
import json
import sys

import anthropic

MODEL = "claude-opus-5-5"
MAX_CONTINUATIONS = 8

SYSTEM = """You research open U.S. class-action settlements for one person.

Goal: find settlements that are (1) still accepting claims today, (2) do NOT require proof of purchase \
or documentation for at least one payout tier, and (3) the person plausibly qualifies for based on their profile.

How to work:
- Search settlement aggregators (topclassactions.com, classaction.org, openclassactions.com, claimdepot.com) \
for "no proof" / "no receipt required" settlements, then confirm each on the official settlement administrator \
site (the URL the court notice names). Ignore listings you cannot confirm.
- Check the claim deadline against today's date. Drop anything past its deadline.
- Match against the profile strictly. A settlement qualifies only if something in the profile puts the person \
in the class (bought the product, used the service, lived in the state, got the breach notice) during the class period. \
If the class period or state limits make it uncertain, list it under "Possible - check eligibility", never as a match.
- Never suggest claiming for a product or service the profile does not mention. Never suggest guessing or \
inventing purchases. Note that claim forms are signed under penalty of perjury.
- Watch for scams: real settlements never charge a fee to file. Flag any site asking for payment or a bank login.

Output a Markdown report:
1. "Strong matches" table: Settlement | Why you qualify (cite the profile item) | No-proof payout | Deadline | Official claim URL
2. "Possible - check eligibility" table with the same columns plus what to check.
3. "Proof required but you may have it" (short list, only if relevant to the profile).
4. A one-line total estimated no-proof payout range (payouts are usually pro rata and often lower than listed).
Sort each table by deadline, soonest first."""


def run(profile: dict) -> str:
    client = anthropic.Anthropic()
    today = datetime.date.today().isoformat()
    messages = [
        {
            "role": "user",
            "content": f"Today is {today}. My profile:\n```json\n{json.dumps(profile, indent=2)}\n```\n"
            "Find open no-proof settlements I qualify for.",
        }
    ]
    tools = [
        {"type": "web_search_20260209", "name": "web_search", "max_uses": 40},
        {"type": "web_fetch_20260209", "name": "web_fetch", "max_uses": 40},
    ]

    for _ in range(MAX_CONTINUATIONS):
        with client.beta.messages.stream(
            model=MODEL,
            max_tokens=64000,
            system=SYSTEM,
            tools=tools,
            messages=messages,
            thinking={"type": "adaptive"},
            output_config={"effort": "high"},
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
        ) as stream:
            for event in stream:
                if event.type == "content_block_start" and event.content_block.type == "server_tool_use":
                    print(f"  ... {event.content_block.name}", file=sys.stderr)
            response = stream.get_final_message()

        if response.stop_reason == "pause_turn":
            # Long server-tool turn; send it back so the model resumes where it stopped.
            messages.append({"role": "assistant", "content": response.content})
            continue
        if response.stop_reason == "refusal":
            raise RuntimeError(f"Request declined: {response.stop_details}")
        return "".join(b.text for b in response.content if b.type == "text")

    raise RuntimeError("Gave up: research still paused after max continuations")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("profile", help="path to your profile JSON (see profile.example.json)")
    parser.add_argument("-o", "--output", default="settlements-report.md")
    args = parser.parse_args()

    with open(args.profile) as f:
        profile = json.load(f)
    print("Searching for open no-proof settlements...", file=sys.stderr)
    report = run(profile)
    header = f"# Open No-Proof Settlements - {datetime.date.today().isoformat()}\n\n"
    with open(args.output, "w") as f:
        f.write(header + report + "\n")
    print(f"Wrote {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
