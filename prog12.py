from turtle import *

screen = Screen()

penup()
goto(-200, -150)  
pendown()

colors = ["blue", "red", "magenta"]
k = 0  

def sierpinskiTriangle(n, l):
    global k  # Use the global k variable
    if n == 0:
        return
    else:
        fillcolor(colors[k % 3])  
        begin_fill()
        for i in range(3):
            forward(l)
            left(120)
            sierpinskiTriangle(n-1, l/2)
        end_fill()
        
        k += 1  

sierpinskiTriangle(3, 2**8)

screen.mainloop()
