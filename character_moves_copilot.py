import pico2d

pico2d.open_canvas(800, 800)
grass = pico2d.load_image('grass.png')
character = pico2d.load_image('character.png')

def draw_scene():
    grass.draw(400, 40)  # 바닥 중앙에 배치 (grass 높이 80 기준)
    character.draw(400, 90)  # 화면 중앙 하단에 배치 (character 높이 90 기준)

while pico2d.running:
    pico2d.clear_canvas()
    draw_scene()
    pico2d.update_canvas()
    pico2d.delay(0.5)  # 딜레이를 0.5초로 늘려서 화면이 보이도록 함
    for event in pico2d.get_events():
        if event.type == pico2d.SDL_QUIT:
            pico2d.running = False

pico2d.close_canvas()