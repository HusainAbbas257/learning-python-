import tkinter as tk

light = "#5BD57E"
dark = "#2F7B45"
equation = []
solution = 0.0

def on_enter(button):
    button.config(bg=dark)

def on_leave(button):
    button.config(bg=light)

def calculator():
    widgets = []
    root = tk.Tk()
    root.title('Calculator')
    root.config(bg=light)

    title = tk.Label(root, text='Enter the equation and get the answer', bg=light)
    title.pack(pady=20)
    widgets.append(title)

    answer = tk.Label(root, text=f'answer={solution}', bg=light)
    answer.pack(pady=10)
    widgets.append(answer)

    question = tk.Label(root, text=f'({''.join(equation)})', bg=light)
    question.pack(pady=10)
    widgets.append(question)

    def action(btn):
        global solution
        if btn == '=':
            try:
                solution = eval(''.join(equation))
            except Exception:
                solution = 'syntax error'
            answer.config(text=f'answer={solution}')
        elif btn == 'x':
            if equation:
                equation.pop()
            question.config(text=f"({''.join(equation)})")
        else:
            equation.append(btn)
            question.config(text=f"({''.join(equation)})")

    bframe = tk.Frame(root, bg=light)
    buttons = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', "/", '//', '(', ')', '.', 'x', '=']
    for i in range(4):
        for j in range(5):
            if buttons:
                button = buttons.pop(0)
                b = tk.Button(bframe, text=button, bg=light, command=lambda b=button: action(b))
                b.grid(row=i, column=j, padx=10, pady=10)
                widgets.append(b)
    bframe.pack()

    for b in widgets:
        b.bind('<Enter>', lambda e, b=b: on_enter(b))
        b.bind('<Leave>', lambda e, b=b: on_leave(b))

    root.mainloop()

if __name__ == '__main__':
    calculator()
