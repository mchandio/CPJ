"""
CPJ Orchestrator
Central script to manage C++, Python, and Java code execution and communication
"""
import subprocess
import sys
import os
import time

def run_cpp(source_file):
    print("Compiling and running C++ code...")
    result = subprocess.run(["g++", source_file, "-o", "cpp_out"])
    if result.returncode != 0:
        print("C++ compilation failed.")
        return
    subprocess.run(["./cpp_out"])

def run_python(source_file):
    print("Running Python code with auto-library installation...")
    subprocess.run([sys.executable, "python/cpj_python.py", source_file])

def run_java(source_file):
    print("Compiling and running Java code...")
    result = subprocess.run(["javac", source_file])
    if result.returncode != 0:
        print("Java compilation failed.")
        return
    class_name = os.path.splitext(os.path.basename(source_file))[0]
    subprocess.run(["java", "-cp", "java", class_name])


def run_gui_and_listen(class_name="GeneratedGUI", java_dir="java", poll_secs=60):
    """Run a generated Java GUI class and poll /tmp/cpj_event.json for events.
    Prints any events found and clears the event file.
    """
    print(f"Running {class_name} from {java_dir} and listening for events...")
    # Ensure compiled class exists; try to compile if .java exists
    java_path = os.path.join(java_dir, class_name + ".java")
    if os.path.exists(java_path):
        print("Compiling generated Java...")
        rc = subprocess.run(["javac", "-d", java_dir, java_path]).returncode
        if rc != 0:
            print("Failed to compile generated Java.")
            return

    proc = subprocess.Popen(["java", "-cp", java_dir, class_name])
    try:
        for i in range(poll_secs):
            evpath = "/tmp/cpj_event.json"
            if os.path.exists(evpath):
                try:
                    with open(evpath, 'r') as f:
                        data = f.read()
                    print("Event:", data)
                    try:
                        os.remove(evpath)
                    except Exception:
                        pass
                except Exception as e:
                    print("Error reading event file:", e)
            time.sleep(1)
    finally:
        proc.terminate()
        proc.wait()

def main():
    if len(sys.argv) < 3:
        print("Usage: cpj_orchestrator.py <language> <source_file>")
        print("Languages: cpp, python, java")
        sys.exit(1)
    lang = sys.argv[1].lower()
    source_file = sys.argv[2]
    if lang == "cpp":
        run_cpp(source_file)
    elif lang == "python":
        run_python(source_file)
    elif lang == "java":
        run_java(source_file)
    else:
        print("Unsupported language.")

if __name__ == "__main__":
    main()
