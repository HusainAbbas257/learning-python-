import tkinter as tk

root = tk.Tk()
root.title("Entry Box Example")
root.geometry("400x200")

entry = tk.Entry(root)
entry.pack()

root.mainloop()
# this does nothing


# to add functionality:

def show_name():
    name = entry.get()
    label.config(text=f"Hello, {name}!")


root = tk.Tk()
root.title("Input Example")
root.geometry("400x250")

label = tk.Label(root, text="Write your name:", font=("Arial", 14))
label.pack()

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

button = tk.Button(root, text="Submit", command=show_name)
button.pack()

root.mainloop()

# for an ultra good user interaction we can do something
from tkinter import messagebox

def show_info():
    messagebox.showinfo("Info", "Hello, this is an info box!")

def ask_exit():
    answer = messagebox.askyesno("Exit?", "Are you sure you want to quit?")
    if answer:
        root.destroy()

root = tk.Tk()
root.title("MessageBox Demo")

btn_info = tk.Button(root, text="Show Info", command=show_info)
btn_info.pack(pady=10)

btn_exit = tk.Button(root, text="Exit", command=ask_exit)
btn_exit.pack(pady=10)

root.mainloop()
