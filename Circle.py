# draw a circle by inputing its radius
import math
import turtle

x = int(input("enter the x1: "))
x2 = int(input("enter the x2: "))
y = int(input("enter the y1: "))
y2 = int(input("enter the y2: "))

t = turtle.Turtle()
t.speed(0)
#t.pensize(10)

t.penup()
t.goto(x,y)
t.pendown()

radx = x2 - x
rady = y2 - y

print(radx,rady)

rad = math.sqrt(pow(radx,2) + pow(rady,2))

t.penup()
t.goto(x2,y2)
t.pendown()

t.left(90)
t.circle(rad)
t.hideturtle()

turtle.mainloop()