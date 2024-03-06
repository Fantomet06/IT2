import pygame

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

        if key[pygame.K_w] or key[pygame.K_UP]:
            self.vel = (0, -self.speed)
        
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            self.vel = (0, self.speed)
        
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.vel = (-self.speed, 0)
        
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.vel = (self.speed, 0)

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.rect.topleft = self.pos
