import random
from pico2d import *
import game_world
import game_framework

# Bird Run Speed
# 새의 평균 이동 속도 100km/h
# 새 크기 90cm * 90cm
# 새 픽셀크기 30 30 (1픽셀당 3cm)
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
FLY_SPEED_KMPH = 100.0  # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
# 초당 50번 (0.02에 한번)
TIME_PER_ACTION = 0.02
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Bird:
	image = None

	def __init__(self):
		if Bird.image == None:
			Bird.image = load_image('bird100x100x14.png')
		self.x, self.y = random.randint(0 + 15, 1600 - 1 - 15), random.randint(150 + 15, 500 - 15)
		self.dir = random.randint(0, 1)
		self.dir = self.dir * 2 - 1
		self.frame = 0

	def get_bb(self):
		# fill here
		return 0, 0, 0, 0

	def draw(self):
		self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y, 30, 30)

	def update(self):
		self.x -= self.dir * FLY_SPEED_PPS * game_framework.frame_time

		self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

		if self.x >= 1600 - 1 - 15:
			self.dir *= -1
			self.x -= self.dir * FLY_SPEED_PPS * game_framework.frame_time
		elif self.x <= 0:
			self.dir *= -1
			self.x -= self.dir * FLY_SPEED_PPS * game_framework.frame_time

# fill here for def stop

# fill here
# class BigBall
