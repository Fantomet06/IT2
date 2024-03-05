import pygame
import sys

# No pycache!!
sys.dont_write_bytecode = True

class Player(pygame.sprite.Sprite):
    def __init__(self, spriteGroup) -> None:
        self.pos = [300, 300]
        self.speed = 2
        self.vel = (0, 0)
        super().__init__(spriteGroup)

        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=self.pos)
        #self.rect = pygame.Rect(self.pos[0], self.pos[1], 30, 30)

    def update(self):
        key = pygame.key.get_pressed()
        movement = {pygame.K_w: (0, -self.speed), pygame.K_s: (0, self.speed), pygame.K_a: (-self.speed, 0), pygame.K_d: (self.speed, 0)}
        for k in movement:
            if key[k]: 
                self.vel = movement[k]

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.rect.topleft = self.pos
