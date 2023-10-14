import pygame

class Window:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

        self.create()

    def create(self):
        pygame.init()
        self.fenetre = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def update(self):
        pygame.display.update()

    def fill(self, color):
        self.fenetre.fill(color)

    def quit(self):
        pygame.quit()