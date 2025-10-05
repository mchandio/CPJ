import subprocess
import shutil
from pathlib import Path
import os


def test_generate_and_compile_java(tmp_path):
    repo = Path.cwd()
    sample = repo / "samples" / "types_demo.cpj"

    # Ensure compiler exists
    compiler = repo / "cpj_compiler"
    if not compiler.exists():
        # Try the compiled binary alternative
        compiler = repo / "cpj_compiler"

    assert compiler.exists(), "cpj_compiler binary not found in repo root"

    # Run the compiler in no-run mode to emit sources only
    proc = subprocess.run([str(compiler), "--no-run", str(sample)], cwd=str(repo), capture_output=True, text=True)
    assert proc.returncode == 0, f"compiler failed: {proc.stderr}\n{proc.stdout}"

    gen_java = repo / "generated" / "java"
    assert gen_java.exists(), "generated/java directory missing"

    java_files = list(gen_java.rglob("*.java"))
    assert java_files, "No generated Java files"

    # Use helper script to compile generated java
    helper = repo / "scripts" / "compile_generated_java.sh"
    assert helper.exists(), "compile_generated_java.sh not found"

    javac = shutil.which("javac")
    assert javac, "javac not found on PATH"

    proc = subprocess.run([str(helper)], cwd=str(repo), capture_output=True, text=True)
    assert proc.returncode == 0, f"Java compilation failed: {proc.stderr}\n{proc.stdout}"
