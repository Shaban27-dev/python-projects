#          DAY-15
# Simple Drawing App using Turtle
import turtle
import random

# ---------------- Screen Setup ----------------
screen = turtle.Screen()
screen.title("Simple Drawing App 🎨🐢")
screen.bgcolor("white")
screen.colormode(255)

# ---------------- Turtle Setup ----------------
tim = turtle.Turtle()
tim.speed(0)
tim.shape("turtle")
tim.pensize(3)
tim.color("black")

pen_is_down = True


# ---------------- Helper Functions ----------------
def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def turn_left():
    tim.left(15)

def turn_right():
    tim.right(15)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def reset_position():
    tim.penup()
    tim.home()
    if pen_is_down:
        tim.pendown()

def pen_up():
    global pen_is_down
    tim.penup()
    pen_is_down = False
    print("Pen is UP ✋ (not drawing)")

def pen_down():
    global pen_is_down
    tim.pendown()
    pen_is_down = True
    print("Pen is DOWN ✍️ (drawing)")

def change_color_red():
    tim.color("red")

def change_color_green():
    tim.color("green")

def change_color_blue():
    tim.color("blue")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r, g, b)

def increase_brush():
    current_size = tim.pensize()
    tim.pensize(current_size + 1)
    print("Brush size:", tim.pensize())

def decrease_brush():
    current_size = tim.pensize()
    if current_size > 1:
        tim.pensize(current_size - 1)
    print("Brush size:", tim.pensize())


# ---------------- Key Bindings ----------------
screen.listen()

# Movement
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

# Pen control
screen.onkey(pen_up, "u")
screen.onkey(pen_down, "p")

# Colors
screen.onkey(change_color_red, "r")
screen.onkey(change_color_green, "g")
screen.onkey(change_color_blue, "b")
screen.onkey(random_color, "x")

# Brush size
screen.onkey(increase_brush, "+")
screen.onkey(decrease_brush, "-")

# Clear / reset
screen.onkey(clear_screen, "c")
screen.onkey(reset_position, "space")

print("🎨 Drawing App Controls:")
print("Arrow Keys: Move/Turn")
print("u = pen up | p = pen down")
print("r/g/b = colors | x = random color")
print("+ / - = brush size")
print("c = clear | space = reset position")

screen.exitonclick()
screen.mainloop()