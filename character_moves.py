from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def SquareMove():
    grass.draw_now(400, 30)
    x = 50
    while x < 750:
        character.draw_now(x, 90)
        x += 5
        delay(0.01)
    y = 90
    while y < 550:
        character.draw_now(750, y)
        y += 5
        delay(0.01)

def TriangleMove():
    pass

def CircleMove():
    pass

while True:
    SquareMove()
    TriangleMove()
    CircleMove()
    break

close_canvas()
