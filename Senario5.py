#immediatestop

import turtle as t
import numpy as np
import random
import time

'''
Things_to_do_lists
1. parameter
2. paper
3. time
additoinal. critical, recovered, dead
'''


#parameters_settings
studentnum = 356
breaktime = 5333
lunchbreak = 15999
Aclass = [6, 1, 1, 5, 1, 1, 1, 3, 10, 1, 3, 1, 6, 1, 1, 12, 10, 10, 10, 1, 1, 12, 10, 1, 12, 10, 1, 1, 1, 1, 1, 1, 6, 1, 10, 12, 5, 1, 1, 3, 10, 1, 12, 3, 10, 1, 5, 1, 1, 10, 3, 1, 5, 1, 3, 10, 1, 9, 10, 1, 1, 12, 1, 5, 1, 1, 2, 10, 2, 7, 11, 7, 2, 3, 4, 8, 9, 5, 4, 6, 2, 5, 4, 2, 11, 3, 3, 4, 4, 9, 2, 8, 10, 4, 11, 11, 11, 5, 6, 8, 2, 5, 5, 10, 9, 12, 4, 8, 9, 3, 8, 12, 3, 5, 8, 2, 6, 9, 11, 12, 8, 4, 6, 7, 4, 6, 12, 10, 11, 2, 7, 5, 6, 6, 8, 2, 8, 3, 8, 8, 9, 4, 11, 10, 6, 12, 12, 12, 6, 4, 7, 7, 7, 3, 2, 7, 5, 12, 2, 6, 9, 8, 8, 2, 6, 9, 11, 7, 7, 8, 8, 3, 2, 6, 3, 8, 6, 10, 8, 2, 9, 3, 10, 8, 12, 2, 3, 3, 6, 12, 5, 3, 10, 5, 9, 12, 11, 4, 4, 9, 9, 5, 5, 9, 9, 7, 11, 2, 4, 10, 9, 8, 9, 6, 10, 9, 6, 5, 7, 7, 3, 2, 6, 7, 7, 7, 9, 4, 4, 5, 3, 7, 11, 9, 11, 2, 7, 9, 11, 5, 2, 11, 3, 9, 5, 3, 6, 7, 6, 2, 4, 8, 11, 11, 3, 7, 9, 4, 6, 12, 2, 10, 10, 8, 8, 11, 4, 4, 3, 8, 7, 5, 11, 7, 2, 5, 12, 10, 4, 8, 9, 7, 12, 2, 8, 12, 5, 2, 4, 11, 4, 5, 8, 7, 7, 11, 6, 3, 9, 4, 6, 11, 7, 4, 5, 6, 3, 3, 5, 7, 8, 5, 9, 7, 12, 11, 8, 8, 6, 4, 8, 6, 12, 12, 5, 12, 4, 12, 6, 11, 11, 5, 11, 6, 9, 11, 9, 4, 5, 2, 9, 6, 4, 11, 3, 3, 3, 6, 4, 2, 6, 4, 8, 5, 3, 4]
Bclass = [8, 11, 8, 11, 1, 1, 8, 1, 7, 1, 4, 11, 8, 11, 1, 4, 5, 1, 4, 1, 8, 1, 11, 1, 4, 11, 11, 11, 1, 8, 1, 8, 1, 11, 4, 1, 11, 8, 1, 7, 1, 11, 2, 4, 4, 11, 1, 2, 7, 1, 4, 11, 1, 11, 11, 1, 1, 1, 7, 4, 11, 7, 4, 1, 4, 2, 12, 1, 12, 5, 10, 7, 9, 3, 6, 5, 9, 2, 4, 5, 7, 9, 7, 5, 8, 12, 7, 8, 1, 3, 2, 6, 6, 9, 8, 2, 5, 8, 11, 3, 2, 9, 6, 12, 9, 1, 10, 3, 8, 11, 5, 6, 1, 3, 6, 10, 6, 4, 10, 8, 5, 7, 9, 12, 9, 12, 2, 12, 7, 4, 3, 2, 5, 6, 7, 8, 10, 7, 3, 6, 9, 4, 5, 12, 9, 2, 3, 3, 10, 6, 8, 10, 10, 11, 12, 4, 10, 2, 10, 6, 9, 4, 5, 10, 6, 7, 2, 7, 11, 6, 5, 4, 8, 9, 6, 7, 2, 11, 7, 8, 1, 6, 7, 5, 3, 10, 7, 3, 5, 4, 10, 4, 12, 9, 9, 6, 10, 7, 3, 9, 1, 11, 2, 9, 5, 8, 7, 10, 4, 11, 7, 7, 1, 12, 6, 6, 5, 5, 9, 2, 3, 10, 10, 4, 2, 4, 3, 6, 10, 12, 3, 3, 2, 9, 10, 8, 10, 9, 2, 10, 12, 2, 12, 5, 10, 3, 2, 2, 9, 1, 6, 10, 10, 10, 11, 4, 6, 7, 5, 2, 4, 4, 12, 6, 1, 1, 3, 7, 11, 5, 8, 10, 9, 7, 2, 5, 2, 7, 9, 7, 4, 12, 1, 9, 7, 2, 10, 5, 9, 8, 9, 9, 5, 11, 2, 7, 9, 12, 9, 10, 5, 4, 3, 3, 8, 2, 11, 12, 5, 8, 3, 10, 9, 7, 1, 2, 6, 5, 6, 9, 5, 11, 6, 6, 3, 2, 3, 2, 5, 12, 2, 12, 5, 4, 4, 9, 3, 9, 10, 12, 5, 6, 12, 10, 6, 1, 12, 9, 7, 12, 2, 3, 5, 9, 6, 4]
Cclass = [2, 1, 2, 1, 1, 10, 10, 7, 10, 10, 10, 2, 2, 1, 7, 1, 2, 3, 10, 3, 2, 7, 7, 1, 1, 3, 3, 2, 1, 2, 1, 10, 10, 2, 10, 7, 1, 2, 10, 2, 10, 2, 2, 2, 2, 2, 10, 2, 1, 10, 2, 3, 10, 7, 7, 7, 10, 10, 10, 2, 3, 2, 2, 1, 2, 2, 1, 7, 12, 6, 4, 9, 6, 7, 4, 12, 9, 11, 6, 4, 11, 8, 7, 4, 12, 2, 10, 5, 6, 9, 11, 7, 11, 3, 5, 11, 7, 9, 8, 9, 11, 6, 6, 8, 5, 1, 8, 3, 5, 3, 8, 12, 3, 6, 9, 4, 1, 5, 4, 5, 3, 6, 12, 1, 5, 1, 7, 8, 1, 9, 1, 8, 4, 9, 2, 11, 3, 11, 9, 3, 9, 4, 6, 5, 8, 7, 1, 7, 4, 4, 11, 7, 9, 12, 12, 4, 12, 12, 4, 6, 9, 6, 3, 7, 1, 4, 7, 6, 8, 6, 8, 11, 12, 6, 9, 6, 11, 8, 5, 11, 3, 12, 12, 6, 1, 9, 11, 11, 6, 8, 12, 12, 5, 8, 8, 12, 9, 4, 4, 9, 9, 5, 11, 7, 8, 8, 10, 9, 4, 12, 4, 5, 9, 2, 12, 9, 5, 6, 6, 11, 3, 7, 8, 1, 10, 1, 9, 7, 4, 1, 12, 1, 2, 8, 4, 8, 4, 5, 2, 9, 12, 11, 12, 5, 8, 10, 11, 10, 9, 11, 4, 2, 9, 4, 7, 3, 4, 5, 6, 5, 3, 12, 5, 3, 9, 10, 4, 6, 3, 6, 10, 3, 9, 5, 11, 6, 7, 5, 8, 9, 12, 7, 1, 3, 9, 7, 4, 4, 2, 5, 3, 12, 7, 8, 11, 6, 9, 3, 9, 3, 8, 6, 11, 6, 12, 2, 3, 8, 12, 8, 9, 4, 9, 10, 3, 2, 6, 6, 6, 5, 6, 1, 1, 1, 3, 3, 4, 8, 6, 5, 11, 5, 6, 1, 12, 3, 7, 12, 8, 7, 3, 1, 5, 3, 10, 7, 5, 2, 12, 8, 12, 3, 5, 8, 10, 4]
Dclass = [7, 3, 2, 3, 6, 12, 3, 7, 3, 12, 3, 5, 7, 3, 7, 3, 7, 7, 3, 12, 7, 12, 3, 2, 3, 3, 3, 2, 2, 6, 7, 3, 12, 2, 3, 12, 3, 7, 2, 7, 5, 5, 5, 7, 7, 5, 12, 7, 3, 6, 7, 3, 12, 3, 3, 7, 2, 12, 3, 12, 3, 12, 12, 7, 7, 7, 9, 9, 12, 10, 1, 10, 2, 11, 8, 2, 3, 11, 3, 8, 12, 1, 10, 2, 2, 4, 9, 8, 5, 2, 11, 1, 6, 4, 6, 6, 2, 5, 11, 8, 2, 1, 1, 4, 1, 9, 5, 6, 9, 11, 2, 12, 9, 10, 8, 1, 7, 10, 2, 8, 8, 10, 8, 2, 5, 9, 11, 2, 1, 10, 7, 11, 8, 10, 8, 11, 11, 4, 5, 8, 11, 8, 5, 11, 8, 9, 2, 12, 11, 8, 4, 1, 10, 9, 6, 1, 10, 5, 1, 10, 6, 2, 8, 10, 3, 1, 11, 10, 12, 6, 2, 4, 7, 1, 8, 11, 3, 3, 8, 6, 1, 7, 1, 3, 11, 10, 4, 11, 11, 4, 10, 4, 6, 1, 1, 12, 2, 9, 8, 2, 5, 12, 9, 4, 2, 2, 12, 6, 8, 6, 3, 1, 5, 12, 4, 10, 10, 11, 5, 4, 9, 10, 10, 7, 9, 4, 10, 5, 4, 4, 6, 6, 7, 2, 5, 5, 2, 1, 5, 9, 12, 4, 4, 6, 10, 2, 4, 2, 6, 5, 5, 5, 2, 1, 3, 10, 1, 10, 9, 6, 10, 9, 11, 1, 8, 6, 8, 9, 3, 4, 5, 11, 5, 7, 9, 4, 9, 7, 8, 8, 10, 4, 9, 1, 8, 4, 11, 5, 8, 6, 9, 1, 3, 12, 4, 10, 8, 4, 4, 10, 8, 10, 12, 10, 9, 7, 9, 4, 10, 6, 6, 1, 9, 9, 11, 6, 1, 4, 1, 8, 2, 9, 11, 1, 10, 3, 8, 2, 3, 5, 6, 11, 6, 9, 5, 1, 10, 5, 10, 11, 9, 3, 12, 6, 6, 7, 11, 1, 12, 6, 7, 6, 6, 2, 5, 8]
Eclass = [2, 9, 1, 2, 1, 4, 4, 2, 2, 7, 2, 11, 2, 4, 11, 2, 2, 2, 2, 1, 8, 2, 2, 1, 2, 2, 11, 11, 1, 1, 8, 8, 2, 11, 2, 2, 2, 3, 11, 2, 2, 11, 2, 2, 2, 11, 2, 8, 1, 2, 2, 11, 2, 11, 2, 2, 11, 2, 2, 1, 11, 2, 1, 2, 11, 8, 9, 1, 8, 4, 4, 7, 3, 1, 4, 8, 4, 12, 6, 5, 10, 4, 12, 8, 1, 9, 5, 4, 6, 6, 8, 7, 12, 7, 5, 12, 6, 10, 11, 9, 5, 5, 6, 8, 8, 8, 6, 7, 5, 10, 7, 4, 1, 3, 4, 4, 5, 3, 3, 10, 12, 5, 3, 12, 7, 12, 12, 12, 9, 7, 4, 1, 12, 7, 3, 8, 9, 5, 8, 3, 9, 12, 6, 9, 9, 12, 5, 5, 3, 9, 8, 6, 4, 9, 11, 7, 3, 10, 9, 3, 10, 10, 12, 3, 1, 10, 12, 3, 9, 4, 8, 10, 8, 5, 4, 3, 12, 4, 3, 5, 6, 8, 7, 4, 9, 8, 10, 9, 6, 11, 3, 1, 10, 7, 4, 4, 6, 7, 8, 12, 6, 10, 12, 3, 6, 1, 12, 6, 12, 10, 3, 9, 6, 12, 8, 4, 8, 6, 9, 8, 1, 3, 3, 12, 9, 1, 8, 6, 9, 10, 1, 1, 8, 3, 3, 1, 3, 4, 1, 6, 9, 9, 4, 6, 3, 5, 5, 12, 10, 11, 7, 3, 6, 4, 5, 7, 8, 7, 6, 10, 3, 1, 9, 7, 9, 11, 8, 6, 10, 9, 10, 6, 7, 11, 8, 6, 5, 10, 9, 10, 3, 11, 9, 7, 10, 5, 4, 7, 4, 1, 7, 7, 7, 9, 4, 3, 10, 5, 9, 5, 6, 3, 7, 4, 1, 10, 5, 4, 7, 1, 7, 10, 4, 11, 11, 5, 9, 9, 6, 4, 12, 12, 8, 5, 3, 10, 4, 12, 6, 11, 12, 11, 6, 3, 6, 7, 4, 8, 3, 11, 6, 1, 5, 6, 5, 10, 9, 7, 8, 11, 10, 6, 4, 3, 5, 10]

