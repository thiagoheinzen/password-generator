import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
import random
import string

# Function to generate password based on user preferences
def generate_password():
    try:
        size = int(entry_length.get())

        if size < 1 or size > 30:
            messagebox.showerror("Invalid Length", "Password length must be between 1 and 30.")
            return

        characters = string.ascii_lowercase

        if var_upper.get():
            characters += string.ascii_uppercase
        if var_digits.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("No Character Set", "Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(size))
        entry_result.delete(0, END)
        entry_result.insert(0, password)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Function to copy the password to the clipboard
def copy_password():
    password = entry_result.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("No Password", "There is no password to copy.")

# === Setup main window ===
root = tb.Window(themename="flatly")
root.title("Password Generator")
root.geometry("400x360")
root.resizable(False, False)

# === Widgets ===

tb.Label(root, text="Password length (1–30):", font=("Segoe UI", 10)).pack(pady=(10, 0))
entry_length = tb.Entry(root, width=10, justify='center')
entry_length.pack(pady=(0, 10))

# Options
var_upper = tb.BooleanVar(value=True)
var_digits = tb.BooleanVar(value=True)
var_symbols = tb.BooleanVar(value=True)

tb.Checkbutton(root, text="Include uppercase letters (A–Z)", variable=var_upper, bootstyle="primary").pack(anchor='w', padx=20)
tb.Checkbutton(root, text="Include digits (0–9)", variable=var_digits, bootstyle="info").pack(anchor='w', padx=20)
tb.Checkbutton(root, text="Include symbols (!@#$...)", variable=var_symbols, bootstyle="warning").pack(anchor='w', padx=20)

# Generate button
tb.Button(root, text="Generate Password", command=generate_password, bootstyle="success").pack(pady=15)

# Output
tb.Label(root, text="Generated password:").pack()
entry_result = tb.Entry(root, width=40, justify='center')
entry_result.pack(pady=(0, 5))

# Copy button
tb.Button(root, text="Copy Password", command=copy_password, bootstyle="secondary").pack(pady=5)

# Run the app
root.mainloop()
