import pygame

class Square:
    def __init__(self, x_0, y_0, x_1, y_1, color):
        self.x_0 = x_0
        self.y_0 = y_0
        self.x_1 = x_1
        self.y_1 = y_1
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win,self.color,[self.x_0,self.y_0,self.x_1,self.y_1])
