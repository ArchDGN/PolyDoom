import math

import pygame

from math import *

from data import *

class Draw:
    def __init__(self, fenetre, width, height, map, map_size):
        self.fenetre = fenetre

        self.map = map
        self.map_size = map_size
        self.map_big_size = self.map_size * self.map_size

        self.screen_width = width
        self.screen_height = height

    def draw_rectangle(self, x, y, widht, height, color):
        pygame.draw.rect(self.fenetre, color, (x, y, widht, height))

    def draw_circle(self, x, y, radius, color):
        pygame.draw.circle(self.fenetre, color, (x, y), radius)

    def draw_line(self, x1, y1, x2, y2, color):
        pygame.draw.line(self.fenetre, color, (x1, y1), (x2, y2))


    def draw_map(self, player):
        mapX = self.map_size
        mapY = self.map_size
        mapS = 64

        # Dessin de la map
        for x in range(mapX):
            for y in range(mapY):
                if self.map[y * mapX + x] > 0:
                    self.draw_rectangle(x * mapS + 1, y * mapS + 1, mapS - 1, mapS - 1, ColorData.white)
                else:
                    self.draw_rectangle(x * mapS + 1, y * mapS + 1, mapS - 1, mapS - 1, ColorData.black)

        # Dessin du pointer du joueur sur la map
        player.px_angle = cos(player.angle * math.pi / 180) * 40
        player.py_angle = sin(player.angle * math.pi / 180) * 40
        self.draw_rectangle(player.pos_x, player.pos_y, 8, 8, ColorData.yellow)
        self.draw_line(player.pos_x + 4, player.pos_y + 4, player.pos_x + 4 + player.px_angle, player.pos_y + 4 + player.py_angle, ColorData.yellow)

    def dist(self, ax, ay, bx, by, ang):
        # Calcul de la distance entre deux points
        return (sqrt((bx - ax) * (bx - ax) + (by - ay) * (by - ay)))
    def raycasting(self, player):
        # Mise a jour de la taille de la fenetre
        self.screen_width = self.fenetre.get_width()
        self.screen_height = self.fenetre.get_height()

        # Initialisation des variables
        r, mx, my, mp, dof, rx, ry, ra, xo, yo = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ra = player.get_angle() - 30

        # Empeche que l'angle soit negatif ou superieur a 360
        ra += 360 if ra < 0 else 0
        ra -= 360 if ra > 360 else 0

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

        # Boucle de raycasting pour chaque colonne de la fenetre
        for r in range(0, 120, 1):

            """"""
            """"""
            """CASTING DES LIGNES HORIZONTALES"""
            dof = 0
            disH = 1000000
            hx = player.pos_x
            hy = player.pos_y

            if ra == 0:
                ra = 0.0000001

            aTan = -1 / tan(ra * math.pi / 180)

            if ra > 180:
                ry = (((int(player.pos_y) >> 6) << 6) - 0.0001)
                rx = (player.pos_y - ry) * aTan + player.pos_x
                yo = -64
                xo = -yo * aTan

            if ra < 180:
                ry = (((int(player.pos_y) >> 6) << 6) + 64)
                rx = (player.pos_y - ry) * aTan + player.pos_x
                yo = 64
                xo = -yo * aTan

            if ra == 0 or ra == 180:
                rx = player.pos_x
                ry = player.pos_y
                dof = self.map_size

            while dof < self.map_size:
                mx = int(rx) >> 6
                my = int(ry) >> 6
                mp = my * self.map_size + mx

                if mp > 0 and mp < self.map_big_size and self.map[mp] > 0:
                    hx = rx
                    hy = ry

                    disH = self.dist(player.pos_x, player.pos_y, hx, hy, ra)
                    dof = self.map_size
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
            vx = player.pos_x
            vy = player.pos_y
            nTan = -tan(ra * math.pi / 180)
            if ra > 90 and ra < 270:
                rx = (((int(player.pos_x) >> 6) << 6) - 0.0001)
                ry = (player.pos_x - rx) * nTan + player.pos_y
                xo = -64
                yo = -xo * nTan

            if ra < 90 or ra > 270:
                rx = (((int(player.pos_x) >> 6) << 6) + 64)
                ry = (player.pos_x - rx) * nTan + player.pos_y
                xo = 64
                yo = -xo * nTan

            if ra == 0 or ra == 180:
                rx = player.pos_x
                ry = player.pos_y
                dof = self.map_size

            while dof < self.map_size:
                mx = int(rx) >> 6
                my = int(ry) >> 6
                mp = my * self.map_size + mx
                if mp > 0 and mp < self.map_big_size and self.map[mp] > 0:
                    vx = rx
                    vy = ry

                    disV = self.dist(player.pos_x, player.pos_y, vx, vy, ra)
                    dof = self.map_size
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
                tempa = int(rx/64) + int(ry/64) * self.map_size
                tampb = self.map[tempa]
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
                tempa = int(rx / 64) + int(ry / 64) * self.map_size
                tampb = self.map[tempa]
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

            ca = player.get_angle() - ra
            ca += 360 if ca < 0 else 0
            ca -= 360 if ca > 360 else 0

            disT = disT * cos(ca * math.pi / 180)
            # Calcul de la hauteur de la colonne
            if disT == 0:
                disT = 0.0000001
            lineH = int(64 * self.screen_height / disT)
            if lineH > self.screen_height:
                lineH = self.screen_height

            # Dessin des colonnes dans le cas d'erreur et que l'ereeure est sur la premiere colonne affichée
            if temp_first == True and r == 1:
                # Dessin du mur
                self.draw_rectangle((r - 1) * (self.screen_width / 120), self.screen_height / 2 - lineH // 2, (self.screen_width / 120) + 1, lineH, temp_color)
                # Dessin du plafond
                self.draw_rectangle((r - 1) * (self.screen_width / 120), 0, (self.screen_width / 120) + 1, self.screen_height / 2 - lineH // 2, ColorData.black)
                # Dessin du sol
                self.draw_rectangle((r - 1) * (self.screen_width / 120), self.screen_height / 2 + lineH // 2, (self.screen_width / 120) + 1, self.screen_height / 2 - lineH // 2, ColorData.gray1)
                temp_first = False

            # Dessin des colonnes dans le cas normal
            if temp_first == False:
                self.draw_rectangle(r * (self.screen_width / 120), self.screen_height / 2 - lineH // 2, (self.screen_width / 120) + 1, lineH, color)
                # Dessin du plafond
                self.draw_rectangle(r * (self.screen_width / 120), 0, (self.screen_width / 120) + 1, self.screen_height / 2 - lineH // 2, ColorData.black)
                # Dessin du sol
                self.draw_rectangle(r * (self.screen_width / 120), self.screen_height / 2 + lineH // 2, (self.screen_width / 120) + 1, self.screen_height / 2 - lineH // 2, ColorData.gray1)

            # Incrementation de l'angle, par 0.5 degre pour avoir 120 rayons sur un angle de 60 degre
            ra += 0.5
            ra += 360 if ra < 0 else 0
            ra -= 360 if ra > 360 else 0
