import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    current_text = entry_var.get()
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception:
            messagebox.showerror("ERROR", "ERROR")
    elif button_text == "%":
        try:
            result = eval(current_text) / 100  # Convert to percentage
            entry_var.set(result)
        except Exception:
            messagebox.showerror("ERROR", "ERROR")
    else:
        entry_var.set(current_text + button_text)

# Colors and Styling
bg_color = "#1E1E1E"          # Dark gray background
button_color = "#3A3D40"      # Soft dark gray buttons
text_color = "#FFFFFF"        # White text
hover_color = "#5A5D60"       # Lighter gray on hover

# Main Window
root = tk.Tk()
root.title("🔥 Ultra Fancy Calculator 🔥")
root.geometry("360x500")
root.configure(bg=bg_color)

root.iconbitmap("icon.ico")  

root.title("Simple Calc")
root.geometry("360x500")
root.configure(bg=bg_color)

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 26, "bold"), 
                 bg="#2A2D30", fg="white", justify='right', bd=12, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=15, pady=20, padx=15, sticky="nsew")

# Buttons Layout (Well-Organized)
buttons = [
    ("C", "(", ")", "/"),
    ("7", "8", "9", "*"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "+"),
    ("0", ".", "%", "=")
]

# Button Styling
def on_hover(event):
    event.widget.config(bg=hover_color)

def on_leave(event):
    event.widget.config(bg=button_color)

# Grid Configurations
for i in range(6):
    root.grid_rowconfigure(i + 1, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Create Buttons
for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        button = tk.Button(root, text=text, font=("Arial", 18, "bold"), width=5, height=2,
                           bg=button_color, fg=text_color, relief="raised", bd=6, 
                           activebackground=hover_color, activeforeground="white",
                           command=lambda t=text: on_click(t))
        button.grid(row=r+1, column=c, padx=5, pady=5, sticky="nsew")

        # Add hover effect
        button.bind("<Enter>", on_hover)
        button.bind("<Leave>", on_leave)

root.mainloop()
