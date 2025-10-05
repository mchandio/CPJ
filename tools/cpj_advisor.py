"""
CPJ Advisor

A local, repo-contained helper that mimics an "AI" decision flow for CPJ.
It scans the workspace for hints about required capabilities (e.g., networking,
GUI, parsing), consults a built-in small knowledge base of candidate
libraries for C++, Python, and Java, scores candidates with simple heuristics,
and emits a short implementation prompt describing the chosen library and why.

This tool is intentionally offline and deterministic — it's a helper to
accelerate maintainers' decisions without external network calls.

Usage: python tools/cpj_advisor.py [--feature FEATURE]...
If no feature is provided, it will auto-detect features from the repo.

Output: JSON object to stdout with keys: detected_features, candidates, choice, prompt
"""

import argparse
import json
import os
import re
from collections import defaultdict

KB = {
    'cpp': [
        {
            'name': 'Boost.Asio',
            'purpose': 'Networking, async IO, timers',
            'score': 9,
            'notes': 'Well-tested, header-only parts, integrates with existing C++ projects.'
        },
        {
            'name': 'Qt',
            'purpose': 'Cross-platform GUI, event system',
            'score': 8,
            'notes': 'Heavyweight but complete GUI stack; good for full-featured desktop apps.'
        },
        {
            'name': 'ANTLR4 C++ runtime',
            'purpose': 'Parsing, lexer/parser runtime',
            'score': 10,
            'notes': 'Matches project which already uses ANTLR for grammar.'
        },
        {
            'name': 'nlohmann/json',
            'purpose': 'JSON serialization',
            'score': 9,
            'notes': 'Lightweight, header-only, excellent for manifest/event payloads.'
        },
    ],
    'python': [
        {
            'name': 'asyncio',
            'purpose': 'Async IO/event loop',
            'score': 9,
            'notes': 'Built-in; works well for event-driven connectors.'
        },
        {
            'name': 'pygls',
            'purpose': 'Language Server Protocol server',
            'score': 10,
            'notes': 'Already used in this repo; keeps LSP work consistent.'
        },
        {
            'name': 'antlr4-python3-runtime',
            'purpose': 'ANTLR runtime',
            'score': 10,
            'notes': 'Used in parser and LSP diagnostics.'
        },
        {
            'name': 'FastAPI',
            'purpose': 'HTTP-based APIs for connector/services',
            'score': 7,
            'notes': 'Great for REST/HTTP endpoints, async capable.'
        },
    ],
    'java': [
        {
            'name': 'Jackson',
            'purpose': 'JSON serialization/deserialization',
            'score': 9,
            'notes': 'Popular and fast; useful for manifests and event payloads.'
        },
        {
            'name': 'Swing',
            'purpose': 'GUI toolkit (existing codegen targets Swing)',
            'score': 8,
            'notes': 'Already used by generated GUI targets in repo; lightweight for desktop.'
        },
        {
            'name': 'gson',
            'purpose': 'JSON (Google)',
            'score': 8,
            'notes': 'Easy to use, good for small projects.'
        },
    ]
}

FEATURE_KEYWORDS = {
    'networking': ['socket', 'http', 'tcp', 'udp', 'requests', 'aiohttp', 'server'],
    'gui': ['swing', 'ui', 'gui', 'java.awt', 'JFrame', 'Swing'],
    'antlr': ['CPJ.g4', 'antlr', 'lexer', 'parser', 'antlr4'],
    'lsp': ['pygls', 'LanguageServer', 'lsp', 'vscode'],
    'json': ['json', 'manifest', '.json', 'nlohmann', 'gson', 'jackson'],
    'async': ['async', 'await', 'asyncio', 'coroutine']
}


def scan_repo(root):
    detected = set()
    file_matches = defaultdict(list)
    pattern = re.compile('|'.join(re.escape(k) for keys in FEATURE_KEYWORDS.values() for k in keys), re.IGNORECASE)
    for dirpath, dirnames, filenames in os.walk(root):
        # skip virtualenvs and build directories
        if 'cpj_venv' in dirpath or 'build' in dirpath or '.git' in dirpath:
            continue
        for fn in filenames:
            path = os.path.join(dirpath, fn)
            try:
                with open(path, 'r', errors='ignore') as f:
                    data = f.read(4096)
            except Exception:
                continue
            for feat, kws in FEATURE_KEYWORDS.items():
                for kw in kws:
                    if kw.lower() in data.lower() or kw.lower() in fn.lower():
                        detected.add(feat)
                        file_matches[feat].append(path)
                        break
    return list(detected), file_matches


def rank_candidates(detected):
    choices = {}
    for lang, options in KB.items():
        # base score 0
        scored = []
        for opt in options:
            score = opt['score']
            # small boosts for detected features
            if 'antlr' in detected and 'ANTLR' in opt['name']:
                score += 10
            if 'lsp' in detected and opt['name'].lower() == 'pygls':
                score += 5
            scored.append((score, opt))
        scored.sort(reverse=True, key=lambda x: x[0])
        choices[lang] = [s[1] for s in scored]
    return choices


