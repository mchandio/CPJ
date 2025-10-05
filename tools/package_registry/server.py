from flask import Flask, request, jsonify
from werkzeug.security import safe_join
import json
import os
import hashlib
import shutil

app = Flask(__name__)

PACKAGE_ROOT = "/var/lib/cpj/packages"
METADATA_FILE = "metadata.json"

class PackageRegistry:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        os.makedirs(root_dir, exist_ok=True)
        
    def add_package(self, name, version, files, metadata):
        package_dir = safe_join(self.root_dir, f"{name}-{version}")
        os.makedirs(package_dir, exist_ok=True)
        
        # Save package files
        for file_name, content in files.items():
            file_path = safe_join(package_dir, file_name)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'wb') as f:
                f.write(content)
        
        # Save metadata
        metadata_path = safe_join(package_dir, METADATA_FILE)
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f)
            
    def get_package(self, name, version):
        package_dir = safe_join(self.root_dir, f"{name}-{version}")
        if not os.path.exists(package_dir):
            return None
            
        # Read metadata
        metadata_path = safe_join(package_dir, METADATA_FILE)
        with open(metadata_path) as f:
            metadata = json.load(f)
            
        # Collect files
        files = {}
        for root, _, filenames in os.walk(package_dir):
            for filename in filenames:
                if filename != METADATA_FILE:
                    file_path = os.path.join(root, filename)
                    with open(file_path, 'rb') as f:
                        files[filename] = f.read()
                        
        return {
            'metadata': metadata,
            'files': files
        }
        
    def search_packages(self, query):
        results = []
        for item in os.listdir(self.root_dir):
            if query.lower() in item.lower():
                package_dir = os.path.join(self.root_dir, item)
                metadata_path = os.path.join(package_dir, METADATA_FILE)
                if os.path.exists(metadata_path):
                    with open(metadata_path) as f:
                        metadata = json.load(f)
                        results.append(metadata)
        return results

registry = PackageRegistry(PACKAGE_ROOT)

@app.route('/packages', methods=['POST'])
def publish_package():
    data = request.get_json()
    name = data['name']
    version = data['version']
    files = data['files']
    metadata = data['metadata']
    
    registry.add_package(name, version, files, metadata)
    return jsonify({'status': 'success'})

@app.route('/packages/<name>/<version>', methods=['GET'])
def get_package(name, version):
    package = registry.get_package(name, version)
    if package is None:
        return jsonify({'error': 'Package not found'}), 404
    return jsonify(package)

@app.route('/packages/search', methods=['GET'])
def search_packages():
    query = request.args.get('q', '')
    results = registry.search_packages(query)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)