
# Class for Tiles
class Tiles():
    
    # constructor
    def __init__(self, x, y, t_id=0):
        self.tile_id = t_id # by default id=0 and corresponds to a flat type tile
        self.x_coord = x # x-coordinate of the tile
        self.y_coord = y # y-coordinate of the tile
        self.economic_cost = 0.05
        self.social_cost = 0.05
        self.env_cost = 0.05
        self.weights = (1.0, 1.0, 1.0)
        self.tile_name = 'FlatOpen'
        self.tile_status = 'Passable'
        self.setTileName(self.tile_id)
        self.setTile_status(self.tile_id)
        self.setCost(self.tile_id)
        #return
        
    def setWeight(self, eco, soc, env):
        self.weights = (eco, soc, env)
        
    def setCost(self, tile_id):
        
        if tile_id == 0:
            self.economic_cost = 0.05
            self.social_cost = 0.05
            self.env_cost = 0.05
        
        if tile_id == 1:
            self.economic_cost = 0.20
            self.social_cost = 0.50
            self.env_cost = 0.90
        
        if tile_id == 2:
            self.economic_cost = 100.0
            self.social_cost = 100.0
            self.env_cost = 100.0
        
        if tile_id == 3:
            self.economic_cost = 0.40
            self.social_cost = 1.0
            self.env_cost = 0.50
        
        if tile_id == 4:
            self.economic_cost = 1.0
            self.social_cost = 0.15
            self.env_cost = 0.85
        
        if tile_id == 5:
            self.economic_cost = 0.10
            self.social_cost = 0.30
            self.env_cost = 1.0
        
        if tile_id == 6:
            self.economic_cost = 100.0
            self.social_cost = 100.0
            self.env_cost = 100.0
        
        if tile_id == 7:
            self.economic_cost = 100.0
            self.social_cost = 100.0
            self.env_cost = 100.0
        
        if tile_id == 8:
            self.economic_cost = 0.60
            self.social_cost = 0.10
            self.env_cost = 0.60
        
        if tile_id == 9:
            self.economic_cost = 100.0
            self.social_cost = 100.0
            self.env_cost = 100.0
    
    def getCost(self):
        return (self.weights[0]*self.economic_cost, self.weights[1]*self.social_cost, self.weights[2]*self.env_cost)
    
    def setTileName(self, tile_id): # description of the tile
        
        if tile_id == 0:
            self.tile_name = 'FlatOpen'
        
        if tile_id == 1:
            self.tile_name = 'Forest'
        
        if tile_id == 2:
            self.tile_name = 'Railroad'
        
        if tile_id == 3:
            self.tile_name = 'Rolling'
        
        if tile_id == 4:
            self.tile_name = 'Stream'
        
        if tile_id == 5:
            self.tile_name = 'ESA' # Environmentally sensitive area
        
        if tile_id == 6:
            self.tile_name = 'Lake'
        
        if tile_id == 7:
            self.tile_name = 'Residential'
        
        if tile_id == 8:
            self.tile_name = 'Farmland'
        
        if tile_id == 9:
            self.tile_name = 'Industry'
        
    
    def setTile_status(self, tile_id): # if the tile is passable or not
        
        if tile_id in [2,6,7]:
            self.tile_status = 'Impassable'
        elif tile_id == 9:
            self.tile_status = 'Target'
        else:
            self.tile_status = 'Passable'
