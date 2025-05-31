import tkinter as tk

# canvas is a place to draw
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Draw a rectangle (x1, y1, x2, y2)
canvas.create_rectangle(50, 50, 150, 100, fill="blue")

# Draw a circle using oval (x1, y1, x2, y2)
canvas.create_oval(200, 50, 300, 150, fill="red")

root.mainloop()

# giving it some animation:

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack()

# Draw a ball (circle)
ball = canvas.create_oval(10, 10, 50, 50, fill="blue")

def move_ball():
    canvas.move(ball, 5, 0)  # Move right by 5 pixels
    root.after(50, move_ball)  # Call this function again after 50ms

move_ball()
root.mainloop()


# we can also give it a bounce animation as:

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack()

ball = canvas.create_oval(10, 10, 50, 50, fill="red")
dx = 5
dy = 3

def move_ball():
    global dx, dy
    canvas.move(ball, dx, dy)
    pos = canvas.coords(ball)  # [x1, y1, x2, y2]
    if pos[2] >= 500 or pos[0] <= 0:
        dx = -dx  # Reverse horizontal direction
    if pos[3] >= 300 or pos[1] <= 0:
        dy = -dy  # Reverse vertical direction
    root.after(50, move_ball)

move_ball()
root.mainloop()



# you can also redirect balls movement  with keys

# Setup
root = tk.Tk()
root.title("Ball Control Game")
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

# Create the ball
ball = canvas.create_oval(230, 180, 270, 220, fill="red")

# Move function
def move_ball(event):
    if event.keysym == "Up":
        canvas.move(ball, 0, -10)
    elif event.keysym == "Down":
        canvas.move(ball, 0, 10)
    elif event.keysym == "Left":
        canvas.move(ball, -10, 0)
    elif event.keysym == "Right":
        canvas.move(ball, 10, 0)

# Bind arrow keys
root.bind("<Up>", move_ball)
root.bind("<Down>", move_ball)
root.bind("<Left>", move_ball)
root.bind("<Right>", move_ball)

root.mainloop()


# afterr using ur brain a little;

root = tk.Tk()
root.title("Ball Game ++")
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

# Ball and Goal
ball = canvas.create_oval(230, 180, 270, 220, fill="red")
goal = canvas.create_oval(400, 300, 440, 340, fill="green")  # goal area

# Movement config
speed = 10
boost_speed = 20
current_speed = speed

# Ball movement logic
def move_ball(event):
    global current_speed
    x1, y1, x2, y2 = canvas.coords(ball)

    dx = dy = 0
    if event.keysym == "Up":
        dy = -current_speed
    elif event.keysym == "Down":
        dy = current_speed
    elif event.keysym == "Left":
        dx = -current_speed
    elif event.keysym == "Right":
        dx = current_speed

    # Boundary check
    if x1 + dx < 0 or x2 + dx > 500:
        dx = 0
    if y1 + dy < 0 or y2 + dy > 400:
        dy = 0

    canvas.move(ball, dx, dy)
    check_goal()

# Boost logic
def boost_on(event):
    global current_speed
    current_speed = boost_speed

def boost_off(event):
    global current_speed
    current_speed = speed

# Goal detection
def check_goal():
    ball_coords = canvas.coords(ball)
    goal_coords = canvas.coords(goal)
    if (ball_coords[0] < goal_coords[2] and ball_coords[2] > goal_coords[0] and
        ball_coords[1] < goal_coords[3] and ball_coords[3] > goal_coords[1]):
        canvas.create_text(250, 200, text=" YOU WIN! ", font=("Arial", 20), fill="blue")

# Key binds
root.bind("<Up>", move_ball)
root.bind("<Down>", move_ball)
root.bind("<Left>", move_ball)
root.bind("<Right>", move_ball)
root.bind("<Shift_L>", boost_on)
root.bind("<KeyRelease-Shift_L>", boost_off)

root.mainloop()
