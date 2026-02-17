import customtkinter as ctk
import time

BG = "#020617"
ACCENT = "#00f5ff"

def show_boot_screen(callback):

    boot = ctk.CTk()
    boot.geometry("500x300")
    boot.title("AIVA Boot")
    boot.configure(fg_color=BG)

    label = ctk.CTkLabel(
        boot,
        text="AIVA INITIALIZING...",
        font=("Orbitron", 24),
        text_color=ACCENT
    )
    label.pack(pady=40)

    progress = ctk.CTkProgressBar(boot, width=300)
    progress.pack(pady=20)
    progress.set(0)

    status = ctk.CTkLabel(boot, text="Starting systems...", text_color="#38bdf8")
    status.pack(pady=10)

    steps = [
        "Loading AI Core...",
        "Initializing Voice Engine...",
        "Connecting Neural Interface...",
        "Starting Modules...",
        "System Ready"
    ]

    def load():
        for i, step in enumerate(steps):
            status.configure(text=step)
            progress.set((i + 1) / len(steps))
            boot.update()
            time.sleep(0.7)

        boot.destroy()
        callback()

    boot.after(100, load)
    boot.mainloop()

