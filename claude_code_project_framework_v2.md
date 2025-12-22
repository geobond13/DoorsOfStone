# Doors of Stone Fan Fiction: Claude Code Project Framework

## The Context Problem

Claude's context window cannot hold 100,000+ words simultaneously. A novel requires:
- Maintaining voice consistency across 50+ chapters
- Tracking plot threads, foreshadowing, callbacks
- Character development arcs
- Timeline coherence
- Style consistency

**Solution**: Modular architecture with reference documents that get loaded selectively.

---

## Lessons from "The Price of Remembering" GitHub Structure

Their repo (frypatch/The-Price-of-Remembering) has 201+ commits and demonstrates a working approach:

### What They Did Right

1. **Flat chapter structure**: All chapters in `/book/` as individual `.md` files
2. **Automated publishing**: `publish.py` generates EPUB/PDF/HTML/TXT from markdown source
3. **Semantic versioning**: Tags like `v3.12.19` for releases
4. **GitHub Pages hosting**: Live HTML version at frypatch.github.io
5. **Multiple output formats**: Readers can choose EPUB (~400KB), PDF (~800KB), or web
6. **Community-friendly**: Open issues, clear README, invitation for feedback
7. **Archive link**: Web Archive backup for permanence

### What We'll Adopt

1. **Simpler structure** than our original nested approach
2. **Build script** for generating reader-friendly formats
3. **Version tags** after each major milestone
4. **Living changelog** in commits

---

## Project Directory Structure (Revised)

```
/doors-of-stone/
├── README.md                    # Project overview, current status, how to contribute
├── CHANGELOG.md                 # Version history, major changes
├── STYLE_GUIDE.md              # Voice, prose rules, Rothfuss patterns
├── MASTER_OUTLINE.md           # Full plot outline (living document)
├── TIMELINE.md                 # Chronological event tracker
├── FORESHADOWING.md            # Plants and payoffs ledger
│
├── /book/                       # THE ACTUAL MANUSCRIPT (flat structure)
│   ├── 00_Prologue.md
│   ├── 01_Chapter_Title.md
│   ├── 02_Chapter_Title.md
│   ├── ...
│   ├── 60_Chapter_Title.md
│   ├── 61_Epilogue.md
│   ├── Appendix.md              # Theory sources, acknowledgments
│   └── Notes.md                 # Author notes on plot choices
│
├── /reference/                  # SUPPORTING DOCUMENTS (for Claude context loading)
│   ├── characters.md            # All character voices, arcs, current states
│   ├── magic_systems.md         # Sympathy, Naming, Yllish, etc.
│   ├── worldbuilding.md         # Locations, factions, history
│   ├── frame_interludes.md      # Pre-written frame story beats
│   └── theory_integration.md    # Which fan theories we're using and why
│
├── /tools/
│   ├── publish.py               # Generates EPUB/PDF/HTML from /book/
│   ├── word_count.py            # Track progress
│   ├── consistency_check.py     # Find timeline/name contradictions
│   └── voice_drift.py           # Compare passages to style guide
│
├── /output/                     # Generated files (gitignored)
│   ├── The_Doors_of_Stone.epub
│   ├── The_Doors_of_Stone.pdf
│   ├── The_Doors_of_Stone.html
│   └── The_Doors_of_Stone.md    # Single combined file
│
└── /archive/                    # Cut material, old drafts
```

---

## The `publish.py` Script

Based on their approach, here's what the build script should do:

