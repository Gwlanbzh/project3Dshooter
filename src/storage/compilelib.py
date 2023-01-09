from storage.storage import *
from storage.values import *
from string import digits

def create_world(data: str, skybox, floor, texture_set, map_scale):
    """
    Parses a string to extract the map grid and
    the props, pickables, mobs, player spawns, and exits located in the map,
    then creates a StorableWorld that can be written to a file.
    Uses the values and associations in values.py.
    """
    props = []
    pickables = []
    mobs = []
    players = []
    exits = []
    grid = []
    
    i = -1
    
    for y, line in enumerate(data.split("\n")):
        grid.append([])
        i += 1
        for x, c in enumerate(line):
            if c == 0:
                # special case for the 10th texture
                grid[i].append(10)
            elif c in digits:
                # walls
                grid[i].append(int(c))
            else:
                if c == "E":
                    # exits
                    exits.append((x, y))
                elif c != " ":
                    # we have a body here.
                    Class = values[c]
                    
                    destination = values_destination[Class]
                    
                    if destination == "props":
                        props.append((Class, (map_scale * (x+.5), map_scale * (y+.5))))
                    elif destination == "pickables":
                        pickables.append((Class, (map_scale * (x+.5), map_scale * (y+.5))))
                    elif destination == "mobs":
                        mobs.append((Class, (map_scale * (x+.5), map_scale * (y+.5))))
                    elif destination == "players":
                        players.append((Class, (map_scale * (x+.5), map_scale * (y+.5))))
                
                grid[i].append(0)
    
    return StorableWorld(props, pickables, mobs, players, exits, grid, skybox, floor, texture_set, map_scale)
