#!/bin/sh
./compile.py ./assets/maps/sources/level_1.txt ./assets/maps/level_1.bin --skybox=sky.png --floor=81,77,70
./compile.py ./assets/maps/sources/level_2.txt ./assets/maps/level_2.bin --skybox=sky3.png --floor=71,67,61
./compile.py ./assets/maps/sources/level_3.txt ./assets/maps/level_3.bin --skybox=sunset.png --floor=71,67,61
./compile.py ./assets/maps/sources/boss.txt ./assets/maps/boss.bin --skybox=space-half1.png --floor=55,52,46
