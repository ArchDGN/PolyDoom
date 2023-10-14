import math

import pygame

from draw import Draw
from data import *
from math import *

class Player:
    def __init__(self, fenetre, name):
        self.fenetre = fenetre

        self.name = name

        self.pos_x = 300
        self.pos_y = 300

        self.angle = 180
        self.px_angle = 0
        self.py_angle = 0

        self.on_map_widht = 8
        self.on_map_color = ColorData.yellow

    def draw_on_map(self, draw):
        draw.draw_rectangle(self.pos_x, self.pos_y, self.on_map_widht, self.on_map_widht, self.on_map_color)

        self.px_angle = cos(self.angle * math.pi / 180) * 40
        self.py_angle = sin(self.angle * math.pi / 180) * 40
        draw.draw_line(self.pos_x + 4, self.pos_y + 4, self.pos_x + 4 + self.px_angle, self.pos_y + 4 + self.py_angle, ColorData.yellow)

    def update_coord(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def get_angle(self):
        return self.angle

    def update_angle(self, angle):
        self.angle = angle
