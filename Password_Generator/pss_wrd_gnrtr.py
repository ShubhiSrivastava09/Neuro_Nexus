import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate a password
def generate_password(length, use_uppercase, use_digits, use_special):
    characters = string.ascii_lowercase  # Always include lowercase letters

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if len(characters) == 0:
        messagebox.showwarning("Warning", "Please select at least one character type.")
        return ""

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to handle button click
def on_generate_click():
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError("Length must be at least 1.")
        use_uppercase = uppercase_var.get()
        use_digits = digits_var.get()
        use_special = special_var.get()

        password = generate_password(length, use_uppercase, use_digits, use_special)
        password_display.config(state=tk.NORMAL)
        password_display.delete(0, tk.END)
        password_display.insert(0, password)
        password_display.config(state=tk.DISABLED)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x300")
app.config(bg="#f0f0f0")

# Label for password length
length_label = tk.Label(app, text="Password Length:", bg="#f0f0f0")
length_label.pack(pady=10)

# Entry for password length
length_entry = tk.Entry(app, width=5)
length_entry.pack(pady=5)

# Checkboxes for character types
uppercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

uppercase_checkbox = tk.Checkbutton(app, text="Include Uppercase Letters", variable=uppercase_var, bg="#f0f0f0")
uppercase_checkbox.pack(pady=5)

digits_checkbox = tk.Checkbutton(app, text="Include Digits", variable=digits_var, bg="#f0f0f0")
digits_checkbox.pack(pady=5)

special_checkbox = tk.Checkbutton(app, text="Include Special Characters", variable=special_var, bg="#f0f0f0")
special_checkbox.pack(pady=5)

# Button to generate password
generate_button = tk.Button(app, text="Generate Password", command=on_generate_click, bg="#4CAF50", fg="white")
generate_button.pack(pady=20)

# Entry to display generated password
password_display = tk.Entry(app, width=30, state=tk.DISABLED)
password_display.pack(pady=5)

# Start the application
app.mainloop()
