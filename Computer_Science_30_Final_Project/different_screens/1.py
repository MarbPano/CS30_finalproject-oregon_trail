import window_creation as wc
import pygame
from os import path
import time

def name_leader(screen, width, height):
    # title
    font_dir = path.join(path.dirname(__file__), "Fonts")
    font = pygame.font.Font(path.join(font_dir, 'ANDYB.TTF'), 50)
    title = wc.Text("Leader's name:", width//2 - 195, height//3 - 175, (path.join(font_dir, 'ANDYB.TTF')), 50, (255, 255, 255), screen, bold=True)
    title.draw(screen)

    input_text = ""
    input_font = pygame.font.Font(path.join(font_dir, 'ANDYB.TTF'), 40)

    cursor_visible = True
    cursor_timer = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha() or event.key == pygame.K_SPACE:
                    input_text += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                print(input_text)

        screen.fill((0, 0, 0))

        img = input_font.render(input_text, True, (255, 255, 255))
        rect = img.get_rect()
        rect.topleft = (300, 40)

        # Update cursor visibility
        if time.time() - cursor_timer > 0.5:
            cursor_visible = not cursor_visible
            cursor_timer = time.time()

        if cursor_visible:
            cursor_rect = pygame.Rect(rect.topright, (3, rect.height))
            pygame.draw.rect(screen, (255, 255, 255), cursor_rect)

        screen.blit(img, rect)
        title.draw(screen)
        pygame.display.flip()


        
        
def naming(screen, width, height):
    font_dir = path.join(path.dirname(__file__), "Fonts")
    title = wc.Text("Enter your Leader's name", width/2, height/3 - 175, (path.join(font_dir, 'ANDYB.TTF')), 100, (255, 255, 255), screen, bold=True)
    player_name = None
    font = pygame.font.SysFont('Corbel', 40, bold=True)
    name = font.render("Enter your name", True, (255, 140, 0))

screen = pygame.display.set_mode((720, 720))
width = screen.get_width()
height = screen.get_height()
name_leader(screen, width, height)