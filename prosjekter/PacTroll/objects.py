import pygame
import sys

# No pycache!!
sys.dont_write_bytecode = True

class Food(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, size: tuple, spriteGroup) -> None:
        self.pos = pos
        self.size = size
        super().__init__(spriteGroup)

        self.image = pygame.Surface(size)
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(topleft=pos)
        #self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def draw(self, win):
        pygame.draw.rect(win, (255,255,0), (self.pos[0], self.pos[1], self.size[0], self.size[1]))

class Obstacle(Food):
    def __init__(self) -> None:
        super().__init__()