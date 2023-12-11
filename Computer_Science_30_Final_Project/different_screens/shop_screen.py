import pygame
import window_creation as wc

# rectangle class


def shop(screen, width, height):
    # main colour

    shop_background = pygame.image.load('different_screens\images\Store-f.png')

    # define line
    line_width = 6
    line_colour = (165, 42, 42)

    # define lines
    line1 = wc.Line(1, height - 705, width, height - 705, line_width, line_colour, screen)
    line2 = wc.Line(1, height - 650, width, height - 650, line_width, line_colour, screen)
    

    # define font
    font = pygame.font.SysFont('Corbel', 40, bold=True)

    # render text
    shop_title = font.render("Dauvin's Country Development", True, (255, 140, 00))


    # line coordinates
#    x1 = 1
#    y1 = height - 650
#    x2 = width
#    y2 = height - 650

    # rectangle coordinates
    rect_width = (width // 2) *1.5
    rect_height = ((height // 2) * 1.35) - 50
    rect_x = (width - rect_width) // 2
    rect_y = ((height - rect_height) // 2) - 35
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # fill background
        screen.blit(pygame.image.load('different_screens\images\Store-f.png'), (0,0))

        # draw line
        #pygame.draw.line(screen, line_colour, (x1, y1), (x2, y2), line_width)
        line1.draw(screen)
        line2.draw(screen)

        # draw title text
        title_text_rect = shop_title.get_rect(center=(width/2, height/3 - 195))
        screen.blit(shop_title, title_text_rect.topleft)

        # draw rectangle with semi-transparancy black
        pygame.draw.rect(screen, (0, 0, 0, 128), (rect_x, rect_y, rect_width, rect_height))
       
        # update display
        pygame.display.update()

