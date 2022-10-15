from turtle import Screen, Turtle

def pixel(ls, width = 1, t = Turtle(), pos = (-20, -20)):
    """
    Draw pixel art according to ls
    """
    t.speed(0)
    t.hideturtle()
    for ind, row in enumerate(ls):
        for col, pixel in enumerate(row):
            if pixel == "":
                continue
            # Draw square
            t.penup()
            t.goto(col * width * 10 + pos[0], -ind * width * 10 + pos[1])
            t.setheading(90)
            t.color(pixel)
            t.pendown()
            t.begin_fill()
            for _ in range(4):
                t.fd(width * 10)
                t.left(90)
            t.end_fill()


a = "black"
b = "white"
c = 'lightcyan'
d = 'turquoise'

dolphin = [
    ['', '', '', '', '', '', '', '', a, a, '', '', '', '', ''],
    ['', '', '', '', '', '', '', a, d, a, '', '', '', '', ''],
    ['', '', '', '', a, a, a, d, d, a, a, '', '', '', ''],
    ['', '', '', a, d, d, d, d, c, c, d, a, "", '', ''],
    ['', '', a, d, b, b, c, c, c, c, c, d, a, '', ''],
    ['', a, a, d, a, b, c, c, c, c, c, c, d, a, ''],
    [a, d, d, c, c, c, c, d, b, b, c, c, c, a, ''],
    ['', a, a, a, a, a, a, d, d, a, b, c, c, d, a],
    ['', '', '', '', a, c, a, a, d, a, a, b, c, c, a],
    ['', '', '', '', '', a, '', '', a, a, '', a, c, c, a],
    ['', '', '', '', '', '', '', '', '', '', '', a, c, a, ''],
    ['', '', '', '', '', '', '', '', '', '', a, a, c, a, ''],
    ['', '', '', '', '', '', '', '', '', a, c, c, a, '', ''],
    ['', '', '', '', '', '', '', '', '', '', a, c, a, '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', a, '', '', '']
]


def draw(pix_grid):
    
    art_grid = []
    for row in pix_grid:
        art_row = []
        for pix in row:
            if pix == 1:
                art_row.append(a)
            else:
                art_row.append('')
        art_grid.append(art_row)
    

    wn = Screen()
    wn.tracer(0)

    pixel(art_grid)

    wn.mainloop()