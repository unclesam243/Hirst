from turtle import *  # let's import all the information from turtle module
from random import choice, randint

franklin = Turtle()
franklin.shape("circle")
franklin.width(6)
franklin.speed("fast")

#Establishing the color palette
color_list = [(246, 242, 244), (202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]
colormode(255)
# Establishing the Screen size
screen = Screen()
screen.reset()
screen.setworldcoordinates(-1,-1,49,49)
#screen.width = 300
#screen.height = 300

def motion():
    dist = 5
    franklin.dot()
    n_dot = 100

    for n in range(1, n_dot):
        franklin.dot(25, choice(color_list))
        franklin.penup()
        franklin.forward(dist)
        franklin.color("white")
        franklin.color(choice(color_list))
        franklin.dot(25, choice(color_list))
        franklin.pendown()
        if n in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
            franklin.setheading(90)
            franklin.fd(5)
            franklin.color("white")
            franklin.setheading(180)
            franklin.fd(50)
            franklin.setheading(0)
    done()



motion()

toexit = screen.exitonclick()
