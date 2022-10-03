import turtle

""""Settings"""

turtle.color("white")
turtle.bgcolor("black")
turtle.speed("fastest")


#turtle.tracer(10000)
#раскомментируйте turtle.tracer(10000), чтобы ускорить программу

SIZE = 400
#SIZE - размер самого большого ребра

MINSIZE = 1
#MINSIZE - размер самого маленького резбра

orientation = 6

# orientation == 3 - "куб"
# orientation == 6 - снежинка
# orientation == 14 - одуванчик

LEVELS = 5

"""start"""
queue = []

for i in range(orientation):
    turtle.forward(SIZE)
    turtle.backward(SIZE)
    turtle.right(360 / orientation)

for j in range(1, LEVELS+1):
    for i in range(orientation):
        queue.append([turtle.pos(), turtle.heading(), 0.75*(SIZE*(1 - j/(LEVELS+1))) ])
        turtle.right(360 / orientation)

turtle.up()

"""Main"""

def edge():

    poss, headd, n = queue.pop(0)

    turtle.setpos(poss)
    turtle.setheading(headd)

    turtle.down()
    turtle.forward(n)
    turtle.left(360 / orientation)
    if n / 2 >= MINSIZE:
        queue.append([turtle.pos(), turtle.heading(), n / 2])
    turtle.forward(n)
    turtle.backward(n)
    turtle.right(360 / orientation * 2)
    if n / 2 >= MINSIZE:
        queue.append([turtle.pos(), turtle.heading(), n / 2])
    turtle.forward(n)
    turtle.backward(n)
    turtle.left(360 / orientation)
    turtle.backward(n)
    turtle.right(360 / orientation)
    turtle.up()
    return 0

while queue:
    edge()


"""Finish"""

turtle.update()
#turtle.done()
turtle.mainloop()

