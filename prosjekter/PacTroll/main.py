import sys
# INGEN pycache!!
sys.dont_write_bytecode = True
import pygame
from pactroll import Game

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
