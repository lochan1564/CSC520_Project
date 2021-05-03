from Tiles import Tiles
import pandas as pd
import numpy as np
import gen_random_env
class Environment:
    def __init__(self, random, fileName):
        self.TileList = []
        if random:
            self.randomTiles()
        else:
            self.importTileFile(fileName)
    
    def randomTiles(self):
        self.TileList = gen_random_env.gen_smoothed_random_env()
    
    def importTileFile(self, fileName):
        self.TileList = importFromFile(fileName)
    
    def getTile(self, x, y):
        if(x >= 0 and x < 15 and y >= 0 and y < 15):
            return self.TileList[y][x]
        else:
            return None
    
    def importFromFile(tileFile):
        filepath = tileFile

        board_summary = pd.read_csv(filepath)

        # List to store tile objects
        tile_list = list()

        for i in range(len(board_summary)):
            x = board_summary['x'][i]
            y = board_summary['y'][i]
            t_id = board_summary['id'][i]
            tile = Tiles(x,y,t_id)
            tile_list.append(tile)
    
 

        board = [[None for _ in range(15)] for _ in range(15)]

        # board = np.full(tuple([15]*2),"   ")

        for i in range(15):
            for j in range(15):
                board[i][j] = tile_list[i*15+j]
                #board[i][j] = tile_list[i*15+j].tile_name

        return board
