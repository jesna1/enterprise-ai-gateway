from fastapi import FastAPI
import yaml
import os

app = FastAPI()

@app.get("/audit")
def get_packages():
    file_path = "pubspec.yaml"
    
    if not os.path.exists(file_path):
        return {"error": "File not found"}

    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            
            # --- THE SAFETY CHECK ---
            if data is None:
                return {"error": "The pubspec.yaml file is empty!"}
            
            # Now it is safe to use .get()
            dependencies = data.get('dependencies', {})
            
            return {
                "project": data.get('name', 'Unknown'),
                "packages": dependencies
            }
    except Exception as e:
        return {"error": f"Parsing failed: {str(e)}"}