from game import Game

class Maze(Game):
    def is_game_over(self):
        curr_cell = (int(self.world.players[0].r.x)//100, int(self.world.players[0].r.y)//100)
        if any([curr_cell == exit for exit in self.world.exits]):
            return "victory"
        if self.world.players[0].health == 0:
            return "defeat"
        return ""

class Boss_level(Game):
    def is_game_over(self):
        if all([mob.health == 0 for mob in self.world.mobs]):
            return "victory"
        if self.world.players[0].health == 0:
            return "defeat"
        return ""

if __name__ == "__main__":
    game = Maze("src/assets/maps/map_dest.bin", True)
    game.run()
