from storage import StorableWorld
from values import values, values_destination
from string import digits

def parse_map(data: str, skybox, floor):
    props = []
    pickables = []
    mobs = []
    players = []
    grid = []
    
    i = -1
    
    print(data.replace(" ", "0"))
    
    for y, line in enumerate(data.replace(" ", "0").split("\n")):
        grid.append([])
        i += 1
        for x, c in enumerate(line):
            if c in digits:
                grid[i].append(int(c))
            else:
                Class = values[c]
                
                destination = values_destination[Class]
                
                if destination == "props":
                    props.append((Class, (x*100+50, y*100+50)))
                elif destination == "pickables":
                    pickables.append((Class, (x*100+50, y*100+50)))
                elif destination == "mobs":
                    mobs.append((Class, (x*100+50, y*100+50)))
                elif destination == "players":
                    players.append((Class, (x*100+50, y*100+50)))
                
                grid[i].append(0)
                
    for line in grid:
        print(line)
    
    return StorableWorld(props=props,
                         pickables=pickables,
                         mobs=mobs,
                         players=players,
                         grid=grid,
                         skybox=skybox,
                         floor=floor
                         )
