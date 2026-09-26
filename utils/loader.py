import json
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent

def load_json_file(relative_path: str) -> dict:
    file_path = BASE_DIR / relative_path
    
    # Check if the file is at project root (contract/...) or inside app/ (contract/...)
    if not file_path.exists():
        # Try one level higher (project root) just in case
        file_path = BASE_DIR.parent / relative_path

    if not file_path.exists():
        raise FileNotFoundError(f"Could not find file at: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)