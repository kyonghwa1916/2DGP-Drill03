from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def SquareMove():
    x = 50
    while x < 750:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x += 5
        delay(0.01)
    y = 90
    while y < 550:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(750, y)
        y += 5
        delay(0.01)
    x = 750
    while x > 50:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 550)
        x -= 5
        delay(0.01)
    y = 550
    while y > 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(50, y)
        y -= 5
        delay(0.01)
def TriangleMove():
    pass

def CircleMove():
    x = 400
    y = 300
    r = 200
    rad = 0
    while rad < 2*math.pi:
        grass.draw_now(400, 30)
        character.draw_now(x + r*math.cos(rad), y + r*math.sin(rad))
        rad += 2*math.pi/360
        delay(0.01)


while True:
    #SquareMove()
    TriangleMove()
    CircleMove()
    break

close_canvas()
