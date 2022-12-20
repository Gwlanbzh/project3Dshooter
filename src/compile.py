from sys import argv
from bodys import *
from storage import StorableWorld
from compilelib import parse_map


# Arguments parsing
skybox_path = "sky.png"
floor_color = (70, 70, 70)
texture_set = "default"
map_scale = 100

pargc = 0

for arg in argv[1:]:
    # options
    if arg.startswith("-"):
        if arg.startswith("--skybox="):
            if len(arg.split("=")) > 2:
                raise ValueError
            else:
                skybox_path = arg.split("=")[1]
                
        elif arg.startswith("--floor="):
            if len(arg.split("=")) != 2:
                raise ValueError
            else:
                color = arg.split("=")[1]
                if len(color.split(",")) != 3:
                    raise ValueError
                else:
                    floor_color = tuple([int(i) for i in color.split(",")])
        elif arg.startswith("--texture-set="):
            if len(arg.split("=")) != 2:
                raise ValueError
            else:
                texture_set = arg.split("=")[1]
        elif arg.startswith("--scale="):
            if len(arg.split("=")) != 2:
                raise ValueError
            else:
                map_scale = int(arg.split("=")[1])
        
        else:
            raise ValueError(f"invalid option: {arg}")
    
    # positional args
    else:
        pargc += 1
        if pargc == 1:
            src = arg
        elif pargc == 2:
            dst = arg
        else:
            raise ValueError("too many arguments.")
            
if pargc < 2:
    raise ValueError("too few arguments.")

# Parsing

with open(src) as f:
    map_data = f.read()

compiled = parse_map(map_data, skybox_path, floor_color, texture_set, map_scale)

compiled.write(dst)
