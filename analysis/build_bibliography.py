"""Build bibliography.bib from the paper-cards under analysis/papers/.

Each card file has multiple ## sections; each section has a YAML frontmatter
block followed by markdown. We extract:
  - id (from YAML)
  - year (from YAML)
  - Citation (the line beneath '**Citation.**')
  - DOI/URL (the line beneath '**DOI / URL.**')
and emit a BibTeX entry.

Best-effort parser: handles the format used in our paper-cards.
"""

from __future__ import annotations
import re
from pathlib import Path

PAPERS_DIR = Path(__file__).resolve().parent / "papers"
OUT = Path(__file__).resolve().parent.parent / "bibliography.bib"

CARD_HEADER_RE = re.compile(r"^##\s+([A-H]\d+)\s*[—-]\s*(.+?)\s*$", re.MULTILINE)
YAML_RE = re.compile(r"^```yaml\n(.*?)\n```", re.MULTILINE | re.DOTALL)
CITATION_RE = re.compile(r"\*\*Citation\.\*\*\s*(.+?)(?=\n\n|\n\*\*)", re.DOTALL)
DOI_RE = re.compile(r"\*\*DOI\s*/\s*URL\.\*\*\s*(.+?)(?=\n\n|\n\*\*)", re.DOTALL)


def parse_yaml_block(s: str) -> dict:
    out = {}
    for line in s.strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def parse_authors_year(citation: str) -> tuple[str, str, str]:
    """From a citation like 'Author, A. B., & Other, C. D. (2024). Title…',
    return (first_author_last, year, suffix). Best-effort."""
    m = re.match(r"\s*([\wÀ-ſ‘’\-]+)", citation)
    first = m.group(1) if m else "Anon"
    ymatch = re.search(r"\(\s*(\d{4})[a-z]?\s*[a-z]?\)", citation)
    year = ymatch.group(1) if ymatch else "n.d."
    return first, year, ""


def card_to_bib(card_id: str, yaml: dict, citation: str, doi_url: str) -> str:
    first, year, _ = parse_authors_year(citation)
    bib_id = f"{first}{year}_{card_id}"
    bib_id = re.sub(r"[^\w]", "_", bib_id)
    # Try to get a title from "Title." pattern in citation, else fall back
    tmatch = re.search(r"\)\s*\.?\s*([^.]+?)\.", citation)
    title = tmatch.group(1).strip() if tmatch else citation[:80]
    # Collapse whitespace
    title = re.sub(r"\s+", " ", title)
    citation_clean = re.sub(r"\s+", " ", citation.strip())
    doi_clean = re.sub(r"\s+", " ", (doi_url or "").strip())
    fields = []
    fields.append(f"  author = {{{citation_clean.split('(')[0].strip().rstrip(',').rstrip('.')}}}")
    fields.append(f"  year = {{{year}}}")
    fields.append(f"  title = {{{title}}}")
    if doi_clean:
        if "doi.org" in doi_clean:
            fields.append(f"  doi = {{{doi_clean.replace('https://doi.org/', '').strip().rstrip('.')}}}")
        elif doi_clean.startswith("http"):
            fields.append(f"  url = {{{doi_clean.split()[0].rstrip('.')}}}")
    fields.append(f"  note = {{{citation_clean[:300]}}}")
    fields.append(f"  keywords = {{{yaml.get('tags', '')}}}")
    body = ",\n".join(fields)
    return f"@misc{{{bib_id},\n{body}\n}}\n"


def main():
    entries = []
    for fp in sorted(PAPERS_DIR.glob("*.md")):
        if fp.name.startswith("_"):
            continue
        text = fp.read_text(encoding="utf-8")
        # split on '## A1 — ...' style headers
        sections = re.split(r"\n(?=##\s+[A-H]\d+\s*[—-])", text)
        for sec in sections:
            mh = CARD_HEADER_RE.search(sec)
            if not mh:
                continue
            card_id = mh.group(1)
            ym = YAML_RE.search(sec)
            yaml = parse_yaml_block(ym.group(1)) if ym else {}
            cm = CITATION_RE.search(sec)
            citation = cm.group(1).strip() if cm else f"Card {card_id}"
            dm = DOI_RE.search(sec)
            doi = dm.group(1).strip() if dm else ""
            entries.append(card_to_bib(card_id, yaml, citation, doi))
    OUT.write_text(
        "% bibliography.bib — auto-generated from analysis/papers/*.md\n"
        "% Re-run: python analysis/build_bibliography.py\n\n"
        + "\n".join(entries),
        encoding="utf-8",
    )
    print(f"Wrote {len(entries)} entries to {OUT}")


if __name__ == "__main__":
    main()
