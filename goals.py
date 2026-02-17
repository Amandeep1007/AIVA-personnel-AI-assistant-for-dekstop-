import json
import os

FILE = "goals.json"

def load_goals():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save_goals(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def set_goal(goal):
    data = load_goals()
    data["main_goal"] = goal
    data["progress"] = []
    save_goals(data)

def get_goal():
    data = load_goals()
    return data.get("main_goal")

def add_progress(update):
    data = load_goals()
    data.setdefault("progress", [])
    data["progress"].append(update)
    save_goals(data)

def roadmap(goal):
    if "python" in goal.lower():
        return """
PYTHON ROADMAP
1. Basics
2. Data Structures
3. OOP
4. Projects
5. AI Integration
"""
    else:
        return "Roadmap generation coming soon."

