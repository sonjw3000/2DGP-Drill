from pico2d import *
from random import randint

def spawnHand():
	global hand_x, hand_y
	global char_x, char_y
	global a, b, goRight, movebyX
	global offset

	char_x, char_y = hand_x, hand_y

	hand_x = randint(0,800)
	hand_y = randint(0,600)

	a = (hand_y - char_y) / (hand_x - char_x)
	b = char_y - char_x * a
	if abs(a) < 1: movebyX = True
	else: movebyX = False

	goRight = (hand_x - char_x) > 0
	offset = 0


def moveChar(x, y, offset):
	global a, b
	ax = x + offset
	ay = a * ax + b

	return ax, ay


def handle_events():
	global loop

	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			loop = False
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			loop = False 


open_canvas()
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

char_x = 400
char_y = 300

hand_x = randint(0,800)
hand_y = randint(0,600)

frame = 0
goRight = True
a = 0
b = 0
movebyX = True
offset = 0

spawnHand()

char_x = 400
char_y = 300

loop = True

while(loop):
	handle_events()

	clear_canvas()
	hand.draw(hand_x, hand_y)
	ax, ay = moveChar(char_x, char_y, offset)
	character.clip_draw(frame * 100, 100 * goRight, 100, 100, ax, ay, 50, 90)
	update_canvas()

	if goRight:	offset += 1
	else: offset -= 1


	frame = (frame + 1) % 8

	if offset + char_x == hand_x:
		spawnHand()

	delay(0.01)
	pass
