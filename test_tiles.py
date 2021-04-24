# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 10:23:48 2021

@author: lbasnet
"""

import pandas as pd
import numpy as np
from Tiles import Tiles


# Filepath of the summary file
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
    
    #for i in range(len(tile_list)):
        #print(tile_list[i].tile_name)
        #print(tile_list[i].x_coord)
        #print(tile_list[i].y_coord)
        #print(tile_list[i].tile_id)

    board = np.full(tuple([15]*2),"   ")

    for i in range(15):
        for j in range(15):
            board[i][j] = tile_list[i*15+j].tile_id
            #board[i][j] = tile_list[i*15+j].tile_name

    return board