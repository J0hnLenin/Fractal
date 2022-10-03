import turtle

#set input parametr's

counteer = 0
DEEP = 8  #глубина рекурсии
len = 900 #длинна стороны
turtle.fillcolor("black")
turtle.pencolor("white")
turtle.bgcolor("black")
turtle.speed(0)

#start
turtle.up()
turtle.setpos(500, -350)
turtle.down()


turtle.backward(len)
turtle.left(60)
turtle.forward(len)
turtle.left(60)
turtle.backward(len)
turtle.up()

#main

def triangle(n):

    turtle.forward(n)
    turtle.left(60)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(n)
    turtle.right(60)
    turtle.backward(n)
    turtle.right(60)
    turtle.forward(n)
    turtle.end_fill()
    turtle.up()
    turtle.left(60)

    return 0

def fractal(n, counteer):

    if counteer >= DEEP:
        counteer -= 1
        return 0

    triangle(n)
    counteer += 1

    turtle.backward(n)
    new_start = turtle.pos()
    fractal(n/2, counteer)

    turtle.setpos(new_start)
    turtle.forward(n)
    fractal(n/2, counteer)

    turtle.setpos(new_start)
    turtle.left(60)
    turtle.forward(n)
    turtle.right(60)
    fractal(n/2, counteer)

    return 0

fractal(len/2, 0)

#finish
turtle.done()