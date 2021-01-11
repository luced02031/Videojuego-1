import turtle as t
import time
import random
from turtle import Turtle

postpone = 0.1

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


class Food(Turtle):
    def __init__(self, speed, color):
        super().__init__(shape='circle')

        self.color("red")
        self.penup()
        self.goto(0, 100)


food = Food("0", ("red"))

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
window.onkeypress(up, "Up")
# Abajo
window.onkeypress(down, "Down")
# Derecha
window.onkeypress(right, "Right")
# Izquierda
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

    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
    movement()

    time.sleep(postpone)


# La GUI no se cierra hasta que hayamos picado 'X'
# t.mainloop()
