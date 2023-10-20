import handler
import pygame
pygame.init()
print("\n")

# 10 pixels = 1 meter

# -- Window --
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption("Rocket Simulator")

# -- Colors --
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
DARK_GRAY = (80, 78, 81)
GREEN = (0, 255, 0)

# -- Fonts --
smallfont = pygame.font.SysFont('Corbel',35)
text = smallfont.render('quit' , True , BLACK)

# -- Main --
def main():
    run = True
    clock = pygame.time.Clock()

    # -- Objects --
  #  square_1 = handler.Square(0, 0, 200, 200, RED)
 #   square_2 = handler.Square(200, 0, 200, 200, BLUE)
#    square_3 = handler.Square(400, 0, 200, 200, RED)

    frame = 0
    while run:
        clock.tick(100)
        WIN.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                #if the mouse is clicked on the
                # button the game is terminated
                if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40:
                    pygame.quit()


        mouse = pygame.mouse.get_pos()

        bg = pygame.image.load("./prosjekter/tictactoe/media/grid.png")
        WIN.blit(bg, (0, 0)) #TODO: change size of image
        # drawing button on screen
        #square_1.draw(WIN)
        #square_2.draw(WIN)
        #square_3.draw(WIN)

        # if mouse is hovered on a button it
        # changes to lighter shade 
        if WIDTH/2 <= mouse[0] <= WIDTH/2+140 and HEIGHT/2 <= mouse[1] <= HEIGHT/2+40:
            pass
            #pygame.draw.rect(WIN,BLUE,[0,0,200,200])
            
        else:
            pygame.draw.rect(WIN,RED,[WIDTH/2,HEIGHT/2,140,40])
        
        # superimposing the text onto our button
        WIN.blit(text , (WIDTH/2+50,HEIGHT/2))
      
        pygame.display.update()
        frame += 1

    pygame.quit()

    
# -- Main --
if __name__ == "__main__":
    main()