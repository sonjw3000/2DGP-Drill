from pico2d import *
import math



open_canvas()
hide_lattice()
grass = load_image('grass.png')
character = load_image('character.png')


def draw():
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y + 90)


# fill here
x = 0
y = 0

while True:
    # right
    while (x < 800):
        draw()
        x = x + 2
        delay(0.001)

    # up
    while (y < 600 - 90):
        draw()
        y = y + 2
        delay(0.001)

    # left
    while (x > 0):
        draw()
        x = x - 2
        delay(0.001)

    # down
    while (y > 0):
        draw()
        y = y - 2
        delay(0.001)

    # right(go center)
    while (x < 400):
        draw()
        x = x + 2
        delay(0.001)

    # circle
    x = -90
    while (x < 270):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(400 - math.cos(x * 3.14 / 180) * 400, 300 + math.sin(x * 3.14 / 180) * 300 + 90)
        x = x + 1
        delay(0.01)
    x = 400

close_canvas()

