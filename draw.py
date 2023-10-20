import math

import pygame

from math import *

from data import *

class Draw:
    def __init__(self, fenetre):
        self.__fenetre = fenetre

    def draw_rectangle(self, fenetre, x, y, widht, height, color):
        pygame.draw.rect(fenetre, color, (x, y, widht, height))

    def draw_circle(self, fenetre, x, y, radius, color):
        pygame.draw.circle(fenetre, color, (x, y), radius)

    def draw_line(self, fenetre, x1, y1, x2, y2, color):
        pygame.draw.line(fenetre, color, (x1, y1), (x2, y2))
