import math

import pygame

from math import *

class Event:
    def __init__(self):
        self.__pressed = {}

    def update(self, window, player):
        angle = player.return_angle()
        pdx = cos(angle * math.pi / 180) * 8
        pdy = sin(angle * math.pi / 180) * 8

        if self.__pressed.get(pygame.K_z):
            player.update_coord(player.return_coord()[0] + pdx, player.return_coord()[1] + pdy)

        if self.__pressed.get(pygame.K_s):
            player.update_coord(player.return_coord()[0] - pdx, player.return_coord()[1] - pdy)

        if self.__pressed.get(pygame.K_q):
            angle -= 2
            angle += 360 if angle <= 0 else 0
            player.update_angle(angle)


        if self.__pressed.get(pygame.K_d):
            angle += 2
            angle -= 360 if angle > 360 else 0
            player.update_angle(angle)

    def event_control(self, event, window, player):

        if event.type == pygame.KEYDOWN:
            self.__pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            self.__pressed[event.key] = False

        self.update(window, player)