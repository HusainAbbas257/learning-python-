import tkinter as tk

root = tk.Tk()
root.title("Button Example")
root.geometry("400x200")

button = tk.Button(root, text="Click Me Bro!")
button.pack()

root.mainloop()


# to add some command on button press we can do so as:
def clicked():
    label=tk.Label(root,text='"Button clicked!"')
    label.pack()

root = tk.Tk()
root.title("Action Button")
root.geometry("400x200")

button = tk.Button(root, text="Click Me!", command=clicked)
button.pack()

root.mainloop()

# you can change attributes of a perticular element  by config method
def change_text():
    label.config(text="Button Pressed")
    button.config(text='pressed',bg='black',fg='white')

root = tk.Tk()
root.title("Button + Label")
root.geometry("400x200")

label = tk.Label(root, text="change me ", font=("Arial", 16))
label.pack()

button = tk.Button(root, text="Click to Change", command=change_text)
button.pack()

root.mainloop()

#  we can also add some cool effects to our butten as
root = tk.Tk()
root.title("Button + Label")
root.geometry("400x200")
def on_enter(e):
    my_btn.config(bg="darkgreen")

def on_leave(e):
    my_btn.config(bg="green")

my_btn = tk.Button(root, text="Hover Me", bg="green", fg="white")
my_btn.pack()

# we use bind to assign a specific function to a event.the function must have a event argument with its own specifications
# here is a list of events:
# Event Name->	Trigger
# <Button-1>	Left mouse click
# <Button-2>	Middle click (scroll wheel)
# <Button-3>	Right click
# <Double-Button-1>	Double left click
# <Enter>	Mouse entered widget
# <Leave>	Mouse left widget
# <Key>	Any key pressed
# <KeyPress-a>	Specific key pressed (e.g. 'a')
# <FocusIn>	Widget got focus
# <FocusOut>	Widget lost focus
my_btn.bind("<Enter>", on_enter)
my_btn.bind("<Leave>", on_leave)
root.mainloop()


# from above u can also make a cool prank like:

root = tk.Tk()
root.title("Button + Label")
root.geometry("1000x1000")
def on_enter(e):
    my_btn.config(bg="darkgreen")

def on_leave(e):
    my_btn.config(bg="green")

my_btn = tk.Button(root, text="Click me if you can", bg="green", fg="white")
import random

def move(event):
    my_btn.place(x=random.randint(0,1000),y=random.randint(0,100))
my_btn.place(x=random.randint(0,1000),y=random.randint(0,1000))
my_btn.bind("<Enter>", move)
root.mainloop()

# you can also make a yes no button

root = tk.Tk()

var = tk.IntVar()  # 0 = unchecked, 1 = checked

chk = tk.Checkbutton(root, text="I agree", variable=var)
chk.pack()

def show_state():
    chk.config(text="Checked?" if var.get() else "Not checked")

btn = tk.Button(root, text="Check state", command=show_state)
btn.pack()

root.mainloop()
#  we can also add some radio buttons as:
root = tk.Tk()
root.geometry('500x500')
choice = tk.StringVar(value="Option1")

r1 = tk.Radiobutton(root, text="Option 1", variable=choice, value="Option1")
r2 = tk.Radiobutton(root, text="Option 2", variable=choice, value="Option2")

r1.pack()
r2.pack()
out=tk.Label(root,text='')
def show_choice():
    out.config(text=("Selected:"+ choice.get()))
    out.pack()

btn = tk.Button(root, text="Show Choice", command=show_choice)
btn.pack()

root.mainloop()

# or a scale
root = tk.Tk()

scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack()
out=tk.Label(root,text='')
def show_value():
    out.config(text=f"Slider value:{scale.get()}" )
    out.pack()

btn = tk.Button(root, text="Show Value", command=show_value)
btn.pack()

root.mainloop()

# or a list box:
root = tk.Tk()

listbox = tk.Listbox(root)
listbox.pack()
for item in ["Apple", "Banana", "Cherry"]:
    listbox.insert(tk.END, item)
out=tk.Label(root,text='')
def show_selection():
    selected = listbox.curselection()
    for i in selected:
        out.config(text=listbox.get(i))
        out.pack()

btn = tk.Button(root, text="Show Selected", command=show_selection)
btn.pack()

root.mainloop()

# you can also create a popup as:
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def popup():
    messagebox.showinfo("Hey!", "This is a popup!")

btn = tk.Button(root, text="Show Popup", command=popup)
btn.pack()

root.mainloop()
