import customtkinter as ctk
from config import ASSISTANT_NAME
from speech import listen, speak
from brain import ask_ai
from actions import perform_action
import threading
from datetime import datetime

# =========================
# THEME
# =========================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

BG = "#020617"
CARD = "#0f172a"
ACCENT = "#00f5ff"
TEXT = "#e2e8f0"

# =========================
# MAIN CLASS
# =========================
class AIVA_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title(f"{ASSISTANT_NAME} HUD")
        self.root.geometry("1200x700")
        self.root.configure(fg_color=BG)

        self.running = True

        self.build_ui()
        self.update_time()

    # =========================
    # UI BUILD
    # =========================
    def build_ui(self):

        # LEFT PANEL
        self.left_frame = ctk.CTkFrame(self.root, fg_color=CARD, width=200)
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)

        ctk.CTkLabel(
            self.left_frame,
            text="SYSTEM STATUS",
            text_color=ACCENT,
            font=("Orbitron", 16)
        ).pack(pady=20)

        for text in [
            "AI CORE : ONLINE",
            "VOICE : ACTIVE",
            "MEMORY : READY",
            "SECURITY : ENABLED",
            "NETWORK : CONNECTED"
        ]:
            ctk.CTkLabel(
                self.left_frame,
                text=text,
                text_color="#38bdf8"
            ).pack(pady=5)

        self.time_label = ctk.CTkLabel(
            self.left_frame,
            text="",
            text_color=ACCENT,
            font=("Orbitron", 14)
        )
        self.time_label.pack(pady=30)

        # =========================
        # CENTER PANEL
        # =========================
        self.center_frame = ctk.CTkFrame(self.root, fg_color=CARD)
        self.center_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.title = ctk.CTkLabel(
            self.center_frame,
            text=ASSISTANT_NAME,
            font=("Orbitron", 32),
            text_color=ACCENT
        )
        self.title.pack(pady=10)

        self.sub_title = ctk.CTkLabel(
            self.center_frame,
            text="Neural Interface Active",
            text_color="#38bdf8"
        )
        self.sub_title.pack(pady=5)

        self.chat_box = ctk.CTkTextbox(
            self.center_frame,
            fg_color=BG,
            text_color=ACCENT,
            height=350
        )
        self.chat_box.pack(padx=20, pady=10, fill="both", expand=True)

        self.entry = ctk.CTkEntry(
            self.center_frame,
            placeholder_text="Enter Command..."
        )
        self.entry.pack(padx=20, pady=10, fill="x")

        self.button_frame = ctk.CTkFrame(self.center_frame, fg_color=CARD)
        self.button_frame.pack(pady=10)

        self.send_btn = ctk.CTkButton(
            self.button_frame,
            text="SEND",
            command=self.handle_text
        )
        self.send_btn.pack(side="left", padx=10)

        self.voice_btn = ctk.CTkButton(
            self.button_frame,
            text="VOICE",
            command=self.handle_voice
        )
        self.voice_btn.pack(side="left", padx=10)

        # =========================
        # RIGHT PANEL (NO ARC REACTOR)
        # =========================
        self.right_frame = ctk.CTkFrame(self.root, fg_color=CARD, width=200)
        self.right_frame.pack(side="right", fill="y", padx=10, pady=10)

        ctk.CTkLabel(
            self.right_frame,
            text="SYSTEM MONITOR",
            text_color=ACCENT,
            font=("Orbitron", 16)
        ).pack(pady=20)

        ctk.CTkLabel(self.right_frame, text="CPU: Stable", text_color="#38bdf8").pack(pady=5)
        ctk.CTkLabel(self.right_frame, text="AI: Active", text_color="#22c55e").pack(pady=5)
        ctk.CTkLabel(self.right_frame, text="Network: Connected", text_color="#38bdf8").pack(pady=5)

    # =========================
    # CLOCK (FIXED)
    # =========================
    def update_time(self):
        try:
            if not self.running:
                return
            now = datetime.now().strftime("%H:%M:%S")
            self.time_label.configure(text=now)
            self.root.after(1000, self.update_time)
        except:
            pass

    # =========================
    # DISPLAY CHAT
    # =========================
    def display(self, sender, text):
        self.chat_box.insert("end", f"{sender}: {text}\n")
        self.chat_box.see("end")

    # =========================
    # TEXT INPUT
    # =========================
    def handle_text(self):
        query = self.entry.get()
        self.entry.delete(0, "end")
        self.display("You", query)
        threading.Thread(target=self.process, args=(query,), daemon=True).start()

    # =========================
    # VOICE INPUT
    # =========================
    def handle_voice(self):
        threading.Thread(target=self.voice_thread, daemon=True).start()

    def voice_thread(self):
        query = listen()
        if query:
            self.display("You", query)
            self.process(query)

    # =========================
    # PROCESS LOGIC
    # =========================
    def process(self, query):
        if not self.running or not query:
            return

        action = perform_action(query)
        if action:
            self.display(ASSISTANT_NAME, action)
            speak(action)
            return

        response = ask_ai(query)
        self.display(ASSISTANT_NAME, response)
        speak(response)

    # =========================
    # SAFE CLOSE
    # =========================
    def on_close(self):
        self.running = False
        self.root.destroy()


# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    root = ctk.CTk()
    app = AIVA_GUI(root)

    root.protocol("WM_DELETE_WINDOW", app.on_close)

    root.mainloop()

