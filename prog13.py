from turtle import *

screen=Screen()

def koch_curve(length, depth): 
   if depth == 0: 
       forward(length) 
       return 
   length /= 3 
   koch_curve(length, depth - 1) 
   left(60) 
   koch_curve(length, depth - 1) 
   right(120) 
   koch_curve(length, depth - 1) 
   left(60) 
   koch_curve(length, depth - 1) 
 
penup() 
goto(-80,20) 
pendown() 

speed(10)
 
fillcolor("pink")
begin_fill()
for i in range(3): 
   koch_curve(300,2) 
   right(120)
end_fill()

