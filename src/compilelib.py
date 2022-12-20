from storage import StorableWorld
from values import values, values_destination
from string import digits

def parse_map(data: str, skybox, floor, texture_set, map_scale):
    props = []
    pickables = []
    mobs = []
    players = []
    grid = []
    
    i = -1
    
    for y, line in enumerate(data.split("\n")):
        grid.append([])
        i += 1
        for x, c in enumerate(line):
            if c == 0:  # special case for the 10th texture
                grid[i].append(10)
            elif c in digits:
                grid[i].append(int(c))
            else:
                if c != " ":
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
    
    return StorableWorld(props, pickables, mobs, players, grid, skybox, floor, texture_set, map_scale)
