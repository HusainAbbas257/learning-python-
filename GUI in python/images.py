import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("500x400")

img = Image.open(r"C:\Users\DELL\Desktop\learning-python-\web_scrapping\images\img_1.jpg")  # Load image
img = img.resize((200, 200))  # Optional resize
tk_img = ImageTk.PhotoImage(img)  # Convert to Tk format

label = tk.Label(root, image=tk_img)
label.pack()

root.mainloop()
