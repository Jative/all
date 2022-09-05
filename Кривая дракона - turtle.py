import turtle as t

t.shape('turtle')
t.speed(100)
t.penup()
t.setposition(100, 100)
t.pendown()
t.pensize(2)
t.bgcolor("gray")
t.pencolor("white")

axiom = "FX"
axm = ""
translate = {"+":"+", "-":"-", "F":"F", "X":"X+YF+", "Y":"-FX-Y"}

for i in range(12):
    for symb in axiom:
        axm += translate[symb]
    axiom = axm
    axm = ""
print(axiom)
for j in axiom:
        if j == "+":
                t.right(90)
        elif j == "-":
                t.left(90)  
        else:
                t.forward(3)
        
t.update()
t.mainloop()
