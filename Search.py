import sys
import Environment
from Tiles import Tiles
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
            # do not need last position because we are only concerned with roads touching goal
            return (path_cost, path[:-1])
        curr_x, curr_y = pos
        locs_visited.add((curr_x, curr_y))
        # look around in each direction to expand
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_pos = curr_x + dx, curr_y + dy
            tile = environment.getTile(*next_pos)
            if tile and next_pos not in locs_visited:
                path_to_next = path + [next_pos]
                total_cost_to_next = path_cost + (0 if next_pos in goal_positions else tile.getCost())
                heapq.heappush(path_options, (total_cost_to_next, next_pos, path_to_next))


def AStarSearch(environment, begin_pos, goal_positions):
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
            # do not need last position because we are only concerned with roads touching goal
            return (path_cost, path[:-1])
        curr_x, curr_y = pos
        locs_visited.add((curr_x, curr_y))
        # look around in each direction to expand
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_pos = curr_x + dx, curr_y + dy
            tile = environment.getTile(*next_pos)
            if tile and next_pos not in locs_visited:
                path_to_next = path + [next_pos]
                # calculate backward cost
                g = path_cost + (0 if next_pos in goal_positions else tile.getCost())
                # calculate heuristic cost
                h = HueristicCost(next_pos, goal_positions)
                total_cost_to_next = g + h
                heapq.heappush(path_options, (total_cost_to_next, next_pos, path_to_next))

  
def HueristicCost(start, end_positions):
    start_x, start_y = start
    return min(abs(end_x - start_x) + abs(end_y - start_y) for end_x, end_y in end_positions)


def roads_built(environment, algorithm):
    # return most_optimal_road_network
    industry_locs = []
    for y in range(15):
        for x in range(15):
            if environment.getTile(x, y).tile_name == 'Industry':
                industry_locs.append((x, y))

    # get all permutations of the industry locations in order to look through performing uniform cost search
    # on the locations in every possible order to find most optimal
    all_permutations = [list(p) for p in permutations(industry_locs)]

    # keep track of the most optimal road network
    min_total_cost = float('inf')
    most_optimal_road_network = None
    for industry_locs_perm in all_permutations:
        # keep a list of all of the positions that roads have been built on
        road_network = []
        road_total_cost = 0
        # keep track of all of the goal locations (roads + industry locs)
        goals = [industry_locs_perm.pop()]

        while len(industry_locs_perm) != 0:
            industry_loc = industry_locs_perm.pop()
            road_cost, road_path = algorithm(environment, industry_loc, goals)

            road_network += road_path
            road_total_cost += road_cost
            goals += [industry_loc] + road_path

        # check if this is the lowest-cost road found so far
        if road_total_cost < min_total_cost:
            min_total_cost = road_total_cost
            most_optimal_road_network = road_network

    return most_optimal_road_network


def a_star_search_roads_built(environment):
    return roads_built(environment, AStarSearch)


def uniform_cost_search_roads_built(environment):
    return roads_built(environment, uniform_cost_search)