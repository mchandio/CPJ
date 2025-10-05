#!/usr/bin/env bash
set -euo pipefail

# publish_release.sh - Create a GitHub release and upload the tarball using gh CLI
# Usage: ./scripts/publish_release.sh <version>

VERSION=${1:-v1.0.0}
TARBALL="releases/cpj-${VERSION}.tar.gz"

if [ ! -f "$TARBALL" ]; then
  echo "Tarball $TARBALL not found. Run ./scripts/create_release.sh $VERSION first."
  exit 1
fi

if ! command -v gh >/dev/null 2>&1; then
  echo "gh CLI not installed. Install from https://github.com/cli/cli"
  exit 2
fi

# Create release (if it already exists, gh will fail)
gh release create "$VERSION" "$TARBALL" --title "CPJ $VERSION" --notes-file RELEASE.md

echo "Published $TARBALL to GitHub release $VERSION"
