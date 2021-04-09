import random
from Tile import Tile

DIM = 15

def rand_tile():
    rand = random.random
    return Tile(rand(), rand(), rand())


def gen_completely_random_env():
    return [[rand_tile() for _ in range(DIM)] for _ in range(DIM)]


# generate an environment with cost values averaged among several
# randomly chosen points
def gen_smoothed_random_env():
    num_points = random.randint(DIM // 3, DIM)
    # create a list of DIM randomly selected points
    points = []
    for _ in range(num_points):
        location = (random.randint(0, DIM - 1), random.randint(0, DIM - 1))
        vals = rand_tile()
        # only add this point to the list if there is not one at this location already
        if sum(point_loc == location for point_loc, _ in points) == 0:
            points.append((location, vals))

    grid = []
    for y in range(DIM):
        row = []
        for x in range(DIM):
            # get the distances from each random point to this (x, y) location
            dist_from_each = [(x - px) ** 2 + (y - py) ** 2 for (px, py), _ in points]

            # compute 'normalized' distances in which the sum of all distances is 0
            
            inv_dist = [float('inf') if d == 0 else 1 / d for d in dist_from_each]
            sum_inv_dist = sum(inv_dist)
            weights = [1 if d == float('inf') else d / sum_inv_dist for d in inv_dist]
            
            # get a tile with values averaged from all points
            tile = Tile(0, 0, 0)
            for i, (_, tile_info) in enumerate(points):
                weight = weights[i]
                tile.env += tile_info.env * weight
                tile.econ += tile_info.econ * weight
                tile.soc += tile_info.soc * weight

            row.append(tile)
        grid.append(row)
    return grid
