# Local development

Notes for future coding agents (and humans) working in this repo on the machine
it was set up on. Two workflows: serving the Jekyll site, and compiling the CV.

## 1. Serving the website locally

### The problem with the repo's Gemfile

`Gemfile` uses the `github-pages` gem, which pulls a `nokogiri` requiring
**Ruby >= 3.0**. The system Ruby here is **2.7.0**, so `bundle install` against
the repo's own Gemfile fails to resolve. Do not "fix" this by editing `Gemfile` —
GitHub Pages builds from it and it is correct for the real build.

### The workaround: a separate pinned Gemfile

Build against plain Jekyll 3.9 with the plugins `_config.yml` lists, using a
Gemfile kept outside the repo (a scratchpad dir is ideal):

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

Prerequisites, already installed on this machine:

- `ruby-dev` + `build-essential` (needed for native extensions; installing them
  requires sudo, which an agent does not have — ask the user)
- bundler **2.4.22** specifically: newer bundler requires Ruby >= 3.2.
  `gem install --user-install bundler -v 2.4.22`
- `~/.gem/ruby/2.7.0/bin` on `PATH`

Then:

```bash
export PATH="$HOME/.gem/ruby/2.7.0/bin:$PATH"
export BUNDLE_GEMFILE=/path/to/scratchpad/Gemfile
bundle install                     # first time only
bundle exec jekyll serve --config _config.yml,_config.dev.yml \
  -d /path/to/scratchpad/site --host 127.0.0.1 --port 4000 --watch
```

Serves at <http://localhost:4000> and rebuilds on save. Hand that URL to the
user; in VS Code they open it with *Simple Browser: Show*. An agent cannot open
the Simple Browser tab itself.

Note this is an approximation of the GitHub Pages stack, not the identical gem
set — good for checking content and layout, but the authoritative build happens
on push. Installing Ruby 3.x (rbenv/rvm) would remove the need for all of this.

Verify a build without serving:

```bash
bundle exec jekyll build -d /path/to/scratchpad/site
```

Then grep the generated HTML — e.g. `site/publications/index.html` should list
every entry in `_publications/`.

## 2. Compiling the CV with web-latex-mcp

The CV source is `.claude/context/resume_elias_ramzi.tex`; the published PDF is
`files/pdf/resume_elias_ramzi.pdf`, embedded by `_pages/cv.md`.

### One-time registration

The MCP server is registered with project id **`resume`**, pointing at this repo
as its git remote with `rootFile: .claude/context/resume_elias_ramzi.tex`:

```
register_project(project="resume", gitUrl="/home/eramzi/workspace/elias-ramzi.github.io",
                 rootFile=".claude/context/resume_elias_ramzi.tex")
```

### The important gotcha

The server works from a **clone** in `.web_latex_mcp/resume`, not from the
working tree. It therefore only ever sees **committed** state. The loop is:

1. edit `.claude/context/resume_elias_ramzi.tex` in the working tree
2. `git commit`
3. `project_sync(project="resume", mode="pull")`
4. `compile(project="resume")`
5. `cp .web_latex_mcp/resume.pdf files/pdf/resume_elias_ramzi.pdf` and commit

Skipping step 2 or 3 silently compiles the previous version. If a rebase or
amend rewrites history, the clone diverges — `rm -rf .web_latex_mcp/resume` and
`project_sync(mode="clone")`.

`viewer(project="resume", target="vscode")` returns a localhost URL for the
pdf.js viewer, which hot-reloads on each compile. The port changes when the
server restarts, so re-run it rather than reusing an old URL.

### fontawesome

The document needs `fontawesome.sty`, which is not in this machine's TeX Live
2019 and cannot be installed with `tlmgr`: system-wide needs sudo, and
`tlmgr --usermode` fails because the configured repository (a 2019 historic
mirror) is unreachable. It is already installed by hand under `~/texmf` in TDS
layout — `.sty`/`.tex`/`.fd` in `tex/latex/fontawesome/`, fonts under
`fonts/{tfm,type1,opentype}/public/fontawesome/`, `fonts/enc/dvips/fontawesome/`,
`fonts/map/dvips/fontawesome/` — followed by `mktexlsr ~/texmf` and
`updmap-user --enable Map=fontawesome.map`. Repeat that recipe for any other
missing package.

### Keeping the CV to two pages

It currently fits on two pages with only ~2 spare lines. `pdftoppm`/`pdftotext`
are not installed, so an agent cannot see the render — but page count is in the
compile result, and a scratch copy can be compiled directly with `latexmk` to
test layout changes before touching the real file. Levers already applied: no
`\medbreak` between `\item`s, hyperlinked publication titles instead of printed
URLs, `\smallskip` between publication entries. Levers still available, in
order: drop the ITEM (TMLR'24) and HEAT (ICML'23) entries (pre-approved by the
author, buys ~5 lines), then `geometry` `scale=0.84` -> `0.85`.
