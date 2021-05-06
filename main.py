from Environment import Environment
from Search import a_star_search_roads_built, uniform_cost_search_roads_built
import Tiles
import png

def write_to_image(env, road_locations, output_file):
    rows = []
    for y in range(15):
        row = []
        for x in range(15):
            if (x, y) in road_locations:
                row += [0, 0, 0]
            else:
                tile = env.TileList[y][x]
                if tile.tile_name == 'FlatOpen':
                    row += [255, 255, 255]
                elif tile.tile_name == 'Forest':
                    row += [146, 208, 80]
                elif tile.tile_name == 'Railroad':
                    row += [237, 125, 49]
                elif tile.tile_name == 'Rolling':
                    row += [226, 239, 218]
                elif tile.tile_name == 'Stream':
                    row += [155, 194, 230]
                elif tile.tile_name == 'ESA':
                    row += [192, 0, 0]
                elif tile.tile_name == 'Lake':
                    row += [0, 176, 240]
                elif tile.tile_name == 'Residential':
                    row += [174, 170, 170]
                elif tile.tile_name == 'Farmland':
                    row += [191, 143, 0]
                elif tile.tile_name == 'Industry':
                    row += [255, 255, 0]
        rows.append(tuple(row))

    with open(output_file, 'wb') as f:
        png.Writer(15, 15, greyscale=False).write(f, rows)


file = open("setup.txt", 'r')
#need to get the file name, start postion, and end position
rand = file.readline()

Tiles.econ_weight = float(file.readline())
Tiles.soc_weight = float(file.readline())
Tiles.env_weight = float(file.readline())

if(rand == 'Y'):
    env = Environment(True, None)
else:
    boardFile = file.readline()   
    env = Environment(False, boardFile)

uniform = uniform_cost_search_roads_built(env)
print(uniform)
envCost = 0 
ecoCost = 0
socCost = 0
for tileCoord in uniform:
    costs = env.getTile(tileCoord[0], tileCoord[1]).getCostTuple()
    ecoCost += costs[0]
    socCost += costs[1]
    envCost += costs[2]
print("UCS Economic cost: "+ str(ecoCost))
print("UCS Social cost: "+ str(socCost))
print("UCS Environmental cost: "+ str(envCost))
print("UCS total cost:", envCost + ecoCost + socCost)
write_to_image(env, uniform, 'ucs_environment_roads.png')


astar = a_star_search_roads_built(env)
print(astar)

envCost = 0 
ecoCost = 0
socCost = 0
for tileCoord in astar:
    costs = env.getTile(tileCoord[0], tileCoord[1]).getCostTuple()
    ecoCost += costs[0]
    socCost += costs[1]
    envCost += costs[2]
print("AStar Economic cost: "+ str(ecoCost))
print("AStar Social cost: "+ str(socCost))
print("AStar Environmental cost: "+ str(envCost))
print("AStar total cost:", envCost + ecoCost + socCost)
write_to_image(env, astar, 'astar_environment_roads.png')
