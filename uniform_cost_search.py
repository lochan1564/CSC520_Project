import heapq
from itertools import permutations

def uniform_cost_search(environment, begin_pos, goal_positions):
    locs_visited = set()

    # priority queue to hold the next available paths in order of least path cost.
    # elements in this PQ are triples of the form (path_cost, path_head_position, path)
    # note: path cost is first element in tuple for priority queue sorting to work properly
    path_options = []
    heapq.heappush(path_options, (0, begin_pos, []))

    while len(path_options) != 0:
        # get the most optimal position from here
        curr = heapq.heappop(path_options)
        path_cost, pos, path = curr
        # if another industry has been found then stop the search
        if pos in goal_positions:
            return path
        curr_x, curr_y = pos
        locs_visited.add((curr_x, curr_y))
        # look around in each direction to expand
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_pos = curr_x + dx, curr_y + dy
            tile = environment.getTile(*next_pos)
            if tile and next_pos not in locs_visited:
                path_to_next = path + [next_pos]
                total_cost_to_next = path_cost + (0 if next_pos in goal_positions else sum(tile.getCost()))
                heapq.heappush(path_options, (total_cost_to_next, next_pos, path_to_next))


def uniform_cost_search_roads_built(environment):
    industry_locs = []
    for y in range(15):
        for x in range(15):
            if environment.getTile(x, y).tile_name == 'Industry':
                industry_locs.append((x, y))

    # get all permutations of the industry locations in order to look through performing uniform cost search
    # on the locations in every possible order to find most optimal
    all_permutations = permutations(industry_locs)
    roads_built_all_perm = []
    for industry_locs_perm in all_permutations:
        
        # keep a list of all of the positions that roads have been built on
        roads_built = []
        while len(industry_locs_perm) != 0:
            industry_loc = industry_locs_perm.pop()

            road_path = uniform_cost_search(environment, industry_loc, industry_locs_perm + roads_built)
            roads_built += road_path

        roads_built_all_perm.append(roads_built)

    # attempt to find the most optimal road network from all of the permutations tried
    min_total_cost = float('inf')
    most_optimal_road_network = None
    for road_network in roads_built_all_perm:
        # get the total cost incurred by this road network
        total_cost = sum(sum(environment.getTile(position).getCost()) for position in road_network)
        # indicate that this road network is most optimal if needed
        if total_cost < min_total_cost:
            min_total_cost = total_cost
            most_optimal_road_network = road_network

    return most_optimal_road_network
