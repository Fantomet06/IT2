import pygame
import sys

sys.dont_write_bytecode = True

# --- COLORS --- #
BLACK = (0, 0, 0) 

class Game:

    def __init__(self) -> None:
        self.spiller = "X"
        self.mat = []
