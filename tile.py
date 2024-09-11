from typing import List, Tuple
import pygame
from settings import TILE_SIZE, TILE_COLOR


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: Tuple, groups: List[pygame.sprite.Group]):
        super().__init__(groups)  # type:ignore
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(TILE_COLOR)
        self.rect = self.image.get_rect(topleft=pos)
