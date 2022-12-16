from render.sprites import SpriteStruct, static_sprites
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
        self.sprite_struct = SpriteStruct(static_sprites["grunt.png"], 110, 70)

    def update(self):
        self.ia_command()
        pass
    
    def ia_command(self):
        """
        Returns a force vector based on the move the IA choses.
        """
        pass
