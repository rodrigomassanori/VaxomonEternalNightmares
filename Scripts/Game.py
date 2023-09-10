import pygame
from Scripts.MapGenerator import MapGenerator

class Game:
    @staticmethod
    def Init():
        Width = 1440
        Height = 690
        backGroundColor = (0, 12, 24)
        Title = "Vaxomon Eternal Nightmares"
        GameIsRunning = True
        pygame.init()
        pygame.display.set_caption(Title)
        Display = (Width, Height)
        Screen = pygame.display.set_mode(Display)
        clock = pygame.time.Clock()
        Map = MapGenerator()
        while GameIsRunning:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            Screen.fill(backGroundColor)
            Map.InitMap()
            pygame.display.flip()
            clock.tick(60)

Game.Init()