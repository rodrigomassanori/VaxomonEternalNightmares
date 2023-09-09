import pygame

class Sprite():
    def __init__(self, imagePath, scrn):
        self.image = pygame.image.load(imagePath)
        self.scrn = scrn

    def draw(self,  x, y):
        self.cords = (x, y)
        self.scrn.blit(self.image, self.cords)