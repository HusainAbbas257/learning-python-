import tkinter as tk 

light="#808080"
dark="#434343"
def calculate(label, from_, magnitude, to):
    conversions = {
        # Volume
        ("Litre", "mililitre"): 1000,
        ("mililitre", "Litre"): 0.001,
        ("Litre", "centimeter  cube"): 1000,
        ("centimeter  cube", "Litre"): 0.001,
        ("Litre", "meter cube"): 0.001,
        ("meter cube", "Litre"): 1000,
        ("centimeter  cube", "meter cube"): 1e-6,
        ("meter cube", "centimeter  cube"): 1e6,

        # Weight
        ("gram", "miligram"): 1000,
        ("miligram", "gram"): 0.001,
        ("gram", "kilogram"): 0.001,
        ("kilogram", "gram"): 1000,
        ("kilogram", "pound"): 2.20462,
        ("pound", "kilogram"): 0.453592,
        ("kilogram", "ounce"): 35.274,
        ("ounce", "kilogram"): 0.0283495,

        # Length
        ("centimeter", "metre"): 0.01,
        ("metre", "centimeter"): 100,
        ("metre", "kilometre"): 0.001,
        ("kilometre", "metre"): 1000,
        ("metre", "foot"): 3.28084,
        ("foot", "metre"): 0.3048,
        ("metre", "inch"): 39.3701,
        ("inch", "metre"): 0.0254,

        # Area
        ("metre square", "centimeter square"): 10000,
        ("centimeter square", "metre square"): 0.0001,
        ("metre square", "kilometer square"): 1e-6,
        ("kilometer square", "metre square"): 1e6,
        ("kilometer square", "acre"): 247.105,
        ("acre", "kilometer square"): 0.00404686,
        ("kilometer square", "hectare"): 100,
        ("hectare", "kilometer square"): 0.01,
    }

    key = (from_, to)
    if key in conversions:
        result = magnitude * conversions[key]
        label.config(text=f'{magnitude} {from_} = {result} {to}')
    elif from_ == to:
        label.config(text=f'{magnitude} {from_} = {magnitude} {to}')
    else:
        label.config(text="Conversion not available yet.")

def volume(rt):
    root=tk.Toplevel(rt)
    root.title('volume converter')
    # root.geometry('550x500')
    root.configure(bg=light)
    units=["Litre", "mililitre", "centimeter  cube","meter cube"]
    tk.Label(root,text='select the unit from which u want to convert',bg=light).pack()

    _from=[]
    from_frame=tk.Frame(root)
    for i in range(len(units)):
        tk.Button(from_frame, text=units[i],command=lambda u=units[i]: _from.append(u) ).grid(row=0,column=i)
    from_frame.pack()
    magnitude= tk.Entry(root, bg=light, fg="black")
    magnitude.pack(pady=5)
    tk.Label(root,text='select the unit to which u want to convert',bg=light).pack()
    
    to=[]
    to_frame=tk.Frame(root)
    for i in range(len(units)):
        tk.Button(to_frame, text=units[i],command=lambda u=units[i]: to.append(u)).grid(row=0,column=i)
    to_frame.pack() 
    answer=tk.Label(root,text=f'',bg=light)
    answer.pack()
    tk.Button(root, text="start conversion", command=lambda e=0: calculate(answer,_from.pop(),float(magnitude.get()),to.pop())).pack()

    root.mainloop()
def weight(rt):
    root=tk.Toplevel(rt)
    root.title('volume converter')
    # root.geometry('550x500')
    root.configure(bg=light)
    units=["gram", "miligram", "kilogram", "pound","ounce"]
    tk.Label(root,text='select the unit from which u want to convert',bg=light).pack()

    _from=[]
    from_frame=tk.Frame(root)
    for i in range(len(units)):
        tk.Button(from_frame, text=units[i],command=lambda u=units[i]: _from.append(u) ).grid(row=0,column=i)
    from_frame.pack()
    magnitude= tk.Entry(root, bg=light, fg="black")
    magnitude.pack(pady=5)
    tk.Label(root,text='select the unit to which u want to convert',bg=light).pack()
    
    to=[]
    to_frame=tk.Frame(root)
    for i in range(len(units)):
        tk.Button(to_frame, text=units[i],command=lambda u=units[i]: to.append(u)).grid(row=0,column=i)
    to_frame.pack() 
    answer=tk.Label(root,text=f'',bg=light)
    answer.pack()
    tk.Button(root, text="start conversion", command=lambda e=0: calculate(answer,_from.pop(),float(magnitude.get()),to.pop())).pack()

    root.mainloop()
def length(rt):
    root=tk.Toplevel(rt)
    root.title('volume converter')
    # root.geometry('550x500')
    root.configure(bg=light)
    units=['centimeter','metre','kilometre','foot','inch']
    tk.Label(root,text='select the unit from which u want to convert',bg=light).pack()

    _from=[]
    from_frame=tk.Frame(root)
    for i in range(len(units)):
        tk.Button(from_frame, text=units[i],command=lambda u=units[i]: _from.append(u) ).grid(row=0,column=i)
    from_frame.pack()
    magnitude= tk.Entry(root, bg=light, fg="black")
    magnitude.pack(pady=5)
    tk.Label(root,text='select the unit to which u want to convert',bg=light).pack()
    
    to=[]
    to_frame=tk.Frame(root)
    for i in range(len(units)):
        tk.Button(to_frame, text=units[i],command=lambda u=units[i]: to.append(u)).grid(row=0,column=i)
    to_frame.pack() 
    answer=tk.Label(root,text=f'',bg=light)
    answer.pack()
    tk.Button(root, text="start conversion", command=lambda e=0: calculate(answer,_from.pop(),float(magnitude.get()),to.pop())).pack()

    root.mainloop()
def Area(rt):
    root=tk.Toplevel(rt)
    root.title('volume converter')
    # root.geometry('550x500')
    root.configure(bg=light)
    units=['metre square','centimeter square','kilometer square','acre','hectare']
    tk.Label(root,text='select the unit from which u want to convert',bg=light).pack()

    _from=[]
    from_frame=tk.Frame(root)
    for i in range(len(units)):
        tk.Button(from_frame, text=units[i],command=lambda u=units[i]: _from.append(u) ).grid(row=0,column=i)
    from_frame.pack()
    magnitude= tk.Entry(root, bg=light, fg="black")
    magnitude.pack(pady=5)
    tk.Label(root,text='select the unit to which u want to convert',bg=light).pack()
    
    to=[]
    to_frame=tk.Frame(root)
    for i in range(len(units)):
        tk.Button(to_frame, text=units[i],command=lambda u=units[i]: to.append(u)).grid(row=0,column=i)
    to_frame.pack() 
    answer=tk.Label(root,text=f'',bg=light)
    answer.pack()
    tk.Button(root, text="start conversion", command=lambda e=0: calculate(answer,_from.pop(),float(magnitude.get()),to.pop())).pack()

    root.mainloop()
def start():

    root=tk.Tk()
    root.title('Unit converter')
    root.geometry('550x500')
    root.configure(bg=light)
    listbox = tk.Listbox(root)
    listbox.pack()
    tools=["volume", "weight", "length","Area"]
    for item in tools:
        listbox.insert(tk.END, item)

    def show_selection():
        selected = listbox.curselection()[0]
        match selected:
            case 0:
                volume(root)
            case 1:
                weight(root)
            case 2:
                length(root)
            case 3:
                Area(root)
            case _:
                print('wtf is:',selected)
            

    btn = tk.Button(root, text="start conversion", command=show_selection)
    btn.pack()

    root.mainloop()


start()