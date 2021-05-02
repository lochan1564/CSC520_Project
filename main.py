import uniform_cost_search as ucs
import Search as astar
from Environment import Environment
import Search

file = open("setup.txt", r)
#need to get the file name, start postion, and end position
rand = file.readline()
if(rand == 'Y'):
    env = Environment(True, None)
else:
    boardFile = file.readline()   
    env = Environment(False, boardFile)

uniform = ucs.uniform_cost_search_roads_built(env)
print(uniform)

astar = astar.a_star_search_roads_built(env)
print(astar)

