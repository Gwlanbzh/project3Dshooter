from game import Game

class Maze(Game):
    def __init__(self, map_file, draw2d, window, delta_time, clock, sound):
        super().__init__(map_file, draw2d, window, delta_time, clock, sound)
        self.description = "Reach the exit without dying."
    
    def is_game_over(self):
        curr_cell = (int(self.world.players[0].r.x)//100, int(self.world.players[0].r.y)//100)
        if any([curr_cell == exit for exit in self.world.exits]):
            print("victory")
            return "victory"
        if self.world.players[0].health == 0:
            print("defeat")
            return "defeat"
        return ""

class Boss_level(Game):
    def __init__(self, map_file, draw2d, window, delta_time, clock, sound):
        super().__init__(map_file, draw2d, window, delta_time, clock, sound)
        self.description = "Kill all the ennemies in the map. Beware the boss."
    
    def is_game_over(self):
        if all([mob.health == 0 for mob in self.world.mobs]):
            return "victory"
        if self.world.players[0].health == 0:
            return "defeat"
        return ""

if __name__ == "__main__":
    game = Maze("src/assets/maps/map_dest.bin", True)
    game.run()
