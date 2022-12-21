from game import Game

class Maze(Game):
    def is_game_over(self):
        res = any([(int(self.world.players[0].r.x)//100, int(self.world.players[0].r.y)//100) == exit for exit in self.world.exits])
        print(res)
        return res

if __name__ == "__main__":
    game = Maze("assets/maps/map_dest.bin")
    game.run()
