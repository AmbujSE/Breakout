import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turns off animation

# Create paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Create ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Create bricks
bricks = []

for i in range(-240, 250, 80):
    for j in range(200, 260, 40):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color("blue")
        brick.penup()
        brick.goto(i, j)
        bricks.append(brick)

# Function to move paddle left
def paddle_left():
    x = paddle.xcor()
    x -= 20
    paddle.setx(x)

# Function to move paddle right
def paddle_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)

# Keyboard bindings
screen.listen()
screen.onkeypress(paddle_left, "Left")
screen.onkeypress(paddle_right, "Right")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision checking
    if ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1
    elif ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1
    elif ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Paddle collision checking
    if (ball.ycor() < -240) and (ball.ycor() > -250) and (ball.xcor() < paddle.xcor() + 50) and (ball.xcor() > paddle.xcor() - 50):
        ball.sety(-240)
        ball.dy *= -1

    # Brick collision checking
    for brick in bricks:
        if (ball.distance(brick) < 20):
            brick.goto(1000, 1000)
            ball.dy *= -1

    # Game over condition
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dx *= -1
