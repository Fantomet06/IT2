import pygame
import random

class Mat:
    def __init__(self) -> None:
        self.pos = (random.randint(30,270),random.randint(30,270))

    def draw(self, win):
        pygame.draw.rect(win, (255,255,0), (self.pos[0], self.pos[1], 20, 20))

class Hinder(Mat):
    def __init__(self) -> None:
        super().__init__()