```python
#!/usr/bin/env python3
"""
Combine markdown chapters into publishable formats.
Usage: python publish.py [--epub] [--pdf] [--html] [--all]
"""

import os
import subprocess
from pathlib import Path
from datetime import datetime

BOOK_DIR = Path("book")
OUTPUT_DIR = Path("output")
VERSION = "0.1.0"  # Update with each release

def get_chapters():
    """Return sorted list of chapter files."""
    chapters = sorted(BOOK_DIR.glob("*.md"))
    return chapters

def combine_markdown():
    """Combine all chapters into single markdown file."""
    combined = []
    combined.append(f"# The Doors of Stone\n")
    combined.append(f"## A Kingkiller Chronicle Fan Fiction\n")
    combined.append(f"### Version {VERSION} - {datetime.now().strftime('%Y-%m-%d')}\n\n")
    combined.append("---\n\n")
    
    for chapter in get_chapters():
        content = chapter.read_text()
        combined.append(content)
        combined.append("\n\n---\n\n")
    
    output_path = OUTPUT_DIR / "The_Doors_of_Stone.md"
    output_path.write_text("\n".join(combined))
    print(f"Created: {output_path}")
    return output_path

def generate_epub(md_path):
    """Generate EPUB using pandoc."""
    output = OUTPUT_DIR / "The_Doors_of_Stone.epub"
    subprocess.run([
        "pandoc", str(md_path),
        "-o", str(output),
        "--metadata", f"title=The Doors of Stone",
        "--metadata", "author=Fan Fiction",
        "--toc",
        "--toc-depth=2"
    ])
    print(f"Created: {output}")

def generate_pdf(md_path):
    """Generate PDF using pandoc + LaTeX."""
    output = OUTPUT_DIR / "The_Doors_of_Stone.pdf"
    subprocess.run([
        "pandoc", str(md_path),
        "-o", str(output),
        "--pdf-engine=xelatex",
        "-V", "geometry:margin=1in",
        "--toc"
    ])
    print(f"Created: {output}")

def generate_html(md_path):
    """Generate single-page HTML."""
    output = OUTPUT_DIR / "The_Doors_of_Stone.html"
    subprocess.run([
        "pandoc", str(md_path),
        "-o", str(output),
        "--standalone",
        "--toc",
        "--css=style.css"  # Optional styling
    ])
    print(f"Created: {output}")

def word_count():
    """Count words across all chapters."""
    total = 0
    for chapter in get_chapters():
        content = chapter.read_text()
        words = len(content.split())
        total += words
        print(f"{chapter.name}: {words:,} words")
    print(f"\nTotal: {total:,} words")
    return total

if __name__ == "__main__":
    import sys
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    if "--count" in sys.argv:
        word_count()
    else:
        md_path = combine_markdown()
        if "--epub" in sys.argv or "--all" in sys.argv:
            generate_epub(md_path)
        if "--pdf" in sys.argv or "--all" in sys.argv:
            generate_pdf(md_path)
        if "--html" in sys.argv or "--all" in sys.argv:
            generate_html(md_path)
        if len(sys.argv) == 1:
            print("Usage: python publish.py [--epub] [--pdf] [--html] [--all] [--count]")
```

---

## Chapter File Format (Simplified)

Each chapter file should be self-contained:

```markdown
# Chapter 17: The Beautiful Game

<!-- METADATA (for tooling, not rendered)
POV: Kvothe (past narrative)
Location: Maer's court, Severen
Timeline: Day 2 of return to court
Word Count Target: 4000
-->

BREDON'S FINGERS MOVED across the tak board with the patience of a man who
had learned that the best moves are often the ones your opponent doesn't see
coming...

[Chapter content continues]
```

**Key insight from their approach**: They don't use elaborate metadata systems. The chapters are just markdown. Simplicity wins for a creative project.

---

## Git Workflow

### Commit Convention
```
feat: Add Chapter 23 first draft
fix: Correct timeline inconsistency in Ch 15-17
style: Voice pass on Act 1 chapters
docs: Update FORESHADOWING.md with new plants
refactor: Split Chapter 30 (too long)
```

### Branching Strategy
```
main          <- stable, publishable versions only
├── develop   <- working branch, daily commits
├── act-1     <- feature branch for Act 1 completion
├── act-2     <- feature branch for Act 2
└── revision  <- major revision passes
```

### Version Tags
```bash
git tag -a v0.1.0 -m "Act 1 complete (Chapters 1-15)"
git tag -a v0.2.0 -m "Act 2 complete (Chapters 16-34)"
git tag -a v0.3.0 -m "Act 3 complete (Chapters 35-50)"
git tag -a v1.0.0 -m "First complete draft"
git tag -a v1.1.0 -m "First revision pass"
```

---

## Context Management Strategy (Unchanged but Simplified)

### The "Loading Dock" Approach

Before each writing session, load ONLY what's needed:

**For a new chapter:**
```
Load:
1. STYLE_GUIDE.md (always, ~1500 words)
2. Previous chapter (last 500 words for continuity)
3. Relevant section of characters.md (~500 words)
4. Current chapter outline from MASTER_OUTLINE.md (~200 words)
```

**For revision:**
```
Load:
1. STYLE_GUIDE.md
2. The chapter being revised
3. Specific feedback notes
```

