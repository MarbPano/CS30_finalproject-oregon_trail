import pygame
import main_screen as ms
import menu_bar as mb

screen = pygame.display.set_mode((720, 720))
width, height, screen_x , screen_y = mb.get_remaining_area(screen)
mb.menu(screen)
ms.main_screen(screen, width, height, screen_x, screen_y)
