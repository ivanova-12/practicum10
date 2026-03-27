import turtle as t

def triangle(v1: tuple, v2: tuple, v3: tuple, color: str) -> None:
    """Draw a triangle with help 3 vertex and color"""
    t.up()
    t.pencolor(color)
    t.goto(v1)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(v2)
    t.goto(v3)
    t.goto(v1)
    t.end_fill()
