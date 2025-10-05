CPJ Release Notes

Version: v1.0.0
Date: 2025-09-14

Contents:
- cpj_compiler (C++ binary)
- java/ (Java modules and generated GUI code)
- python/ (Python integration and connector)
- cpp/ (C++ modules)
- samples/ (example CPJ sources)
- README.md
- CPJ_Guide.md

Installation:
1. Extract the tarball: tar xzf cpj-v1.0.0.tar.gz
2. cd cpj-v1.0.0
3. Run the compiler: ./cpj_compiler samples/demo.cpj

Notes:
- Ensure Java (javac/java) and Python3 are installed.
- The release tarball contains pre-built artifacts where applicable. If compilation is needed, run `make`.

Publishing to GitHub
1. Automated (recommended): push a tag `git tag v1.0.0 && git push origin --tags`. The GitHub Actions workflow in `.github/workflows/release.yml` will build and publish the release automatically.
2. Manual: Use the `gh` CLI. Example:
	```bash
	./scripts/create_release.sh v1.0.0
	./scripts/publish_release.sh v1.0.0
	```

Requirements for manual publish:
- `gh` CLI authenticated (`gh auth login`)
- Repository push permissions
