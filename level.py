from pydoc import describe
from tkinter.tix import TixSubWidget
import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        
        # level setup
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group() # sprites in this group will be diplayed, other won't
        self.active_sprites = pygame.sprite.Group() # sprites in this group will be updated, others will remain static
        self.collision_sprites = pygame.sprite.Group() # sprites in this group will collide with player

        self.setup_level()

    def setup_level(self):
        for row_index, row in enumerate(LEVEL_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                
                if col == 'X':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites])
                if col == 'P':
                    Player((x,y), [self.visible_sprites, self.active_sprites], self.collision_sprites)

    def run(self):
        self.active_sprites.update()
        self.visible_sprites.draw(self.display_surface)

if __name__ == '__main__':
    from main import main
    main()