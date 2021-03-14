import turtle

win = turtle.Screen()
win.title("Ping-pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Создаем ракетки

rocket_a = turtle.Turtle()
rocket_a.speed(0)
rocket_a.shape("square")
rocket_a.color("blue")
rocket_a.shapesize(stretch_len=0.5, stretch_wid=5)
rocket_a.penup()
rocket_a.goto(-350, 0)

rocket_b = turtle.Turtle()
rocket_b.speed(0)
rocket_b.shape("square")
rocket_b.color("red")
rocket_b.shapesize(stretch_len=0.5, stretch_wid=5)
rocket_b.penup()
rocket_b.goto(350, 0)

# Создаем гудаперчивый мячик

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Табло очков

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Blue: 0 Red: 0", align="center", font=("verdana", 20, "normal"))

score_a = 0
score_b = 0

# Создаем функции движения ракеток

def rocket_a_up():
    y = rocket_a.ycor()
    if y > 245:
        y = 245
    else:
        y += 20
        rocket_a.sety(y)

def rocket_a_down():
    y = rocket_a.ycor()
    if y < -230:
        y = -230
    else:
        y -= 20
        rocket_a.sety(y)

def rocket_b_up():
    y = rocket_b.ycor()
    if y > 240:
        y = 240
    else:
        y += 20
        rocket_b.sety(y)

def rocket_b_down():
    y = rocket_b.ycor()
    if y < -230:
        y = -230
    else:
        y -= 20
        rocket_b.sety(y)

# Биндим движение ракеток на клавиатуру

win.listen()
win.onkeypress(rocket_a_up, "w")
win.onkeypress(rocket_a_down, "s")
win.onkeypress(rocket_b_up, "Up")
win.onkeypress(rocket_b_down, "Down")

# Запускаем цикл игры

while True:
    win.update()

    # Движение мячика

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Отбивание от стенок и изменение табло

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Blue: {} Red: {}".format(score_a, score_b), align="center",
                  font=("verdana", 20, "normal"))

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Blue: {} Red: {}".format(score_a, score_b), align="center",
                  font=("verdana", 20, "normal"))

    # Отбивание ракетками

    if ball.xcor() > 340 and ball.ycor() < rocket_b.ycor() + 50 and ball.ycor() > rocket_b.ycor() - 50:
        ball.dx *= -1

    if ball.xcor() < -340 and ball.ycor() < rocket_a.ycor() + 50 and ball.ycor() > rocket_a.ycor() - 50:
        ball.dx *= -1