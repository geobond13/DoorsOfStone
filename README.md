# The Doors of Stone
## A Kingkiller Chronicle Fan Fiction

This is a fan-written completion of Patrick Rothfuss's Kingkiller Chronicle trilogy. This project is not affiliated with Patrick Rothfuss or his publishers.

### Project Status

**Current Version**: v0.0.1 (Setup)
**Status**: In Development
**Word Count**: 0 / ~100,000 target

### Structure

```
/book/          - The manuscript (chapter files)
/reference/     - Supporting documents for writing sessions
/tools/         - Build scripts for publishing
/output/        - Generated EPUB/PDF/HTML (gitignored)
/archive/       - Cut material and old drafts
```

### Building

Requires [Pandoc](https://pandoc.org/) for generating output formats.

```bash
# Generate all formats
python tools/publish.py --all

# Generate specific format
python tools/publish.py --epub
python tools/publish.py --pdf
python tools/publish.py --html

# Word count
python tools/publish.py --count
```

### Key Documents

- `STYLE_GUIDE.md` - Voice and prose patterns
- `MASTER_OUTLINE.md` - Complete plot structure
- `TIMELINE.md` - Chronological event tracker
- `FORESHADOWING.md` - Plants and payoffs ledger

### Reference Documents

Located in `/reference/`:
- `characters.md` - Character voices and arcs
- `magic_systems.md` - Sympathy, Naming, Yllish, etc.
- `worldbuilding.md` - Locations, factions, history
- `frame_interludes.md` - Frame story beat planning
- `theory_integration.md` - Fan theories being used

### License

This is a work of fan fiction. All original Kingkiller Chronicle characters, settings, and concepts belong to Patrick Rothfuss.
