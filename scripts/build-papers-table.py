"""
Utility script to generate `resources/papers.md` from a BibTeX file.

Usage (from the repository root):

    pip install -r requirements.txt
    # Export your Style Survey references to BibTeX, e.g. `resources/papers.bib`
    python scripts/build-papers-table.py resources/papers.bib resources/papers.md

The BibTeX file should contain one entry per referenced work. We extract:
  - title   -> "title" field
  - authors -> "author" field, used as-is
  - year    -> "year" field
  - venue   -> first non-empty of "booktitle", "journal", "publisher"
  - link    -> "url" if present, otherwise a URL built from "doi" if present

The generated Markdown table is then wired up with:
  - tablesort.js for client-side sorting
  - a small JS helper to add sorting + filtering and build a venue bar chart
"""

import sys
from pathlib import Path

import bibtexparser


TABLE_COLUMNS = ["Title", "Authors", "Link", "Year", "Venue"]


def load_entries(bib_path: Path):
  with bibtexparser.open(bib_path) as bib_db:
    return bib_db.entries


def entry_to_row(entry):
  title = entry.get("title", "").replace("\n", " ").strip()
  author = entry.get("author", "").replace("\n", " ").strip()
  year = entry.get("year", "").strip()

  venue = (
    entry.get("booktitle")
    or entry.get("journal")
    or entry.get("publisher")
    or ""
  ).strip()

  url = entry.get("url", "").strip()
  if not url and "doi" in entry:
    doi = entry["doi"].strip()
    if doi:
      url = f"https://doi.org/{doi}"

  link_cell = url if not url else f"[link]({url})"

  # Basic escaping for pipes in Markdown cells.
  def esc(text: str) -> str:
    return text.replace("|", "\\|")

  return [
    esc(title),
    esc(author),
    link_cell,
    esc(year),
    esc(venue),
  ]


def build_markdown(entries):
  lines = []
  lines.append("## Papers and works from the Style Survey\n")
  lines.append(
    "*This page is generated from a BibTeX file. "
    "To update it, edit the BibTeX and re-run "
    "`python scripts/build-papers-table.py`.*\n"
  )
  lines.append(
    "This page lists the references from the Style Survey paper as a "
    "**sortable, searchable table**, and provides simple visualizations "
    "over that list.\n"
  )
  lines.append(
    "To filter the table, start typing in the search box below; click any "
    "column header to sort (uses "
    "[`tablesort`](https://github.com/tristen/tablesort)).\n"
  )
  lines.append(
    '<input\n'
    '  type="search"\n'
    '  placeholder="Filter by title, author, year, venue…"\n'
    '  data-table-filter=""\n'
    '  style="width: 100%; padding: 0.4rem; margin: 0.5rem 0;"\n'
    '/>\n'
  )

  # Table header (Markdown table)
  header = "| " + " | ".join(TABLE_COLUMNS) + " |"
  sep = "| " + " | ".join(["---"] * len(TABLE_COLUMNS)) + " |"
  lines.append(header)
  lines.append(sep)

  # Rows
  for e in entries:
    row = entry_to_row(e)
    lines.append("| " + " | ".join(row) + " |")

  lines.append(
    "\n## Venue distribution\n\n"
    "The bar chart below is computed directly from the **Venue** column "
    "of the table above.\n\n"
    '<div style="width: 100%; max-width: 900px; height: 400px;">\n'
    '  <canvas id="venue-chart"></canvas>\n'
    "</div>\n"
  )

  lines.append(
    '<link rel="stylesheet" href="../assets/tablesort.css">\n\n'
    '<script src="https://unpkg.com/tablesort@5.6.0/dist/tablesort.min.js"></script>\n'
    '<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>\n'
    '<script src="../assets/sort-tables.js"></script>\n'
    '<script src="../assets/papers-visualizations.js"></script>\n'
  )

  return "\n".join(lines) + "\n"


def main(argv=None):
  argv = argv or sys.argv[1:]
  if len(argv) != 2:
    print(
      "Usage: python scripts/build-papers-table.py INPUT_BIB OUTPUT_MD",
      file=sys.stderr,
    )
    raise SystemExit(1)

  bib_path = Path(argv[0])
  out_path = Path(argv[1])

  if not bib_path.is_file():
    print(f"Error: BibTeX file not found at {bib_path}", file=sys.stderr)
    raise SystemExit(1)

  entries = load_entries(bib_path)
  md = build_markdown(entries)
  out_path.write_text(md, encoding="utf-8")
  print(f"Wrote {out_path} with {len(entries)} entries.")


if __name__ == "__main__":
  main()


