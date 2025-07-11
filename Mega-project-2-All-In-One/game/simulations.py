import tkinter as tk
from tkinter import messagebox
import random

# Colors
LIGHT = "#808080"
DARK = "#434343"

def toss():
    messagebox.showinfo("coin tossed!", f"coin is tossed ! and you got ...\n\t{random.choice(['HEAD','TAILS'])}")
    

def roll():
    messagebox.showinfo("dice rolled!", f"dice is rolled! and you got ...\n\t{random.randint(1,6)}")

def spin():
    root=tk.Toplevel()
    root.title('spin the wheel')
    data=[]
    label=tk.Label(root,text=f'please enter the contents of spin',bg=LIGHT)
    label.pack(pady=10)
    entry=tk.Entry(root,bg=LIGHT)
    entry.pack(pady=20)
    tk.Button(root,text='Submit',command=lambda e=0:data.append(entry.get()),bg=LIGHT).pack(padx=10,pady=10)
    tk.Button(root,text='SPIN',command=lambda s=data:messagebox.showinfo("whell spinned!", f"WHEEL IS SPINNED! and you got ...\n\t{random.choice(s)}"),bg=LIGHT).pack(padx=10,pady=10)

def start():
    root=tk.Tk()
    root.title('Probability Simulator')
    root.config(bg=LIGHT)
    
    tk.Label(root,text='!WELCOME!\nPlEASE SELECT THE CHOICE',bg=LIGHT).pack(pady=50)

    tk.Button(root,text='Toss coins',command=toss,bg=LIGHT).pack(padx=10,pady=10)

    tk.Button(root,text='roll Dice',command=roll,bg=LIGHT).pack(padx=10,pady=10)
 
    tk.Button(root,text='spin the wheel',command=spin,bg=LIGHT).pack(padx=10,pady=10)

    root.mainloop()

if __name__=='__main__':    
    start()

        
