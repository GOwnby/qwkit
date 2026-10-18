#!/bin/sh
# Copies the files intended for a public qwkit repository into ../qwkit-public (or the folder given as $1).
# Private research-planning material (roadmap, research notes, parked submission steps, unpublished manuscript
# sources) is left out. Review the result before publishing.
set -e
SRC=$(cd "$(dirname "$0")/.." && pwd)
DST=${1:-"$SRC/../qwkit-public"}
mkdir -p "$DST"
cd "$SRC"
for f in qwkit tests examples docs/examples.py docs/examples_output.txt docs/guide.tex \
         paper_software/qwkit_software.tex paper_software/refs.bib paper_software/figures \
         .github pyproject.toml MANIFEST.in LICENSE README.md CHANGELOG.md CITATION.cff CONTRIBUTING.md \
         CODE_OF_CONDUCT.md .zenodo.json .gitignore qwkit_user_guide.pdf; do
  mkdir -p "$DST/$(dirname "$f")"; cp -R "$f" "$DST/$(dirname "$f")/"
done
find "$DST" -name "__pycache__" -type d -prune -exec rm -rf {} +
echo "Public tree written to $DST. Remove the 'Project folder contents' section from its README before publishing."
