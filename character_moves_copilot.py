import pico2d

pico2d.open_canvas(800, 800)
grass = pico2d.load_image('grass.png')
character = pico2d.load_image('character.png')

running = True  # running 변수 선언

def draw_scene():
    grass.draw(400, 40)  # 바닥 중앙에 배치 (grass 높이 80 기준)
    character.draw(400, 90)  # 화면 중앙 하단에 배치 (character 높이 90 기준)

while running:  # running 변수를 사용
    pico2d.clear_canvas()
    draw_scene()
    pico2d.update_canvas()
    pico2d.delay(0.5)
    for event in pico2d.get_events():
        if event.type == pico2d.SDL_QUIT:
            running = False  # running을 False로 변경

pico2d.close_canvas()