import uniform_cost_search as ucs
from Environment import Environment

env = Environment(False, 'Board_summary.csv')
optimal = ucs.uniform_cost_search_roads_built(env)

for y in range(15):
    for x in range(15):
        if (x, y) in optimal:
            print('@', end=' ')
        else:
            tile = env.TileList[y][x]
            if tile.tile_name == 'FlatOpen':
                print('_', end=' ')
            elif tile.tile_name == 'Forest':
                print('F', end=' ')
            elif tile.tile_name == 'Railroad':
                print('#', end=' ')
            elif tile.tile_name == 'Rolling':
                print('^', end=' ')
            elif tile.tile_name == 'Stream':
                print('~', end=' ')
            elif tile.tile_name == 'ESA':
                print('E', end=' ')
            elif tile.tile_name == 'Lake':
                print('-', end=' ')
            elif tile.tile_name == 'Residential':
                print('R', end=' ')
            elif tile.tile_name == 'Farmland':
                print('F', end=' ')
            elif tile.tile_name == 'Industry':
                print('!', end=' ')
    print()