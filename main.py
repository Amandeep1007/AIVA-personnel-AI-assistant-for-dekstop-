import customtkinter as ctk
from boot_screen import show_boot_screen
from elite_gui import AIVA_GUI
from speech import listen, speak
from brain import ask_ai
from actions import perform_action


# =========================
# CLI MODE (YOUR OLD SYSTEM)
# =========================
def run_AIVA():

    speak("Hello. I am AIVA. How can I help you?")

    while True:
        command = listen()

        if command == "":
            continue

        if "exit" in command or "stop" in command or "quit" in command:
            speak("Goodbye")
            break

        action_result = perform_action(command)

        if action_result:
            speak(action_result)
        else:
            response = ask_ai(command)
            speak(response)


# =========================
# GUI MODE
# =========================
def start_gui():

    root = ctk.CTk()
    root.geometry("1200x700")

    app = AIVA_GUI(root)

    root.protocol("WM_DELETE_WINDOW", app.on_close)

    root.mainloop()


# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":

    print("1. Run AIVA (Voice CLI)")
    print("2. Run AIVA HUD (GUI)")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        run_AIVA()

    else:
        show_boot_screen(start_gui)

