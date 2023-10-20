import math
from math import *

from data import *

class Map:
    def __init__(self):
        self.__path = ""
        self.__map = []
        self.__map_data = []

        self.__map_size = 64

        self.__data = []

    def load_map(self, path):

        # Chargement de la map depuis un fichier texte
        self.__path = path

        with open(self.__path, "r") as file:
            self.__data = []
            for line in file:
                if line[0] == '#':
                    self.__data = line.strip().split(',')
                    self.__data[0] = self.__data[0][1:]
                    self.__data = [int(num) for num in self.__data]
                else:
                    square_row = line.strip().split(',')
                    square_row = [int(num) for num in square_row]
                    self.__map.extend(square_row)

        self.__map_data = self.__data

    def map_window_debug(self, player, draw, window, fenetre, map_data):
        # Dessin de la map
        y = 0

        for x in range(0, map_data[0]**2 - 1, 1):
            y += 1 if x % map_data[0] == 0 and x != 0 else 0

            if self.__map[x] > 0:
                draw.draw_rectangle(fenetre, x % map_data[0] * self.__map_size + 1, y * self.__map_size + 1, self.__map_size - 1, self.__map_size - 1, ColorData.white)
            else:
                draw.draw_rectangle(fenetre, x % map_data[0] * self.__map_size + 1, y * self.__map_size + 1, self.__map_size - 1, self.__map_size - 1, ColorData.black)

        angle = player.return_angle()

        # Dessin du pointer du joueur sur la map
        px_angle = cos(angle * math.pi / 180) * 40
        py_angle = sin(angle * math.pi / 180) * 40
        draw.draw_rectangle(fenetre, player.pos_x, player.pos_y, 8, 8, ColorData.yellow)
        draw.draw_line(fenetre, player.pos_x + 4, player.pos_y + 4, player.pos_x + 4 + px_angle, player.pos_y + 4 + py_angle, ColorData.yellow)

    def return_data(self):
        return self.__map_data

    def return_map(self):
        return self.__map