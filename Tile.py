class Tile:
    def __init__(self, env, econ, soc):
        self.env = env
        self.econ = econ
        self.soc = soc

    def getEnv(self):
        return self.env

    def getEcon(self):
        return self.econ
    
    def getSoc(self):
        return self.soc

    def setEnv(self, env):
         self.env = env

    def setEcon(self, econ):
         self.econ = econ

    def setSoc(self, soc):
         self.soc = soc

    
