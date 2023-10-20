import pygame

class Window:
    def __init__(self, width, height, title):
        self.__width = width
        self.__height = height
        self.__title = title

        self.create()

    def create(self):
        pygame.init()
        self.__fenetre = pygame.display.set_mode((self.__width, self.__height), pygame.RESIZABLE)
        pygame.display.set_caption(self.__title)

    def return_fenetre(self):
        return self.__fenetre

    def update(self):
        pygame.display.update()

    def change_screen_size(self, width, height):
        self.__fenetre = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    def fill(self, color):
        self.__fenetre.fill(color)

    def quit(self):
        pygame.quit()