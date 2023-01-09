import pickle
import os


class StorableWorld:
    """
    A simple class that can be used to store a map in a file,
    then loaded to a world by World.__init__().
    """
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
        Write a StorableWorld to a path.
        Warning: will overwrite the file.
        """
        data = self.serialize()
        if not os.path.exists(path):
            os.mknod(path)
        with open(path, "wb") as f:
            f.write(data)
        return 0
        

def load(path: str):
    """
    Reads a StorableWorld from a file and returns it deserialized.
    """
    with open(path, "rb") as f:
        return pickle.loads(f.read())
