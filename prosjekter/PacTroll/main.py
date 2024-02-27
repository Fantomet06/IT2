import pygame
import objects

background_colour = (0, 0, 0)
win = pygame.display.set_mode((300, 300))

pygame.display.set_caption('PacTroll')

running = True

mat = objects.Mat()
clock = pygame.time.Clock()
clock.tick(100)

while running:
    win.fill(background_colour)
    mat.draw(win)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
