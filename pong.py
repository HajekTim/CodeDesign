import turtle

# Erstellen des Fensters
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# sofortiges zeichnen
wn.tracer(0)

# inizialisieren der Punkte
score_a = 0
score_b = 0

# Linkes Paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("White")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Rechtes Paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("White")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("White")
ball.penup()
ball.goto(0, 0)
# iniziale Bewegung
ball_speed = 0.3
ball.dx = ball_speed
ball.dy = -ball_speed

# Score 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B :0", align="center", font=("Courier", 24, "normal"))


# Steuerung für linkes Paddle

# hoch mit w
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


# runter mit s
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


# warte auf Eingabe
wn.listen()
wn.onkeypress(paddle_a_up, "w")

wn.listen()
wn.onkeypress(paddle_a_down, "s")


# Bewegung für rechtes Paddle

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


wn.listen()
wn.onkeypress(paddle_b_up, "Up")

wn.listen()
wn.onkeypress(paddle_b_down, "Down")

# Game Loop
while True:
    # update das Fenster um die Änderungen anzuzeigen
    wn.update()

    # Bewegung des Balles
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # wenn Ball oben anstößt, invertiere das Y-Delta
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # wenn Ball unten anstößt, invertiere das Y-Delta
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # wenn Ball links an dem Spieler vorbei ins aus geht gib Spieler recht einen Punkt
    # und setze den Ball zurück
    if ball.xcor() > 390:
        ball.goto(0, 0)
        if ball.dx < 0:
            ball.dx = ball_speed
        else:
            ball.dx = -ball_speed
        print(ball.dx)
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B :{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # andersrum
    if ball.xcor() < -390:
        ball.goto(0, 0)
        if ball.dx < 0:
            ball.dx = ball_speed
        else:
            ball.dx = -ball_speed
        print(ball.dx)
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B :{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # wenn Ball auf Spieler rechts den Ball trifft
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        # verschnellere den Ball
        ball.dx *= -1.05
        print(ball.dx)

    # wenn Ball auf Spieler links trifft
    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1.05
        print(ball.dx)

    # # KI Spieler (auskommentieren wenn Multiplayer)
    #
    # if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
    #     paddle_b_up()
    #
    # elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
    #     paddle_b_down()
