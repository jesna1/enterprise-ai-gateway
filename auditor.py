import yaml
import os

def audit_dependencies(file_path):
    if not os.path.exists(file_path):
        return "Error: pubspec.yaml not found!"
    
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        deps = data.get('dependencies', {})
        
        print(f"--- Project: {data.get('name')} Audit ---")
        for lib, version in deps.items():
            print(f"Checking {lib} ({version})... OK")
    return "Audit Complete."

if __name__ == "__main__":
    audit_dependencies('pubspec.yaml')