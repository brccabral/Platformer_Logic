from typing import List, Tuple
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos: Tuple, groups: List[pygame.sprite.Group], collisions_sprites: pygame.sprite.Group):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE//2, TILE_SIZE))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft = pos)

        # player movement
        self.direction = pygame.math.Vector2()
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = 16
        self.collisions_sprites = collisions_sprites
        self.on_floor = False
    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        
        if keys[pygame.K_SPACE] and self.on_floor:
            self.direction.y = -self.jump_speed
    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def horizontal_collisions(self):
        self.rect.x += self.direction.x * self.speed
        for sprite in self.collisions_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left

    def vertical_collisions(self):
        for sprite in self.collisions_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_floor = True
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
        if self.on_floor and self.direction.y != 0:
            self.on_floor = False

    def update(self):
        self.input()
        self.horizontal_collisions()
        self.apply_gravity()
        self.vertical_collisions()

if __name__ == '__main__':
    from main import main
    main()