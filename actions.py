import os
import webbrowser
from datetime import datetime
import wikipedia

# Custom Modules
from memory import remember, recall
from dashboard import daily_dashboard
from goals import set_goal, get_goal, add_progress, roadmap
from personality import set_mode



def perform_action(command):

    command = command.lower()

    # =================================================
    # MEMORY
    # =================================================

    if "remember that my name is" in command:
        name = command.replace("remember that my name is","").strip()
        remember("username", name)
        return f"I will remember that your name is {name}"

    elif "what is my name" in command:
        name = recall("username")
        if name:
            return f"Your name is {name}"
        else:
            return "I do not know your name yet."

    # =================================================
    # DAILY DASHBOARD
    # =================================================

    elif "show my dashboard" in command:
        return daily_dashboard()

    # =================================================
    # GOAL SYSTEM
    # =================================================

    elif "my goal is" in command:
        goal = command.replace("my goal is","").strip()
        set_goal(goal)
        return f"Goal saved.\n{roadmap(goal)}"

    elif "what is my goal" in command:
        goal = get_goal()
        if goal:
            return f"Your goal is: {goal}"
        else:
            return "You have not set any goal."

    elif "i made progress" in command:
        update = command.replace("i made progress","").strip()
        add_progress(update)
        return "Progress saved."

    elif "motivate me" in command:
        return "Stay consistent. Small progress daily builds greatness."

    # =================================================
    # WIKIPEDIA
    # =================================================

    elif command.startswith(("who is","what is","tell me about")):
        try:
            topic = command.replace("who is","")\
                           .replace("what is","")\
                           .replace("tell me about","").strip()
            return wikipedia.summary(topic, sentences=2)
        except:
            return None

    # =================================================
    # WEBSITES
    # =================================================

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "open whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        return "Opening WhatsApp"

    # =================================================
    # APPLICATIONS
    # =================================================

    elif "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad"

    elif "open calculator" in command:
        os.system("calc")
        return "Opening Calculator"

    # =================================================
    # DATE & TIME
    # =================================================

    elif "time" in command:
        return datetime.now().strftime("The time is %H:%M")

    elif "date" in command:
        return datetime.now().strftime("Today's date is %d %B %Y")

    # =================================================
    # FALLBACK TO AI
    # =================================================

    else:
        return None
