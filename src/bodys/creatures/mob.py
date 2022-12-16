from render.sprites import SpriteStruct, static_sprites
from bodys.creatures.creature import Creature
import math
from bodys.creatures.path_finding import *

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
        self.speed = 0.06 # small value because of the * dt
        self.has_seen_player = False
        self.fov = math.pi/2
        self.test = game.window
        self.path_finding = Path_finding(game)
        self.sprite_struct = SpriteStruct(static_sprites["demon.png"], 150)

    def update(self):
        self.ia_command()
        if self.is_dead():
            self.color = "black"
    
    def ia_command(self):
        """
        Behavior of the mob
        """
        if not self.has_seen_player: 
            self.mob_view_player()
        if self.has_seen_player:
            self.movement()
        pass

    def movement(self):
        # Get player and self position
        x,y = self.r
        target_pos = self.game.world.players[0].r

        # compute nex postion
        angle = math.atan2(target_pos[1] - y, target_pos[0] - x)
        dx = math.cos(angle) * self.speed * self.game.delta_time
        dy = math.sin(angle) * self.speed * self.game.delta_time
        self.orientation = angle

        # check colision with not_colliding's Creature methode
        x_permission, y_permission = self.not_colliding(dx, dy)
        if x_permission:
            x += dx
        if y_permission:
            y += dy 
        self.r = x, y


    def mob_view_player(self):
        """
        Algo to trigger mob to move toward player 
        TODO : add ray cast for removoing mob been able to see us through wall 
        """

        MAX_LENGHT_RAY = 1660

        # Info Player
        x_player,y_player = self.game.world.players[0].r[0],self.game.world.players[0].r[1]
        tile_player_x,tile_player_y = x_player//100,y_player//100

        # Info Mob
        x,y = self.r[0],self.r[1]

        # if player in FOV of mob
        angle_mob_player = math.atan2(y_player - y,x_player - x)
        if self.orientation - math.pi/4 < angle_mob_player < self.orientation + math.pi/4:
            self.has_seen_player = True

    