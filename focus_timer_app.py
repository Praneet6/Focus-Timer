import tkinter as tk
from tkinter import ttk, messagebox
import time, threading, random

# 🌟 List of motivational quotes
quotes = [
    "🌸 Believe in yourself — you are capable of amazing things!",
    "📚 Focus on your goals, one step at a time.",
    "🌞 Progress, not perfection. Keep moving forward!",
    "💪 You’ve got this! Every second counts.",
    "🌻 Don’t stop when you’re tired, stop when you’re done!",
    "🌈 Trust the process — you’re growing even when it’s hard."
]

# 🕑 Function to start timer
def start_timer():
    try:
        total_time = int(time_entry.get())
    except ValueError:
        messagebox.showwarning("⏰ Input Error", "Please enter time in minutes.")
        return

    activity = activity_var.get()
    if activity == "":
        messagebox.showwarning("⚠️ Missing Selection", "Please select an activity type.")
        return

    quote_label.config(text=random.choice(quotes))
    messagebox.showinfo("Timer Started", f"✨ {activity} session started for {total_time} minutes!")
    start_btn.config(state="disabled")

    total_seconds = total_time * 60
    progress_bar["maximum"] = total_seconds

    def countdown():
        for i in range(total_seconds, -1, -1):
            mins, secs = divmod(i, 60)
            timer_label.config(text=f"⏳ Time Left: {mins:02d}:{secs:02d}")
            progress_bar["value"] = total_seconds - i
            time.sleep(1)
        messagebox.showinfo("Done 🎉", f"Time's up! {activity} session completed.")
        start_btn.config(state="normal")

    threading.Thread(target=countdown, daemon=True).start()

# ♻️ Reset fields
def reset_fields():
    time_entry.delete(0, tk.END)
    activity_var.set("")
    quote_label.config(text="🌼 Your motivational quote will appear here!")
    timer_label.config(text="⏳ Time Left: 00:00")
    progress_bar["value"] = 0

# 🌈 Create gradient background using Canvas
def create_gradient(canvas, color1, color2):
    width = 500
    height = 600
    gradient_steps = 100
    r1, g1, b1 = canvas.winfo_rgb(color1)
    r2, g2, b2 = canvas.winfo_rgb(color2)
    r_ratio = (r2 - r1) / gradient_steps
    g_ratio = (g2 - g1) / gradient_steps
    b_ratio = (b2 - b1) / gradient_steps

    for i in range(gradient_steps):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = f'#{nr//256:02x}{ng//256:02x}{nb//256:02x}'
        canvas.create_rectangle(0, (i * height / gradient_steps), width,
                                ((i + 1) * height / gradient_steps),
                                outline="", fill=color)

# 🌷 Main window
root = tk.Tk()
root.title("🧠 Focus Timer + Productivity Companion")
root.geometry("500x600")

# Create gradient background
bg_canvas = tk.Canvas(root, width=500, height=600, highlightthickness=0)
bg_canvas.pack(fill="both", expand=True)
create_gradient(bg_canvas, "#f9f9ff", "#d6e0ff")

# Container frame for widgets
main_frame = tk.Frame(bg_canvas, bg="#f9f9ff")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# 🌼 Title
tk.Label(main_frame, text="🧠 Focus Timer & Productivity App",
         font=("Comic Sans MS", 16, "bold"), bg="#f9f9ff", fg="#34495E").pack(pady=10)

# 🎯 Activity selection
activity_var = tk.StringVar(value="Study")
tk.Label(main_frame, text="Choose Activity Type:", font=("Arial", 12, "bold"), bg="#f9f9ff").pack(pady=5)
activity_frame = tk.Frame(main_frame, bg="#f9f9ff")
activity_frame.pack(pady=5)
for text in ["Study", "Break", "Revision"]:
    tk.Radiobutton(activity_frame, text=text, variable=activity_var, value=text,
                   bg="#f9f9ff", font=("Arial", 11)).pack(side="left", padx=8)

# ⏰ Time input
tk.Label(main_frame, text="Enter Time (minutes):", font=("Arial", 12, "bold"), bg="#f9f9ff").pack(pady=10)
time_entry = tk.Entry(main_frame, font=("Arial", 12), width=10, justify="center")
time_entry.pack(pady=5)

# Progress bar
progress_bar = ttk.Progressbar(main_frame, orient="horizontal", length=350, mode="determinate")
progress_bar.pack(pady=15)

# Timer label
timer_label = tk.Label(main_frame, text="⏳ Time Left: 00:00", font=("Arial", 13, "bold"),
                       bg="#f9f9ff", fg="#34495E")
timer_label.pack(pady=5)

# Motivational quote box
quote_frame = tk.Frame(main_frame, bg="#EAF6F6", bd=2, relief="ridge")
quote_frame.pack(pady=15)
quote_label = tk.Label(quote_frame, text="🌼 Your motivational quote will appear here!",
                       wraplength=400, bg="#EAF6F6", font=("Arial", 11, "italic"), justify="center")
quote_label.pack(padx=10, pady=10)

# Buttons
btn_frame = tk.Frame(main_frame, bg="#f9f9ff")
btn_frame.pack(pady=10)
start_btn = tk.Button(btn_frame, text="▶ Start", command=start_timer, bg="#58D68D", fg="white",
                      font=("Arial", 11, "bold"), width=10)
start_btn.grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="🔁 Reset", command=reset_fields, bg="#F5B041", fg="white",
          font=("Arial", 11, "bold"), width=10).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="❌ Exit", command=root.destroy, bg="#E74C3C", fg="white",
          font=("Arial", 11, "bold"), width=10).grid(row=0, column=2, padx=5)

# Footer
tk.Label(main_frame, text="✨ Stay calm, stay consistent, stay kind ✨",
         font=("Arial", 10, "italic"), bg="#f9f9ff", fg="#7F8C8D").pack(pady=15)

root.mainloop()
