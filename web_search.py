import webbrowser

def google_search(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return "I couldn't find a good answer. Opening Google."

