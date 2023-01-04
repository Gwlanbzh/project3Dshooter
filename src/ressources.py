from render import load_texture_set, load_skybox, load_static_sprites, load_animated_sprites, mob_models_names

class Ressources():
    """
    This class is used to centralize the storage of the assets in RAM.
    It is called by the World class, which stores its instance into a member.
    No better way was found to so that.
    """
    def __init__(self, texture_set, skybox, floor):
        
        self.textures = load_texture_set(texture_set)
        self.textures_units_per_strip = {t:100/len(self.textures[t]) for t in self.textures}
        
        self.skybox_data = load_skybox(skybox)
        self.floor = floor
        
        self.static_sprites = load_static_sprites()
        
        self.animated_sprites = dict()
        for key in mob_models_names:
            self.animated_sprites[key] = load_animated_sprites(key + "/walking")

