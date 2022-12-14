import pickle
import os


class StorableWorld:
    def __init__(self, props=[], pickables=[], mobs=[], players=[], grid=[], skybox="sky.png", floor=(70, 70, 70)):
        self.props = props
        self.pickables = pickables
        self.mobs = mobs
        self.players = players
        self.grid = grid
        
        self.skybox = skybox
        self.floor = floor

    def serialize(self):
        return pickle.dumps(self)
    
    def write(self, path: str):
        """
        If file does not exist, returns 0 and write to it.
        Returns -1 and does nothing otherwise.
        """
        data = self.serialize()
        if os.path.exists(path):
            return -1
        else:
            os.mknod(path)
            with open(path, "wb") as f:
                f.write(data)
            return 0
        

def load(path: str):
    with open(path, "rb") as f:
        return pickle.loads(f.read())
