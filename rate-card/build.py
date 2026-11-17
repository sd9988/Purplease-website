"""Rebuild index.html from the rate card spreadsheet.

Usage: python3 build.py path/to/Resource_Rate_Card_by_Tech_Stack.xlsx
Only the four client-facing sheets are read; costs, margins and stack premiums stay out of the page.
"""
import json
import sys
from pathlib import Path

import openpyxl

SHEETS = {
    "indiaUsdHr": ("Indian – USD per hr", 2),
    "indiaInrMonth": ("Indian – INR per month", 2),
    "overseasUsdHr": ("Overseas – USD per hr", 1),
    "onshoreUsdHr": ("Onshore – USD per hr", 1),
}
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
    stacks = [[c, s] for c, s, _ in sheets["overseasUsdHr"]]
    for k, rows in sheets.items():
        if [[c, s] for c, s, _ in rows] != stacks:
            sys.exit(f"Sheet {SHEETS[k][0]} lists different roles from the overseas sheet")
    data = {"stacks": stacks, **{k: [v for _, _, v in rows] for k, rows in sheets.items()}}
    here = Path(__file__).parent
    html = (here / "template.html").read_text().replace("__DATA__", json.dumps(data, separators=(",", ":")))
    (here / "index.html").write_text(html)
    print(f"Wrote index.html with {len(stacks)} roles")


if __name__ == "__main__":
    main(sys.argv[1])
