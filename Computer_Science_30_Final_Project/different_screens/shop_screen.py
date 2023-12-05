import pygame
import sys

class ShopScene():
    def __init__(self):
        pass
    
    
def shop():
    pygame.init()

    # screen resolution
    res = (720, 720)

    # open the window
    screen = pygame.display.set_mode(res)

    # main color
    color = (0, 0, 0)

    # width of screen
    width = screen.get_width()

    # height of screen
    height = screen.get_height()

    # define line
    line_width = 3
    line_color = (165, 42, 42)

    # define font
    font = pygame.font.SysFont('Corbel', 25, bold=True)

    # render text
    shop_title = font.render("Dauvan's Country Development", True, (255, 140, 00))

    # line coordinates
    x1 = 1
    y1 = 720 -2
    x2 = width
    y2 = 720 -2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 

        #fill background
        screen.fill((60,26,60))

        # draw line
        pygame.draw.line(screen, line_color, (x1, y1), (x2, y2), line_width)

        # draw title text
        title_text_rect = shop_title.get_rect(center=(width/2, height/3))
        screen.blit(shop_title, title_text_rect.center)

        
        mouse = pygame.mouse.get_pos()

        # update display
        pygame.display.update()

shop()
