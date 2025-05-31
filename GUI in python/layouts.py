import tkinter as tk
# creating a basic adder to show layout functionality;
root=tk.Tk()
root.title("layout Example")
root.geometry("400x250")
instruction=tk.Label(root,text='ENTER TWO NUMBERS:')
instruction.pack()
num1=tk.Entry(root)
num1.pack()
num2=tk.Entry(root)
num2.pack()
answer=tk.Label(root,text='')
def add():
    n1,n2=float(num1.get()),float(num2.get())
    answer.config(text=f'Answer={n1+n2}')
    answer.pack()
button=tk.Button(root,text='add',command=add)
button.pack()
root.mainloop()



# by pack every thing is arranged top to bottom we can costumisse it 
root=tk.Tk()
root.title("layout Example")
root.geometry("400x250")
instruction=tk.Label(root,text='ENTER TWO NUMBERS:')
instruction.pack(side="top", fill="x", padx=5, pady=5)

num1=tk.Entry(root)
num1.pack(side='left',padx=5,pady=5)
num2=tk.Entry(root)
num2.pack(side='right',padx=5,pady=5)
answer=tk.Label(root,text='')
def add():
    n1,n2=float(num1.get()),float(num2.get())
    answer.config(text=f'Answer={n1+n2}')
    answer.pack(side='bottom')
button=tk.Button(root,text='add',command=add)
button.pack(side='bottom',padx=15,pady=15)
root.mainloop()

# for better readability we can arrande thing into row and coloumns:
root=tk.Tk()
root.title("layout Example")
root.geometry("400x250")
instruction=tk.Label(root,text='ENTER TWO NUMBERS:')
instruction.grid(row=1,column=2)

num1=tk.Entry(root)
num1.grid(row=2,column=1)
num2=tk.Entry(root)
num2.grid(row=2,column=3)
answer=tk.Label(root,text='')
def add():
    n1,n2=float(num1.get()),float(num2.get())
    answer.config(text=f'Answer={n1+n2}')
    answer.grid(row=6,column=2)
button=tk.Button(root,text='add',command=add)
button.grid(row=5,column=2)
root.mainloop()