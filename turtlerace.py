# Designed  by Ravi Patidar
from turtle import *
import random


t=Turtle()
w=Screen()

w.bgcolor("orange")
t.penup()
t.goto(-180,150)
t.right(90)
t.speed(8)

#for drawing the lines
for i in  range(15):
    t.speed(0)
    t.write(i)
    if i==14:
        x,y=t.position()
    for j in range(10):
        t.penup()
        t.forward(10)
        t.pendown()
        t.forward(10)
    t.penup()
    t.backward(200)
    t.left(90)
    t.forward(30)
    t.right(90)
   # x,y=t.position()

t.hideturtle()


T=[]
y=10
col=['red','yellow','blue','green']

# loop for setting turtle position

for i in range(4):
    T.append(Turtle())
    T[i].penup()
    T[i].goto(-180,y)
    T[i].speed(4)
    T[i].right(360)
    T[i].shape("turtle")
    T[i].shapesize(1, 1, 2)
    T[i].color(col[i])
    T[i].pendown()
    T[i].pen(pencolor=col[i])
    T[i].write(col[i]+" turtle")
    y=y+30

#loop for move the turtle   
for i in range(200): 
    T[0].forward(random.randint(1,5))
    a,b=T[0].position()
    print(a,b)
    T[1].forward(random.randint(1,5))
    c,d=T[1].position()
    T[2].forward(random.randint(1,5))
    e,f=T[2].position()
    T[3].forward(random.randint(1,5))
    g,h=T[3].position()
    if(a>=x-10):
        t.goto(0,-200)
        t.pencolor(col[0])
        t.write("RED TURTLE IS WINNER")
        break
    elif(c>=x-10):
        t.goto(0,-200)
        t.pencolor(col[1])
        t.write("YELLOW TURTLE IS WINNER")
        break
    elif(e>=x-10):
        t.goto(0,-200)
        t.pencolor(col[2])
        t.write("BLUE TURTLE IS WINNER")
        break
    elif(g>=x-10):
        t.goto(0,-200)
        t.pencolor(col[3])
        t.write("GREEN TURTLE IS WINNER")
        break
exitonclick()
