import turtle
import colorsys
#Flores un detallito 
def dibujar_flor(tortuga, radio, petalos):
    for _ in range(petalos):
        color = colorsys.hsv_to_rgb(_/petalos, 1.0, 1.0)
        tortuga.pencolor(color)
        dibujar_petalos(tortuga, radio)
        tortuga.left(360/petalos)

def dibujar_petalos(tortuga, radio):
    heading = tortuga.heading()
    tortuga.circle(radio, 60)
    tortuga.left(120)
    tortuga.circle(radio, 60)
    tortuga.setheading(heading)

mi_tortuga = turtle.Turtle()
mi_tortuga.speed(-1000)  # Dibuja lo más rápido posible

dibujar_flor(mi_tortuga, 200,500)

mi_tortuga.penup()
mi_tortuga.goto(-50,-150)
mi_tortuga.pendown()
mi_tortuga.write("Te amo", font=("Arial", 100, "normal"))

turtle.done()
