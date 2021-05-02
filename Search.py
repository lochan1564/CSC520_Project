import sys
import Environment
from Tiles import Tiles
import heapq
from itertools import permutations
class Node():
    
    def __init__(self, tile, parent, cost):
        self.tile = tile 
        self.parent = parent
        if parent == None:
            self.cost = cost
        else:
            self.cost = cost + parent.getCost()

    def getTile(self):
        return self.tile

    def getParent(self):
        return self.parent

    def getCost(self):
        return self.cost 
    
def AStarSearch(environment, start, end):
    #List that represents the locations that need to have their neighbors expanded
    open = []
    #List that represents the locations that have been expanded
    closed = []
    #List of tiles along the final path (Where the road will be built)
    path= []

    #TODO Add huristic cost here
    first = Node(start, None, HueristicCost(start, end))
    open.append(first)

    #Keep track of if the goal has been met (Has a path between start and end been found)
    goalFound = False

    while len(open) != 0 and not goalFound:
        expand = Node(None, None, sys.maxint)
        
        #Iterate through the unexpaned list and find the node with the smallest hueristic cost
        for n in open:
            if n.getCost() < expand.getCost():
                expand = n
        
        open.remove(expand)

        for i in range(4):
            successor = None
            if(i == 0):
                #TODO Add huristic cost here
                successor = Node(environment.getTile(expand.x_coord + 1, expand.y_coord), expand, HueristicCost(start, end))
                
                if successor.getTile().tile_status == 'Impassable':
                    goalFound = False
                    #Do nothing
                elif CHECK_IF_GOAL_MET:
                    goalFound = True
                    path.append(sucessor)
                    break
                else:
                    addToOpen = True

                    #Check if the tile already exists in the open list with a lower cost
                    for nodesToExplore in open:
                        if nodesToExplore.getTile() == successor.getTile() and nodesToExplore.getCost() <= successor.getCost():
                            addToOpen = False
                            break
                    
                    #Check if the tile already exists in the closed list with a lower cost
                    for nodesExplored in closed:
                        if nodesExplored.getTile() == successor.getTile() and nodesExplored.getCost() <= successor.getCost():
                            addToOpen = False
                            break

                    if addToOpen:
                        open.append(successor)
            
            elif(i == 1):
                #TODO Add huristic cost here
                successor = Node(environment.getTile(expand.x_coord - 1, expand.y_coord), expand, HueristicCost(start, end))
                
                if successor.getTile().tile_status == 'Impassable':
                    goalFound = False
                    #Do nothing
                elif CHECK_IF_GOAL_MET:
                    goalFound = True
                    path.append(sucessor)
                    break
                else:
                    addToOpen = True

                    #Check if the tile already exists in the open list with a lower cost
                    for nodesToExplore in open:
                        if nodesToExplore.getTile() == successor.getTile() and nodesToExplore.getCost() <= successor.getCost():
                            addToOpen = False
                            break
                    
                    #Check if the tile already exists in the closed list with a lower cost
                    for nodesExplored in closed:
                        if nodesExplored.getTile() == successor.getTile() and nodesExplored.getCost() <= successor.getCost():
                            addToOpen = False
                            break

                    if addToOpen:
                        open.append(successor)
            elif(i == 2):
                #TODO Add huristic cost here
                successor = Node(environment.getTile(expand.x_coord, expand.y_coord + 1), expand, HueristicCost(start, end))
                
                if successor.getTile().tile_status == 'Impassable':
                    goalFound = False
                    #Do nothing
                elif CHECK_IF_GOAL_MET:
                    goalFound = True
                    path.append(sucessor)
                    break
                else:
                    addToOpen = True

                    #Check if the tile already exists in the open list with a lower cost
                    for nodesToExplore in open:
                        if nodesToExplore.getTile() == successor.getTile() and nodesToExplore.getCost() <= successor.getCost():
                            addToOpen = False
                            break
                    
                    #Check if the tile already exists in the closed list with a lower cost
                    for nodesExplored in closed:
                        if nodesExplored.getTile() == successor.getTile() and nodesExplored.getCost() <= successor.getCost():
                            addToOpen = False
                            break

                    if addToOpen:
                        open.append(successor)
            
            elif(i == 3):
                #TODO Add huristic cost here
                successor = Node(environment.getTile(expand.x_coord, expand.y_coord - 1), expand, HueristicCost(start, end))
                
                if successor.getTile().tile_status == 'Impassable':
                    goalFound = False
                    #Do nothing
                elif CHECK_IF_GOAL_MET:
                    goalFound = True
                    path.append(sucessor)
                    break
                else:
                    addToOpen = True

                    #Check if the tile already exists in the open list with a lower cost
                    for nodesToExplore in open:
                        if nodesToExplore.getTile() == successor.getTile() and nodesToExplore.getCost() <= successor.getCost():
                            addToOpen = False
                            break
                    
                    #Check if the tile already exists in the closed list with a lower cost
                    for nodesExplored in closed:
                        if nodesExplored.getTile() == successor.getTile() and nodesExplored.getCost() <= successor.getCost():
                            addToOpen = False
                            break

                    if addToOpen:
                        open.append(successor)
        
        closed.append(successor)

    for n in closed:
        add = closed.pop.getTile
        path.append = (add.x_coord, add.y_coord)
    
    return path
    
def HueristicCost(start, end):
    return abs(start.getTile.x_coord - end.getTile.x_coord) + abs(start.getTile.y_coord - end.getTile.y_coord)

def a_star_search_roads_built(environment):
    industry_locs = []
    for y in range(15):
        for x in range(15):
            if environment.getTile(x, y).tile_name == 'Industry':
                industry_locs.append(environment.getTile(x, y))
    network = []
    start = industry_locs.index(0)
    for locations in industry_locs:
        network.append(AStarSearch(environment, start, locations))

    return most_optimal_road_network