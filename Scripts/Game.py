import rubato as Rub

class Game:
    @staticmethod
    def Init():
        Width = 1440
        Height = 690
        ScreenFull = False
        Rub.init(name = "Vaxomon Eternal Nightmares", res = (Width, Height), fullscreen = ScreenFull)
        Rub.begin()
Game.Init()