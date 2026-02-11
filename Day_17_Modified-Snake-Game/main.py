#          DAY-17
#Modify Snake Game:
# Change speed
# Change colors
# Add pause feature
from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.colormode(255)

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

segments = []

for position in STARTING_POSITION:
    new_piece = Turtle("square")
    new_piece.color("white")
    new_piece.penup()
    new_piece.goto(position)
    segments.append(new_piece)

head = segments[0]

# ---------------- Movement Controls ----------------
def up():
    if head.heading() != DOWN:
        head.setheading(UP)

def down():
    if head.heading() != UP:
        head.setheading(DOWN)

def left():
    if head.heading() != RIGHT:
        head.setheading(LEFT)

def right():
    if head.heading() != LEFT:
        head.setheading(RIGHT)

# ---------------- Color Controls ----------------
def snake_color_red():
    for seg in segments:
        seg.color("red")

def snake_color_green():
    for seg in segments:
        seg.color("green")

def snake_color_blue():
    for seg in segments:
        seg.color("blue")

def snake_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    for seg in segments:
        seg.color(r, g, b)

def background_color_black():
    screen.bgcolor("black")

def background_color_navy():
    screen.bgcolor("navy")

def background_color_yellow():
    screen.bgcolor("yellow")

# ---------------- Speed + Pause ----------------
delay = 0.1
paused = False

def speed_up():
    global delay
    if delay > 0.02:
        delay -= 0.01

def speed_down():
    global delay
    delay += 0.01

def toggle_pause():
    global paused
    paused = not paused

# ---------------- Snake Movement ----------------
def move():
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(MOVE_DISTANCE)

# ---------------- Key Bindings ----------------
screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

screen.onkey(snake_color_red, "r")
screen.onkey(snake_color_green, "g")
screen.onkey(snake_color_blue, "b")
screen.onkey(snake_random_color, "x")

screen.onkey(background_color_black, "1")
screen.onkey(background_color_navy, "2")
screen.onkey(background_color_yellow, "3")

screen.onkey(speed_up, "+")
screen.onkey(speed_down, "-")
screen.onkey(toggle_pause, "p")

# ---------------- Game Loop ----------------
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(delay)

    if not paused:
        move()

        # Wall collision check
        if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
            print("GAME OVER! You hit the wall.")
            game_is_on = False

screen.exitonclick()