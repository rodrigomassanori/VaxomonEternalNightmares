class MapGenerator:
    TileSetX = 64
    TileSetY = 64
    @staticmethod
    def InitMap(scrn):
        img0 = ("Tilesets/MissingTexture.png", scrn)
        img1 = ("Tilesets/Flor.png", scrn)
        img2 = ("Tilesets/GrassTop.png", scrn)

    def load(filename, scrn):
        imgMap = (filename, scrn)
        mapSize = imgMap.image.get_size()
        mat = [[0] * mapSize[1] for _ in range(mapSize[0])]
        
        for i in range(0, mapSize[0]):
            for j in range(0, mapSize[1]):
                color = imgMap.image.get_at((i, j))

                if color == (0, 0, 0):
                    mat[i][j] = 0
                    
                elif color == (255, 255, 255):
                    mat[i][j] = 1
                    
                else:
                    mat[i][j] = -1

    def draw(self):
        for i in range(0, self.mapSize[0]):
            for j in range(0, self.mapSize[1]):
                if self.mat[i][j] == 0:
                    self.img1.draw(i * self.TileSetX, j*self.TileSetY)
                    
                elif self.mat[i][j] == 1:
                    self.img2.draw(i * self.TileSetX, j * self.TileSetY)
                    
                else:
                    self.img0.draw(i * self.TileSetX, j * self.TileSetY)