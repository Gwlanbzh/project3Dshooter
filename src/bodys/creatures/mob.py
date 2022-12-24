from render.sprites import SpriteStruct
from bodys.creatures.creature import Creature

class Mob(Creature):
    def __init__(self, game, r):
        """
        Spawns a Mob.
        
        Inputs:
            <none>
        
        Outputs:
            Mob
        """
        super().__init__(game, r)
        self.color = 'red' 
        self.sprite_data = SpriteStruct("grunt.png", 110, 70)

    def update(self):
        self.ia_command()
        pass
    
    def ia_command(self):
        """
        Returns a force vector based on the move the IA choses.
        """
        pass


class Grunt(Mob):
    def __init__(self, game, r):
        super().__init__(game,r)
        
        self.health = 100
        self.weapons = []        # TODO add pistol
        self.sprite_data = None  # TODO implement dynamic sprites

class Heavy(Mob):
    def __init__(self, game, r):
        super().__init__(game,r)
        
        self.health = 200
        self.weapons = []        # TODO add pistol
        self.sprite_data = None  # TODO implement dynamic sprites

class Boss(Mob):
    def __init__(self, game, r):
        super().__init__(game,r)
        
        self.health = 500
        self.weapons = []        # TODO add pistol
        self.sprite_data = None  # TODO implement dynamic sprites
