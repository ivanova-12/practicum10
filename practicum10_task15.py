import turtle as t
import random as r

def house(side: int) -> None:
    """Draw the shadow of one house"""
    t.left(90)
    t.forward(side)
    t.right(90)
    t.forward(side/1.5)
    t.right(90)
    t.forward(side)
    t.left(90)
    t.forward(side // 2)


def moon(size: int) -> None:
    """Draw the moon"""
    t.penup()
    t.goto(0, 300)
    t.pendown()
    t.color('white')
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    t.penup()


def shadow(y1: int , color: str) -> None:
    """Draw the shadow of all houses in one line"""
    t.penup()
    t.color(color)
    t.goto(-900, y1)
    t.pendown()
    side = r.randint(50, 200)
    nums_of_houses = r.randint(15, 30)

    t.begin_fill()
    for i in range(nums_of_houses):
        house(side)
        side = r.randint(50, 200)
    t.right(90)
    t.forward(side * 20)
    t.goto(-900, -900)
    t.end_fill()

    t.setheading(0)
    t.penup()


def stars() -> None:
    """Draw the stars"""
    t.penup()
    nums_of_stars = r.randint(100, 500)

    for i in range(nums_of_stars):
        x = r.randint(-900, 900)
        y = r.randint(-900, 900)
        t.goto(x, y)
        t.pendown()
        t.dot(5, 'white')
        t.penup()
    t.setheading(0)


def windows() -> None:
    """Draw the windows"""
    t.color('yellow')
    nums_of_windows = r.randint(50, 200)

    for i in range(nums_of_windows):
        t.begin_fill()
        x = r.randint(-900, 900)
        y = r.randint(-400, 50)
        radius = r.randint(5, 10)
        t.goto(x, y)
        t.pendown()
        t.circle(radius)
        t.end_fill()
        t.penup()

    t.setheading(0)


def night_town() -> None:
    """Draw the night town/the end picture"""
    t.speed(500)
    t.screensize(1200, 1920)
    t.bgcolor('darkblue')
    stars()
    shadow(0, 'azure4')
    windows()
    shadow(-200, 'black')
    moon(20)
    t.hideturtle()
    t.done()

if __name__ == '__main__':
    night_town()
    
