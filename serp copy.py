import turtle as t
import time

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
    def __init__(self, speed, positon):
        super().__init__(shape='square')

        self.color("green")
        self.penup()
        self.direction = "stop"


h = Head("0", (0, 0))


# Funciones
class Movement(Turtle):

    def __init__(self, up, down, left, right):
        super().__init__(direction='stop')


def up():
    h.direction = "up"


def down():
    h.direction = "down"


def left():
    h.direction = "left"


def right():
    h.direction = "right"


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
    if h.direction == "up":
        y = h.ycor()
        h.sety(y + 20)
# Movimientod de la cabeza hacia abajo
    if h.direction == "down":
        y = h.ycor()
        h.sety(y - 20)
# Movimientod de la cabeza hacia la izquierda
    if h.direction == "left":
        x = h.xcor()
        h.setx(x - 20)
# Movimientod de la cabeza hacia la derecha
    if h.direction == "right":
        x = h.xcor()
        h.setx(x + 20)


# BUCLE PRINCIPAL
while True:
    window.update()

    movement()

    time.sleep(postpone)


# La GUI no se cierra hasta que hayamos picado 'X'
# t.mainloop()