**For continuity check:**
```
Load:
1. TIMELINE.md
2. FORESHADOWING.md
3. Specific chapters being cross-referenced
```

### Document Size Targets
- STYLE_GUIDE.md: ~1,500 words (fits every session)
- characters.md: ~3,000 words (load relevant sections)
- Each chapter: 3,000-5,000 words
- MASTER_OUTLINE.md: ~2,000 words (load relevant act)

---

## Session Workflow (Revised)

### Starting a New Chapter

```bash
# In Claude Code
claude "Load STYLE_GUIDE.md, last 500 words of Chapter 16, 
        Kvothe section of characters.md, 
        Act 2 section of MASTER_OUTLINE.md.
        
        Write Chapter 17: The Beautiful Game.
        
        Key requirements:
        - Bredon reveals his true nature (Amyr, not Cinder)
        - Tak game as metaphor for their conversation
        - End on Kvothe making a decision
        - Target: 4,000 words"
```

### After Each Chapter

```bash
# Update tracking files
echo "Ch 17: Bredon Amyr reveal, tak metaphor" >> CHANGELOG.md
# Add to foreshadowing ledger
echo "| Ch 17 | Bredon's walking stick | Ch 29 | Pending |" >> FORESHADOWING.md
# Commit
git add book/17_The_Beautiful_Game.md
git commit -m "feat: Add Chapter 17 first draft"
```

### After Each Act

```bash
# Run consistency check
python tools/consistency_check.py --act 2

# Generate word count report
python tools/word_count.py

# Tag the milestone
git tag -a v0.2.0 -m "Act 2 complete"

# Generate preview outputs
python tools/publish.py --all

# Push to GitHub for community feedback (optional)
git push origin develop --tags
```

---

## Quality Gates (Revised)

### Before Moving to Next Act

- [ ] All chapters drafted
- [ ] TIMELINE.md updated
- [ ] FORESHADOWING.md current
- [ ] Voice consistency check passed
- [ ] Word count on target (~15-20k per act)
- [ ] No orphaned plot threads
- [ ] Commit and tag

### Before "Complete Draft" (v1.0.0)

- [ ] All 4 acts complete
- [ ] Frame interludes integrated
- [ ] Prologue/Epilogue written
- [ ] Full read-through completed
- [ ] EPUB/PDF generated and tested
- [ ] Appendix and Notes written

---

## Handling the Handoff Problem (Simplified)

When you return to Claude Code after a break:

**Quick Context Restore (same day):**
```
Continuing Doors of Stone fan fiction.
Currently writing Act 2, Chapter 23.
Last scene: Kvothe discovered the Lackless door.
Load: STYLE_GUIDE.md, Chapter 22 ending, Act 2 outline.
Continue.
```

**Deep Context Restore (after days/weeks):**
```
Returning to Doors of Stone fan fiction project.
Load: README.md, MASTER_OUTLINE.md, CHANGELOG.md (last 20 entries).
Summarize current status and what happens next.
```

**The key insight from their 201 commits**: Small, frequent commits with clear messages ARE the memory. You don't need elaborate session notes if your git history tells the story.

---

## GitHub Pages Setup (Optional but Recommended)

Their project hosts a live HTML version. To replicate:

1. Enable GitHub Pages in repo settings
2. Set source to `main` branch, `/output` folder
3. Generate HTML with `python publish.py --html`
4. Readers can access at `yourusername.github.io/doors-of-stone`

This creates a shareable, linkable version for community feedback.

---

## Community Feedback Integration

Their approach: Open issues, invite editing suggestions, credit contributors in Appendix.

**Recommended workflow:**
1. Complete Act 1, push to GitHub
2. Post to r/KingkillerChronicle: "Fan fiction Book 3, Act 1 draft - feedback welcome"
3. Collect issues/suggestions
4. Integrate feedback in revision branch
5. Credit contributors in Appendix.md
6. Repeat for each act

This is how they caught lore errors and improved the work iteratively.

---

## Backup Strategy

```bash
# After each session
git add .
git commit -m "progress: Ch [X] work"

# After each chapter
git push origin develop

# After each act
git tag act-N-complete
git push origin --tags

# Weekly: Export to external backup
python publish.py --all
# Copy /output/ to cloud storage
```

**Their lesson**: 201 commits means they never lost significant work. Commit early, commit often.
