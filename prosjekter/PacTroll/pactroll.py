import sys
import pygame
from objects import Food
from player import Player
from config import *
from random import randint
import sys

# No pycache!!
sys.dont_write_bytecode = True


class Game:
    """Selve spill-klassen. """
    def __init__(self):
        # pygame setup
        pygame.init()
        pygame.font.init()

        self.invulnerable = False
        self.invulnerable_time = pygame.time.get_ticks()

        # game setup
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("PacTroll")
        self.clock = pygame.time.Clock()

        # text setup
        self.font = pygame.font.SysFont("calibri", 24)
        self.test_text = self.font.render("Score: ", True, WHITE)

        self.points = 0

        # PacTroll setup
        self.player = pygame.sprite.GroupSingle()
        Player(self.player)

        # food setup
        self.food = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()

        # initial spawn
        self.spawn_food()
        self.spawn_food()
        self.spawn_food()

    def spawn_food(self):
        food_coords = [(sprite.rect.x, sprite.rect.y) for sprite in self.food.sprites()]
        while True:
            new_coords = (randint(0, WIDTH - TILE_SIZE), randint(0, HEIGHT - TILE_SIZE))
            if new_coords not in food_coords: break
            
        Food((randint(0, WIDTH - TILE_SIZE), randint(0, HEIGHT - TILE_SIZE)), (TILE_SIZE, TILE_SIZE), (self.food))

    def kill_food(self, food: pygame.sprite.GroupSingle):
        food.add(self.obstacles)
        food.remove(self.food)
        food.image.fill(GREY)

    def collision_food(self):
        for food in self.food.sprites():
            if pygame.sprite.spritecollide(food, self.player, False):
                self.points += 1
                self.kill_food(food)
                self.spawn_food()
                self.start_invulnerable()

    def collision_obstacle(self):
        if self.invulnerable: return # If Invulnerable, don't check for collision

        for obstacle in self.obstacles.sprites():
            if pygame.sprite.spritecollide(obstacle, self.player, False):
                pygame.quit()

    def start_invulnerable(self):
        """Start udødelighet"""
        self.invulnerable = True
        start_ticks=pygame.time.get_ticks()
        self.invulnerable_time = start_ticks

    def check_invulnerable(self):
        """Sjekk tid igjen på udødelighet"""
        start_ticks = self.invulnerable_time
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        if seconds > INVULNERABLE_TIME:
            self.invulnerable = False

    def update(self):
        self.player.update()
        self.collision_food()
        self.collision_obstacle()
        #print(self.points)

    def draw(self):
        self.win.fill(BLACK)
        self.obstacles.draw(self.win)
        self.food.draw(self.win)
        self.player.draw(self.win)
        # unnecessary check if not invulnerable
        if self.invulnerable: 
            self.check_invulnerable()
        pygame.display.update()

    def run(self):
        run = True
        while run:
            self.clock.tick(TICK_RATE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.update()
            self.draw()