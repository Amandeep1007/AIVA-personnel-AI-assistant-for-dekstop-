# personality.py

current_mode = "friendly"

modes = {
    "friendly": "You are a friendly, helpful assistant.",
    "strict": "You are strict, short, and professional.",
    "sarcastic": "You are sarcastic but still helpful."
}

def set_mode(mode):
    global current_mode
    current_mode = mode

def get_prompt():
    return modes.get(current_mode, modes["friendly"])