def make_prompt(choice, lang, feature_hints):
    prompt = {
        'title': f'Implement {choice["name"]} integration in CPJ ({lang})',
        'why': choice['purpose'],
        'notes': choice['notes'],
        'tasks': []
    }
    # simple task list
    prompt['tasks'].append(f"Add dependency: {choice['name']} to the project's {lang} build.")
    if lang == 'python':
        prompt['tasks'].append('Update `requirements.txt` and `pyproject.toml` if needed.')
    elif lang == 'cpp':
        prompt['tasks'].append('Update `Makefile` or CMake files and add include/link steps.')
    elif lang == 'java':
        prompt['tasks'].append('Update `build.gradle` or Maven pom.xml, or vendor the JAR into `lib/`.')

    prompt['tasks'].append('Write a small integration module that exposes the features to CPJ runtime.')
    prompt['tasks'].append('Add unit tests that validate basic serialization and round-trip behaviour.')

    if feature_hints:
        prompt['tasks'].append(f"Pay attention to these detected features: {', '.join(feature_hints)}")
    return prompt


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--feature', '-f', action='append', help='Feature to consider (can be repeated)')
    parser.add_argument('--root', default='.', help='Repo root path')
    parser.add_argument('--json', action='store_true', help='Emit machine-readable JSON')
    parser.add_argument('--apply', action='store_true', help='Apply recommended edits to local build files (creates backups)')
    args = parser.parse_args(argv)

    if args.feature:
        detected = list(set(args.feature))
        file_matches = {}
    else:
        detected, file_matches = scan_repo(args.root)

    candidates = rank_candidates(detected)

    # pick top choice per language
    choice = {lang: opts[0] for lang, opts in candidates.items()}

    # prepare prompts
    prompts = {lang: make_prompt(choice[lang], lang, detected) for lang in choice}

    output = {
        'detected_features': detected,
        'file_matches': {k: v[:5] for k, v in file_matches.items()},
        'candidates': candidates,
        'choice': choice,
        'prompts': prompts
    }

    if args.json:
        print(json.dumps(output, indent=2))
    else:
        print('\nCPJ Advisor Results')
        print('Detected features:', ', '.join(detected) or '<none>')
        for lang in ['cpp', 'python', 'java']:
            c = choice[lang]
            print(f"\n{lang.upper()} -> {c['name']}: {c['purpose']}")
            print('  Notes:', c['notes'])
            for t in prompts[lang]['tasks']:
                print('   -', t)

    # Auto-apply edits if requested
    if args.apply:
        # Make simple edits: requirements.txt, pyproject.toml, Makefile, and create lib/
        edits = []
        root = args.root
        # Backup function
        def backup(path):
            try:
                import shutil
                if os.path.exists(path):
                    shutil.copy2(path, path + '.bak')
                    return True
            except Exception:
                return False
            return False

        # 1) requirements.txt (python)
        req_path = os.path.join(root, 'requirements.txt')
        try:
            backup(req_path)
            with open(req_path, 'a') as f:
                py_choice = choice['python']['name']
                # simple mapping: use package name as listed in KB, but normalize known cases
                map_pkg = {'antlr4-python3-runtime': 'antlr4-python3-runtime', 'pygls': 'pygls', 'asyncio': ''}
                pkg = map_pkg.get(py_choice.lower(), py_choice)
                if pkg:
                    f.write('\n' + pkg + '\n')
                    edits.append(('requirements.txt', pkg))
        except Exception as e:
            print('Failed to patch requirements.txt:', e)

        # 2) pyproject.toml: add dependency if missing
        pyproj = os.path.join(root, 'pyproject.toml')
        try:
            backup(pyproj)
            with open(pyproj, 'r') as f:
                data = f.read()
            dep = choice['python']['name']
            if dep not in data:
                # naive insert before closing ] of dependencies
                newdata = data.replace('dependencies = [', 'dependencies = [\n    "' + dep + '",')
                with open(pyproj, 'w') as f:
                    f.write(newdata)
                edits.append(('pyproject.toml', dep))
        except Exception as e:
            print('Failed to patch pyproject.toml:', e)

        # 3) Makefile: add target to vendor Java libs or mention how to handle C++ includes
        mk = os.path.join(root, 'Makefile')
        try:
            backup(mk)
            with open(mk, 'r') as f:
                mkdata = f.read()
            added = False
            if choice['java']['name'].lower() in ('jackson', 'gson'):
                vendor_block = '\n# Vendor Java libs\nLIB_DIR=lib\nlib/%.jar:\n\tmkdir -p lib\n\t@echo "Place $* in lib/ or use a build tool to fetch it"\n'
                if 'LIB_DIR=lib' not in mkdata:
                    mkdata = mkdata + '\n' + vendor_block
                    added = True
            if choice['cpp']['name'].lower() in ('nlohmann/json', 'boost.asio', 'antlr4 c++ runtime'):
                # add a comment guidance for C++ dependencies
                guidance = '\n# C++ deps guidance\n# Add include paths and link flags for chosen libraries (e.g. -I/path/to/include -L/path/to/lib)\n'
                if 'C++ deps guidance' not in mkdata:
                    mkdata = mkdata + '\n' + guidance
                    added = True
            if added:
                with open(mk, 'w') as f:
                    f.write(mkdata)
                edits.append(('Makefile', 'vendor/java or cpp guidance'))
        except Exception as e:
            print('Failed to patch Makefile:', e)

        # 4) create lib/ placeholder
        lib_dir = os.path.join(root, 'lib')
        try:
            if not os.path.exists(lib_dir):
                os.makedirs(lib_dir, exist_ok=True)
                edits.append(('lib/', 'created'))
        except Exception as e:
            print('Failed to create lib/ folder:', e)

        print('\nApplied edits:')
        for e in edits:
            print(' -', e[0], ':', e[1])


if __name__ == '__main__':
    main()
