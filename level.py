import pygame
from settings import *

class Level:
    def __init__(self):
        
        # level setup
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group() # sprites in this group will be diplayed, other won't
        self.active_sprites = pygame.sprite.Group() # sprites in this group will be updated, others will remain static
        self.collision_sprites = pygame.sprite.Group() # sprites in this group will collide with player

    def run(self):
        pass