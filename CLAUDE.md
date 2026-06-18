# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Personal academic website for Elias Ramzi (AI Research Scientist), served at https://elias-ramzi.github.io via GitHub Pages. It is a Jekyll site built on the [Academic Pages](https://academicpages.github.io/) fork of the Minimal Mistakes theme. Pushing to `main` triggers the GitHub Pages build automatically — there is no separate deploy step.

## Commands

```bash
# Install Ruby dependencies (delete Gemfile.lock first if it errors)
bundle install

# Serve locally at localhost:4000 with live reload (uses hawkins/liveserve)
bundle exec jekyll liveserve

# Plain serve / build
bundle exec jekyll serve
bundle exec jekyll build

# Rebuild minified JS after editing files in assets/js/ (requires npm install)
npm run build:js
```

There is no test suite or linter. Verification = build succeeds and the page renders correctly in the local server.

## Content model

The site is content-driven through Jekyll **collections**, each a top-level `_<collection>/` directory of Markdown files. Collections and their permalinks/defaults are declared in `_config.yml` (`collections:` and `defaults:` blocks):

- `_publications/` — papers. Filenames are date-prefixed (`YYYY-MM-DD-slug.md`).
- `_talks/`, `_teaching/`, `_portfolio/` — same pattern; `_talks` uses the `talk` layout, others use `single`.
- `_posts/` — blog posts. `_pages/` — standalone pages (about, cv, phd, 404, archive pages).

To add a publication/talk, create a new Markdown file in the matching collection directory with the required front matter (`title`, `collection`, `permalink`, `excerpt`, `date`, `venue`, `paperurl`, `citation`). Copy an existing file in that directory as a template — `excerpt` carries the abstract and an inline `<img>` thumbnail. PDFs and other assets go in `files/`; images go in `images/`.

Collection defaults (layout, `author_profile`, `share`, `comments`) are set centrally in `_config.yml`, not per-file — don't repeat them in front matter unless overriding.

## Key configuration & layout

- `_config.yml` — global site config: title, author block, social links, collections, defaults, plugins, `markdown: kramdown` / `highlighter: rouge`. Most site-wide changes happen here. `_config.dev.yml` overrides for local dev.
- `_data/navigation.yml` — top nav menu. `_data/authors.yml`, `_data/ui-text.yml` — author info and UI strings.
- `_layouts/` — page templates (`single`, `talk`, `archive`, `splash`, `default`). `_includes/` — partials composed by layouts. `_sass/` — styles compiled into `assets/css`.
- `_site/` — generated build output; never edit by hand (gitignored output, regenerated on build).

## Generating publication/talk markdown (optional)

`markdown_generator/` contains Python scripts and Jupyter notebooks that bulk-generate collection Markdown files from TSV (`publications.tsv`, `talks.tsv`) or BibTeX:

```bash
cd markdown_generator
python publications.py   # reads publications.tsv -> writes ../_publications/*.md
python talks.py          # reads talks.tsv -> writes ../_talks/*.md
```

`talkmap.py` / `talkmap.ipynb` build the geographic talk map from talk locations.
