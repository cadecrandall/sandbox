CANVAS_SIZE = 500
DENSITY = 12

import turtle
import random

def draw_line(row, col):
    lower_left = (
        (col * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        (row * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )
    upper_right = (
        ((col + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        ((row + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )
    lower_right = (
        ((col + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        (row * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )
    upper_left = (
        (col * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        ((row + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )

    res = random.randint(0, 1)

    if res == 0:
        t.goto(upper_left)
        t.pendown()
        t.goto(lower_right)
        t.penup()
    else:
        t.goto(lower_left)
        t.pendown()
        t.goto(upper_right)
        t.penup()

t = turtle.Turtle()
s = turtle.Screen()
s.setup(CANVAS_SIZE, CANVAS_SIZE)

t.penup()

for row in range(DENSITY):
    for col in range(DENSITY):
        draw_line(row, col)


if __name__ == '__main__':
    s.mainloop()