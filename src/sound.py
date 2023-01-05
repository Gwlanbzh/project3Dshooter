import pygame as pg
from config import *
from math import hypot
from random import choice

class Sound():
    def __init__(self) -> None:
        self.debug_dry_fire_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/debug_no_ammo.mp3")
        ]
        
        self.debug_weapon_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/debug_ammo.mp3")
        ]
        
        self.dry_fire_sound = [ 
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/dryfire_pistol.mp3"),
        ]

        self.pistol_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/fire_pistol.mp3")
        ]

        self.rifle_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/rifle-firing.mp3"),
        ]

        self.punch_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/punch.wav")
        ]

        self.shotgun_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/fire_shotgun.mp3"),
        ]

        self.superweapon_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/superweapon_sound.mp3")
        ]

        self.sound_ids = {
            "weapon" : self.debug_weapon_sound,
            "dry_weapon" : self.debug_dry_fire_sound,
            "dryfire" : self.dry_fire_sound,
            "pistol" : self.pistol_sound,
            "rifle" : self.rifle_sound,
            "punch" : self.punch_sound,
            "shotgun" : self.shotgun_sound,
            "superweapon" : self.superweapon_sound,
        }

    def play_sound(self, id, player_pos, sound_pos):
        hearing_sound_dist = WALL_WIDTH * 15
        x, y = player_pos - sound_pos
        dist_player_sound = hypot(x, y)

        volume = (hearing_sound_dist - dist_player_sound)/hearing_sound_dist
        volume = 0 if volume < 0 else volume

        s = choice(self.sound_ids[id])
        s.set_volume(volume)

        s.play()