import pygame as pg
from render.textures import load_texture


spritesdir = "assets/sprites/"

static_sprites_names = ["default.png",
                        "light.png",
                        "tree.png",
                        ]

static_sprites = {sprite:load_texture(spritesdir+sprite) for sprite in static_sprites_names}
