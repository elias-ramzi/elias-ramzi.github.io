#!/usr/bin/env python3
# coding: utf-8
"""Generate _publications/*.md stubs from an OpenAlex author profile.

Why OpenAlex instead of Google Scholar: Scholar has no API and blocks scrapers.
OpenAlex is a free JSON API with good ML-venue coverage and no key required.

This script is ADDITIVE and SAFE:
  - It never overwrites an existing file in _publications/.
  - It skips any work whose title already matches an existing publication
    (matched on a normalized title, so curated slugs like "roadmap" still match).
  - New papers are written as stubs you then hand-edit (add the image to the
    excerpt, fix the venue/citation, pick the best paper URL).

Usage:
    cd markdown_generator
    python from_openalex.py            # create stubs for any missing papers
    python from_openalex.py --dry-run  # list what would be created, write nothing

Configure AUTHOR_ID below if it ever changes (find it via
https://api.openalex.org/authors?search=Your+Name).
"""

import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request

# --- Configuration -----------------------------------------------------------

AUTHOR_ID = "A5069047479"          # Elias Ramzi on OpenAlex
MAILTO = "elias.ramzi@gmail.com"   # OpenAlex "polite pool" contact (faster, kinder)
OWN_NAME = "Elias Ramzi"           # bolded in the generated citation

# OpenAlex work types to keep. Drop preprints when a published version exists
# (handled by dedup), and ignore things that aren't really publications.
SKIP_TYPES = {"paratext", "erratum", "editorial", "letter", "grant", "dissertation"}

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PUBLICATIONS_DIR = os.path.join(SCRIPT_DIR, "..", "_publications")

# Rank work types so the "best" version of a duplicated title wins dedup.
TYPE_RANK = {
    "article": 3,
    "book-chapter": 3,
    "proceedings-article": 3,
    "dissertation": 2,
    "preprint": 1,
}

html_escape_table = {"&": "&amp;", '"': "&quot;", "'": "&apos;"}


def html_escape(text):
    return "".join(html_escape_table.get(c, c) for c in text)


def normalize_title(title):
    """Lowercase, strip punctuation/whitespace so the same paper matches
    regardless of formatting or a preprint/published title tweak."""
    return re.sub(r"[^a-z0-9]+", " ", (title or "").lower()).strip()


def slugify(title):
    slug = re.sub(r"[^a-z0-9]+", "-", (title or "").lower()).strip("-")
    # Keep slugs short: drop a trailing ":subtitle" and cap word count.
    slug = slug.split("--")[0]
    words = [w for w in slug.split("-") if w]
    return "-".join(words[:8]) or "untitled"


def fetch_works():
    base = "https://api.openalex.org/works"
    params = {
        "filter": f"author.id:{AUTHOR_ID}",
        "per-page": "200",
        "mailto": MAILTO,
    }
    url = base + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=30) as resp:
        data = json.load(resp)
    return data.get("results", [])


def reconstruct_abstract(inverted_index):
    """OpenAlex stores abstracts as an inverted index {word: [positions]}.
    Rebuild the plain text from it."""
    if not inverted_index:
        return ""
    positions = {}
    for word, idxs in inverted_index.items():
        for i in idxs:
            positions[i] = word
    return " ".join(positions[i] for i in sorted(positions))


def author_list(work):
    names = [a.get("author", {}).get("display_name", "")
             for a in work.get("authorships", [])]
    names = [n for n in names if n]
    return ", ".join(f"<b>{n}</b>" if n == OWN_NAME else n for n in names)


def venue_of(work):
    """Return the published venue if OpenAlex has one. Many of these works only
    exist as arXiv preprints in OpenAlex (no conference/journal version recorded
    yet), so fall back to a clear "arXiv preprint" placeholder to edit by hand."""
    # Prefer a real published venue: a location that is not a preprint repository.
    for loc in work.get("locations") or []:
        source = loc.get("source") or {}
        name = source.get("display_name")
        if name and source.get("type") not in ("repository", None):
            return name
    # Otherwise it's only on arXiv/HAL/etc. — flag it for manual review.
    loc = work.get("primary_location") or {}
    source = loc.get("source") or {}
    name = (source.get("display_name") or "").lower()
    if "arxiv" in name or source.get("type") == "repository":
        return "arXiv preprint"
    return source.get("display_name") or ""


def paper_url_of(work):
    oa = work.get("open_access") or {}
    if oa.get("oa_url"):
        return oa["oa_url"]
    loc = work.get("primary_location") or {}
    return loc.get("landing_page_url") or work.get("doi") or ""


def dedup(works):
    """Keep one work per normalized title: the highest-ranked type, breaking
    ties by most recent publication date (the published version)."""
    best = {}
    for w in works:
        if w.get("type") in SKIP_TYPES:
            continue
        key = normalize_title(w.get("title"))
        if not key:
            continue
        rank = (TYPE_RANK.get(w.get("type"), 0), w.get("publication_date") or "")
        if key not in best or rank > best[key][0]:
            best[key] = (rank, w)
    return [w for _, w in best.values()]


def existing_titles():
    titles = set()
    if not os.path.isdir(PUBLICATIONS_DIR):
        return titles
    for fname in os.listdir(PUBLICATIONS_DIR):
        if not fname.endswith(".md"):
            continue
        with open(os.path.join(PUBLICATIONS_DIR, fname), encoding="utf-8") as f:
            for line in f:
                m = re.match(r'\s*title:\s*"?(.+?)"?\s*$', line)
                if m:
                    titles.add(normalize_title(m.group(1)))
                    break
    return titles


def build_markdown(work):
    title = (work.get("title") or "").strip()
    date = work.get("publication_date") or f"{work.get('publication_year', '1900')}-01-01"
    slug = slugify(title)
    html_filename = f"{date}-{slug}"
    venue = venue_of(work)
    paper_url = paper_url_of(work)
    abstract = reconstruct_abstract(work.get("abstract_inverted_index"))
    authors = author_list(work)
    year = date[:4]

    citation = f"{authors}: {title}."
    if venue:
        citation += f" {venue}"
    citation += f" ({year})."

    md = f'---\ntitle: "{title}"\n'
    md += "collection: publications\n"
    md += f"permalink: /publication/{html_filename}\n"
    if len(abstract) > 5:
        # TODO add a thumbnail: append <br/><img src='/images/your-figure.png'>
        md += f"excerpt: \"{html_escape(abstract)}\"\n"
    md += f"date: {date}\n"
    md += f"venue: '{html_escape(venue)}'\n"
    if len(paper_url) > 5:
        md += f"paperurl: '{paper_url}'\n"
    md += f"citation: '{html_escape(citation)}'\n"
    md += "---"

    return f"{html_filename}.md", md


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true",
                        help="list new papers without writing files")
    args = parser.parse_args()

    works = dedup(fetch_works())
    have = existing_titles()

    created, skipped = [], []
    for work in sorted(works, key=lambda w: w.get("publication_date") or ""):
        if normalize_title(work.get("title")) in have:
            skipped.append(work.get("title"))
            continue
        fname, md = build_markdown(work)
        path = os.path.join(PUBLICATIONS_DIR, fname)
        if os.path.exists(path):
            skipped.append(work.get("title"))
            continue
        created.append(fname)
        if args.dry_run:
            print(f"[dry-run] would create {fname}")
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(md)
            print(f"created {fname}")

    print(f"\n{len(created)} new, {len(skipped)} already present (skipped).")
    if created and not args.dry_run:
        print("Review the new stubs: add a thumbnail image to the excerpt and "
              "check the venue/citation before committing.")


if __name__ == "__main__":
    sys.exit(main())
