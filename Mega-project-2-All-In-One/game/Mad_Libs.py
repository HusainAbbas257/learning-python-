import tkinter as tk
from tkinter import messagebox
import random

# Colors
LIGHT = "#808080"
DARK = "#434343"

templates = [
    "One day, in the {place}, a {adjective} {animal} saw a {noun}.\nIt {verb} towards the {object} very {adverb}.\nSuddenly, the {object} started twerking aggressively.\nThe {animal} couldn't believe its third eye.\nIn the end, everything turned into a cheese pizza.",

    "In the {place}, there was a {adjective} {noun}.\nA {animal} {verb} near it {adverb}.\nThe {object} farted and rolled down the hill like a drunk potato.\nPeople watched in complete brain damage.\nFinally, the mystery was solved by a confused chicken.",

    "Every night, the {adjective} {animal} visited the {place}.\nIt would {verb} around the {object} {adverb}.\nThe moonlight made the {noun} do a backflip.\nSuddenly, a loud burp broke the silence.\nBut the {animal} kept watching, sipping its invisible coffee.",

    "The {place} was silent, only the {adjective} {animal} was awake.\nIt {verb} the {object} {adverb}.\nA {noun} appeared out of nowhere wearing sunglasses.\nWind howled like an emotional tiktoker.\nThe {animal} disappeared into a microwave.",

    "Long ago, in the {place}, a {noun} was guarded by a {adjective} {animal}.\nIt would {verb} anyone who came near {object}, {adverb} and doing Fortnite dances.\nOne day, a traveler appeared riding a rubber duck.\nBut the {animal} allowed him to pass after a staring contest.\nThe legend became true and Netflix made a documentary.",

    "At dawn, the {adjective} {animal} entered the {place}.\nIt {verb} near the {object} {adverb}.\nThe {noun} floated in mid-air like a confused balloon.\nEverything froze like my brain during exams.\nThen reality twisted into a giant spaghetti monster.",

    "In the {place}, a {adjective} {noun} was cursed.\nThe {animal} {verb} to protect the {object} {adverb}.\nStorm clouds gathered while playing sad violin music.\nThe ground started moonwalking.\nBut fate changed everything when a flying toaster appeared.",

    "The {adjective} {animal} lived alone in the {place}.\nEvery day, it would {verb} the {object} {adverb}.\nOne day, the {noun} spoke in autotune.\n\"Your destiny awaits at McDonald's.\"\nThe {animal} finally understood it was a sandwich.",

    "Deep in the {place}, a {adjective} {animal} guarded a {noun}.\nIt {verb} around the {object} {adverb}.\nAn explorer arrived, trembling like a vibrating phone.\nThe {animal} stared without blinking like a psycho anime villain.\nAnd the journey ended before it even loaded.",

    "The {place} held a terrible secret: the {adjective} {animal}.\nIt {verb} the {object} {adverb} every full moon.\nThe {noun} glimmered like a disco ball on steroids.\nNo one dared to enter except a brave goldfish.\nBut some stories never die, unlike my wifi connection."
]


def generate(rt,values):
    if "" in values:
        messagebox.showerror("Error", "Please fill all the fields!")
        return
        
        
    root=tk.Toplevel(rt)
    root.title('Madlibs: the fun story game')
    root.configure(bg=LIGHT)

    story=random.choice(templates)
    story=story.format(
        place=values[0],
        adjective=values[1],
        animal=values[2],
        noun=values[3],
        verb=values[4],
        object=values[5],
        adverb=values[6],
    )
    
    tk.Label(root,text=story,bg=LIGHT,font=('Comic Sans MS',20),wraplength=700).pack(padx=20,pady=20)

def on_enter(button):
    button.config(bg=DARK)

def on_leave(button):
    button.config(bg=LIGHT)

def start():
    root=tk.Tk()
    root.title('Madlibs: the fun story game')
    root.configure(bg=LIGHT)

    tk.Label(root,text='!WELCOME!\n!PLEASE ENTER THE VALUES TO GET A STORY!',bg=LIGHT).pack(pady=20)
    fields_frame=tk.Frame(root,bg=LIGHT)
    fields_frame.pack(pady=10)

    widgets=[]
    fields=[]
    blanks=['place','adjective','animal','noun','verb','object','adverb']
    

    for i,blank in enumerate(blanks):
        label=tk.Label(fields_frame,text=f'please enter {blank}',bg=LIGHT)
        label.grid(row=i,column=1,padx=5,pady=10)
        widgets.append(label)
        entry=tk.Entry(fields_frame,bg=LIGHT)
        entry.grid(row=i,column=2,padx=20,pady=5)
        widgets.append(entry)
        fields.append(entry)
    
    submit=tk.Button(root,text='Submit',command=lambda e=0:generate(root,[f.get() for f in fields]),bg=LIGHT)
    widgets.append(submit)
    submit.pack()
    
    for b in widgets:
        b.bind('<Enter>', lambda e, b=b: on_enter(b))
        b.bind('<Leave>', lambda e, b=b: on_leave(b))

    root.mainloop()

if __name__=='__main__':    
    start()

        



