#!/usr/bin/env python3
"""
Combine markdown chapters into publishable formats.
Usage: python publish.py [--epub] [--pdf] [--html] [--all] [--count]

Requires pandoc for EPUB/PDF/HTML generation.
"""

import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# Configuration
BOOK_DIR = Path(__file__).parent.parent / "book"
OUTPUT_DIR = Path(__file__).parent.parent / "output"
VERSION = "0.0.1"  # Update with each release
TITLE = "The Doors of Stone"
SUBTITLE = "A Kingkiller Chronicle Fan Fiction"


def get_chapters():
    """Return sorted list of chapter files."""
    chapters = sorted(BOOK_DIR.glob("*.md"))
    # Filter out Notes.md and other non-chapter files
    chapters = [c for c in chapters if not c.name.startswith("Notes")]
    return chapters


def combine_markdown():
    """Combine all chapters into single markdown file."""
    combined = []
    combined.append(f"# {TITLE}\n")
    combined.append(f"## {SUBTITLE}\n")
    combined.append(f"### Version {VERSION} - {datetime.now().strftime('%Y-%m-%d')}\n\n")
    combined.append("---\n\n")

    for chapter in get_chapters():
        content = chapter.read_text(encoding='utf-8')
        # Strip metadata comments
        lines = content.split('\n')
        filtered_lines = []
        in_metadata = False
        for line in lines:
            if line.strip().startswith('<!-- METADATA'):
                in_metadata = True
                continue
            if in_metadata and line.strip() == '-->':
                in_metadata = False
                continue
            if not in_metadata:
                filtered_lines.append(line)

        combined.append('\n'.join(filtered_lines))
        combined.append("\n\n---\n\n")

    output_path = OUTPUT_DIR / "The_Doors_of_Stone.md"
    output_path.write_text("\n".join(combined), encoding='utf-8')
    print(f"Created: {output_path}")
    return output_path


def generate_epub(md_path):
    """Generate EPUB using pandoc."""
    output = OUTPUT_DIR / "The_Doors_of_Stone.epub"
    cmd = [
        "pandoc", str(md_path),
        "-o", str(output),
        "--metadata", f"title={TITLE}",
        "--metadata", f"subtitle={SUBTITLE}",
        "--metadata", "author=Fan Fiction",
        "--toc",
        "--toc-depth=2"
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"Created: {output}")
    except FileNotFoundError:
        print("Error: pandoc not found. Please install pandoc.")
    except subprocess.CalledProcessError as e:
        print(f"Error generating EPUB: {e}")


def generate_pdf(md_path):
    """Generate PDF using pandoc + LaTeX."""
    output = OUTPUT_DIR / "The_Doors_of_Stone.pdf"
    cmd = [
        "pandoc", str(md_path),
        "-o", str(output),
        "--pdf-engine=xelatex",
        "-V", "geometry:margin=1in",
        "--toc"
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"Created: {output}")
    except FileNotFoundError:
        print("Error: pandoc or xelatex not found. Please install pandoc and a LaTeX distribution.")
    except subprocess.CalledProcessError as e:
        print(f"Error generating PDF: {e}")


def generate_html(md_path):
    """Generate single-page HTML."""
    output = OUTPUT_DIR / "The_Doors_of_Stone.html"
    cmd = [
        "pandoc", str(md_path),
        "-o", str(output),
        "--standalone",
        "--toc",
        "--metadata", f"title={TITLE}"
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"Created: {output}")
    except FileNotFoundError:
        print("Error: pandoc not found. Please install pandoc.")
    except subprocess.CalledProcessError as e:
        print(f"Error generating HTML: {e}")


def word_count():
    """Count words across all chapters."""
    total = 0
    print("\nWord Count by Chapter:")
    print("-" * 40)

    for chapter in get_chapters():
        content = chapter.read_text(encoding='utf-8')
        # Remove metadata comments for accurate count
        lines = content.split('\n')
        filtered_lines = []
        in_metadata = False
        for line in lines:
            if line.strip().startswith('<!-- METADATA'):
                in_metadata = True
                continue
            if in_metadata and line.strip() == '-->':
                in_metadata = False
                continue
            if not in_metadata:
                filtered_lines.append(line)

        clean_content = '\n'.join(filtered_lines)
        words = len(clean_content.split())
        total += words
        print(f"{chapter.name}: {words:,} words")

    print("-" * 40)
    print(f"Total: {total:,} words")
    print(f"Target: ~100,000 words")
    print(f"Progress: {total/1000:.1f}%")

    return total


def main():
    """Main entry point."""
    OUTPUT_DIR.mkdir(exist_ok=True)

    if len(sys.argv) == 1:
        print(f"{TITLE} - Build Script")
        print("=" * 40)
        print("\nUsage: python publish.py [options]")
        print("\nOptions:")
        print("  --epub    Generate EPUB format")
        print("  --pdf     Generate PDF format")
        print("  --html    Generate HTML format")
        print("  --all     Generate all formats")
        print("  --count   Show word count")
        print("\nRequires pandoc for format generation.")
        return

    if "--count" in sys.argv:
        word_count()
        return

    # Generate combined markdown first
    md_path = combine_markdown()

    if "--epub" in sys.argv or "--all" in sys.argv:
        generate_epub(md_path)

    if "--pdf" in sys.argv or "--all" in sys.argv:
        generate_pdf(md_path)

    if "--html" in sys.argv or "--all" in sys.argv:
        generate_html(md_path)


if __name__ == "__main__":
    main()
