#!/usr/bin/env python3

import os
import sys
import json
import subprocess
import argparse
import tempfile
from dataclasses import dataclass
from typing import List, Dict, Optional
from pathlib import Path

@dataclass
class PackageSpec:
    name: str
    version: str
    language: str
    dependencies: List['PackageSpec']
    source: str

class CPJPackageManager:
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.pkg_file = project_root / "cpj_packages.json"
        self.pkg_lock = project_root / "cpj_packages.lock"
        self.cache_dir = project_root / ".cpj" / "cache"
        self.ensure_directories()

    def ensure_directories(self):
        """Create necessary directories if they don't exist."""
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def read_package_file(self) -> Dict:
        """Read and parse the package file."""
        if not self.pkg_file.exists():
            return {"dependencies": {}}
        with open(self.pkg_file) as f:
            return json.load(f)

    def read_lock_file(self) -> Dict:
        """Read and parse the lock file."""
        if not self.pkg_lock.exists():
            return {"packages": {}}
        with open(self.pkg_lock) as f:
            return json.load(f)

    def write_lock_file(self, data: Dict):
        """Write to the lock file."""
        with open(self.pkg_lock, 'w') as f:
            json.dump(data, f, indent=2)

    def install_python_package(self, spec: PackageSpec):
        """Install a Python package using pip."""
        cmd = [sys.executable, "-m", "pip", "install", f"{spec.name}=={spec.version}"]
        subprocess.run(cmd, check=True)

    def install_java_package(self, spec: PackageSpec):
        """Install a Java package using Maven."""
        # Add Maven dependency to build.gradle
        with open(self.project_root / "build.gradle", "a") as f:
            f.write(f'\nimplementation "{spec.name}:{spec.version}"\n')

    def install_cpp_package(self, spec: PackageSpec):
        """Install a C++ package using Conan."""
        conanfile = self.project_root / "conanfile.txt"
        if not conanfile.exists():
            with open(conanfile, "w") as f:
                f.write("[requires]\n")
        
        with open(conanfile, "a") as f:
            f.write(f"{spec.name}/{spec.version}\\n")
        
        # Run conan install
        subprocess.run(["conan", "install", "."], cwd=self.project_root, check=True)

    def install_package(self, spec: PackageSpec):
        """Install a package based on its language."""
        installers = {
            "python": self.install_python_package,
            "java": self.install_java_package,
            "cpp": self.install_cpp_package
        }
        
        installer = installers.get(spec.language)
        if installer:
            installer(spec)
        else:
            raise ValueError(f"Unsupported language: {spec.language}")

    def install_all(self):
        """Install all packages from the package file."""
        pkg_data = self.read_package_file()
        lock_data = self.read_lock_file()
        
        for lang, packages in pkg_data["dependencies"].items():
            for pkg_name, pkg_ver in packages.items():
                spec = PackageSpec(
                    name=pkg_name,
                    version=pkg_ver,
                    language=lang,
                    dependencies=[],
                    source="registry"
                )
                self.install_package(spec)
                
                # Update lock file
                if lang not in lock_data["packages"]:
                    lock_data["packages"][lang] = {}
                lock_data["packages"][lang][pkg_name] = {
                    "version": pkg_ver,
                    "resolved": True
                }
        
        self.write_lock_file(lock_data)

    def add_package(self, name: str, version: str, language: str):
        """Add a package to the project."""
        pkg_data = self.read_package_file()
        
        if language not in pkg_data["dependencies"]:
            pkg_data["dependencies"][language] = {}
        
        pkg_data["dependencies"][language][name] = version
        
        with open(self.pkg_file, 'w') as f:
            json.dump(pkg_data, f, indent=2)
        
        # Install the new package
        spec = PackageSpec(
            name=name,
            version=version,
            language=language,
            dependencies=[],
            source="registry"
        )
        self.install_package(spec)

def main():
    parser = argparse.ArgumentParser(description="CPJ Package Manager")
    parser.add_argument('command', choices=['install', 'add'])
    parser.add_argument('--name', help="Package name")
    parser.add_argument('--version', help="Package version")
    parser.add_argument('--language', choices=['python', 'java', 'cpp'])
    
    args = parser.parse_args()
    
    pm = CPJPackageManager(Path.cwd())
    
    if args.command == 'install':
        pm.install_all()
    elif args.command == 'add':
        if not all([args.name, args.version, args.language]):
            parser.error("add command requires --name, --version, and --language")
        pm.add_package(args.name, args.version, args.language)

if __name__ == "__main__":
    main()