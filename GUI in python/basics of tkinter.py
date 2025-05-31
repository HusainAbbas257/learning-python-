import tkinter as tk

# Create the window
root = tk.Tk()

# Title & size
root.title("My first  GUI")
root.geometry("400x300")

# Run the app
root.mainloop()





# you can also add a lable as

root = tk.Tk()
root.title("Label Example")
root.geometry("400x200")

# Make a label
label = tk.Label(root, text="Hello Husain Abbas", font=("Arial", 16),bg='black',fg='white')
label.pack()  # Show it on the window

root.mainloop()
