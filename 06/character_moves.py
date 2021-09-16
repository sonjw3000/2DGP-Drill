from pico2d import *

open_canvas()
hide_lattice()
grass = load_image('grass.png')
character = load_image('character.png')

# fill here
x = 0
while (x < 800):
    clear_canvas_now()              # Game Rendering
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x = x + 2                       # Game Logic
    delay(0.01)

close_canvas()
