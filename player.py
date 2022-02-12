from typing import List, Tuple
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos: Tuple, groups: List[pygame.sprite.Group]):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE//2, TILE_SIZE))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft = pos)

        # player movement
        self.direction = pygame.math.Vector2()
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = 16
    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        
        if keys[pygame.K_SPACE]:
            self.direction.y = -self.jump_speed
    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def update(self):
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.apply_gravity()

if __name__ == '__main__':
    from main import main
    main()