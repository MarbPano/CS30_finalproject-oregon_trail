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

# define font
title_font = pygame.font.Font('different_screens\Fonts\ANDYB.TTF', 125)
smallfont = pygame.font.SysFont('Corbel',35, bold=True)


# render text
#title_text = title_font.render('Oregon Trail', True, colour)
#start_text = smallfont.render('Start Game', True, colour)
#quit_text = smallfont.render('Quit Game', True, colour)
#fullscreen_text = smallfont.render('Toggle Fullscreen', True, colour)

#this batch of code I need help with
title_text = wc.Text('Courier de Bois', width/2, height/3 - 150, 'different_screens\Fonts\ANDYB.TTF', 125, colour, screen, bold=True)
title_text.draw(self, screen)
start_text = wc.Button(width/2 - 100, height - 250, 225, 60, colour_light, colour_dark, screen)
start_text.with_text('Start Game','Corbel', 35, colour)
quit_text = wc.Button(width/2 - 100, height - 175, 225, 60, colour_light, colour_dark, screen)
quit_text.with_text('Quit Game','Corbel', 35, colour)


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
    

 # Draw the title text
#    title_text_rect = title_text.get_rect(center=(width/2, height/3 - 150))
#    screen.blit(title_text, title_text_rect.topleft)

 # Draw the start game button
#    start_button_rect = pygame.Rect(width/2 - 100, height - 250, 225, 60)
#    pygame.draw.rect(screen, colour_light, start_button_rect)
#    pygame.draw.rect(screen, colour_dark, start_button_rect, 3)
#    start_text_rect = start_text.get_rect(center=start_button_rect.center)
#    screen.blit(start_text, start_text_rect.topleft)

  # Draw the quit button
#    quit_button_rect = pygame.Rect(width/2 - 100, height - 175, 225, 60)
#    pygame.draw.rect(screen, colour_light, quit_button_rect)
#    pygame.draw.rect(screen, colour_dark, quit_button_rect, 3)
#    quit_text_rect = quit_text.get_rect(center=quit_button_rect.center)
#    screen.blit(quit_text, quit_text_rect.topleft)

    # a toggle full screen button at the bottom right  
#    fullscreen_button_rect = pygame.Rect(width - 50, height - 50, 50, 50)
#    pygame.draw.rect(screen, colour_light, fullscreen_button_rect)
#    pygame.draw.rect(screen, colour_dark, fullscreen_button_rect, 3)
#    fullscreen_text_rect = fullscreen_text.get_rect(center=fullscreen_button_rect.center)
#    screen.blit(fullscreen_text, fullscreen_text_rect.topleft)


    # mouse position
    mouse = pygame.mouse.get_pos()

    # update display
    pygame.display.update()

