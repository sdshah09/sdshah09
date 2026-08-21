#!/usr/bin/env python3
"""Regenerate the generated blocks in README.md.

The chakra chart counts repositories by primary language rather than bytes:
notebook outputs and vendored build files are stored base64, so a byte count
says a Jupyter repo is 58% of the account's code, which is not true of
anything. The quote rotates once a day, chosen by date so the same day always
renders the same line and the workflow stays idempotent.
"""
import datetime, json, os, re, urllib.request

USER = "sdshah09"
START, END = "<!-- chakra:start -->", "<!-- chakra:end -->"
Q_START, Q_END = "<!-- quote:start -->", "<!-- quote:end -->"

QUOTES = [
    ("In the ninja world, those who break the rules are trash. But those who\nabandon their friends are worse than trash.", "Kakashi Hatake"),
    ("A dropout will beat a genius through hard work.", "Rock Lee"),
    ("People's lives don't end when they die. It ends when they lose faith.", "Itachi Uchiha"),
    ("I'm not gonna run away, I never go back on my word.\nThat's my ninja way.", "Naruto Uzumaki"),
    ("The next generation will always surpass the previous one.\nIt's one of the never-ending cycles in life.", "Hiruzen Sarutobi"),
    ("Hard work is worthless for those that don't believe in themselves.", "Naruto Uzumaki"),
    ("A place where someone still thinks about you is a place you can call home.", "Jiraiya"),
    ("How troublesome.", "Shikamaru Nara"),
    ("Knowledge and awareness are vague, and perhaps better called illusions.", "Itachi Uchiha"),
    ("Failing doesn't give you a reason to give up, as long as you believe.", "Naruto Uzumaki"),
]
# Repos whose detected language is an artifact of the build, not the source.
RELABEL = {"Distributed-Message-Broker-CPP": "C++"}


def api(path):
    req = urllib.request.Request(
        f"https://api.github.com/{path}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": USER},
    )
    if os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", f"Bearer {os.environ['GITHUB_TOKEN']}")
    return json.load(urllib.request.urlopen(req, timeout=30))


def collect():
    repos, page = [], 1
    while True:
        batch = api(f"users/{USER}/repos?per_page=100&page={page}")
        repos += batch
        if len(batch) < 100:
            return [r for r in repos if not r["fork"]]
        page += 1


def render(repos):
    counts = {}
    for r in repos:
        lang = RELABEL.get(r["name"], r["language"])
        if lang:
            counts[lang] = counts.get(lang, 0) + 1
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    top = max(c for _, c in ranked)
    width = 34
    rows = [
        f"  {lang:<18}{'█' * max(1, round(c / top * width)):<{width}} {c:>2}"
        for lang, c in ranked
    ]
    return "\n".join(
        [
            "```",
            f"CHAKRA DISTRIBUTION   {len(repos)} repositories, by primary language",
            "",
            *rows,
            "```",
        ]
    )


def quote(today=None):
    today = today or datetime.date.today()
    text, who = QUOTES[today.toordinal() % len(QUOTES)]
    lines = "<br>".join(text.split("\n"))
    return f"<sub><i>&ldquo;{lines}&rdquo;</i><br><br>&mdash; {who}</sub>"


def replace(text, start, end, block):
    return re.sub(
        f"{re.escape(start)}.*?{re.escape(end)}",
        f"{start}\n{block}\n{end}",
        text,
        flags=re.S,
    )


def main():
    readme = open("README.md").read()
    out = replace(readme, START, END, render(collect()))
    out = replace(out, Q_START, Q_END, quote())
    if out != readme:
        open("README.md", "w").write(out)
        print("README blocks updated")
    else:
        print("README blocks unchanged")


if __name__ == "__main__":
    main()
