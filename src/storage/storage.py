import pickle
import os


class StorableWorld:
    def __init__(self, props, pickables, mobs, players, exits, grid, skybox, floor, texture_set, map_scale):
        self.props = props
        self.pickables = pickables
        self.mobs = mobs
        self.players = players
        
        self.exits = exits
        self.grid = grid
        
        self.skybox = skybox
        self.floor = floor
        self.texture_set = texture_set
        self.map_scale = map_scale

    def serialize(self):
        return pickle.dumps(self)
    
    def write(self, path: str):
        """
        If file does not exist, returns 0 and write to it.
        Returns -1 and does nothing otherwise.
        """
        data = self.serialize()
        if not os.path.exists(path):
            os.mknod(path)
        with open(path, "wb") as f:
            f.write(data)
        return 0
        

def load(path: str):
    with open(path, "rb") as f:
        return pickle.loads(f.read())
