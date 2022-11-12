from ..creature import Creature
import math
class Mob(Creature):
    def __init__(self,game,r):
        """
        Spawns a Mob.
        
        Inputs:
            <none>
        
        Outputs:
            Mob
        """
        super().__init__(game,r)
        self.color = 'red' 
        self.speed = 1

    def update(self):
        self.ia_command()
        pass

    def movement(self):

        x,y = self.r
        target_pos = self.game.world.players[0].r
        angle = math.atan2(target_pos[1] - y, target_pos[0] - x)
        dx = math.cos(angle) * self.speed
        dy = math.sin(angle) * self.speed

        self.orientation = angle

        x_permission, y_permission = self.not_colliding(dx, dy)
        if x_permission:
            x += dx
        if y_permission:
            y += dy 
        self.r = x, y


    
    def ia_command(self):
        """
        Returns a force vector based on the move the IA choses.
        """
        self.movement()
        pass