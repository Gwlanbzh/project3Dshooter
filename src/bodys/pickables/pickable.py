from bodys import Body

class Pickable(Body):
    def __init__(self, game, r):
        super().__init__(game, r)
        
        self.color = "green"
    
    def picker(self):
        """
        If a player is currently on the object, returns that Player,
        otherwise None.
        """
        i = 0
        player = self.game.world.players[i]
        distance = (player.r - self.r).magnitude()
        if distance < player.size + self.size:
            return player
        return None
    
    def update(self):
        #  picker = self.picker()
        #  return False
        pass
