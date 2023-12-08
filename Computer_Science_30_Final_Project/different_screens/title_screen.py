import pygame
import sys
from time import sleep
import shop_screen as ss
import window_creation as wc

  
pygame.init()

title_background = pygame.image.load('different_screens\images\Title-f.png')

# screen resolution
res = (720, 720)

# open the window
screen = pygame.display.set_mode(size=(res))#, flags=pygame.FULLSCREEN)

# small_font colour
colour = (150, 75, 0)

# shades for button
colour_light = (232, 204, 149) #(245, 245, 220) for lighter
colour_dark = (159, 140, 118)

# width of screen
width = screen.get_width()

# height of screen
height = screen.get_height()

title_text = wc.Text('Woodrunners', width/2, height/3 - 150, 'different_screens\Fonts\ANDYB.TTF', 125, colour, screen, bold=True)

start_button = wc.Button(width/2 - 100, height - 250, 225, 60, colour_light, colour_dark, screen)
start_button_rect = start_button.get_rect_b()
quit_button = wc.Button(width/2 - 100, height - 175, 225, 60, colour_light, colour_dark, screen)
quit_button_rect = quit_button.get_rect_b()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):
                # Start the game logic here
                print("Game started!")
                sleep(2)
                ss.shop(screen, width, height)
            elif quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
            # a toggle full screen button at the bottom right
            elif width - 50 <= event.pos[0] <= width and height - 50 <= event.pos[1] <= height:
                screen = pygame.display.toggle_fullscreen()

    #fill background with the title_background
    screen.blit(pygame.image.load('different_screens\images\Title-f.png'), (0,0))
    
    # draw the texts
    title_text.draw(screen)
    start_button.with_text('Start Game','Corbel', 35, colour, screen, bold=True)
    quit_button.with_text('Quit Game','Corbel', 35, colour, screen, bold=True)

    # mouse position
    mouse = pygame.mouse.get_pos()

    # update display
    pygame.display.update()

