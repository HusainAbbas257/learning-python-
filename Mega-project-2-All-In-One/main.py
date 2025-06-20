import tkinter as tk
import pyautogui as pg
screen_size=pg.size()
size=f'{screen_size[0]}x{screen_size[1]}'
light="#8002D4"
dark="#580092"

root =tk.Tk()
root.title('All In One App')
root.geometry(size)
root.config(bg=light)

def on_enter(button):
    button.config(bg=dark)

def on_leave(button):
    button.config(bg=light)

def tools_window():
    troot=tk.Toplevel(root)
    # troot.geometry(size)
    troot.title('Tools window')
    troot.config(bg=light)
    heading=tk.Label(troot,text='please select a tool to test',bg=light)
    heading.grid(row=1,column=1)
    buttons=['calculator','unit-converter','password-generator','to do list','contact-book','expences-tracker','password-manager','weathedr app','currency-converter','news-app','clock','financial dashboard','web-crawler','email-automation','downlowder','search engine']
    btns=[heading,]
    for i in range(3,7):
        for j in range(4):
            button =buttons[0]
            buttons.remove(button)
            b=tk.Button(troot,text=button,bg=light)
            b.grid(row=i,column=j,padx=10,pady=10)
            btns.append(b)
    for b in btns:
        b.bind('<Enter>',lambda e,b=b: on_enter(b))
        b.bind('<Leave>',lambda e,b=b: on_leave(b))
def game_window():
    groot = tk.Toplevel(root)
    groot.title('Games Window')
    groot.config(bg=light)
    heading = tk.Label(groot, text='Please select a game to play', bg=light, font='ariel')
    heading.grid(row=1, column=1, pady=20)
    
    games = [
        'Number Guessing Game', 'Rock Paper Scissors', 'Mad Libs Generator', 'Dice Rolling Simulator',
        'Hangman Game', 'Tic-Tac-Toe with AI', 'Text-based Adventure Game', 'Simple Quiz Game',
        'Basic Paint Program', 'Coin Toss Simulation', 'I Can Guess What You Think',
        'Funny Answer Maker', 'Word Jumble', 'Simple Slot Machine', 'Typing Speed Test'
    ]
    
    btns = [heading,]
    
    for i in range(3, 7):  # 4 rows
        for j in range(4):  # 4 columns
            if games:  # make sure list isn't empty
                game = games.pop(0)
                b = tk.Button(groot, text=game, bg=light)
                b.grid(row=i, column=j, padx=10, pady=10)
                btns.append(b)
    
    for b in btns:
        b.bind('<Enter>', lambda e, b=b: on_enter(b))
        b.bind('<Leave>', lambda e, b=b: on_leave(b))
    
        




tk.Label(root,text='!Welcome to All in one App!\nPlease select the Cotegory you want to explore',bg=light,font='ariel').pack(pady=100)

tools_button=tk.Button(root,text='TOOLS',width=20,height=5,bg=light,command=tools_window)
tools_button.pack(pady=10)
games_Button=tk.Button(root,text='GAMES',width=20,height=5,bg=light,command=game_window)
games_Button.pack(pady=10)

tools_button.bind('<Enter>',lambda e: on_enter(tools_button))
tools_button.bind('<Leave>',lambda e: on_leave(tools_button))
games_Button.bind('<Enter>',lambda e: on_enter(games_Button))
games_Button.bind('<Leave>',lambda e: on_leave(games_Button))

root.mainloop()