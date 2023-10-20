import math

import pygame

from data import *
from math import *

class Player:
    def __init__(self, fenetre, name):
        self.__fenetre = fenetre

        # Nom du joueur
        self.__name = name

        # Position de depart du joueur
        self.__pos_x = 0
        self.__pos_y = 0

        # Angle de depart du joueur
        self.angle = 0

    def set_player_start(self, loaded_map, map_data):

        # Placement du joueur sur la map, si la case est egale a -1.
        for i in range(0, len(loaded_map)):
            if loaded_map[i] == -1:
                self.update_coord((i % map_data[0]) * 64 + 32, (i // map_data[0]) * 64 + 32)
                break
        self.update_angle(map_data[1])


    def update_coord(self, x, y):
        # Mise à jour des coordonnées du joueur par rapport au coordonnées données a la fonction
        self.__pos_x = x
        self.__pos_y = y

    def return_coord(self):
        # Retourne les coordonnées du joueur
        return [self.__pos_x, self.__pos_y]

    def update_angle(self, angle):
        # Mise à jour de l'angle du joueur par rapport a l'angle donné a la fonction
        self.angle = angle

    def return_angle(self):
        # Retourne l'angle du joueur
        return self.angle
