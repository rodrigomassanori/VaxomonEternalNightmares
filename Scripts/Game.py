import pygame
from pygame import OPENGL, DOUBLEBUF
from Scripts.MapGenerator import MapGenerator

class Game:
    @staticmethod
    def Init():
        Width = 1440
        Height = 690
        Title = "Vaxomon Eternal Nightmares"
        GameIsRunning = True
        pygame.init()
        pygame.display.set_caption(Title)
        Display = (Width, Height)
        pygame.display.set_mode(Display, DOUBLEBUF | OPENGL)
        Map = MapGenerator()
        while GameIsRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

Game.Init()