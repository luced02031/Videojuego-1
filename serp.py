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

        self.color('green')
        self.penup()
        self.goto(0, 0)


# Cabeza de la serpiente
head = t.Turtle()
head.speed(0)
# Se le da una forma cuadrara a la figura
head.shape("square")
# Se elimina el rastro que deja la figura
head.penup()
# Se pocisiona el elemento gráfico en las coo. del plano
head.goto(0, 0)
# Se mantiene estático el elemento hasta que lo movamos
head.direction = "stop"
# Color de head
head.color("green")


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


# Teclado
window.listen()
window.onkeypress(up, "Up")


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

    movement()

    time.sleep(postpone)


# La GUI no se cierra hasta que hayamos picado 'X'
# t.mainloop()
