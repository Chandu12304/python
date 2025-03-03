import turtle 
 
def koch_curve(t, length, depth): 
   if depth == 0: 
       t.forward(length) 
       return 
   length /= 3 
   koch_curve(t, length, depth - 1) 
   t.left(60) 
   koch_curve(t, length, depth - 1) 
   t.right(120) 
   koch_curve(t, length, depth - 1) 
   t.left(60) 
   koch_curve(t, length, depth - 1) 
 
# Setup Turtle 
t = turtle.Turtle() 
t.speed(0) 
 
# Define the Koch Snowflake 
depth = 2  # Change this for complexity 
size = 300 
points = [(-size / 2, -100), (size / 2, -100), (0, size * (3**0.5) / 3 - 
100)] 
 
# Move to starting point 
t.penup() 
t.goto(points[0]) 
t.pendown() 
 
# Draw the three sides of the Koch Snowflake 
for i in range(3): 
   koch_curve(t, size, depth) 
   t.right(120) 
 
turtle.done() 
