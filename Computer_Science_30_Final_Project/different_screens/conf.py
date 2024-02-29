import pygame
import window_creation as wc

screen = pygame.display.set_mode((720, 720))
width = screen.get_width()
height = screen.get_height()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    confirmation = wc.Confirm(screen)
    confirmation.create(screen)
    pygame.display.update()