import math

import pygame

from math import *

class Event:
    def __init__(self):
        self.pressed = {}
        self.pdx = 0
        self.pdy = 0

    def update(self, window, player):
        angle = player.get_angle()
        self.pdx = cos(angle * math.pi / 180) * 8
        self.pdy = sin(angle * math.pi / 180) * 8

        if self.pressed.get(pygame.K_z):
            player.update_coord(player.pos_x + self.pdx, player.pos_y + self.pdy)

        if self.pressed.get(pygame.K_s):
            player.update_coord(player.pos_x - self.pdx, player.pos_y - self.pdy)

        if self.pressed.get(pygame.K_q):
            angle -= 4
            if angle <= 0:
                angle += 360
            player.update_angle(angle)


        if self.pressed.get(pygame.K_d):
            angle += 4
            if angle > 360:
                angle -= 360
            player.update_angle(angle)

    def event_control(self, event, window, player):

        if event.type == pygame.KEYDOWN:
            self.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            self.pressed[event.key] = False

        self.update(window, player)