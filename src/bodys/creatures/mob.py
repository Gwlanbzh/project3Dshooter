from render.sprites import SpriteStruct, static_sprites
from bodys.creatures.creature import Creature
from math import pi, cos, sin, atan2
from pygame import Vector2 as v2
from render.ray import Ray

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
        self.fov = pi/2
        self.test = game.window
        self.sprite_struct = SpriteStruct(static_sprites["demon.png"], 150)

    def update(self):
        self.ia_command()
        if self.is_dead():
            self.color = "black"
    
    def ia_command(self):
        """
        Behavior of the mob
        """
        if not self.is_dead() :
            if not self.has_seen_player and self.mob_view_player():
                self.has_seen_player = True
            if self.has_seen_player:
                self.movement()
        pass

    def movement(self):
        # Get player and self position
        x,y = self.r
        target_pos = self.game.world.players[0].r

        # next_pos = self.game.path_finding.Astar((),)

        # compute nex postion
        angle = atan2(target_pos[1] - y, target_pos[0] - x)
        dx = cos(angle) * self.speed * self.game.delta_time
        dy = sin(angle) * self.speed * self.game.delta_time
        self.orientation = angle

        # check colision with not_colliding's Creature methode
        x_permission, y_permission = self.not_colliding(dx, dy)
        if x_permission:
            x += dx
        if y_permission:
            y += dy 
        self.r = v2(x, y)


    def mob_view_player(self):
        """
        Algo to trigger mob to move toward player 
        TODO : add ray cast for removoing mob been able to see us through wall 
        """
        player = self.game.world.players[0]
        mob_list = self.game.world.sorted_mob_list
        for dist_mob, mob in mob_list:
            # test mur
            direction = v2(player.r - mob.r)
            rayon = Ray(mob.r, direction, self.game.world.map.map)

            # Debug
            # print("ray :",rayon.distance)
            # print("mob : ",dist_mob)
            # print(" ")

            if rayon.distance > dist_mob:
                # if self.player_in_fov():
                    return True

    def player_in_fov(self): 
        # Info Player
        player = self.game.world.players[0]
        x_player,y_player = player.r.x, player.r.y

        # Info Mob
        mob_x,mob_y = self.r.x,self.r.y

        # if player in FOV of mob
        angle_mob_player = atan2(y_player - mob_y,x_player - mob_x)
        if self.orientation - pi/4 < angle_mob_player < self.orientation + math.pi/4:
            self.has_seen_player = True