#functions
def square(i):
    for j in range(0,i):
        drawingturtle.fd(87.5)
        drawingturtle.rt(90)
        drawingturtle.fd(75)
        drawingturtle.rt(90)
        drawingturtle.up()
        drawingturtle.fd(87.5)
        drawingturtle.rt(90)
        drawingturtle.down()
        drawingturtle.fd(75)
        drawingturtle.rt(90)
        drawingturtle.fd(87.5)
def classroom():
    drawingturtle.rt(90)
    drawingturtle.fd(75)
    drawingturtle.lt(90)
    drawingturtle.fd(87.5)
    drawingturtle.lt(90)
    drawingturtle.fd(75)
    drawingturtle.rt(90)
    square(6)
    drawingturtle.rt(90)
    drawingturtle.fd(75)
    drawingturtle.lt(90)
    drawingturtle.fd(87.5)
    drawingturtle.lt(90)
    drawingturtle.fd(75)
    drawingturtle.rt(90)
    square(4)
    drawingturtle.rt(90)
    drawingturtle.fd(75)
    drawingturtle.fd(22.5)
    drawingturtle.rt(90)
    drawingturtle.fd(87.5)
    drawingturtle.lt(90)
    drawingturtle.fd(75)
    drawingturtle.rt(90)
    drawingturtle.fd(87.5)
    drawingturtle.rt(90)
    drawingturtle.fd(75)
    drawingturtle.lt(90)
    for i in range(0,7):
        drawingturtle.fd(87.5)
    drawingturtle.lt(90)
    drawingturtle.fd(75)
    drawingturtle.rt(90)
    drawingturtle.fd(87.5)
    drawingturtle.rt(90)
    drawingturtle.fd(75)
    drawingturtle.lt(90)
    for i in range(0,4):
        drawingturtle.fd(87.5)
    drawingturtle.goto(-612.5,86.25)
    drawingturtle.goto(-612.5,11.25)
    drawingturtle.rt(90)
    drawingturtle.rt(90)
    drawingturtle.hideturtle()
