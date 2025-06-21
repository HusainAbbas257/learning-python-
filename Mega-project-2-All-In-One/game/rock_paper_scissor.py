import tkinter as tk
import random

def rock_paper_scissors():
    # Constants
    BG_COLOR = "#1F1F1F"
    BTN_COLOR = "#3A3A3A"
    HOVER_COLOR = "#5A5A5A"
    TEXT_COLOR = "#FFFFFF"
    ACCENT_COLOR = "#00FFAB"
    EXIT_HOVER_COLOR = "#FF4C4C"
    FONT = ("Segoe UI", 16, "bold")
    BIG_FONT = ("Segoe UI", 24, "bold")

    user_score, comp_score = 0, 0

    # Logic
    def get_winner(player, computer):
        if player == computer:
            return "Draw"
        elif (player == "Rock" and computer == "Scissors") or \
             (player == "Paper" and computer == "Rock") or \
             (player == "Scissors" and computer == "Paper"):
            return "You Win!"
        return "You Lose!"

    def play(player_choice):
        nonlocal user_score, comp_score
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = get_winner(player_choice, computer_choice)

        user_label.config(text=f"You: {player_choice}")
        comp_label.config(text=f"Computer: {computer_choice}")
        result_label.config(text=result)

        if result == "You Win!":
            user_score += 1
        elif result == "You Lose!":
            comp_score += 1

        score_label.config(text=f"Score: You {user_score} - {comp_score} Computer")

    # Button creation
    def create_button(text):
        btn = tk.Button(btn_frame, text=text, font=FONT, bg=BTN_COLOR, fg=TEXT_COLOR, width=10, height=2,
                        activebackground=HOVER_COLOR, activeforeground=ACCENT_COLOR,
                        command=lambda: play(text))
        btn.pack(side="left", padx=15)
        btn.bind("<Enter>", lambda e: e.widget.config(bg=HOVER_COLOR))
        btn.bind("<Leave>", lambda e: e.widget.config(bg=BTN_COLOR))
        return btn

    # Window
    root = tk.Tk()
    root.title("Rock Paper Scissors - Ultra Modern Edition")
    root.config(bg=BG_COLOR)
    root.geometry("500x500")
    root.resizable(False, False)

    # Widgets
    tk.Label(root, text="Rock Paper Scissors", bg=BG_COLOR, fg=ACCENT_COLOR, font=BIG_FONT).pack(pady=30)

    score_label = tk.Label(root, text="Score: You 0 - 0 Computer", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
    score_label.pack(pady=10)

    user_label = tk.Label(root, text="You: ", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
    user_label.pack(pady=5)
    comp_label = tk.Label(root, text="Computer: ", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
    comp_label.pack(pady=5)
    result_label = tk.Label(root, text="", bg=BG_COLOR, fg=ACCENT_COLOR, font=BIG_FONT)
    result_label.pack(pady=20)

    btn_frame = tk.Frame(root, bg=BG_COLOR)
    btn_frame.pack(pady=20)

    for choice in ["Rock", "Paper", "Scissors"]:
        create_button(choice)

    # Exit Button
    exit_btn = tk.Button(root, text="Exit", font=FONT, bg=BTN_COLOR, fg="red", width=10, height=1, command=root.destroy)
    exit_btn.pack(pady=20)
    exit_btn.bind("<Enter>", lambda e: e.widget.config(bg=EXIT_HOVER_COLOR))
    exit_btn.bind("<Leave>", lambda e: e.widget.config(bg=BTN_COLOR))

    root.mainloop()

if __name__ == "__main__":
    rock_paper_scissors()
