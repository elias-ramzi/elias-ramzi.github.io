# Local development

Notes for future coding agents (and humans) working in this repo. Two
workflows: serving the Jekyll site, and compiling the CV. The repo is used on
two machines whose toolchains differ, so each section says which one it is
about:

|  | macOS (`/Users/elias/...`) | Linux (`/home/eramzi/...`) |
| --- | --- | --- |
| Ruby | system 2.6 + system Jekyll 3.9.3 | 2.7.0 + pinned Gemfile |
| TeX | TeX Live 2023, moderncv 2.3.1 | TeX Live 2019 |
| web-latex-mcp | 0.7.1, `resume` is a local project | 0.4.0 when last noted |

## 1. Serving the website locally

`Gemfile` uses the `github-pages` gem, whose `nokogiri` requires
**Ruby >= 3.0**, so neither machine can `bundle install` the repo's own Gemfile.
Do not "fix" this by editing `Gemfile` — GitHub Pages builds from it and it is
correct for the real build. Both workarounds below build against plain Jekyll
3.9: an approximation of the GitHub Pages stack, good for checking content and
layout, while the authoritative build happens on push. Installing Ruby 3.x
(rbenv/rvm) would remove the need for either.

### macOS: system Jekyll, bundler bypassed

Jekyll 3.9.3 and the plugins `_config.yml` lists are installed as system gems.
Plain `jekyll` finds the repo's Gemfile and crashes in bundler; setting
`JEKYLL_NO_BUNDLER_REQUIRE=true` makes it skip the Gemfile and use the system
gems:

```bash
JEKYLL_NO_BUNDLER_REQUIRE=true jekyll build \
  --config _config.yml,_config.dev.yml -d /path/to/scratchpad/site
JEKYLL_NO_BUNDLER_REQUIRE=true jekyll serve \
  --config _config.yml,_config.dev.yml -d /path/to/scratchpad/site \
  --host 127.0.0.1 --port 4000 --watch
```

### Linux: a separate pinned Gemfile

A Gemfile kept outside the repo (a scratchpad dir is ideal):

```ruby
source "https://rubygems.org"
gem "jekyll", "~> 3.9.5"
gem "jekyll-feed"
gem "jekyll-sitemap"
gem "jekyll-paginate"
gem "jekyll-gist"
gem "jekyll-redirect-from"
gem "kramdown-parser-gfm"
gem "webrick"
```

Prerequisites, already installed there: `ruby-dev` + `build-essential` (need
sudo, which an agent does not have — ask the user); bundler **2.4.22**
specifically (newer requires Ruby >= 3.2),
`gem install --user-install bundler -v 2.4.22`; `~/.gem/ruby/2.7.0/bin` on
`PATH`. Then:

```bash
export PATH="$HOME/.gem/ruby/2.7.0/bin:$PATH"
export BUNDLE_GEMFILE=/path/to/scratchpad/Gemfile
bundle install                     # first time only
bundle exec jekyll serve --config _config.yml,_config.dev.yml \
  -d /path/to/scratchpad/site --host 127.0.0.1 --port 4000 --watch
```

### Either machine

`serve` listens at <http://localhost:4000> and rebuilds on save. Hand that URL
to the user; in VS Code they open it with *Simple Browser: Show*. An agent
cannot open the Simple Browser tab itself.

To verify without serving, `build` and grep the generated HTML — e.g.
`site/publications/index.html` should list every entry in `_publications/`.

## 2. Compiling the CV with web-latex-mcp

The CV source is `.claude/context/resume_elias_ramzi.tex`; the published PDF is
`files/pdf/resume_elias_ramzi.pdf`, embedded by `_pages/cv.md`.

**Check the server version first — the workflow differs.** `server_info()`
reports it, and `list_projects()` shows whether `resume` is registered and how.

### 0.5.0 and later (macOS): a local project

Registered once, persisted in `.web_latex_mcp/registry.json`:

```text
register_project(project="resume", path="<repo>/.claude/context/resume_elias_ramzi.tex")
```

Nothing is cloned: `read_file`, `edit_file`, `compile` act on the real
working-tree file. The loop is edit → `compile(project="resume")` →
`cp .web_latex_mcp/resume.pdf files/pdf/resume_elias_ramzi.pdf` → commit both
with plain `git`.

- Every git tool (`status`, `diff`, `commit`, `push`, `discard`,
  `project_sync`, `reset_to_remote`, `read_file` with a `ref`) **refuses** a
  local project by design. Use `git` in the shell.
- `compile` failures carry `missingPackages` plus an install hint.
- `doctor()` reports the whole toolchain in one call — run it before debugging
  a machine-level failure.
- `render_pages` rasterizes pages (with `clip` for a close-up) and
  `extract_text` returns the typeset text, so an agent *can* see the render —
  use them after every layout change.

### 0.4.0 (Linux, as last noted): the clone-based workflow

Registered with the repo itself as the git remote (`gitUrl=<repo>`,
`rootFile=".claude/context/resume_elias_ramzi.tex"`), the server compiles a
**clone** in `.web_latex_mcp/resume` and only ever sees **committed** state:
edit → `git commit` → `project_sync(project="resume", mode="pull")` → compile.
Skipping the commit or the sync silently compiles the previous version. Never
use the server's `edit_file`/`write_file` there — they write to the clone.
Upgrading to 0.5.0+ and re-registering with `path` removes all of this; delete
the stale clone afterwards.

### The viewer

`viewer(project="resume", target="vscode")` returns a localhost URL for the
pdf.js viewer, which hot-reloads on each compile. The port changes when the
server restarts, so re-run it rather than reusing an old URL. Hand the URL to
the user — an agent cannot open the Simple Browser tab itself.

### Font Awesome icons

The source uses **`fontawesome5`**, loaded by moderncv 2.3's
`moderncviconsawesome.sty` — do **not** add `\usepackage{fontawesome}` (v4).
Loading both makes `fontawesome5` error out with *Incompatible version of Font
Awesome*, and v4 takes over the `\fa…` commands, so moderncv's own
`\faCircle[regular]` bullets print a literal `regular]`. Use Font Awesome 5
names: `\faEnvelope[regular]`, not v4's `\faEnvelopeO`.

Unverified on the Linux box: its TeX Live 2019 moderncv predates fontawesome5
and relied on `fontawesome.sty` (v4), installed by hand under `~/texmf` because
`tlmgr` there points at an unreachable 2019 mirror. If the current source fails
to compile there, prefer upgrading TeX Live over reintroducing v4.

### Header spacing

`\vspace*{-15mm}` right after `\makecvtitle` pulls the contact row up under
the name. It is tuned for moderncv 2.3.1's banking title; the old `-23mm`
(tuned for TeX Live 2019) makes the contact row overlap the name. Re-check with
`render_pages` (clip the top quarter of page 1) after any change.

### Keeping the CV to two pages

It fits on two pages with ~3 spare lines. Test layout changes on a scratch copy
compiled directly with `latexmk` before touching the real file. Levers already
applied: no `\medbreak` between `\item`s, hyperlinked publication titles
instead of printed URLs, `\smallskip` between publication entries, the Sancare
and Balto internships commented out, a one-line engineering-diploma summary.
Levers still available, in order: drop the ITEM (TMLR'24) and HEAT (ICML'23)
entries (pre-approved by the author, buys ~5 lines), then `geometry`
`scale=0.84` -> `0.85` (tested: holds the layout).
