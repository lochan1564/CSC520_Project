import random
from Tiles import Tiles as Tile

DIM = 15

def rand_tile(x, y):
    tid = random.randint(0, 9)
    return Tile(x, y, tid)


def gen_completely_random_env():
    return [[rand_tile(x, y) for x in range(DIM)] for y in range(DIM)]


# try to generate a 'realistic' environment
def gen_smoothed_random_env():
    grid = [[None for _ in range(DIM)] for _ in range(DIM)]

    num_industries = random.randint(DIM // 4, DIM // 2)
    # create a list of DIM randomly selected points
    industries = []
    for _ in range(num_industries):
        origin_location = (random.randint(0, DIM - 1), random.randint(0, DIM - 1))
        x, y = origin_location
        vals = rand_tile(x, y)
        # only add this point to the list if there is not one at this location already
        if sum(point_loc == origin_location for point_loc, _ in industries) == 0:
            grid[y][x] = Tile(x, y, 9)
            industries.append((origin_location, vals))

    industry_locs = [loc for loc, _ in industries]
    # keep a list of all of the locations that something has been placed in
    available_locs = []
    for x in range(DIM):
        for y in range(DIM):
            if (x, y) not in industry_locs:
                available_locs.append((x, y))

    # randomly choose origin points for certain environment features (forest, residential area, etc)
    # and organically expand these areas to create realistic-looking terrain
    while len(available_locs) != 0:
        origin_location = available_locs[random.randint(0, len(available_locs) - 1)]
        orig_x, orig_y = origin_location
        available_locs.remove(origin_location)
        # keep a list of all locations that are a part of this environment feature
        environment_feature_locs = [origin_location]

        # take a random choice of non-industry tiles
        tile_id = random.randint(0, 8)

        grid[orig_y][orig_x] = Tile(orig_x, orig_y, tile_id)

        # choose a relatively high but arbitrary threshold ([0.7, 0.9]) to determine whether this environment
        # feature should continue getting expanded
        thres = 0.7 + random.random() * 0.2

        r = random.random()
        while r < thres:
            possible_next_locs = set()

            # get all available locations to expand by taking mapping of the current environment feature
            # expanded one unit in each direction and finding which ones are available

            def add_locs(dx, dy):
                for loc_x, loc_y in environment_feature_locs:
                    if (loc_x + dx, loc_y + dy) in available_locs:
                        possible_next_locs.add((loc_x + dx, loc_y + dy))
            add_locs(1, 0)
            add_locs(-1, 0)
            add_locs(0, 1)
            add_locs(0, -1)

            if len(possible_next_locs) == 0:
                break

            # sort the possible locations by distance away from origin of environment feature (to
            # make new points closer to origin more likely to be expanded to create organic-looking
            # terrain)

            def get_dist(loc_1, loc_2):
                l1x, l1y = loc_1
                l2x, l2y = loc_2
                return (l1x - l2x)**2 + (l1y - l2y)**2

            possible_next_locs = list(possible_next_locs)
            random.shuffle(possible_next_locs)
            possible_next_locs = sorted(possible_next_locs, key=lambda loc: get_dist(loc, origin_location))

            # allow closer locations to be more likely
            next_loc_i = int(random.randint(0, len(possible_next_locs) - 1) ** 0.8)

            next_loc = possible_next_locs[next_loc_i]
            next_loc_x, next_loc_y = next_loc

            environment_feature_locs.append(next_loc)

            grid[next_loc_y][next_loc_x] = Tile(next_loc_x, next_loc_y, tile_id)
            available_locs.remove(next_loc)

            r = random.random()

    return grid


# def gen_smoothed_random_env_old():
    # grid = []
    # for y in range(DIM):
    #     row = []
    #     for x in range(DIM):
            
    #         # get a tile with values averaged from all points
    #         tile = Tile(0, 0, 0)
    #         for i, (_, tile_info) in enumerate(industries):
    #             weight = weights[i]
    #             tile.env += tile_info.env * weight
    #             tile.econ += tile_info.econ * weight
    #             tile.soc += tile_info.soc * weight

    #         row.append(tile)
    #     grid.append(row)
    # return grid


    # num_points = random.randint(DIM // 3, DIM)
    # # create a list of DIM randomly selected points
    # points = []
    # for _ in range(num_points):
    #     location = (random.randint(0, DIM - 1), random.randint(0, DIM - 1))
    #     vals = rand_tile()
    #     # only add this point to the list if there is not one at this location already
    #     if sum(point_loc == location for point_loc, _ in points) == 0:
    #         points.append((location, vals))

    # grid = []
    # for y in range(DIM):
    #     row = []
    #     for x in range(DIM):
    #         # get the distances from each random point to this (x, y) location
    #         dist_from_each = [(x - px) ** 2 + (y - py) ** 2 for (px, py), _ in points]

    #         # compute 'normalized' distances in which the sum of all distances is 0
            
    #         inv_dist = [float('inf') if d == 0 else 1 / d for d in dist_from_each]
    #         sum_inv_dist = sum(inv_dist)
    #         weights = [1 if d == float('inf') else d / sum_inv_dist for d in inv_dist]
            
    #         # get a tile with values averaged from all points
    #         tile = Tile(0, 0, 0)
    #         for i, (_, tile_info) in enumerate(points):
    #             weight = weights[i]
    #             tile.env += tile_info.env * weight
    #             tile.econ += tile_info.econ * weight
    #             tile.soc += tile_info.soc * weight

    #         row.append(tile)
    #     grid.append(row)
    # return grid

def print_smoothed_env():
    grid = gen_smoothed_random_env()
    for row in grid:
        for tile in row:
            if tile.tile_id == 0:
                print('_', end=' ')
            elif tile.tile_id == 1:
                print('F', end=' ')
            elif tile.tile_id == 2:
                print('|', end=' ')
            elif tile.tile_id == 3:
                print('^', end=' ')
            elif tile.tile_id == 4:
                print('~', end=' ')
            elif tile.tile_id == 5:
                print('E', end=' ')
            elif tile.tile_id == 6:
                print('#', end=' ')
            elif tile.tile_id == 7:
                print('R', end=' ')
            elif tile.tile_id == 8:
                print('F', end=' ')
            elif tile.tile_id == 9:
                print('X', end=' ')
        print()

# print_smoothed_env()