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
        self.props = [Body(game,(350,150)),
                      Body(game,(950,450)),
                      Body(game,(550,550)),
                      Body(game,(850,650))]
        self.mobs = [Mob(game,(450,150)),
                     Mob(game,(450,450)),
                     Mob(game,(550,650)),
                     Mob(game,(750,450))]
        self.players = [Player(game,(150,150))]
        self.map = Map(game)
  
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
        for mob in self.mobs:
            mob.update()
            pass
  
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