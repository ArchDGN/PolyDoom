import math

import pygame

from math import *

from data import *
from draw import Draw

class RayCastingEngine:
    def __init__(self, width, height):
        self.__screen_width = width
        self.__screen_height = height

    def dist(self, ax, ay, bx, by, ang):
        # Calcul de la distance entre deux points
        return (sqrt((bx - ax) * (bx - ax) + (by - ay) * (by - ay)))

    def raycasting(self, player, draw_on_screen, fenetre, map, map_size):
        # Mise a jour de la taille de la fenetre
        self.__screen_width = fenetre.get_width()
        self.__screen_height = fenetre.get_height()

        map_big_size = map_size * map_size

        # Initialisation des variables
        r, mx, my, mp, dof, rx, ry, ra, xo, yo = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ra = player.return_angle() - 30

        """Variable de gestion d'erreur pour les cas 90, 180 et 270 degre"""
        temp_color = ColorData.red
        temp_first = False
        temp_disT = 0
        """
            Les valeurs de gestion d'errur:
                temp_color = couleur de la colonne precedente
                temp_first = permet de savoir si on est sur la premiere colonne de la fenetre
                temp_disT = permet de savoir la distance de la colonne precedente

        """

        # Empeche que l'angle soit negatif ou superieur a 360
        ra += 360 if ra < 0 else 0
        ra -= 360 if ra > 360 else 0

        # Boucle de raycasting pour chaque colonne de la fenetre
        ray_number = self.__screen_width
        for r in range(0, ray_number, 1):

            """"""
            """"""
            """CASTING DES LIGNES HORIZONTALES"""
            dof = 0
            disH = 1000000
            hx = player.return_coord()[0]
            hy = player.return_coord()[1]

            if ra == 0:
                ra = 0.0000001

            aTan = -1 / tan(ra * math.pi / 180)

            if ra > 180:
                ry = (((int(player.return_coord()[1]) >> 6) << 6) - 0.0001)
                rx = (player.return_coord()[1] - ry) * aTan + player.return_coord()[0]
                yo = -64
                xo = -yo * aTan

            if ra < 180:
                ry = (((int(player.return_coord()[1]) >> 6) << 6) + 64)
                rx = (player.return_coord()[1] - ry) * aTan + player.return_coord()[0]
                yo = 64
                xo = -yo * aTan

            if ra == 0 or ra == 180:
                rx = player.return_coord()[0]
                ry = player.return_coord()[1]
                dof = map_size

            while dof < map_size:
                mx = int(rx) >> 6
                my = int(ry) >> 6
                mp = my * map_size + mx

                if mp > 0 and mp < map_big_size and map[mp] > 0:
                    hx = rx
                    hy = ry

                    disH = self.dist(player.return_coord()[0], player.return_coord()[1], hx, hy, ra)
                    dof = map_size
                else:
                    rx += xo
                    ry += yo
                    dof += 1
            """"""
            """"""


            """"""
            """"""
            """CASTING DES LIGNES VERTICALES"""
            dof = 0
            disV = 1000000
            vx = player.return_coord()[0]
            vy = player.return_coord()[1]
            nTan = -tan(ra * math.pi / 180)
            if ra > 90 and ra < 270:
                rx = (((int(player.return_coord()[0]) >> 6) << 6) - 0.0001)
                ry = (player.return_coord()[0] - rx) * nTan + player.return_coord()[1]
                xo = -64
                yo = -xo * nTan

            if ra < 90 or ra > 270:
                rx = (((int(player.return_coord()[0]) >> 6) << 6) + 64)
                ry = (player.return_coord()[0] - rx) * nTan + player.return_coord()[1]
                xo = 64
                yo = -xo * nTan

            if ra == 0 or ra == 180:
                rx = player.return_coord()[0]
                ry = player.return_coord()[1]
                dof = map_size

            while dof < map_size:
                mx = int(rx) >> 6
                my = int(ry) >> 6
                mp = my * map_size + mx
                if mp > 0 and mp < map_big_size and map[mp] > 0:
                    vx = rx
                    vy = ry

                    disV = self.dist(player.return_coord()[0], player.return_coord()[1], vx, vy, ra)
                    dof = map_size
                else:
                    rx += xo
                    ry += yo
                    dof += 1
            """"""
            """"""

            """"""
            """"""
            """SELECTION DE LA PLUS PETITE DISTANCE ET DE LA COULEUR"""
            color = ColorData.green
            if disV < disH:

                rx = vx
                ry = vy

                # tempa et tempb permete de savoir sur quelle case de la map le rayon touche un mur et donc de savoir quelle couleur afficher
                tempa = int(rx/64) + int(ry/64) * map_size
                tampb = map[tempa]
                #


                """
                    Gestions des couleurs avec if ( temporaire, a changer quand on aura les textures )
                """
                if tampb == 1:
                    color = ColorData.red2
                    temp_color = color
                elif tampb == 2:
                    color = ColorData.blue
                    temp_color = color
                elif tampb == 3:
                    color = ColorData.green
                    temp_color = color
                """
                    Gestions des couleurs avec if ( temporaire, a changer quand on aura les textures )
                """

                disT = disV
                temp_disT = disV


            elif disH < disV:
                rx = hx
                ry = hy

                # tempa et tempb permete de savoir sur quelle case de la map le rayon touche un mur et donc de savoir quelle couleur afficher
                tempa = int(rx / 64) + int(ry / 64) * map_size
                tampb = map[tempa]
                #

                """
                    Gestions des couleurs avec if ( temporaire, a changer quand on aura les textures )
                """
                if tampb == 1:
                    color = ColorData.red3
                    temp_color = color
                elif tampb == 2:
                    color = ColorData.blue2
                    temp_color = color
                elif tampb == 3:
                    color = ColorData.green2
                    temp_color = color
                """
                    Gestions des couleurs avec if ( temporaire, a changer quand on aura les textures )
                """

                disT = disH
                temp_disT = disH
            else:
                color = temp_color
                disT = temp_disT

                # Indique que la colonne est la premiere colonne affichée
                if r == 0:
                    temp_first = True

            """"""
            """"""

            """
            if color == ColorData.red2 or color == ColorData.red3:
                self.draw_rectangle(rx - 2, ry - 2, 4, 4, ColorData.red)
                self.draw_line(player.pos_x + 4, player.pos_y + 4, rx, ry, ColorData.red)
            else:
                self.draw_rectangle(rx - 2, ry - 2, 4, 4, ColorData.green)
                self.draw_line(player.pos_x + 4, player.pos_y + 4, rx, ry, ColorData.green)
            """



            """3D PROJECTION"""

            ca = player.return_angle() - ra
            ca += 360 if ca < 0 else 0
            ca -= 360 if ca > 360 else 0

            disT = disT * cos(ca * math.pi / 180)
            # Calcul de la hauteur de la colonne
            if disT == 0:
                disT = 0.0000001
            lineH = int(64 * self.__screen_height / disT)
            if lineH > self.__screen_height:
                lineH = self.__screen_height

            # Dessin des colonnes dans le cas d'erreur et que l'ereeure est sur la premiere colonne affichée
            if temp_first == True and r == 1:
                # Dessin du mur
                draw_on_screen.draw_rectangle(fenetre, (r - 1) * (self.__screen_width / ray_number), self.__screen_height / 2 - lineH // 2, (self.__screen_width / ray_number) + 1, lineH, temp_color)
                # Dessin du plafond
                draw_on_screen.draw_rectangle(fenetre, (r - 1) * (self.__screen_width / ray_number), 0, (self.__screen_width / ray_number) + 1, self.__screen_height / 2 - lineH // 2, ColorData.black)
                # Dessin du sol
                draw_on_screen.draw_rectangle(fenetre, (r - 1) * (self.__screen_width / ray_number), self.__screen_height / 2 + lineH // 2, (self.__screen_width / ray_number) + 1, self.__screen_height / 2 - lineH // 2, ColorData.gray1)
                temp_first = False

            # Dessin des colonnes dans le cas normal
            if temp_first == False:
                draw_on_screen.draw_rectangle(fenetre, r * (self.__screen_width / ray_number), self.__screen_height / 2 - lineH // 2, (self.__screen_width / ray_number) + 1, lineH, color)
                # Dessin du plafond
                draw_on_screen.draw_rectangle(fenetre, r * (self.__screen_width / ray_number), 0, (self.__screen_width / ray_number) + 1, self.__screen_height / 2 - lineH // 2, ColorData.black)
                # Dessin du sol
                draw_on_screen.draw_rectangle(fenetre, r * (self.__screen_width / ray_number), self.__screen_height / 2 + lineH // 2, (self.__screen_width / ray_number) + 1, self.__screen_height / 2 - lineH // 2, ColorData.gray1)

            # Incrementation de l'angle, par 0.5 degre pour avoir 120 rayons sur un angle de 60 degre
            ra += 60 / ray_number
            ra += 360 if ra < 0 else 0
            ra -= 360 if ra > 360 else 0
