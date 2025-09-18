import pico2d
import math

pico2d.open_canvas(800, 800)
grass = pico2d.load_image('grass.png')
character = pico2d.load_image('character.png')

running = True

# 캐릭터 크기(중심 기준) 보정값
CHARACTER_OFFSET_Y = 50  # 캐릭터 이미지 높이의 절반 정도로 가정

# 사각형 경로 정보
SQUARE_SIZE = 600
SQUARE_START_X = 100
SQUARE_START_Y = 100 + CHARACTER_OFFSET_Y
SQUARE_POINTS = [
    (SQUARE_START_X, SQUARE_START_Y),
    (SQUARE_START_X + SQUARE_SIZE, SQUARE_START_Y),
    (SQUARE_START_X + SQUARE_SIZE, SQUARE_START_Y + SQUARE_SIZE),
    (SQUARE_START_X, SQUARE_START_Y + SQUARE_SIZE)
]

# 삼각형 경로 정보 (정삼각형, 시계 반대방향)
TRIANGLE_SIZE = 600
TRIANGLE_CENTER = (400, 400)
TRIANGLE_RADIUS = TRIANGLE_SIZE / (math.sqrt(3))  # 내접원의 반지름
TRIANGLE_POINTS = []
for i in range(3):
    angle = math.radians(90 + i * 120)  # 90도부터 시작, 시계 반대방향
    x = TRIANGLE_CENTER[0] + TRIANGLE_RADIUS * math.cos(angle)
    y = TRIANGLE_CENTER[1] + TRIANGLE_RADIUS * math.sin(angle)
    TRIANGLE_POINTS.append((x, y + CHARACTER_OFFSET_Y))

# 원 경로 정보 (시계방향)
CIRCLE_CENTER = (400, 400)
CIRCLE_RADIUS = 300


def draw_scene(x, y):
    grass.draw(400, 40)
    character.draw(x, y)

def move_linear(start, end, steps):
    for i in range(steps):
        t = i / steps
        x = start[0] + (end[0] - start[0]) * t
        y = start[1] + (end[1] - start[1]) * t
        pico2d.clear_canvas()
        draw_scene(x, y)
        pico2d.update_canvas()
        pico2d.delay(0.01)
        for event in pico2d.get_events():
            if event.type == pico2d.SDL_QUIT:
                return False
    return True

def animate_square():
    for i in range(4):
        start = SQUARE_POINTS[i]
        end = SQUARE_POINTS[(i+1)%4]
        if not move_linear(start, end, 120):
            return False
    return True

def animate_triangle():
    for i in range(3):
        start = TRIANGLE_POINTS[i]
        end = TRIANGLE_POINTS[(i+1)%3]
        if not move_linear(start, end, 120):
            return False
    return True

def animate_circle():
    steps = 360
    for i in range(steps):
        angle = math.radians(-i)  # 시계방향
        x = CIRCLE_CENTER[0] + CIRCLE_RADIUS * math.cos(angle)
        y = CIRCLE_CENTER[1] + CIRCLE_RADIUS * math.sin(angle) + CHARACTER_OFFSET_Y
        pico2d.clear_canvas()
        draw_scene(x, y)
        pico2d.update_canvas()
        pico2d.delay(0.01)
        for event in pico2d.get_events():
            if event.type == pico2d.SDL_QUIT:
                return False
    return True

while running:
    if not animate_square():
        break
    if not animate_triangle():
        break
    if not animate_circle():
        break
    running = False  # 한 번만 실행 후 종료

pico2d.close_canvas()