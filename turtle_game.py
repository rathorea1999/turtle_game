from turtle import *
from random import randint
speed(0)
penup()
goto(-180,140)
pendown()


for step in range (0,16):
    write(step, align ="center")
    right(90)
    penup()
    forward(10)
    pendown()
    forward(150)
    left(180)
    penup()
    forward(160)
    right(90)
    forward(30)
    

t1 = Turtle()
t1.shape("turtle")
t1.color("red")

t1.penup()
t1.goto(-200,100)
t1.pendown()


t2 = Turtle()
t2.shape("turtle")
t2.color("blue")

t2.penup()
t2.goto(-200,70)
t2.pendown()


t3 = Turtle()
t3.shape("turtle")
t3.color("yellow")

t3.penup()
t3.goto(-200,40)
t3.pendown()


t4 = Turtle()
t4.shape("turtle")
t4.color("brown")

t4.penup()
t4.goto(-200,10)
t4.pendown()

for i in range (0,150):
    t1.forward(randint(1,5))
    t2.forward(randint(1,5))
    t3.forward(randint(1,5))
    t4.forward(randint(1,5))
