import tkinter as tk
from tkinter import messagebox
import random
import json
import os
import string

# File path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASSWORD_FILE = os.path.join(BASE_DIR, 'passwords.json')

# Colors
LIGHT = "#808080"
DARK = "#434343"

# Load password data
def load_data():
    if not os.path.exists(PASSWORD_FILE):
        return {}
    with open(PASSWORD_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

# Save password data
def save_data(data):
    with open(PASSWORD_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Add new password
def add_password(name, password):
    data = load_data()
    data[name] = password
    save_data(data)

# Show all passwords
def show_passwords():
    data = load_data()
    root = tk.Tk()
    root.title("Stored Passwords")
    root.configure(bg=LIGHT)
    
    if not data:
        tk.Label(root, text="No passwords stored yet!", bg=LIGHT).pack(pady=10)
    else:
        for name, pwd in data.items():
            tk.Label(root, text=f"{name}: {pwd}", bg=LIGHT).pack(anchor='w', padx=10, pady=5)

    tk.Button(root, text="Close", command=root.destroy, bg=DARK, fg="white").pack(pady=10)
    root.mainloop()

# Generate random password
def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choices(characters, k=12))
    return password

# Save password (manual or generated)
def save_password(pre_filled_password=None):
    def submit():
        name = name_entry.get().strip()
        pwd = password_entry.get().strip()
        if not name or not pwd:
            messagebox.showerror("Error", "Both fields are required!")
            return
        add_password(name, pwd)
        messagebox.showinfo("Saved", "Password saved successfully!")
        window.destroy()

    window = tk.Tk()
    window.title("Save Password")
    window.configure(bg=LIGHT)

    tk.Label(window, text="Account Name:", bg=LIGHT).pack(pady=5)
    name_entry = tk.Entry(window, bg=DARK, fg="white")
    name_entry.pack(pady=5)

    tk.Label(window, text="Password:", bg=LIGHT).pack(pady=5)
    password_entry = tk.Entry(window, bg=DARK, fg="white")
    password_entry.pack(pady=5)

    if pre_filled_password:
        password_entry.insert(0, pre_filled_password)

    tk.Button(window, text="Save", command=submit, bg=DARK, fg="white").pack(pady=10)
    window.mainloop()

# Generate and ask to save
def generate_and_save():
    password = generate_password()
    answer = messagebox.askyesno("Save Generated Password", f"Generated Password: {password}\n\nDo you want to save it?")
    if answer:
        save_password(pre_filled_password=password)

# Main GUI
def main_window():
    root = tk.Tk()
    root.title("Simple Password Manager")
    root.configure(bg=LIGHT)

    tk.Label(root, text="Choose an option:", bg=LIGHT, font=("Arial", 14)).pack(pady=20)

    tk.Button(root, text="Generate Password", command=generate_and_save, bg=DARK, fg="white").pack(pady=10)
    tk.Button(root, text="Save Password Manually", command=lambda: save_password(), bg=DARK, fg="white").pack(pady=10)
    tk.Button(root, text="View Saved Passwords", command=show_passwords, bg=DARK, fg="white").pack(pady=10)
    tk.Button(root, text="Exit", command=root.destroy, bg=DARK, fg="white").pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_window()
