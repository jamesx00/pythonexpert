# PythonExpert

Source code for [pythonexpert.dev](https://www.pythonexpert.dev) — a free,
open-source site for learning to program, one interactive lesson at a time.

## Tech stack

- [Eleventy (11ty)](https://www.11ty.dev/) — static site generator (Nunjucks templates)
- [Tailwind CSS](https://tailwindcss.com/) — styling, terminal-inspired theme
- [Alpine.js](https://alpinejs.dev/) — client-side interactivity
- [Monaco Editor](https://microsoft.github.io/monaco-editor/) — in-browser code editor for exercises
- Code execution via a [Piston](https://github.com/engineer-man/piston)-compatible API

## Project structure

```
src/                  Pages, courses, lessons, blog posts (Eleventy input)
  courses/<course>/   One folder per lesson, numerically prefixed (e.g. 2.3-...)
_includes/            Nunjucks layouts and partials
_data/                 Global data (site metadata, contacts, env)
public/                Static assets copied as-is (css, js, images, fonts)
eleventy.config*.js    Eleventy configuration, collections, drafts, images
builds/                Monaco editor build scripts
```

Each course is defined by a `<course>.11tydata.js` file (`course_id`,
`course_name`, `course_slug`). Lessons are plain Markdown files tagged
`lesson` by that data file; folder name prefixes (e.g. `4.2-...`) control
ordering and grouping into sections via the `sortByDirectoryPrefix` filter.

## Getting started

Requires Node >= 14 (see `.nvmrc` for the version used in development).

```bash
npm install
cp .env.example .env
npm start
```

`npm start` runs the Eleventy dev server, the Tailwind CSS watcher, and the
Monaco editor build in parallel. The site is served at `http://localhost:8080`.

Other useful scripts:

- `npm run build` — production build (Eleventy + Tailwind) into `_site/`
- `npm run serve` — Eleventy dev server only
- `npm run tw:watch` — Tailwind CSS watcher only
- `npm run deploy` — build, sync `_site/` to S3, and invalidate the CloudFront cache

## Keyboard navigation

The site is fully navigable without a mouse:

| Shortcut | Action |
| --- | --- |
| `⌘K` / `Ctrl+K` | Open the command palette (jump to any course, lesson, or blog post) |
| `/` | Also opens the command palette |
| `↑` / `↓` | Move through command palette results |
| `Enter` | Go to the highlighted result |
| `n` | Go to the next lesson |
| `p` | Go to the previous lesson |
| `Ctrl+Enter` (`⌘+Enter` on Mac) | Run code in the exercise editor |
| `?` | Show the keyboard shortcuts help dialog |
| `Esc` | Close the command palette or any open dialog |

Single-key shortcuts (`n`, `p`, `?`, `/`) are automatically disabled while
typing in an input, textarea, or the Monaco code editor.

## License

MIT — see [LICENSE](LICENSE).
