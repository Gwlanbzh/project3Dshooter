from config import *
from map import *
from bodys import *
from storage import *
from render import load_skybox
from ressources import *

class World:
    """
    World containing a map, props, mobs and players evolving in it,
    and updating them.
    """ 
    def __init__(self, game, map_file):
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
        map_data = load(map_file)

        self.props = [Class(game, pos) for Class, pos in map_data.props]
        self.pickables = [Class(game, pos) for Class, pos in map_data.pickables]
        self.mobs = [Class(game, pos) for Class, pos in map_data.mobs]
        self.players = [Class(game, pos) for Class, pos in map_data.players]
        
        self.exits = map_data.exits
        self.map = Map(game, map_data.grid)
        self.map_scale = map_data.map_scale
        
        self.ressources = Ressources(map_data.texture_set, map_data.skybox, map_data.floor)
    
    def update(self, game):
        """
        call upadate for every Body(or more) in the world
        and
  
        Input:
            game : Game
        
        Outputs:
            <none>
        """
        self.players[0].update()
        self.mobs_position = [mob.map_pos for mob in self.mobs if not mob.is_dead()]
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
        for pickable in self.pickables:
            pickable.draw(game)
        
        self.players[0].draw(game)