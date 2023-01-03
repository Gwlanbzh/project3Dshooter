from game import Game

class Maze(Game):
    def is_game_over(self):
        curr_cell = (int(self.world.players[0].r.x)//100, int(self.world.players[0].r.y)//100)
        return any([curr_cell == exit for exit in self.world.exits])

if __name__ == "__main__":
    game = Maze("assets/maps/map_dest.bin")
    game.run()
