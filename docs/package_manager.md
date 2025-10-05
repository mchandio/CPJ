# CPJ Package Manager Guide

The CPJ Package Manager provides unified dependency management across C++, Python, and Java projects within CPJ applications.

## Installation

The package manager is included with the CPJ toolchain. Ensure you have the following prerequisites:
- Python 3.10 or higher
- pip (Python package installer)
- Maven or Gradle (for Java dependencies)
- Conan (for C++ dependencies)

## Usage

### Initialize a New Project
```bash
cpj init my-project
cd my-project
```

This creates a new CPJ project with a `cpj_packages.json` file.

### Add Dependencies
```bash
# Add a Python package
cpj pkg add --name numpy --version 1.24.0 --language python

# Add a Java package
cpj pkg add --name "com.fasterxml.jackson.core:jackson-databind" --version 2.16.1 --language java

# Add a C++ package
cpj pkg add --name boost --version 1.83.0 --language cpp
```

### Install Dependencies
```bash
cpj pkg install
```

This command:
1. Reads `cpj_packages.json`
2. Resolves all dependencies
3. Installs packages using appropriate package managers
4. Creates/updates `cpj_packages.lock`

### Package File Format
```json
{
  "name": "my-cpj-project",
  "version": "1.0.0",
  "dependencies": {
    "python": {
      "numpy": "1.24.0",
      "pandas": "2.1.1"
    },
    "java": {
      "com.fasterxml.jackson.core:jackson-databind": "2.16.1"
    },
    "cpp": {
      "boost": "1.83.0",
      "eigen": "3.4.0"
    }
  }
}
```

## Features

### Cross-Language Dependency Resolution
- Automatically handles dependencies for all three languages
- Resolves version conflicts
- Maintains consistent versions across projects

### Lock File
- Ensures reproducible builds
- Tracks exact versions of all dependencies
- Records dependency tree and resolution status

### Caching
- Caches downloaded packages
- Speeds up repeated installations
- Reduces network usage

### Integration
- Works with pip for Python packages
- Integrates with Maven/Gradle for Java
- Uses Conan for C++ dependencies

### Security
- Verifies package signatures
- Checks for known vulnerabilities
- Supports private repositories

## Best Practices

1. Always commit both `cpj_packages.json` and `cpj_packages.lock`
2. Use specific versions rather than version ranges
3. Regularly update dependencies for security fixes
4. Review dependency licenses before adding packages

## Troubleshooting

### Common Issues

1. Package Not Found
```bash
cpj pkg doctor  # Run diagnostics
cpj pkg clean   # Clear cache and try again
```

2. Version Conflicts
```bash
cpj pkg resolve  # Interactive conflict resolution
```

3. Build Failures
```bash
cpj pkg verify   # Verify package integrity
cpj pkg rebuild  # Force rebuild of dependencies
```

## Advanced Usage

### Custom Repositories
```json
{
  "repositories": {
    "private-python": {
      "type": "pypi",
      "url": "https://private.pypi.org"
    },
    "private-maven": {
      "type": "maven",
      "url": "https://private.maven.org"
    }
  }
}
```

### Version Constraints
```json
{
  "dependencies": {
    "python": {
      "numpy": ">=1.24.0,<2.0.0"
    }
  }
}
```

### Development Dependencies
```json
{
  "devDependencies": {
    "python": {
      "pytest": "7.4.2"
    }
  }
}
```