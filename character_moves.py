from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def SquareMove():
    grass.draw_now(400, 30)
    character.draw_now(50, 90)
    delay(5)

def TriangleMove():
    pass

def CircleMove():
    pass

while True:
    SquareMove()
    TriangleMove()
    CircleMove()

close_canvas()
