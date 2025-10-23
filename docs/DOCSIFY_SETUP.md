# Docsify Documentation Setup Guide

## Overview

Incident Zero now uses **Docsify** to generate a beautiful, searchable documentation site from markdown files. The site is served directly from the root directory and covers all game modules, rules, and card documentation.

## File Structure

```
incident-zero/
├── index.html          # Docsify entry point (root)
├── _sidebar.md         # Navigation structure
├── _coverpage.md       # Landing page
├── .nojekyll           # Disable Jekyll on GitHub Pages
├── README.md           # Homepage content
│
├── docs/               # Documentation folder
│   ├── FRAMEWORK.md
│   ├── gameplay-modes.md
│   ├── module-combinations.md
│   ├── rules/          # Module rules files
│   └── standalone-games/
│
└── cards/              # Card documentation
    ├── README.md
    ├── CARD_REFERENCE.md
    ├── hardening/
    ├── incident-response/
    ├── network-building/
    ├── disaster-recovery/
    └── audit-compliance/
```

## Deployment to GitHub Pages

### Option 1: Deploy from Root (Recommended)

1. Go to your GitHub repository settings
2. Navigate to **Settings → Pages**
3. Under "Build and deployment":
   - Source: `Deploy from a branch`
   - Branch: `main` (or your default branch)
   - Folder: `/ (root)`
4. Click "Save"

GitHub Pages will now serve `index.html` from the root directory.

### Option 2: Deploy from Docs Folder (Alternative)

If you prefer to keep deployment files in a dedicated folder:

1. Create a `docs/` folder at the root (if not already present)
2. Move `index.html`, `_sidebar.md`, `_coverpage.md`, `.nojekyll` into `docs/`
3. Update GitHub Pages settings to serve from `/docs`
4. Update `basePath` in `index.html` back to `/incident-zero/` (if repo is at that path)

## Local Testing

### Using Python (built-in)

```bash
# Python 3.x
python -m http.server 3000

# Python 2.x
python -m SimpleHTTPServer 3000
```

Then visit: `http://localhost:3000`

### Using Node.js

```bash
# Install docsify CLI globally
npm install -g docsify-cli

# Serve from current directory
docsify serve .
```

Then visit: `http://localhost:3000`

### Using Docker

```bash
docker run -p 3000:3000 \
  --volume $(pwd):/docs \
  docsify/docsify:latest
```

Then visit: `http://localhost:3000`

## Configuration Details

### index.html Settings

- **basePath:** `/` (serves from root)
- **homepage:** `README.md` (content when visiting root)
- **coverpage:** `true` (shows `_coverpage.md` as landing page)
- **loadSidebar:** `true` (loads `_sidebar.md` for navigation)
- **search:** Enabled with custom placeholder
- **plugins:** Emoji, copy-to-clipboard, search

### _sidebar.md Structure

Organized hierarchically:
1. **Overview** - Getting started and framework
2. **Core Rules** - Base game mechanics
3. **Module Rules** - Rules for each of the 5 modules
4. **Standalone Games** - How to play each module independently
5. **Card Decks** - Complete card documentation organized by module

## Sidebar Navigation

The `_sidebar.md` file provides hierarchical navigation:

```markdown
- **Section Title**
  - [Link Name](path/to/file.md)
  - [Subsection](path/to/file.md)
    - [Sub-item](path/to/file.md)
```

Current structure includes:
- All module rules (5 files)
- All standalone game guides (5 files)
- All card documentation (19 files + overview files)

## Search Functionality

The search feature in docsify will index:
- All markdown files referenced in `_sidebar.md`
- Headings and subheadings
- Code blocks and inline content

Search is performed client-side, so no backend is required.

## Styling

Custom CSS in `index.html` includes:
- Purple gradient sidebar (#667eea → #764ba2)
- Themed headings and code blocks
- Table styling with hover effects
- Blockquote and callout styling

## Troubleshooting

### Pages not appearing in search
- Ensure files are linked in `_sidebar.md`
- Check file paths are relative to root
- Rebuild search index (cache is 24 hours)

### 404 errors for card files
- Verify card file paths in `_sidebar.md` match actual file locations
- Check that all folder paths exist (especially `cards/*/core-deck/` and `cards/*/expansion-deck/`)

### Sidebar not loading
- Ensure `_sidebar.md` exists in root directory
- Check that `loadSidebar: true` is set in `index.html`
- Verify markdown syntax is valid

### GitHub Pages not updating
- Wait a few minutes for GitHub to rebuild pages
- Check GitHub Pages settings show "Your site is published"
- Force browser cache clear (Ctrl+F5 or Cmd+Shift+R)

## Next Steps

1. ✅ Docsify configured at root
2. ✅ Sidebar navigation created
3. ✅ Cover page designed
4. ⏳ Deploy to GitHub Pages (configure in repo settings)
5. ⏳ Test on GitHub Pages URL
6. ⏳ Customize styling if desired
7. ⏳ Add analytics (optional)

## Additional Resources

- [Docsify Documentation](https://docsify.js.org/)
- [GitHub Pages Help](https://docs.github.com/en/pages)
- [Markdown Guide](https://www.markdownguide.org/)

---

*Last Updated: October 2025*
