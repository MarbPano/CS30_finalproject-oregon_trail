import pygame
import window_creation as wc
#import menu_bar as mb
import shop_screen as ss
import math as m
from os import path

pygame.init()

def main_screen(screen, width , height, screen_x, screen_y):
    #make background green
    GREEN = (0, 255, 0)  # Define the color green

    clock = pygame.time.Clock()
    FPS = 60
    
    img_dir = path.join(path.dirname(__file__), "Sprites", "Wagon")
    grass_image = pygame.image.load(path.join(img_dir, "grass.png")).convert()
    grass_image_width = grass_image.get_width()
    grass_image_rect = grass_image.get_rect()

    # define game variables
    tiles = m.ceil(width / grass_image_width) + 1
    scroll = 0
    
    while True:
        
        clock.tick(FPS)
       
        # draw the scrolling background
        for i in range(0, tiles):
            screen.blit((grass_image), (i * grass_image_width + scroll, 0))
            # visualize what's happening
            #grass_image_rect.x = i * grass_image_width + scroll
            #pygame.draw.rect(screen, (255, 0, 0), grass_image_rect, 1)

        # scroll background
        scroll -= 5

        # reset scroll
        if abs(scroll) > grass_image_width:
            scroll = 0
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                     pass
        #pygame.draw.rect(screen, GREEN, pygame.Rect(screen_x, screen_y, width, height))  # Use the defined color

        # add the menu bar
        #mb.menu(screen)

        pygame.display.update()  # Update the display






















#screen = pygame.display.set_mode((720, 720))
#width, height, screen_x , screen_y = mb.get_remaining_area(screen)

#main_screen(screen, width, height, screen_x, screen_y)