import turtle as t
import time

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
head.direction = "up"
# Color de head
head.color("green")


# Funciones
def movement():
    '''
    Función para controlar el movimiento de la cabeza
    '''
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)


# BUCLE PRINCIPAL
while True:
    window.update()

    movement()

    time.sleep(pos)


# La GUI no se cierra hasta que hayamos picado 'X'
# t.mainloop()
