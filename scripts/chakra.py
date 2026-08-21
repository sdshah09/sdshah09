#!/usr/bin/env python3
"""Regenerate the chakra block in README.md from live GitHub data.

Counts repositories by primary language rather than bytes: notebook outputs and
vendored build files are stored base64, so a byte count says a Jupyter repo is
58% of the account's code, which is not true of anything.
"""
import json, os, re, urllib.request

USER = "sdshah09"
START, END = "<!-- chakra:start -->", "<!-- chakra:end -->"
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


def main():
    block = render(collect())
    readme = open("README.md").read()
    out = re.sub(
        f"{re.escape(START)}.*?{re.escape(END)}",
        f"{START}\n{block}\n{END}",
        readme,
        flags=re.S,
    )
    if out != readme:
        open("README.md", "w").write(out)
        print("chakra block updated")
    else:
        print("chakra block unchanged")


if __name__ == "__main__":
    main()
