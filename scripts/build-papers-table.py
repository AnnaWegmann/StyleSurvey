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

The generated Markdown table is then wired up with tablesort.js for
client-side sorting and a small JS helper to add sorting + filtering.
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
  abstract = entry.get("abstract", "PLACEHOLDER").replace("\n", " ").strip() or "PLACEHOLDER"
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

  # For HTML tables we prefer explicit anchors when a URL is present.
  if url:
    link_cell = f'<a href="{url}">link</a>'
  else:
    link_cell = ""

  # Basic escaping for pipes in Markdown cells.
  def esc(text: str) -> str:
    return text.replace("|", "\\|")

  return [
    esc(title),
    esc(abstract),
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
    "**sortable, searchable table**.\n"
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
    '  data-table-filter="#papers-table"\n'
    '  style="width: 100%; padding: 0.4rem; margin: 0.5rem 0;"\n'
    '/>\n'
  )

  # HTML table so that sorting and filtering can reliably target it.
  lines.append('<table id="papers-table">\n')
  lines.append("  <thead>")
  lines.append("    <tr>")
  for col in TABLE_COLUMNS:
    lines.append(f"      <th>{col}</th>")
  lines.append("    </tr>")
  lines.append("  </thead>")
  lines.append("  <tbody>")

  for e in entries:
    title, abstract, authors, link_cell, year, venue = entry_to_row(e)
    lines.append("    <tr>")
    lines.append(f'      <td><span class="has-tooltip"><em>{title}</em><span class="tooltip">{abstract}</span></span></td>')
    lines.append(f"      <td>{authors}</td>")
    lines.append(f"      <td>{link_cell}</td>")
    lines.append(f"      <td>{year}</td>")
    lines.append(f"      <td>{venue}</td>")
    lines.append("    </tr>")

  lines.append("  </tbody>")
  lines.append("</table>\n")

  lines.append(
    '<link rel="stylesheet" href="../assets/tablesort.css">\n\n'
    '<script src="https://unpkg.com/tablesort@5.6.0/dist/tablesort.min.js"></script>\n'
    '<script src="../assets/sort-tables.js"></script>\n'
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


