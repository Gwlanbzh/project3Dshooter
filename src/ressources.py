from render import load_texture_set, load_skybox, static_sprites

class Ressources():
    def __init__(self, texture_set, skybox):
        
        self.textures = load_texture_set(texture_set)
        self.textures_units_per_strip = {t:100/len(self.textures[t]) for t in self.textures}
        
        self.skybox_data = load_skybox(skybox)
        
        self.static_sprites = static_sprites

