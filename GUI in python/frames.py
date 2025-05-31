import tkinter as tk

# FRAMES ARE NOTHING BUT SECTIONS OF YOUR PAGE
root = tk.Tk()
root.title("Login Form")
root.geometry("300x150")

#  Top Frame for inputs
top_frame = tk.Frame(root,bg='red')
top_frame.pack(pady=10)


tk.Label(top_frame, text="Username").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(top_frame).grid(row=0, column=1, padx=5)

tk.Label(top_frame, text="Password").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(top_frame, show="*").grid(row=1, column=1, padx=5)

#  Bottom Frame for button
bottom_frame = tk.Frame(root,bg='yellow')
bottom_frame.pack()

tk.Button(bottom_frame, text="Login").pack()

root.mainloop()

# you can also make menus
from tkinter import Menu

root = tk.Tk()
menu_bar = Menu(root)

# File Menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

# Help Menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)
root.mainloop()