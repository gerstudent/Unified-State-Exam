from turtle import *

tracer(0)
r = 25

for i in range(9):
    fd(3 * r)
    rt(45)
    fd(3 * r)
    lt(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * r, y * r)
        dot(3, "blue")

update()
exitonclick()
