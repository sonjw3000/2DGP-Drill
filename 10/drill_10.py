from pico2d import *
import random


# Game object class here

class Ball:
    def __init__(self):
        self.x = random.randint(0, 600)
        self.y = 599
        self.falling_speed = random.randint(1, 10)

        self.bBig = True
        if random.randint(0, 1):
            self.image = load_image('ball21x21.png')
            self.bBig = False
        else:
            self.image = load_image('ball41x41.png')

    def update(self):
        self.y -= self.falling_speed
        if self.y - (21 + self.bBig * 20) <= 90:
            self.falling_speed = 0

    def draw(self):
        self.image.clip_draw(0, 0, 21 + self.bBig * 20, 21 + self.bBig * 20, self.x, self.y)


class Boy:
    def __init__(self):
        self.x = random.randint(0, 100)
        self.y = 90
        self.image = load_image('animation_sheet.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def update():
    for ball in balls:
        ball.update()
    for boy in boys:
        boy.update()


def draw():
    for ball in balls:
        ball.draw()
    for boy in boys:
        boy.draw()


# initialization code
running = True
boys = [Boy() for i in range(20)]
balls = [Ball() for i in range(20)]


# game main loop code

while running:
    handle_events()
    update()
    draw()

# finalization code
