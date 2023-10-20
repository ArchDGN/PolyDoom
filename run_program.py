import pygame

from window import Window
from draw import Draw
from player import Player
from event import Event
from map_loadding import Map
from raycasting import RayCastingEngine
from data import *

class Prog:
    def __init__(self, width, height, title):
        self.__width = width
        self.__height = height
        self.__title = title

        self.__quit = False

    def run(self):
        # Initialisation de la fenêtre
        prog_window = Window(self.__width, self.__height, self.__title)

        # Initialisation de la Map
        map = Map()
        map.load_map("Map/carre_16.txt")

        # Initialisation du joueur
        player1 = Player(prog_window.return_fenetre(), "DoomBOYS")
        player1.set_player_start(map.return_map(), map.return_data())

        # Initialisation de la classe Draw
        draw_on_screen = Draw(prog_window.return_fenetre())

        # Initialisation de la classe RaycastingEngine
        raycasting_engine = RayCastingEngine( self.__width, self.__height)

        # Initialisation de la classe Event
        prog_event = Event()

        # Boucle principale
        while self.__quit == False:

            # Remplissage de la fenêtre
            prog_window.fill(ColorData.gray1)

            # Dessin de la map
            #map.map_window_debug(player1, draw_on_screen, prog_window, prog_window.return_fenetre(), map.return_data())

            # Raycasting
            raycasting_engine.raycasting(player1,    draw_on_screen, prog_window.return_fenetre(), map.return_map(), map.return_data()[0])
            #draw_on_screen.raycasting(player1)

            # Mise à jour de la fenêtre
            prog_window.update()

            # Gestion des évènements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    prog_window.quit()
                    self.__quit = True
                else:
                    prog_event.event_control(event, prog_window, player1)