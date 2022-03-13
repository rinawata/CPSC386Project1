import random

import pygame as pg
from timer import Timer


class UFO:
    ufo_images = [pg.transform.rotozoom(pg.image.load(f'images/ufo__0.png'), 0, 0.25),
                  pg.transform.rotozoom(pg.image.load(f'images/ufo__1.png'), 0, 0.25)]

    ufo_movement_height = 100

    def __init__(self, game):
        self.animation = Timer(image_list=UFO.ufo_images, delay=1000, is_loop=True)
        self.position = {"x": 100, "y": 100}
        self.game = game
        self.onScreen = False
        self.orbitTime = 100

    def update(self):
        if not self.onScreen and self.orbitTime == 0:
            print("DEBUG: UFO START FLYBY")
            self.position = {"x": -20, "y": UFO.ufo_movement_height}
            self.onScreen = True
        if not self.onScreen and self.orbitTime > 0:
            print("DEBUG: ORBIT REMAINING: " + str(self.orbitTime))
            self.orbitTime -= 1
        if self.onScreen:
            self.position["x"] += 0.1
        if self.position["x"] > 700:
            self.orbitTime = random.randint(100, 1000)
            self.onScreen = False
        pass

    def draw(self):
        frame = self.animation.image()
        rect = frame.get_rect()
        rect.x, rect.y = self.position["x"], self.position["y"]
        self.game.screen.blit(frame, rect)
