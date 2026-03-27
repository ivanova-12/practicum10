import turtle as t

def triangle(x: int, y: int, a: int,
             destination: int, color: str):
    """Draws a triangle with help of 1 vertex
    and particular size of side
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()

    if destination == 1:
        t.forward(a)
        t.goto(x, y)
        t.left(90)
        t.forward(a)
        t.right(135)
        t.forward((a ** 2 * 2) ** 0.5)

    elif destination == 2:
        t.left(90)
        t.forward(a)
        t.goto(x, y)
        t.left(90)
        t.forward(a)
        t.right(135)
        t.forward((a ** 2 * 2) ** 0.5)

    elif destination == 3:
        t.right(180)
        t.forward(a)
        t.goto(x, y)
        t.left(90)
        t.forward(a)
        t.right(135)
        t.forward((a ** 2 * 2) ** 0.5)

    elif destination == 4:
        t.forward(a)
        t.goto(x, y)
        t.right(90)
        t.forward(a)
        t.left(135)
        t.forward((a ** 2 * 2) ** 0.5)

    elif destination == 5:
        t.right(45)
        t.forward(a)
        t.goto(x, y)
        t.left(90)
        t.forward(a)
        t.right(135)
        t.forward((a ** 2 * 2) ** 0.5)

    elif destination == 6:
        t.left(180)
        t.left(45)
        t.forward(a)
        t.goto(x, y)
        t.right(90)
        t.forward(a)
        t.left(135)
        t.forward((a ** 2 * 2) ** 0.5)

    elif destination == 7:
        t.right(45)
        t.forward(a)
        t.goto(x, y)
        t.right(90)
        t.forward(a)
        t.left(135)
        t.forward((a ** 2 * 2) ** 0.5)

    elif destination == 8:
        t.left(45)
        t.forward(a)
        t.goto(x, y)
        t.left(90)
        t.forward(a)
        t.right(135)
        t.forward((a ** 2 * 2) ** 0.5)

    t.penup()
    t.end_fill()
    t.setheading(to_angle=0)


def trapezoid(x: int, y: int, a: int, b: int,
              height: int, placement: int, color: str):
    """Draws a trapezoid with help of 1 vertex
    and sizes of sides and height
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.fillcolor(color)

    if placement == 1:
        t.begin_fill()
        t.forward(a)
        t.right(90)
        t.penup()
        t.forward(height)
        t.pendown()
        t.left(90)
        t.forward((b - a) / 2)
        t.goto(x + a, y)
        t.right(90)
        t.penup()
        t.forward(height)
        t.pendown()
        t.right(90)
        t.forward((b + a) / 2)
        t.goto(x, y)
        t.end_fill()

    elif placement == 2:
        t.forward(b)
        t.right(90)
        t.penup()
        t.forward(height)
        t.right(90)
        t.forward((b - a) / 2)
        t.pendown()
        t.forward(a)
        t.begin_fill()
        t.goto(x, y)
        t.goto(x + b, y)
        t.left(t.towards(x + ((b + a) / 2), y - height))
        t.backward((((b - a) / 2) ** 2 + height ** 2) ** 0.5)
        t.end_fill()

    elif placement == 3:
        t.right(90)
        t.forward(a)
        t.left(90)
        t.penup()
        t.forward(height)
        t.pendown()
        t.begin_fill()
        t.right(90)
        t.forward((b - a) / 2)
        t.goto(x, y - a)
        t.goto(x, y)
        t.left(90)
        t.penup()
        t.forward(height)
        t.pendown()
        t.left(90)
        t.forward((b - a) / 2)
        t.goto(x, y)
        t.penup()
        t.right(90)
        t.forward(height)
        t.pendown()
        t.right(90)
        t.forward((b + a) / 2)
        t.end_fill()

    elif placement == 4:
        t.right(90)
        t.forward(b)
        t.left(90)
        t.penup()
        t.forward(height)
        t.left(90)
        t.forward((b - a) / 2)
        t.begin_fill()
        t.pendown()
        t.forward(a)
        t.goto(x, y)
        t.right(180)
        t.forward(b)
        t.goto(x + height, y - ((b + a) / 2))
        t.end_fill()

    t.penup()
    t.setheading(to_angle=0)


def square(x: int, y: int, a: int,
           alpha: int, color: str):
    """Draws a square with help of 1 vertex, side
    and angle of turning
    """
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    t.up()
    t.goto(x, y)
    t.down()
    t.right(alpha)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90 - alpha)
    t.up()
    t.end_fill()


def drawing():
    """Draw the end picture"""
    for i in range(25):
        triangle(-600 + 50*i, 100, 70, 7, 'lightpink')

    for i in range(25):
        square(-600 + 50*i, 150,  25, 45, 'lightgreen')

    for i in range(1, 15):
        if i % 2 == 0:
            color = 'plum3'
            trapezoid(-600 + 70*i, 49, 40, 70, 50, 1, color)
        else:
            color = 'orchid4'
            trapezoid(-600 + 70*i, 49, 40, 70, 50, 2, color)
    t.done()

if __name__ == '__main__':
    drawing()



