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
envCost = 0 
ecoCost = 0
socCost = 0
for tileCoord in uniform:
    costs = env.getTile(tileCoord[0], tileCoord[1]).getCost()
    ecoCost += costs[0]
    socCost += costs[1]
    envCost += costs[2]
print("Economic cost: "+ str(ecoCost))
print("Social cost: "+ str(socCost))
print("Environmental cost: "+ str(envCost))

astar = astar.a_star_search_roads_built(env)
print(astar)

envCost = 0 
ecoCost = 0
socCost = 0
for tileCoord in uniform:
    costs = env.getTile(tileCoord[0], tileCoord[1]).getCost()
    ecoCost += costs[0]
    socCost += costs[1]
    envCost += costs[2]
print("Economic cost: "+ str(ecoCost))
print("Social cost: "+ str(socCost))
print("Environmental cost: "+ str(envCost))