def initposition():
    for i in range(0,len(student)):
        Yposition = 86.25
        classnumber = (substudent[i]-20000)//100
        studentnumber = substudent[i]%100
        if classnumber == 1:Xclassposition.append(87.5*7)
        elif classnumber == 2:Xclassposition.append(87.5*6)
        elif classnumber == 3:Xclassposition.append(87.5*5)
        elif classnumber == 4:Xclassposition.append(87.5*4)
        elif classnumber == 5:Xclassposition.append(87.5*2)
        elif classnumber == 6:Xclassposition.append(87.5*1)
        elif classnumber == 7:Xclassposition.append(87.5*-0)
        elif classnumber == 8:Xclassposition.append(87.5*-1)
        elif classnumber == 9:Xclassposition.append(87.5*-2)
        elif classnumber == 10:Xclassposition.append(87.5*-3)
        elif classnumber == 11:Xclassposition.append(87.5*-5)
        elif classnumber == 12:Xclassposition.append(87.5*-6)
        Xpos.append(Xclassposition[i]-((studentnumber%5)*2)*87.5/11)
        if studentnumber%5 == 0:Xpos[i] = Xclassposition[i]-(5*2)*87.5/11
        if classnumber == 1 or classnumber == 2:Ypos.append(Yposition-(studentnumber//5+1)*2*75/15)
        else :Ypos.append(Yposition-(studentnumber//5+1)*2*75/13)
        if studentnumber%5 == 0 : 
            if classnumber == 1 or classnumber == 2 : Ypos[i] = Yposition-(studentnumber//5)*2*75/15
            else :Ypos[i] = Yposition-(studentnumber//5)*2*75/13
        student[i].goto(Xpos[i],Ypos[i])
def initturn(i,initialangle):
    student[i].setheading(initialangle)
def move(i):
    turnangle = (random.randint(-10,10))
    for j in range(0,random.randint(0,20)):
        movedistance = random.random()/4
        if abs(student[i].xcor())>612.5:
            student[i].rt(180)
            student[i].fd(1)
        else:
            if abs(student[i].ycor())>=11.25:
                if 87.5-student[i].xcor()%87.5 <=1 or student[i].xcor()%87.5 <=1:
                    student[i].rt(180)
                    student[i].fd(1)
            if student[i].ycor()>=86.25:
                student[i].setheading(random.randint(250,290))
                student[i].fd(1)
            if student[i].ycor()<=-86.25:
                student[i].setheading(random.randint(70,110))
                student[i].fd(1)
            if (student[i].xcor()>=175 and student[i].xcor()<=262.5 and student[i].ycor()>=11.05) or (student[i].xcor()>=-437.5 and student[i].xcor()<=-350 and student[i].ycor()>=11.05):
                if student[i].heading()>=0 and student[i].heading()<90:
                    student[i].setheading(random.randint(340,350))
                    student[i].fd(1)
                elif student[i].heading()>=90 and student[i].heading()<180:
                    student[i].setheading(random.randint(190,200))
                    student[i].fd(1)
                elif student[i].heading()>=180 and student[i].heading()<270:
                    student[i].setheading(random.randint(160,170))
                    student[i].fd(1)
                elif student[i].heading()>=270 and student[i].heading()<360:
                    student[i].setheading(random.randint(10,20))
                    student[i].fd(1)
            if student[i].ycor()<=-11.25:
                if student[i].xcor()<=-262.5 or student[i].xcor()>= -175 and student[i].xcor()<=437.5 or student[i].xcor()>=525:
                    if student[i].heading()>=0 and student[i].heading()<90:
                        student[i].setheading(random.randint(340,350))
                        student[i].fd(1)
                    elif student[i].heading()>=90 and student[i].heading()<180:
                        student[i].setheading(random.randint(190,200))
                        student[i].fd(1)
                    elif student[i].heading()>=180 and student[i].heading()<270:
                        student[i].setheading(random.randint(160,170))
                        student[i].fd(1)
                    elif student[i].heading()>=270 and student[i].heading()<360:
                        student[i].setheading(random.randint(10,20))
                        student[i].fd(1)
        student[i].fd(movedistance)
    student[i].rt(turnangle)
def goclass():
   check =[]
   for i in range(len(student)):
      check.append(0)
   aisle=[]
   rightposition =0
   for mm in range(len(student)):
      aisle.append(random.randint(-1075,1075)/100)
   while rightposition < len(student):
      for i in range(len(student)):
         if abs(student[i].xcor()-Xpos[i])<=0.5 and abs(student[i].ycor()-Ypos[i])<=0.5 and check[i]==0:
            rightposition += 1
            check[i]=1
         else:
            if student[i].xcor()<Xclassposition[i]-87.5:
               if student[i].ycor()<=aisle[i]-0.25:
                  student[i].setheading(90)
               elif student[i].ycor()>=aisle[i]+0.25:
                  student[i].setheading(270)
               else:student[i].setheading(0)

            elif student[i].xcor()>Xclassposition[i]:
               if student[i].ycor()<=aisle[i]-0.25:
                  student[i].setheading(90)
               elif student[i].ycor()>=aisle[i]+0.25:
                  student[i].setheading(270)
               else:student[i].setheading(180)

            elif student[i].ycor()<Ypos[i] and student[i].xcor()<Xpos[i] :
               student[i].setheading(random.randint(25,65)) 
            elif student[i].ycor()>Ypos[i] and student[i].xcor()<Xpos[i] :
               student[i].setheading(random.randint(-65,-25)) 
            elif student[i].ycor()<Ypos[i] and student[i].xcor()>Xpos[i] :
               student[i].setheading(random.randint(115,155)) 
            elif student[i].ycor()>Ypos[i] and student[i].xcor()>Xpos[i] :
               student[i].setheading(random.randint(205,245)) 
            for j in range(0,random.randint(0,20)):
               student[i].fd(random.random()/3)
         distanceOfInfectious(i)      
def gomovingclass(movingclasstype):
   check =[]
   for i in range(len(student)):
      check.append(0)
   movingXpos=[]
   movingYpos=[]
   Xmovingclassposition=[]
   c1 =[]
   c2 =[]
   c3 =[]
   c4 =[]
   c5 =[]
   c6 =[]
   c7 =[]
   c8 =[]
   c9 =[]
   c10 =[]
   c11 =[]
   c12 =[]
   for i in range(0,len(student)):
      Yposition = 86.25
      if movingclasstype == "A" : movingclassnumber = Aclass[i]
      if movingclasstype == "B" : movingclassnumber = Bclass[i]
      if movingclasstype == "C" : movingclassnumber = Cclass[i]
      if movingclasstype == "D" : movingclassnumber = Dclass[i]
      if movingclasstype == "E" : movingclassnumber = Eclass[i]

      if movingclassnumber == 1 :
         c1.append(i)
         movingstudentnumber = c1.index(i) +1
      if movingclassnumber == 2 :
         c2.append(i)
         movingstudentnumber = c2.index(i) +1
      if movingclassnumber == 3 :
         c3.append(i)
         movingstudentnumber = c3.index(i) +1
      if movingclassnumber == 4 :
         c4.append(i)
         movingstudentnumber = c4.index(i) +1
      if movingclassnumber == 5 :
         c5.append(i)
         movingstudentnumber = c5.index(i) +1
      if movingclassnumber == 6 :
         c6.append(i)
         movingstudentnumber = c6.index(i) +1
      if movingclassnumber == 7 :
         c7.append(i)
         movingstudentnumber = c7.index(i) +1
      if movingclassnumber == 8 :
         c8.append(i)
         movingstudentnumber = c8.index(i) +1
      if movingclassnumber == 9 :
         c9.append(i)
         movingstudentnumber = c9.index(i) +1
      if movingclassnumber == 10 :
         c10.append(i)
         movingstudentnumber = c10.index(i) +1
      if movingclassnumber == 11 :
         c11.append(i)
         movingstudentnumber = c11.index(i) +1
      if movingclassnumber == 12 :
         c12.append(i)
         movingstudentnumber = c12.index(i) +1
      if movingclassnumber ==1:Xmovingclassposition.append(87.5*7)
      elif movingclassnumber ==2:Xmovingclassposition.append(87.5*6)
      elif movingclassnumber ==3:Xmovingclassposition.append(87.5*5)
      elif movingclassnumber ==4:Xmovingclassposition.append(87.5*4)
      elif movingclassnumber ==5:Xmovingclassposition.append(87.5*2)
      elif movingclassnumber ==6:Xmovingclassposition.append(87.5*1)
      elif movingclassnumber ==7:Xmovingclassposition.append(87.5*-0)
      elif movingclassnumber ==8:Xmovingclassposition.append(87.5*-1)
      elif movingclassnumber ==9:Xmovingclassposition.append(87.5*-2)
      elif movingclassnumber ==10:Xmovingclassposition.append(87.5*-3)
      elif movingclassnumber ==11:Xmovingclassposition.append(87.5*-5)
      elif movingclassnumber ==12:Xmovingclassposition.append(87.5*-6)
      movingXpos.append(Xmovingclassposition[i] - ((movingstudentnumber%5)*2)*87.5/11)
      if movingstudentnumber%5 == 0:movingXpos[i] = Xmovingclassposition[i] - (5*2)*87.5/11
      if movingclassnumber ==1 or movingclassnumber ==2:movingYpos.append(Yposition - (movingstudentnumber//5+1)*2*75/15)
      else :movingYpos.append(Yposition - (movingstudentnumber//5+1)*2*75/13)
      if movingstudentnumber%5 == 0 : 
         if movingclassnumber ==1 or movingclassnumber ==2 : movingYpos[i] = Yposition - (movingstudentnumber//5)*2*75/15
         else :movingYpos[i] = Yposition - (movingstudentnumber//5)*2*75/13 
   aisle=[]
   rightposition =0
   for mm in range(len(student)):
      aisle.append(random.randint(-1075,1075)/100)
   while rightposition < len(student):
      for i in range(len(student)):
         if abs(student[i].xcor()-movingXpos[i])<=0.5 and abs(student[i].ycor()-movingYpos[i])<=0.5 and check[i]==0:
            rightposition += 1
            check[i]=1
         else:
            if student[i].xcor()<Xmovingclassposition[i]-87.5:
               if student[i].ycor()<=aisle[i]-0.25:
                  student[i].setheading(90)
               elif student[i].ycor()>=aisle[i]+0.25:
                  student[i].setheading(270)
               else:student[i].setheading(0)

            elif student[i].xcor()>Xmovingclassposition[i]:
               if student[i].ycor()<=aisle[i]-0.25:
                  student[i].setheading(90)
               elif student[i].ycor()>=aisle[i]+0.25:
                  student[i].setheading(270)
               else:student[i].setheading(180)
            elif student[i].ycor()<movingYpos[i] and student[i].xcor()<movingXpos[i] :
               student[i].setheading(random.randint(25,65)) 
            elif student[i].ycor()>movingYpos[i] and student[i].xcor()<movingXpos[i] :
               student[i].setheading(random.randint(-65,-25)) 
            elif student[i].ycor()<movingYpos[i] and student[i].xcor()>movingXpos[i] :
               student[i].setheading(random.randint(115,155)) 
            elif student[i].ycor()>movingYpos[i] and student[i].xcor()>movingXpos[i] :
               student[i].setheading(random.randint(205,245)) 
            for j in range(0,random.randint(0,20)):
               student[i].fd(random.random()/3)
         distanceOfInfectious(i)      
def period(Day, classperiod):
   if Day == "Tue" and classperiod == 7 or Day == "Thu" and classperiod == 1 : gomovingclass("A")
   elif Day == "Mon" and classperiod == 3 or Day == "Wed" and classperiod == 5 : gomovingclass("B")
   elif Day == "Wed" and classperiod == 2 or Day == "Thu" and classperiod == 4 : gomovingclass("C")
   elif Day == "Tue" and classperiod == 1 or Day == "Thu" and classperiod == 6 : gomovingclass("D")
   elif Day == "Mon" and classperiod == 5 or Day == "Fri" and classperiod == 3 : gomovingclass("E")
   else : goclass()
def breaktimemove():
    for numm in range(0,int(breaktime)):
      for ii in movingstudent:
         move(ii)
      for i in range(len(student)):
         distanceOfInfectious(i)      
def lunchbreakmove():
   for numm in range(0,int(lunchbreak)):
      for ii in movingstudent:
         move(ii)
      for i in range(len(student)):
         distanceOfInfectious(i)  
def studentsetting():
   for i in range(studentnum):
      student.append(i)
      if i<=32 : substudent.append(20100+i+1)
      elif i<=65 : substudent.append(20200+i-32)
      else : substudent.append(20000+((i-66)//29+3)*100+(i-66)%29+1)
      student[i] = t.Turtle()
      student[i].color('Lime')
      student[i].up()
      student[i].speed(0)
      student[i].shape('circle') 
      student[i].turtlesize(0.1,0.1,0)
def contact():
    for k in range(len(student)):
        c=random.randint(1,100)
        if c<=ContactTime[k]:
            if state[k] == 3 or state[k] == 4:
                state[k] = 5
                ip=2*np.random.f(20,20,len(student))+1.2
                ip=ip.astype('int8')
                IncubationPeriod[k] = ip[k]
        else:
            if state[k] == 3 or state[k] == 4:
                state[k] = 1
def funcExposed():
    for member in range(len(student)):
        if state[member] == 5:
            IncubationPeriod[member] = IncubationPeriod[member] -1
            if IncubationPeriod[member] <= 0:
                prob = random.randint(1,100)
                if prob >= AsymptomRate:
                    state[member] = 6
                if prob < AsymptomRate:
                    state[member] = 8
def distanceOfInfectious(im):
    if len(Confirmed) != 0:
      for m in Confirmed:
         student[init].color("Red")
    for m in Infectious:#I->S
      if state[im] == 1 or 3:
         if student[im].distance(m)<=10 and student[im].distance(m)>0:
            if abs(student[im].xcor()%87.5 - m.xcor()%87.5) <=30 or m.ycor()<=11.25:
               ContactTime[im] += InfectRate
               if state[im] == 1:
                  state[im] = 3
                  student[im].color("Green")
                  Contacted.append(student[im])
         if student[im].distance(m)<=20 and student[im].distance(m)>10:
            if abs(student[im].xcor()%87.5 - m.xcor()%87.5) <=30 or m.ycor()<=11.25:
               ContactTime[im] += InfectRate/5
               if state[im] == 1:
                  state[im] = 3
                  student[im].color("Green")
                  Contacted.append(student[im])
    for m in IMasking:#Im->S
      if state[im] == 1 or 3:
         if student[im].distance(m)<=10 and student[im].distance(m)>0:
            if abs(student[im].xcor()%87.5 - m.xcor()%87.5) <=30 or m.ycor()<=11.25:
               ContactTime[im] += InfectRate*2/10
               if state[im] == 1:
                  state[im] = 3
                  student[im].color("Green")
                  Contacted.append(student[im])
         if student[im].distance(m)<=20 and student[im].distance(m)>10:
            if abs(student[im].xcor()%87.5 - m.xcor()%87.5) <=30 or m.ycor()<=11.25:
               ContactTime[im] += InfectRate*2/50
               if state[im] == 1:
                  state[im] = 3
                  student[im].color("Green")
                  Contacted.append(student[im])
    for m in Asymptomatic:#A->S
      if state[im] == 1 or 3:
         if student[im].distance(m)<=10 and student[im].distance(m)>0:
            if abs(student[im].xcor()%87.5 - m.xcor()%87.5) <=30 or m.ycor()<=11.25:
               ContactTime[im] += InfectRate/100
               if state[im] == 1:
                  state[im] = 3
                  student[im].color("Green")
                  Contacted.append(student[im])
    for m in AMasking:#Am->S
      if state[im] == 1 or 3:
         if student[im].distance(m)<=10 and student[im].distance(m)>0:
            if abs(student[im].xcor()%87.5 - m.xcor()%87.5) <=30 or m.ycor()<=11.25:
               ContactTime[im] += InfectRate*2/1000
               if state[im] == 1:
                  state[im] = 3
                  student[im].color("Green")
                  Contacted.append(student[im])
    for m in Confirmed:#Ic->S
      if state[im] == 1 or 3:
            if student[im].distance(m)<=10 and student[im].distance(m)>0:
                if abs(student[im].xcor()%87.5 - m.xcor()%87.5) <=30 or m.ycor()<=11.25:
                    ContactTime[im] += InfectRate
                    if state[im] == 1:
                        state[im] = 3
                        student[im].color("Green")
                        Contacted.append(student[im])
            if student[im].distance(m)<=20 and student[im].distance(m)>10:
                if abs(student[im].xcor()%87.5 - m.xcor()%87.5) <=30 or m.ycor()<=11.25:
                    ContactTime[im] += InfectRate/5
                    if state[im] == 1:
                        state[im] = 3
                        student[im].color("Green")
                        Contacted.append(student[im])
    for m in Infectious:#I->Sm
      if state[im] == 2 or 4:
         if student[im].distance(m)<=10 and student[im].distance(m)>0:
            if abs(student[im].xcor()%87.5 - m.xcor()%87.5) <=30 or m.ycor()<=11.25:
               ContactTime[im] += InfectRate*7/10
               if state[im] == 2:
                  state[im] = 4
                  student[im].color("Green")
                  CMasking.append(student[im])
         if student[im].distance(m)<=20 and student[im].distance(m)>10:
            if abs(student[im].xcor()%87.5 - m.xcor()%87.5) <=30 or m.ycor()<=11.25:
               ContactTime[im] += InfectRate*7/50
               if state[im] == 2:
                  state[im] = 4
                  student[im].color("Green")
                  CMasking.append(student[im])
    for m in IMasking:#Im->Sm
      if state[im] == 2 or 4:
         if student[im].distance(m)<=10 and student[im].distance(m)>0:
            if abs(student[im].xcor()%87.5 - m.xcor()%87.5) <=30 or m.ycor()<=11.25:
               ContactTime[im] += InfectRate*5/100
               if state[im] == 2:
                  state[im] = 4
                  student[im].color("Green")
                  CMasking.append(student[im])
         if student[im].distance(m)<=20 and student[im].distance(m)>10:
            if abs(student[im].xcor()%87.5 - m.xcor()%87.5) <=30 or m.ycor()<=11.25:
               ContactTime[im] += InfectRate*5/500
               if state[im] == 2:
                  state[im] = 4
                  student[im].color("Green")
                  CMasking.append(student[im])
    for m in Asymptomatic:#A->Sm
      if state[im] == 2 or 4:
         if student[im].distance(m)<=10 and student[im].distance(m)>0:
            if abs(student[im].xcor()%87.5 - m.xcor()%87.5) <=30 or m.ycor()<=11.25:
               ContactTime[im] += InfectRate*7/1000
               if state[im] == 2:
                  state[im] = 4
                  student[im].color("Green")
                  CMasking.append(student[im])
    for m in AMasking:#Am->Sm
      if state[im] == 2 or 4:
         if student[im].distance(m)<=10 and student[im].distance(m)>0:
            if abs(student[im].xcor()%87.5 - m.xcor()%87.5) <=30 or m.ycor()<=11.25:
               ContactTime[im] += InfectRate*5/10000
               if state[im] == 2:
                  state[im] = 4
                  student[im].color("Green")
                  CMasking.append(student[im])
    for m in Confirmed:#Ic->Sm
      if state[im] == 2 or 4:
            if student[im].distance(m)<=10 and student[im].distance(m)>0:
                if abs(student[im].xcor()%87.5 - m.xcor()%87.5) <=30 or m.ycor()<=11.25:
                    ContactTime[im] += InfectRate*7/10
                    if state[im] == 2:
                        state[im] = 4
                        student[im].color("Green")
                        CMasking.append(student[im])
            if student[im].distance(m)<=20 and student[im].distance(m)>10:
                if abs(student[im].xcor()%87.5 - m.xcor()%87.5) <=30 or m.ycor()<=11.25:
                    ContactTime[im] += InfectRate*7/50
                    if state[im] == 2:
                        state[im] = 4
                        student[im].color("Green")
                        CMasking.append(student[im])
def week():
   
   Day = ["Mon", "Tue", "Wed", "Thu", "Fri"]
   for day in Day:
      print(day)
      global DayNum
      DayNum += 1
      global rp
      global avrrp
      avrrp =0
      global pop
      rp = 0
      ContactTime.clear()
      for i in range(len(student)):
        ContactTime.append(0)
      for d in ContactTime:
         rp += d
      avrrp = rp/len(ContactTime)
      pop.append(avrrp)
      global rh
      global hour
      initposition()
      for ji in range(len(student)):
        if random.randint(1,100) <= maskingPercent:
            if state[ji] == 1:
                state[ji] = 2
            if state[ji] == 6:
                state[ji] = 7
            if state[ji] == 8:
                state[ji] = 9
      for mi in range(0, len(student)):
         initturn(mi,random.randint(0,360)) 
      for classtime in range (1, 8):
         if day != "Fri" or classtime != 7:
            pass
            pass
            if day == "Mon": pass
            if day == "Tue": pass
            if day == "Wed": pass
            if day == "Thu": pass
            if day == "Fri": pass
            pass
            if classtime == 1: 
               pass
               pass
            elif classtime == 2: 
               pass
               pass
            elif classtime == 3: 
               pass
               pass
            else : 
               pass
               pass
            pass
            period(day,classtime)
            time.sleep(1)
            if classtime != 7:
               if day != "Fri" or classtime !=6:
                  pass
                  pass
                  if day == "Mon": pass
                  if day == "Tue": pass
                  if day == "Wed": pass
                  if day == "Thu": pass
                  if day == "Fri": pass
                  if classtime == 4:
                     pass
                     movingstudent.clear()
                     movingrestriction()
                     lunchbreakmove()
                     rp = 0
                     avrrp =0
                     for d in ContactTime:
                        rp += d
                     avrrp = rp/len(ContactTime)
                     pop.append(avrrp)
                     hour.append(rh)
                     rh += 1
                  else:
                     pass
                     movingstudent.clear()
                     movingrestriction()
                     breaktimemove()
                     rp = 0
                     avrrp =0
                     for d in ContactTime:
                        rp += d
                     avrrp = rp/len(ContactTime)
                     pop.append(avrrp)
                     hour.append(rh)
                     rh += 1
      pass
      pass
      pass
      for ik in range(len(student)):
        if state[ik] == 2:
            state[ik] = 1
        if state[ik] == 7:
            state[ik] = 6
        if state[ik] == 9:
            state[ik] = 8
      SMasking.clear()
      IMasking.clear()
      AMasking.clear()
      goclass()
      funcExposed()
      contact()
      movingstudent.clear()
      movingrestriction()
      breaktimemove()
      rp = 0
      avrrp =0
      for d in ContactTime:
         rp += d
      avrrp = rp/len(ContactTime)
      pop.append(avrrp)
      hour.append(rh)
      rh += 1
      statecheck()
      coloring()
      
      hour.append(rh)
      rh += 16
      pop.append(0)
      if DayNum == testday:
        break  
def record():
    
    recorder.clear()
    SusceptibleNum = 0
    ContactedNum = 0
    ExposedNum = 0
    InfectiousNum = 0
    AsymptomaticNum = 0
    SusceptibleNum = len(Susceptible)+len(SMasking)-len(Contacted)-len(CMasking)
    ContactedNum = len(Contacted)+len(CMasking)
    ExposedNum = len(Exposed)
    InfectiousNum = len(Infectious)+len(IMasking)+1
    AsymptomaticNum = len(Asymptomatic)+len(AMasking)
    recorder.write("Susceptible : ", True)
    recorder.write(SusceptibleNum, True)
    recorder.write("    Contacted : ", True)
    recorder.write(ContactedNum, True)
    recorder.write("    Exposed : ", True)
    recorder.write(ExposedNum, True)
    recorder.write("    Infectious : ", True)
    recorder.write(InfectiousNum, True)
    recorder.write("    Asymptomatic : ", True)
    recorder.write(AsymptomaticNum, True)
    recorder.goto(200,200)  
def movingrestriction():
    for oo in range(len(student)):
        if random.randint(1,100) >= movingRestrictionPercent: movingstudent.append(oo)
def coloring():
    for sc in range(len(student)):
        if state[sc] == 0: student[sc].color("Red")
        if state[sc] == 1: student[sc].color("Lime")
        if state[sc] == 2: student[sc].color("Lime")
        if state[sc] == 3: student[sc].color("Green")
        if state[sc] == 4: student[sc].color("Green")
        if state[sc] == 5: student[sc].color("Blue")
        if state[sc] == 6: student[sc].color("Orange")
        if state[sc] == 7: student[sc].color("Orange")
        if state[sc] == 8: student[sc].color("Magenta")
        if state[sc] == 9: student[sc].color("Magenta")
        if state[sc] == 10: student[sc].hideturtle()
        if state[sc] == 11: student[sc].hideturtle()
        if state[sc] == 12: student[sc].color("Pink")
        if state[sc] == 13: student[sc].hideturtle()
def statecheck():
    Susceptible.clear()
    SMasking.clear()
    Contacted.clear()
    CMasking.clear()
    Exposed.clear()
    Infectious.clear()
    IMasking.clear()
    Asymptomatic.clear()
    AMasking.clear()
    for e in range(len(student)):
        if state[e] == 0:
            Confirmed.append(student[e])
        if state[e] == 1:
            Susceptible.append(student[e])
        if state[e] == 2:
            SMasking.append(student[e])
        if state[e] == 3:
            Contacted.append(student[e])
        if state[e] == 4:
            CMasking.append(student[e])
        if state[e] == 5:
            Exposed.append(student[e])
        if state[e] == 6:
            Infectious.append(student[e])
        if state[e] == 7:
            IMasking.append(student[e])
        if state[e] == 8:
            Asymptomatic.append(student[e])
        if state[e] == 9:
            AMasking.append(student[e])
        if state[e] == 10:
            Quarantined.append(student[e])
        if state[e] == 12:
            Recovered.append(student[e])

for inin in range(2):
    f=open("C:/Users/user/Desktop/이상원 2020/program/PY/Academia/Senario5.txt",'a')
    f.write("senario5 ___immediatestop_____")
    f.close()

    
    # studentnum = class[1,2] : 33, else[]:29
    student = []
    substudent = []
    movingstudent = []

    #parameters_disease
    #average_incubating_period = 5days
    InfectRate = 0.00010875
    AsymptomRate = 36.4

    #parameters_implements
    maskingPercent = 65.2
    movingRestrictionPercent = 50 
    testday = 3

    #variables
    Xpos = []
    Ypos = []
    Xclassposition = []
    DayNum = 0
    Confirmed = []    # Red     (0)
    Susceptible = []  # Lime    (1)
    SMasking = []     # Lime    (2)
    Contacted = []    # Green   (3)
    CMasking = []     # Green   (4)
    Exposed = []      # Blue    (5)
    Infectious = []   # Orange  (6)
    IMasking = []     # Orange  (7)
    Asymptomatic = [] # Magenta (8)
    AMasking = []     # Magenta (9)
    Quarantined = []  # hide    (10)
    Critical = []     # hide    (11)
    Recovered = []    # Pink    (12)
    Dead = []         # hide    (13)
    IncubationPeriod = []
    state = []
    ContactTime = []
    hour = []
    pop = []
    rh = 0
    rp = 0

    #main_function

    #make_rooms
    t.tracer(0,0)
    drawingturtle = t.Turtle()
    drawingturtle.shape('turtle')
    drawingturtle.speed(0) 
    drawingturtle.up()   
    drawingturtle.goto(-612.5,86.25)
    drawingturtle.down()
    square(2)
    t.delay(0)
    classroom()
    studentsetting()

    #time_writer
    pass
    pass
    pass
    pass

    #day_writer
    Daywriter = t.Turtle()
    Daywriter.up()
    Daywriter.hideturtle()
    Daywriter.goto(-450,200)

    #recorder
    recorder = t.Turtle()
    recorder.up()
    recorder.hideturtle()
    recorder.goto(200,200)

    #state_setting
    np.random.seed(random.randint(1,50))
    init = random.randint(1,studentnum)
    for i in range(len(student)):
        ContactTime.append(0)
        IncubationPeriod.append(0)
        state.append(1)
        if i != init:
            Susceptible.append(student[i])
        else:
            Confirmed.append(student[init])
    for ic in Confirmed:
        state[student.index(ic)] = 0
        ic.color("Red")
    t.update()

    #week
    while True:
        t.tracer(0,0)
        week()
        if DayNum == testday:
            break
        t.update()
    f = open("C:/Users/user/Desktop/이상원 2020/program/PY/Academia/Senario5.txt", 'a')
    data = "Exposed : %d    Infectious : %d    Asymptomatic : %d    \n" %(len(Exposed),len(Infectious)+len(IMasking)+1,len(Asymptomatic)+len(AMasking))
    f.write(data)
    f.write("contacted per hour : ")
    for writing in pop:
        datavalue = "%s, " %writing
        f.write(datavalue)
    f.write("\n")
    f.close()
    print("Dayend")
t.mainloop()