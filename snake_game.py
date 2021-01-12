import turtle as t
import time
import random
from turtle import Turtle

postpone = 0.1

# Marcador
score = 0
h_score = 0

# Creación de la ventana
window = t.Screen()
# Title
window.title("Juego prueba")
# Background color
window.bgcolor("black")
# Window size
window.setup(width=600, height=600)
window.tracer(0)


class Head(Turtle):
    '''
    Cabeza de la serpiente
    '''

    def __init__(self, speed, positon):
        super().__init__(shape='square')

        self.color("green")
        self.penup()
        self.direction = "stop"


head = Head("0", (0, 0))

# Comida


class Food(Turtle):
    '''
    Manzanas
    '''

    def __init__(self, speed, color):
        super().__init__(shape='circle')

        self.color("red")
        self.penup()
        self.goto(0, 100)


food = Food("0", ("red"))

# Marcador de puntos


class Score(Turtle):
    '''
    Marcador de puntos dentro del juego
    '''

    def __init__(self, speed, color):
        super().__init__(shape='circle')

        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.write("Score: 0        High Score: 0",
                   align="Center",
                   font=("Courier", 20, "normal"))


scre = Score("0", ("white"))


# Segmentos de cuerpo
segmentos = []

# Funciones
'''class Movement(Turtle):

    def __init__(self, up, down, left, right):
        super().__init__(direction='stop')'''


def up():
    head.direction = "up"


def down():
    head.direction = "down"


def left():
    head.direction = "left"


def right():
    head.direction = "right"


# Entrada del teclado
window.listen()
# Arriba
window.onkeypress(up, "w")
window.onkeypress(up, "Up")
# Abajo
window.onkeypress(down, "s")
window.onkeypress(down, "Down")
# Derecha
window.onkeypress(right, "d")
window.onkeypress(right, "Right")
# Izquierda
window.onkeypress(left, "a")
window.onkeypress(left, "Left")


def movement():
    '''
    Función para controlar el movimiento de la cabeza
    '''
# Movimientod de la cabeza hacia arriba
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
# Movimientod de la cabeza hacia abajo
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
# Movimientod de la cabeza hacia la izquierda
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
# Movimientod de la cabeza hacia la derecha
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# BUCLE PRINCIPAL
while True:
    window.update()
# Colisiones Bordes
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Esconder los segmentos
        for seg in segmentos:
            seg.goto(1000, 1000)

        # Limpiar lista de segmentos
        segmentos.clear()

        # Resetear marcador
        score = 0
        scre.clear()
        scre.write(f"Score: {score}      High Score: {h_score}",
                   align="Center",
                   font=("Courier", 20, "normal"))

    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

# Cabeza de la serpiente
        nw = t.Turtle()
        nw.speed(0)
        nw.shape("square")
        nw.penup()
        nw.color("green")
        segmentos.append(nw)
    # Aumentar marcador
        score += 10

        if score >= h_score:
            h_score = score
        scre.clear()
        scre.write(f"Score: {score}      High Score: {h_score}",
                   align="Center",
                   font=("Courier", 20, "normal"))


# Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg - 1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        segmentos[0].goto(x, y)

    movement()

    # Colsiones con el cuerpo de la serpiente
    for seg in segmentos:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for seg in segmentos:
                seg.goto(1000, 1000)

            segmentos.clear()
            # Resetar marcador
            score = 0
            scre.clear()
            scre.write(f"Score: {score}      High Score: {h_score}",
                       align="Center",
                       font=("Courier", 20, "normal"))
    time.sleep(postpone)


# La GUI no se cierra hasta que hayamos picado 'X'
# t.mainloop()
