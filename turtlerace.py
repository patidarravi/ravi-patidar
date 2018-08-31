"""
Created on Mon Aug 13 21:32:22 2018
@author: Ravi
"""


from turtle import *                               # Turtle is a predefined module
import random                                       # random module used for generating random no's 
import time 

title("TURTLE RACE")                              # set the title of screen
t=Turtle()                                        # t is object of turtle method
w=Screen()                                        # w is object of screen method                                        
w.screensize(800,600)                             #  sets the screen size
w.bgcolor("orange")                               # sets the back ground color of display
t.penup()                                         # Pull the pen up – no drawing when moving  
t.goto(10,200)                                   # Move turtle to an absolute position(10,200)
t.pendown()                                        # Pull the pen up – no drawing when moving 
t.write("TURTLE RACE" ,move=False, align="CENTER", font=("arial", 30, "normal"))   # set heading of turtle race
t.penup()                                         #
t.goto(-180,150)                                  # Move turtle to an absolute position(-180,150)
t.right(90)                                       # turn turtle right by angle units(90)
                                           


for step in  range(15):                            
    t.speed(0)                                  # Set the turtle’s speed to an integer value(set to 8) in the range 0..10
    t.write(step)                                  # write the track no on display
    if step==14:
        x,y=t.position()                        #x and y is to know the co-oridinate of turtle at step:12
    for j in range(10):
        t.penup()                               
        t.forward(10)                           #move forward the turtle by specified distance(10)  
        t.pendown()
        t.forward(10)
    t.penup()
    t.backward(200)                             #move backward the turtle by specified distance(200)
    t.left(90)                                  # turn turtle left by angle units(90)
    t.forward(30)
    t.right(90)
   

t.hideturtle()                                #it hide the turtle at it is current position


turtle=[]                                           #list of turtle 
y=10                                  
col=['red','yellow','blue','green']                 # list of color



for i in range(4):
    turtle.append(Turtle())                         #append the turtle(1...4) in list turtle
    turtle[i].penup()   
    turtle[i].goto(-180,y)                          #Move turtle to an absolute position(-180,y)
    turtle[i].speed(4)                              #set speed of turtle 
    turtle[i].right(360)                            #rotate turtle by angle unit(360)
    turtle[i].shape("turtle")                       #used to change the cursor into 'turtle' shape
    turtle[i].shapesize(1, 1, 2)                     #shapesize is used to change height ,width, outline of turtle
    turtle[i].color(col[i])
    turtle[i].pendown()
    turtle[i].pen(pencolor=col[i])                     #set the 'turtle' of different color
    turtle[i].write(col[i]+" turtle")          
    y=y+30                                              #set the turtle at different position
    
def winner(color):                                    #'winner' method is used  to show the winner turtle 
    penup() 
    goto(50,-200)
    pendown()
    pencolor(color)
    write(color.upper()+" turtle won the game ", align='center',font=('arial',15,'normal')  )
    penup()
    goto(-120,-200)
    pendown()
    shape("turtle")
    shapesize(2, 2, 1)
    fillcolor(color)
    #color(color)
    left(90)
    for i in range(100):
        left(90)
    
    
 
for i in range(200):                                      
    turtle[0].forward(random.randint(1,5))                        #for forwarding the turtle randomly in range(1,5)
    a,b=turtle[0].position()                                       # for getting the turtle x,y co-ordinate
    turtle[1].forward(random.randint(1,5))
    c,d=turtle[1].position()
    turtle[2].forward(random.randint(1,5))
    e,f=turtle[2].position()
    turtle[3].forward(random.randint(1,5))
    g,h=turtle[3].position()
    if(a>=x-10):
        winner(col[0])
        break
    elif(c>=x-10):
        winner(col[1])
        break
    elif(e>=x-10):
        winner(col[2])
        break
    elif(g>=x-10):
        winner(col[3])
        break
exitonclick()
