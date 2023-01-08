import pygame as pg
from config import *
from math import hypot
from random import choice
from os import listdir
from pygame import Vector2 as v2

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
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/uzi_fire.mp3"),
        ]

        self.punch_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/punch.wav")
        ]

        self.shotgun_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/shotgun_fire.ogg"),
        ]

        self.superweapon_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/superweapon_sound.mp3")
        ]

        self.ui_sound_button = [ pg.mixer.Sound(Config.SOUNDS_FOLDER + "menu/button.mp3") ]
        self.ui_sound_hover = [ pg.mixer.Sound(Config.SOUNDS_FOLDER + "menu/hover.mp3") ]

        self.pickable_generic = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "pickables/generic.ogg")
        ]

        self.mine_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "pickables/mine_exp.mp3")
        ]

        self.grunt_hurt = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + f"ennemies/grunt/pain{i}.ogg") for i in range(4)
        ]

        self.heavy_hurt = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + f"ennemies/heavy/pain{i}.ogg") for i in range(4)
        ]

        self.boss_hurt = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + f"ennemies/boss/pain{i}.ogg") for i in range(4)
        ]

        self.player_hurt = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + f"ennemies/player/pain{i}.ogg") for i in range(3)
        ]

        self.grunt_death = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + f"ennemies/grunt/death{i}.ogg") for i in range(3)
        ]

        self.heavy_death = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + f"ennemies/heavy/death{i}.ogg") for i in range(3)
        ]

        self.boss_death = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + f"ennemies/boss/death{i}.ogg") for i in range(3)
        ]

        self.player_death = self.player_hurt


        self.sound_ids = {
            "weapon" : self.debug_weapon_sound,
            "dry_weapon" : self.debug_dry_fire_sound,
            "dryfire" : self.dry_fire_sound,
            "pistol" : self.pistol_sound,
            "rifle" : self.rifle_sound,
            "punch" : self.punch_sound,
            "shotgun" : self.shotgun_sound,
            "superweapon" : self.superweapon_sound,
            "hover" : self.ui_sound_hover,
            "click" : self.ui_sound_button,

            "pickable": self.pickable_generic,
            "mine": self.mine_sound,

            "grunt_hurt": self.grunt_hurt,
            "heavy_hurt": self.heavy_hurt,
            "boss_hurt": self.boss_hurt,
            "player_hurt": self.player_hurt,

            "grunt_death": self.grunt_death,
            "heavy_death": self.heavy_death,
            "boss_death": self.boss_death,
            "player_death": self.player_death,
        }

        self.musics = listdir(Config.SOUNDS_FOLDER + "musics")
        self.end_music_time = -1
        self.current_music = choice(self.musics)
        self.musics.remove(self.current_music)
        self.effect_volume = 1
    

    def play_sound(self, id, player_pos = v2(0,0), sound_pos = v2(0,0)):
        hearing_sound_dist = WALL_WIDTH * 10
        x, y = player_pos - sound_pos
        dist_player_sound = hypot(x, y)

        volume = (hearing_sound_dist - dist_player_sound)/hearing_sound_dist
        volume *= self.effect_volume
        volume = 0 if volume < 0 else volume

        s = choice(self.sound_ids[id])
        s.set_volume(volume)

        s.play()

    def update_music(self):
        if pg.mixer.music.get_pos() == -1:
            self.next_music()
    
    def pause_music(self):
        pg.mixer.music.pause()
    
    def resume_music(self):
        pg.mixer.music.unpause()

    def next_music(self):
        old = self.current_music
        try:
            self.current_music = choice(self.musics)
            self.musics.remove(self.current_music)
            self.musics.append(old)
        except IndexError: # only one music in the folder
            pass
        
        music_path = Config.SOUNDS_FOLDER + "musics/" + self.current_music
        pg.mixer.music.load(music_path)
        pg.mixer.music.play()

    def set_music_volume(self, vol):
        """vol between 0 and 1, other values mean 1 for pygame"""
        pg.mixer.music.set_volume(vol)
    
    def shut_music(self):
        self.set_music_volume(0)

    def set_effect_volume(self, vol):
        if vol < 0 or vol > 1:
            self.effect_volume = 1
        else:
            self.effect_volume = vol
