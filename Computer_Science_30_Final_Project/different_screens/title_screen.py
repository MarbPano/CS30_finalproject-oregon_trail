import pygame
import sys
from time import sleep
from os import path
import window_creation as wc
import introduction_screen as intro

  
pygame.init()
img_dir = path.join(path.dirname(__file__), "images")
title_background = pygame.image.load(path.join(img_dir, "Title-f.png"))

# screen resolution
res = (720, 720)

# open the window
screen = pygame.display.set_mode(size=(res))#, flags=pygame.FULLSCREEN)

# font colour
text_colour = (255, 248, 220)
title_colour = (0, 100, 0)

# shades for button
border_colour = (80, 80, 80)
button_colour = (101, 67, 33)

# width of screen
width = screen.get_width()

# height of screen
height = screen.get_height()

# creating text and buttons
font_dir = path.join(path.dirname(__file__), "Fonts")
title_text = wc.Text('Woodrunners', width/2, height/3 - 150, (path.join(font_dir, 'ANDYB.TTF')), 125, title_colour, screen, bold=True)
start_button = wc.Button(width/2 - 100, height - 250, 225, 60, border_colour, button_colour, screen)
start_button_rect = start_button.rect
quit_button = wc.Button(width/2 - 100, height - 175, 225, 60, border_colour, button_colour, screen)
quit_button_rect = quit_button.rect

# mouse position
pos = pygame.mouse.get_pos()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):
                # Start the game logic here
                print("Game started!")
                sleep(2)
                intro.Family(screen, width, height)
            elif quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()      

    #fill background with the title_background
    screen.blit((title_background), (0,0))
    
    # draw the texts
    title_text.draw(screen)
    start_button.draw(screen)
    start_button.with_text('Start Game','Corbel', 35, text_colour, screen, bold=True)
    start_button.update()
    quit_button.draw(screen)
    quit_button.with_text('Quit Game','Corbel', 35, text_colour, screen, bold=True)
    quit_button.update()


    # update display
    pygame.display.flip()

