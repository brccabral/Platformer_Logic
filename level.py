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
        self.visible_sprites = CameraGroup() # sprites in this group will be diplayed, other won't
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
                    self.player = Player((x,y), [self.visible_sprites, self.active_sprites], self.collision_sprites)

    def run(self):
        self.active_sprites.update()
        self.visible_sprites.custom_draw(self.player)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(100, 300)

        # center camera setup
        # camera follows Player always
        # Player always on the center

        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
    
    def custom_draw(self, player: Player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

if __name__ == '__main__':
    from main import main
    main()