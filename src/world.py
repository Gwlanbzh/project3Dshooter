from config import *
from map import *
from bodys import *

class World:
    """
    World containing a map, props, mobs and players evolving in it,
    and updating them.
    """ 
    def __init__(self,game):
        """
        Spawns a Body.
         # For now Body are purple
         #         Mob are red
         #         Player are blue
         # Creature have a tray for orientation
        
        Input:
            game : Game
        
        Outputs:
            World
        """
        self.map = Map(game)

        

    def init_bodys(self,game):
        self.props = [
            Light(game,(450,150)),
            Light(game,(950,450)),
            Tree(game,(550,550)),
            Tree(game,(850,650))
            ]
        
        self.pickables = [
            HealthPack25(game, (150, 250)),
            AmmoPack20(game, (150, 350))
            ]
        
        self.mobs = [
            #Mob(game,(350,150)),
            Mob(game,(350,450)),
            Mob(game,(550,650)),
            Mob(game,(750,450))
            ]
        
        self.players = [
            Player(game,(150,150))
            ]


    def update (self, game):
        """
        call upadate for every Body(or more) in the world
        and
  
        Input:
            game : Game
        
        Outputs:
            <none>
        """
        self.players[0].update()

        self.mobs_position = [mob.map_pos for mob in self.mobs]
        for mob in self.mobs:
            mob.update()
        
        for pickable in self.pickables:
            disappears = pickable.update()
            if disappears:
                self.pickables.remove(pickable)
  
    def draw2d(self,game):
        """
        Draw world on a 2d plane
  
        """
        game.window.fill('grey')
        
        for prop in self.props:
           prop.draw(game)
        self.map.draw(game)
        for mob in self.mobs:
            mob.draw(game)
        self.players[0].draw(game)
        pass