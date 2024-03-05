import pygame
from pactroll import Game
import sys

# No pycache!!
sys.dont_write_bytecode = True

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
