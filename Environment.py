from Tiles import Tiles
import gen_random_env
import 
class Environment:
    def __init__(self, random):
        self.TileList = []
        if random:
            self.randomTiles()
        else:
            self.importTileFile()
    
    def randomTiles(self):
        self.TileList = gen_random_env.gen_smoothed_random_env()
    
    def importTileFile(self):
        #fill in the board based on a file
    
    def getTile(self, x, y):
        if(x >= 0 and x <= 15 and y >= 0 and y <= 15):
            return self.TileList[x][y]
        else:
            return None
