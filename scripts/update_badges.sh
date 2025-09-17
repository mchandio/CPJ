#!/usr/bin/env bash
# Replace <OWNER>/<REPO> placeholders in README and workflow badges
set -euo pipefail
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 owner/repo"
  exit 2
fi
REPO="$1"
FILES=(README.md .github/workflows/*.yml)
for f in "${FILES[@]}"; do
  # Use perl in-place to handle macOS/BSD sed differences
  if [ -f "$f" ]; then
    perl -pi -e "s#<OWNER>/<REPO>#$REPO#g" "$f"
  else
    for g in $f; do
      [ -f "$g" ] || continue
      perl -pi -e "s#<OWNER>/<REPO>#$REPO#g" "$g"
    done
  fi
done
echo "Updated badges to $REPO"
