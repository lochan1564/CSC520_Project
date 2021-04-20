import sys
import Environment
from Tiles import Tiles
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
    first = Node(start, None, hCost())
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
            if(i == 0):
                #TODO Add huristic cost here
                successor = Node(environment.getTile(expand.x_coord + 1, expand.y_coord), expand, COST)
                
                if successor.getTile().tile_status == 'Impassable':
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
            
            
            successor = None
            elif(i == 1):
                #TODO Add huristic cost here
                successor = Node(environment.getTile(expand.x_coord - 1, expand.y_coord), expand, COST)
                
                if successor.getTile().tile_status == 'Impassable':
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
                successor = Node(environment.getTile(expand.x_coord, expand.y_coord + 1), expand, COST)
                
                if successor.getTile().tile_status == 'Impassable':
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
                successor = Node(environment.getTile(expand.x_coord, expand.y_coord - 1), expand, COST)
                
                if successor.getTile().tile_status == 'Impassable':
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