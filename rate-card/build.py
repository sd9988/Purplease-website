"""Rebuild index.html from the rate card spreadsheet.

Usage: python3 build.py path/to/Resource_Rate_Card_by_Tech_Stack.xlsx
Only the two outside-India sheets are read (remote and onsite). Indian rates, costs, margins
and stack premiums stay out of the page.
"""
import json
import shutil
import sys
from pathlib import Path

import openpyxl

SHEETS = {
    "remote": ("Overseas – USD per hr", 1),
    "onsite": ("Onshore – USD per hr", 1),
}
STANDALONE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Purplease rates by tech stack and experience, with a team cost calculator for weekly, monthly and project pricing.">
<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
__BODY__
</body>
</html>
"""
SKIP = ("Category", "Notes", "•", "RATE", "Hourly", "Monthly")


def read_sheet(ws, step):
    rows = []
    for r in ws.iter_rows(values_only=True):
        if isinstance(r[0], str) and r[1] and not r[0].startswith(SKIP):
            vals = [r[2 + i * step] for i in range(5)]
            rows.append((r[0], r[1], [None if v in ("N/A", None) else v for v in vals]))
    return rows


def main(xlsx):
    wb = openpyxl.load_workbook(xlsx, data_only=True)
    sheets = {k: read_sheet(wb[name], step) for k, (name, step) in SHEETS.items()}
    stacks = [[c, s] for c, s, _ in sheets["remote"]]
    for k, rows in sheets.items():
        if [[c, s] for c, s, _ in rows] != stacks:
            sys.exit(f"Sheet {SHEETS[k][0]} lists different roles from the overseas sheet")
    data = {"stacks": stacks, **{k: [v for _, _, v in rows] for k, rows in sheets.items()}}
    here = Path(__file__).parent
    html = (here / "template.html").read_text().replace("__DATA__", json.dumps(data, separators=(",", ":")))
    (here / "index.html").write_text(html)
    # Standalone copy for uploading to the web host (e.g. public_html/rate-card/ on Hostinger).
    dist = here / "dist" / "rate-card"
    dist.mkdir(parents=True, exist_ok=True)
    (dist / "index.html").write_text(STANDALONE.replace("__BODY__", html))
    shutil.copy(here / "team-engineers.jpg", dist / "team-engineers.jpg")
    print(f"Wrote index.html and dist/rate-card/ with {len(stacks)} roles")


if __name__ == "__main__":
    main(sys.argv[1])
