import pygame as pg
from config import *
from math import hypot
from random import choice
from os import listdir
from pygame import Vector2 as v2

class Sound():
    def __init__(self) -> None:
        # sounds are in list so random can be added
        debug_dry_fire_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/debug_no_ammo.mp3")
        ]
        
        debug_weapon_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/debug_ammo.mp3")
        ]
        
        dry_fire_sound = [ 
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/dryfire_pistol.mp3"),
        ]

        pistol_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/fiveseven-1.wav"),
        ]

        rifle_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/uzi_fire.mp3"),
        ]

        punch_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/punch.wav")
        ]

        shotgun_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "weapons/shotgun_fire.ogg"),
        ]

        superweapon_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + f"weapons/machgf{i}b.mp3") for i in range(1, 4)
        ]

        pickable_generic = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "pickables/generic.ogg")
        ]

        mine_sound = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "pickables/mine_exp.mp3")
        ]

        grunt_hurt = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + f"ennemies/grunt/pain{i}.ogg") for i in range(4)
        ]

        heavy_hurt = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + f"ennemies/heavy/pain{i}.ogg") for i in range(4)
        ]

        boss_hurt = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + f"ennemies/boss/pain{i}.ogg") for i in range(4)
        ]

        player_hurt = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + f"ennemies/player/pain{i}.ogg") for i in range(3)
        ]

        grunt_death = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + f"ennemies/grunt/death{i}.ogg") for i in range(3)
        ]

        heavy_death = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + f"ennemies/heavy/death{i}.ogg") for i in range(3)
        ]

        boss_death = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + f"ennemies/boss/death{i}.ogg") for i in range(3)
        ]

        ui_sound_button = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "menu/button.mp3")
        ]

        ui_sound_hover = [
            pg.mixer.Sound(Config.SOUNDS_FOLDER + "menu/hover.mp3")
        ]

        self.sound_ids = {
            "weapon" : debug_weapon_sound,
            "dry_weapon" : debug_dry_fire_sound,
            "dryfire" : dry_fire_sound,
            "pistol" : pistol_sound,
            "rifle" : rifle_sound,
            "punch" : punch_sound,
            "shotgun" : shotgun_sound,
            "superweapon" : superweapon_sound,
            "hover" : ui_sound_hover,
            "click" : ui_sound_button,

            "pickable": pickable_generic,
            "mine": mine_sound,

            "grunt_hurt": grunt_hurt,
            "heavy_hurt": heavy_hurt,
            "boss_hurt": boss_hurt,
            "player_hurt": player_hurt,

            "grunt_death": grunt_death,
            "heavy_death": heavy_death,
            "boss_death": boss_death,
            "player_death": player_hurt,
        }


        self.musics = listdir(Config.SOUNDS_FOLDER + "musics")
        self.end_music_time = -1
        self.current_music = choice(self.musics)
        self.musics.remove(self.current_music)
        pg.mixer.music.set_volume(.7)

        self.effect_volume = 1

        self.player_channel = pg.mixer.find_channel()
    

    def play_sound(self, id, player_pos=v2(0, 0), sound_pos=v2(0, 0), is_player=False):
        """
        play a sound in function of his position in the world
        more the sound is away from the position of the player, more the volume wille be low
        """
        if Config.NO_SOUND:
            return

        s = choice(self.sound_ids[id])
        
        if is_player:
            s.set_volume(1)
            self.player_channel.play(s)
            return
        
        hearing_sound_dist = WALL_WIDTH * 10
        x, y = player_pos - sound_pos
        dist_player_sound = hypot(x, y)

        volume = (hearing_sound_dist - dist_player_sound)/hearing_sound_dist
        volume *= self.effect_volume
        volume = 0 if volume < 0 else volume

        s.set_volume(volume)

        s.play()

    def update_music(self):
        """if the current music has stop playing, start a new one"""
        if Config.NO_SOUND:
            return

        if pg.mixer.music.get_pos() == -1:
            self.next_music()
    
    def pause_music(self):
        pg.mixer.music.pause()
    
    def resume_music(self):
        pg.mixer.music.unpause()

    def next_music(self):
        """stop playing the current music and play another. If there is only one music, this reset the music"""
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
        """turn music volume on"""
        self.set_music_volume(0)
    
    def turn_on_music(self):
        self.set_effect_volume(0.5)

    def set_effect_volume(self, vol):
        """change the volumes of the sound"""
        self.player_channel.set_volume(vol)
        if vol < 0 or vol > 1:
            self.effect_volume = 1
        else:
            self.effect_volume = vol
    
    def stop_music(self):
        """stop playing the current music"""
        pg.mixer.music.stop()
