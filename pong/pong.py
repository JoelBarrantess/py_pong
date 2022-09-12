import turtle
import random

# Crear pantalla
pan = turtle.Screen()
pan.title("Pong Hecho por Joel Barrantes")
pan.bgcolor("black")
pan.setup(width=800, height=600)

# Pala jugador 1 
p1 = turtle.Turtle()
p1.speed (0)
p1.shape("square")
p1.color("white")
p1.penup()
p1.shapesize(stretch_len=1, stretch_wid=5)
p1.goto (-380, 0)

# Pala jugador 2
p2 = turtle.Turtle()
p2.speed (0)
p2.shape("square")
p2.color("white")
p2.penup()
p2.shapesize(stretch_len=1, stretch_wid=5)
p2.goto (380, 0)

# Bola
bola = turtle.Turtle()
bola.speed (0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto (0, 0)
bola.dx = 5
bola.dy = -3

# Tabla de puntuaciones
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
Jugador1_score = 0
Jugador2_score = 0
pen.write("Jugador 1: 0   Jugador 2: 0 ", align="center", font=("courier", 24, "normal"))

# Funciones 
def p1_arriba():
    y = p1.ycor()
    y += (20)
    p1.sety(y)

def p1_abajo():
    y = p1.ycor()
    y -= (20)
    p1.sety(y)


def p2_arriba():
    y = p2.ycor()
    y += (20)
    p2.sety(y)

def p2_abajo():
    y = p2.ycor()
    y -= (20)
    p2.sety(y)


#Bindear Controles
pan.listen()
pan.onkeypress(p1_arriba, "w")
pan.onkeypress(p1_abajo, "s")
pan.onkeypress(p2_arriba, "Up")
pan.onkeypress(p2_abajo, "Down")

# main loop
while True:
    pan.update()

    # Mover la Bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Checkear los bordes
    if bola.ycor() > 290:
        bola.sety (290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety (-285)
        bola.dy *= -1

    # Colisiones
    if (bola.xcor() > 355 and bola.xcor() < 365 and bola.ycor() < p2.ycor() + 40 and bola.ycor() > p2.ycor() -40):
        bola.setx(350)
        bola.dx += 2
        bola.dx *= -1
        bola.dy = random.randrange(-5, 5)

    if (bola.xcor() < -355 and bola.xcor() > -365 and bola.ycor() < p1.ycor() + 40 and bola.ycor() > p1.ycor() -40):
        bola.setx(-350)
        bola.dx += 2
        bola.dx *= -1
        bola.dy = random.randrange(-5, 5)

    # Marcador
    if bola.xcor() > 390:
        bola.goto(0,0)
        bola.dx *= -1
        Jugador1_score += 1
        pen.clear()
        pen.write("Jugador 1: {}   Jugador 2: {}".format(Jugador1_score, Jugador2_score), align="center", font=("courier", 24, "normal"))
        bola.dy = random.randrange(-5, 5)
    
    if bola.xcor() < -390:
        bola.goto(0,0)
        bola.dx *= -1
        Jugador2_score += 1
        pen.clear()
        pen.write("Jugador 1: {}   Jugador 2: {}".format(Jugador1_score, Jugador2_score), align="center", font=("courier", 24, "normal"))
        bola.dy = random.randrange(-5, 5)




