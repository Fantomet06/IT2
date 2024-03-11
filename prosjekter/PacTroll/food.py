import pygame

class Food(pygame.sprite.Sprite):
    """Mat som spilleren skal spise"""
    def __init__(self, pos: tuple, size: tuple, spriteGroup) -> None:
        self.pos = pos
        self.size = size
        super().__init__(spriteGroup)

        self.image = pygame.Surface(size)
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(topleft=pos)