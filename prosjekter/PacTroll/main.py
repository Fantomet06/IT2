import pygame
import objects
import player
import time

background_colour = (0, 0, 0)
win = pygame.display.set_mode((600, 600))

pygame.display.set_caption('PacTroll')

running = True

mat = objects.Mat()
player = player.Player()
clock = pygame.time.Clock()
clock.tick(60)

while running:
    win.fill(background_colour)
    mat.draw(win)
    player.update_pos()
    player.draw(win)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            player.move(pygame.key.get_pressed())

    pygame.display.update()
    time.sleep(0.01)
