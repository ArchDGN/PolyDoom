import math

import pygame

from data import *
from math import *

class Player:
    def __init__(self, fenetre, name):
        self.fenetre = fenetre

        # Nom du joueur
        self.name = name

        # Position de depart du joueur
        self.pos_x = 300
        self.pos_y = 300

        # Angle de depart du joueur
        self.angle = 180
        self.px_angle = 0
        self.py_angle = 0

        self.on_map_widht = 8
        self.on_map_color = ColorData.yellow

    def update_coord(self, x, y):
        # Mise à jour des coordonnées du joueur par rapport au coordonnées données a la fonction
        self.pos_x = x
        self.pos_y = y

    def get_angle(self):
        # Retourne l'angle du joueur
        return self.angle

    def update_angle(self, angle):
        # Mise à jour de l'angle du joueur par rapport a l'angle donné a la fonction
        self.angle = angle
