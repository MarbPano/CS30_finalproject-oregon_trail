import pygame
import window_creation as wc
#import menu_bar as mb
import shop_screen as ss
import math as m
from os import path


def mountains(screen, width, height, screen_x, screen_y):
    #make background green
    GREEN = (0, 255, 0)  # Define the color green

    clock = pygame.time.Clock()
    FPS = 30
    



    

    img_dir = path.join(path.dirname(__file__), "Sprites", "Wagon")
    image_long = pygame.image.load(path.join(img_dir, "mountains_long.png")).convert()
    #image_1 = pygame.image.load(path.join(img_dir, "mountains_1.png")).convert()
    #image_2 = pygame.image.load(path.join(img_dir, "mountains_2.png")).convert()
    #image_3 = pygame.image.load(path.join(img_dir, "mountains_3.png")).convert()
    #image_4 = pygame.image.load(path.join(img_dir, "mountains_4.png")).convert()
    #image_5 = pygame.image.load(path.join(img_dir, "mountains_5.png")).convert()

    image = image_long
    #mountains = [image_1, image_2, image_3, image_4, image_5]

    #total_width = sum([image.get_width() for image in mountains])

    image_width = image.get_width()
    tiles = m.ceil(width / image_width) + 1
    scroll = 0
 
    
    return image, image_width, tiles
    

 
        # define game variables




def grass(screen, width , height, screen_x, screen_y):
    #make background green
    GREEN = (0, 255, 0)  # Define the color green

    clock = pygame.time.Clock()
    FPS = 60
    
    img_dir = path.join(path.dirname(__file__), "Sprites", "Wagon")
    image = pygame.image.load(path.join(img_dir, "grass_1.png")).convert()
    image_width = image.get_width()


    # define game variables
    tiles = m.ceil(width / image_width) + 1
    scroll = 0
            
    clock.tick(FPS)
       
    return image, image_width, tiles

    pygame.display.update()  # Update the display






















#screen = pygame.display.set_mode((720, 720))
#width, height, screen_x , screen_y = mb.get_remaining_area(screen)
#main_screen(screen, width, height, screen_x, screen_y)