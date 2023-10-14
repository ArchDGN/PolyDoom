import math

import pygame

from math import *

from data import *

class Draw:
    def __init__(self, fenetre):
        self.fenetre = fenetre

        self.map = \
            [
                1, 1, 1, 1, 1, 1, 1, 1,
                1, 0, 0, 0, 1, 0, 0, 1,
                1, 0, 1, 0, 1, 1, 0, 1,
                1, 0, 0, 0, 0, 1, 0, 1,
                1, 0, 0, 0, 0, 0, 0, 1,
                1, 0, 0, 0, 0, 1, 0, 1,
                1, 0, 0, 0, 0, 1, 0, 1,
                1, 1, 1, 1, 1, 1, 1, 1
            ]

    def draw_rectangle(self, x, y, widht, height, color):
        pygame.draw.rect(self.fenetre, color, (x, y, widht, height))

    def draw_circle(self, x, y, radius, color):
        pygame.draw.circle(self.fenetre, color, (x, y), radius)

    def draw_line(self, x1, y1, x2, y2, color):
        pygame.draw.line(self.fenetre, color, (x1, y1), (x2, y2))


    def draw_map(self):
        mapX = 8
        mapY = 8
        mapS = 64

        # Dessin de la map
        for x in range(mapX):
            for y in range(mapY):
                if self.map[y * mapX + x] == 1:
                    self.draw_rectangle(x * mapS + 1, y * mapS + 1, mapS - 1, mapS - 1, ColorData.white)
                else:
                    self.draw_rectangle(x * mapS + 1, y * mapS + 1, mapS - 1, mapS - 1, ColorData.black)

    def dist(self, ax, ay, bx, by, ang):
        return (sqrt((bx - ax) * (bx - ax) + (by - ay) * (by - ay)))
    def raycasting(self, player):
        r, mx, my, mp, dof, rx, ry, ra, xo, yo = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        disT = 0
        ra = player.get_angle() - 30
        if ra < 0:
            ra += 360
        if ra > 360:
            ra -= 360

        """Variable de gestion d'erreur pour les cas 90, 180 et 270 degre"""
        temp_color = ColorData.red
        temp_first2 = False
        temp_disT = 0
        """"""

        for r in range(0, 60, 1):
            temp_first = False

            """HORIZONTAL LINES CASTING"""
            dof = 0
            disH = 1000000
            hx = player.pos_x
            hy = player.pos_y
            if ra != 0:
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
                #print(r, "Cool", ra, ra+60)
                rx = player.pos_x
                ry = player.pos_y
                dof = 8

            while dof < 8:
                mx = int(rx) >> 6
                my = int(ry) >> 6
                mp = my * 8 + mx
                if mp > 0 and mp < 64 and self.map[mp] == 1:
                    hx = rx
                    hy = ry
                    disH = self.dist(player.pos_x, player.pos_y, hx, hy, ra)
                    dof = 8
                else:
                    rx += xo
                    ry += yo
                    dof += 1

            #self.draw_line(player.pos_x + 4, player.pos_y + 4, hx, hy, ColorData.green)


            """VERTICAL LINES CASTING"""
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
                #print(r, "Coucou", ra, ra+60)
                rx = player.pos_x
                ry = player.pos_y
                dof = 8

            while dof < 8:
                mx = int(rx) >> 6
                my = int(ry) >> 6
                mp = my * 8 + mx
                if mp > 0 and mp < 64 and self.map[mp] == 1:
                    vx = rx
                    vy = ry
                    disV = self.dist(player.pos_x, player.pos_y, vx, vy, ra)
                    dof = 8
                else:
                    rx += xo
                    ry += yo
                    dof += 1

            color = ColorData.green
            if disV < disH:
                color = ColorData.red2
                temp_color = ColorData.red2
                rx = vx
                ry = vy
                disT = disV
                temp_disT = disV

            elif disH < disV:
                color = ColorData.red3
                temp_color = ColorData.red3
                rx = hx
                ry = hy
                disT = disH
                temp_disT = disH
            else:
                color = temp_color
                disT = temp_disT
                if r == 0:
                    temp_first = True

            self.draw_line(player.pos_x + 4, player.pos_y + 4, rx, ry, ColorData.red)

            """3D PROJECTION"""
            ca = player.get_angle() - ra
            ca += 360 if ca < 0 else 0
            ca -= 360 if ca > 360 else 0

            disT = disT * cos(ca * math.pi / 180)

            if disT == 0:
                disT = 0.0000001
            lineH = int(64 * 320 / disT)
            if lineH > 320:
                lineH = 320

            if temp_first2 == True:
                self.draw_rectangle((r-1) * 8 + 530, 256 - lineH // 2, 8, lineH, temp_color)
                temp_first2 = False

            if temp_first == False:
                self.draw_rectangle(r * 8 + 530, 256 - lineH // 2, 8, lineH, color)

            if temp_first == True:
                temp_first2 = True
                temp_color = color


            ra += 1
            ra += 360 if ra < 0 else 0
            ra -= 360 if ra > 360 else 0
