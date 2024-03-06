import sys
# INGEN pycache!!
sys.dont_write_bytecode = True

import pygame
from food import Food
from player import Player
from config import *
from random import randint

class Game:
    """Selve spill-klassen. """
    def __init__(self):
        # pygame setup
        sys.dont_write_bytecode = True
        pygame.init()
        pygame.font.init()

        # some game variables
        self.invulnerable = False
        self.invulnerable_clock = pygame.time.get_ticks()
        self.invulnerable_time = INVULNERABLE_TIME
        self.game_over = False

        # game setup
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("PacTroll")
        self.clock = pygame.time.Clock()
        self.points = 0

        # text setup
        self.font = pygame.font.SysFont("Comic Sans MS", 24)
        self.score_text = self.font.render(f"Score: {self.points}", True, WHITE) # AA on

        # Player (pactroll) setup
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
        while True: # Lag ny mat og sjekk om den kolliderer med noe på brettet, hvis ja, ødelegg og lag ny
            new_food = Food((randint(0, WIDTH - TILE_SIZE), randint(0, HEIGHT - TILE_SIZE)), (TILE_SIZE, TILE_SIZE), (self.food))
            if not pygame.sprite.spritecollide(new_food, self.obstacles, False) \
            and pygame.sprite.spritecollide(new_food, self.food, False): 
                break
            else: 
                new_food.kill()

            

    def kill_food(self, food: pygame.sprite.GroupSingle):
        food.add(self.obstacles)
        food.remove(self.food)
        food.image.fill(GREY)

    def collision_food(self):
        """Kollisjon med mat"""
        for food in self.food.sprites():
            if pygame.sprite.spritecollide(food, self.player, False):
                self.points += 1
                self.player.sprite.speed += 0.1
                self.invulnerable_time -= 0.01
                self.kill_food(food)
                self.spawn_food()
                self.start_invulnerable()

    def collision_obstacle(self):
        """Kollisjon med hindringer"""
        if self.invulnerable: return # If Invulnerable, don't check for collision

        for obstacle in self.obstacles.sprites():
            if pygame.sprite.spritecollide(obstacle, self.player, False):
                self.game_over = True

    def collision_wall(self):
        """Kollisjon med vegger"""
        if self.player.sprite.rect.x < 0 or self.player.sprite.rect.x > WIDTH - TILE_SIZE:
            self.game_over = True
        if self.player.sprite.rect.y < 0 or self.player.sprite.rect.y > HEIGHT - TILE_SIZE:
            self.game_over = True

    def start_invulnerable(self):
        """Start udødelighet"""
        self.invulnerable = True
        start_ticks=pygame.time.get_ticks()
        self.invulnerable_time = start_ticks

    def check_invulnerable(self):
        """Sjekk tid igjen på udødelighet"""
        start_ticks = self.invulnerable_clock
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        if seconds > self.invulnerable_time:
            self.invulnerable = False

    def update(self):
        self.player.update()
        self.collision_food()
        self.collision_obstacle()
        self.collision_wall()
        # unnecessary check if not invulnerable
        if self.invulnerable: 
            self.check_invulnerable()
        #print(self.points)

    def draw(self):
        self.win.fill(BLACK)
        self.obstacles.draw(self.win)
        self.food.draw(self.win)
        self.player.draw(self.win)

        #draw text based on game state
        if self.game_over:
            self.score_text = self.font.render(f"Game Over! Score: {self.points}", True, WHITE)
            self.win.blit(self.score_text, (WIDTH//2 - self.score_text.get_width()//2, HEIGHT//2 - self.score_text.get_height()//2))
        else:
            self.score_text = self.font.render(f"Score: {self.points}", True, WHITE)
            self.win.blit(self.score_text, (10, 10))

        pygame.display.update()

    def run(self):
        run = True
        while run:
            self.clock.tick(TICK_RATE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if self.game_over == False: 
                self.update()
            self.draw()