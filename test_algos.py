import uniform_cost_search as ucs
from Environment import Environment
import png

env = Environment(False, 'Board_summary.csv')
optimal = ucs.uniform_cost_search_roads_built(env)

rows = []
for y in range(15):
    row = []
    for x in range(15):
        if (x, y) in optimal:
            print('@', end=' ')
            row += [0, 0, 0]
        else:
            tile = env.TileList[y][x]
            if tile.tile_name == 'FlatOpen':
                print('_', end=' ')
                row += [255, 255, 255]
            elif tile.tile_name == 'Forest':
                print('F', end=' ')
                row += [146, 208, 80]
            elif tile.tile_name == 'Railroad':
                print('#', end=' ')
                row += [237, 125, 49]
            elif tile.tile_name == 'Rolling':
                print('^', end=' ')
                row += [226, 239, 218]
            elif tile.tile_name == 'Stream':
                print('~', end=' ')
                row += [155, 194, 230]
            elif tile.tile_name == 'ESA':
                print('E', end=' ')
                row += [192, 0, 0]
            elif tile.tile_name == 'Lake':
                print('-', end=' ')
                row += [0, 176, 240]
            elif tile.tile_name == 'Residential':
                print('R', end=' ')
                row += [174, 170, 170]
            elif tile.tile_name == 'Farmland':
                print('F', end=' ')
                row += [191, 143, 0]
            elif tile.tile_name == 'Industry':
                print('!', end=' ')
                row += [255, 255, 0]
    rows.append(tuple(row))
    print()

with open('environment_roads.png', 'wb') as f:
    png.Writer(15, 15, greyscale=False).write(f, rows)