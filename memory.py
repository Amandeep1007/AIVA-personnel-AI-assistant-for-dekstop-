import json
import os

FILE = "memory.json"

def load_memory():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def remember(key, value):
    data = load_memory()
    data[key] = value
    save_memory(data)

def recall(key):
    data = load_memory()
    return data.get(key)

