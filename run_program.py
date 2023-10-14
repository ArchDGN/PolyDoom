import pygame

from window import Window
from draw import Draw
from player import Player
from event import Event
from data import *

class Prog:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

        self.quit = False

    def run(self):
        # Initialisation de la fenêtre
        prog_window = Window(self.width, self.height, self.title)

        # Initialisation de la classe Draw
        draw_on_screen = Draw(prog_window.fenetre)

        # Initialisation du joueur
        player1 = Player(prog_window.fenetre, "DoomBOYS")

        prog_event = Event()

        # Boucle principale
        #clock = pygame.time.Clock()
        while self.quit == False:

            # Mise à jour de la fenêtre
            prog_window.fill(ColorData.gray1)

            # Dessin de la map
            draw_on_screen.draw_map()

            # Raycasting
            draw_on_screen.raycasting(player1)

            player1.draw_on_map(draw_on_screen)

            prog_window.update()

            # Gestion des évènements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    prog_window.quit()
                    self.quit = True
                else:
                    prog_event.event_control(event, prog_window, player1)

            #clock.tick(60)
            #print(clock.get_fps())