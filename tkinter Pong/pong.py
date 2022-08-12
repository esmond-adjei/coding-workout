import turtle
import winsound

# turtle objects
window = turtle.Screen()
paddle_a = turtle.Turtle()
paddle_b = turtle.Turtle()
ball = turtle.Turtle()
pen = turtle.Turtle()

# sounds
def hit_sound():
    winsound.PlaySound(winsound.Beep(300,100), winsound.SND_ASYNC)

def gave_over_sound(start_freq):
    winsound.Beep(start_freq, 500)
    winsound.Beep(start_freq + 500, 300)
    winsound.Beep(start_freq - 500, 700)

# reset game to default positions
def reset_game():
    paddle_a.goto(-350, 0)
    paddle_b.goto(350, 0)
    ball.goto(0, 0)

# Themes
def default_theme():
    window.bgcolor("blue")
    paddle_a.color("orange")
    paddle_b.color("orange")
    ball.color("white")
    pen.color("white")

def dark_theme():
    window.bgcolor("black")
    paddle_a.color("white")
    paddle_b.color("white")
    ball.color("white")
    pen.color("orange")

# FUNCTIONS
# paddle a
def paddle_a_move():
    y = paddle_a.ycor() + 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() - 20
    paddle_a.sety(y)

# paddle b
def paddle_b_up():
    y = paddle_b.ycor() + 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() - 20
    paddle_b.sety(y)

# window object setup
window.title("Pong by @xmon")
window.setup(width=800,height=600)
window.tracer(0)

# paddle A object setup
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.speed(0)
paddle_a.penup()

# paddle B object setup
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.speed(0)
paddle_b.penup()

# ball setup
ball.shape("circle")
ball.dx, ball.dy = 0.1, 0.1
ball.speed(0)
ball.penup()

# score board
score_a = 0
score_b = 0

# feature setup
reset_game()
default_theme()
#dark_theme()

# Pen
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 18, "normal"))

# keyboard binding
window.listen()
window.onkeypress(paddle_a_move, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if (ball.ycor() > 290) or ball.ycor() < -290:
        ball.dy *= -1
        hit_sound()

    # paddle and ball collisions
    # between 350-340 right and between length of paddle ie -40 to + 40
    hit_right_paddle = (ball.xcor() > 340 and ball.xcor() < 350)
    on_side_right_paddle = (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40)
    hit_left_paddle = (ball.xcor() < -340 and ball.xcor() > -350)
    on_side_left_paddle = (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40)

    if (hit_right_paddle and on_side_right_paddle) or (hit_left_paddle and on_side_left_paddle):
        ball.dx *= -1
        hit_sound()

    if ball.xcor() > 390:   # game over for B
        score_a += 1 
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 18, "normal"))
        ball.dx *= -1
        reset_game()
        gave_over_sound(1000)

    if ball.xcor() < -390:      # game over for A
        score_b += 1 
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 18, "normal"))
        ball.dx *= -1
        reset_game()
        gave_over_sound(1000)
