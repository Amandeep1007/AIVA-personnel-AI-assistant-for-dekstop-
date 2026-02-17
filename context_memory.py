from collections import deque

history = deque(maxlen=10)

def add(role, text):
    history.append({"role": role, "content": text})

def get():
    return list(history)

