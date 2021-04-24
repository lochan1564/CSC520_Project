import Environment
import Tiles
import uniform_cost_search

file = open("setup.txt", r)
#need to get the file name, start postion, and end position

env = Environment(false, "Board_summary.csv")

uniform_cost_search(env, start, goal)

