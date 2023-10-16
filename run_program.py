import pygame

from window import Window
from draw import Draw
from player import Player
from event import Event
from map_loadding import Map
from data import *

class Prog:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

        self.path = "Map/carre_16.txt"
        self.map = []
        self.map_size = 0

        self.quit = False

    def run(self):
        # Initialisation de la fenêtre
        prog_window = Window(self.width, self.height, self.title)

        # Initialisation de la Map
        map = Map()
        self.map = map.load_map(self.path)
        self.map_size = map.get_map_info(self.path)[0]

        # Initialisation du joueur
        player1 = Player(prog_window.fenetre, "DoomBOYS")
        # Placement du joueur sur la map, si la case est egale a -1
        for i in range(0, len(self.map)):
            if self.map[i] == -1:
                player1.update_coord((i % self.map_size) * 64 + 32, (i // self.map_size) * 64 + 32)
                break
        player1.update_angle(map.get_map_info(self.path)[1])

        # Initialisation de la classe Draw
        draw_on_screen = Draw(prog_window.fenetre, self.width, self.height, self.map, self.map_size)

        # Initialisation de la classe Event
        prog_event = Event()

        # Boucle principale
        while self.quit == False:

            # Mise à jour de la fenêtre
            prog_window.fill(ColorData.gray1)

            # Dessin de la map
            #draw_on_screen.draw_map(player1)

            # Raycasting
            draw_on_screen.raycasting(player1)

            #player1.draw_on_map(draw_on_screen)

            prog_window.update()

            # Gestion des évènements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    prog_window.quit()
                    self.quit = True
                else:
                    prog_event.event_control(event, prog_window, player1)