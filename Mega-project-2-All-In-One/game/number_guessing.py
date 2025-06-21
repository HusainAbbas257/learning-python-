import tkinter as tk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

light = "#5BD57E"
dark = "#2F7B45"

# Global variables
start = 0
end = 100
spacing = 1
number_to_guess = None

def on_enter(e):
    e.widget.config(bg=dark, fg="white")

def on_leave(e):
    e.widget.config(bg=light, fg="black")

def start_game():
    guesses = []

    global number_to_guess
    number_to_guess = random.randrange(start, end, spacing)

    root = tk.Tk()
    root.title("Guessing Game with Live Graph (Matplotlib)")
    root.configure(bg=light)

    fig, ax = plt.subplots()
    ax.set_ylim(start, end)
    ax.set_xlabel("Attempt")
    ax.set_ylabel("Guess Value")

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    label = tk.Label(root, text=f"Enter your guess ({start}-{end}):", bg=light, fg="black")
    label.pack(pady=5)

    entry = tk.Entry(root, bg=light, fg="black", insertbackground="black")
    entry.pack(pady=5)

    result_label = tk.Label(root, text="", bg=light, fg="black")
    result_label.pack(pady=5)

    def submit_guess():
        try:
            guess = int(entry.get())
            guesses.append(guess)

            ax.clear()
            ax.set_ylim(start, end)
            ax.set_xlabel("Attempt")
            ax.set_ylabel("Guess Value")
            ax.plot(range(1, len(guesses) + 1), guesses, marker='o', linestyle='-')
            canvas.draw()

            if guess == number_to_guess:
                result_label.config(text=f"Correct! The number was {number_to_guess}")
            elif guess < number_to_guess:
                result_label.config(text="Too Low!")
            else:
                result_label.config(text="Too High!")
        except ValueError:
            result_label.config(text="Enter a valid integer!")

    button = tk.Button(root, text="Submit", command=submit_guess, bg=light, fg="black", activebackground=dark, activeforeground="white")
    button.pack(pady=10)

    # Hover effect
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    root.mainloop()

def game():
    game_win = tk.Tk()
    game_win.title("Game Settings")
    game_win.configure(bg=light)

    lbl1 = tk.Label(game_win, text='Enter Starting Point', bg=light, fg="black")
    lbl1.pack(pady=5)

    scale1 = tk.Scale(game_win, from_=0, to=1000, orient=tk.HORIZONTAL, bg=light, fg="black", troughcolor=dark)
    scale1.pack(pady=5)

    lbl2 = tk.Label(game_win, text='Enter Ending Point', bg=light, fg="black")
    lbl2.pack(pady=5)

    scale2 = tk.Scale(game_win, from_=0, to=1000, orient=tk.HORIZONTAL, bg=light, fg="black", troughcolor=dark)
    scale2.pack(pady=5)

    lbl3 = tk.Label(game_win, text='Enter Steps/Spacing', bg=light, fg="black")
    lbl3.pack(pady=5)

    scale3 = tk.Scale(game_win, from_=1, to=100, orient=tk.HORIZONTAL, bg=light, fg="black", troughcolor=dark)
    scale3.pack(pady=5)

    def set_values_and_start():
        global start, end, spacing
        start = scale1.get()
        end = scale2.get()
        spacing = scale3.get()

        game_win.destroy()
        start_game()

    btn = tk.Button(game_win, text="Start Game", command=set_values_and_start, bg=light, fg="black", activebackground=dark, activeforeground="white")
    btn.pack(pady=10)

    # Hover effect
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    game_win.mainloop()

if __name__ == '__main__':
    game()
