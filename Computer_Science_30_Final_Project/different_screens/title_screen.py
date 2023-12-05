import pygame
import sys
from time import sleep
#import shop_screen as ss

pygame.init()

# screen resolution
res = (720, 720)

# open the window
screen = pygame.display.set_mode(res)

# marroon background for SHS acquiantancy 
color = (165, 42, 42)

# shades for button
color_light = (170,170,170)
color_dark = (100,100,100)

# width of screen
width = screen.get_width()

# height of screen
height = screen.get_height()

# define font
title_font = pygame.font.SysFont('Corbel', 70, bold=True)
smallfont = pygame.font.SysFont('Corbel',35)


# render text
title_text = title_font.render('Oregon Trail', True, (255, 140, 00))
start_text = smallfont.render('Start Game', True, color)
quit_text = smallfont.render('Quit Game', True, color)
fullscreen_text = smallfont.render('Toggle Fullscreen', True, color)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/2 - 100 <= event.pos[0] <= width/2 + 100 and height/2 - 50 <= event.pos[1] <= height/2:
                # Start the game logic here
                print("Game started!")
                sleep(2)
                #ss.shop()
            elif width/2 - 100 <= event.pos[0] <= width/2 + 100 and height/2 <= event.pos[1] <= height/2 + 50:
                pygame.quit()
                sys.exit()
            # a toggle full screen button at the bottom right
            elif width - 50 <= event.pos[0] <= width and height - 50 <= event.pos[1] <= height:
                screen = pygame.display.toggle_fullscreen()

    #fill background
    screen.fill((60,26,60))

 # Draw the title text
    title_text_rect = title_text.get_rect(center=(width/2, height/3))
    screen.blit(title_text, title_text_rect.topleft)

 # Draw the start game button
    start_button_rect = pygame.Rect(width/2 - 100, height/2 - 50, 200, 50)
    pygame.draw.rect(screen, color_light, start_button_rect)
    pygame.draw.rect(screen, color_dark, start_button_rect, 3)
    start_text_rect = start_text.get_rect(center=start_button_rect.center)
    screen.blit(start_text, start_text_rect.topleft)

  # Draw the quit button
    quit_button_rect = pygame.Rect(width/2 - 100, height/2, 200, 50)
    pygame.draw.rect(screen, color_light, quit_button_rect)
    pygame.draw.rect(screen, color_dark, quit_button_rect, 3)
    quit_text_rect = quit_text.get_rect(center=quit_button_rect.center)
    screen.blit(quit_text, quit_text_rect.topleft)

    # fullscreen button
    fullscreen_button_rect = pygame.Rect(width - 50, height - 50, 50, 50)
    pygame.draw.rect(screen, color_light, fullscreen_button_rect)
    pygame.draw.rect(screen, color_dark, fullscreen_button_rect, 3)
    fullscreen_text_rect = fullscreen_text.get_rect(center=fullscreen_button_rect.center)
    screen.blit(fullscreen_text, fullscreen_text_rect.topleft)

    # mouse position
    mouse = pygame.mouse.get_pos()

    # update display
    pygame.display.update()

