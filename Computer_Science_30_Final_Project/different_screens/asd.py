import pygame
import window_creation as wc
import math as m
from os import path


screen = pygame.display.set_mode((720, 720))
width = screen.get_width()
clock = pygame.time.Clock()
FPS = 60
    
img_dir = path.join(path.dirname(__file__), "Sprites", "Wagon")
image = pygame.image.load(path.join(img_dir, "grass_1.png")).convert()
image_width = image.get_width()


# define game variables
tiles = m.ceil(width / image_width) + 1
scroll = 0

while True:     
    clock.tick(FPS)
        
    for i in range(0, tiles):
        screen.blit((image), (i * image_width + scroll, 0))
        # visualize what's happening
        #grass_image_rect.x = i * grass_image_width + scroll
        #pygame.draw.rect(screen, (255, 0, 0), grass_image_rect, 1)

        # scroll background
        scroll -= 5

        # reset scroll
        if abs(scroll) > image_width:
            scroll = 0
        pygame.display.update()  # Update the display