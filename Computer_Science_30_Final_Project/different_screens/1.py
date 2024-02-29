import pygame
import window_creation as wc
from time import sleep

def month(screen, width, height):
    border_colour = (80, 80, 80)

    background = pygame.image.load('different_screens\images\Camp-f.png')
    #pygame.image.load('different_screens\images\salt.png')
    pos = pygame.mouse.get_pos()

    # creating buttons for each month choice
    Spring = wc.Button(200, 200, 200, 70, border_colour, (0, 0, 139), screen)
    Springpring_button_rect = Spring.rect
    Summer = wc.Button(500, 200, 200, 70, border_colour, (128, 0, 0), screen)
    Summer_button_rect = Summer.rect
    Fall = wc.Button(800, 200, 200, 70, border_colour, (0, 128, 0), screen)
    Fall_button_rect = Fall.rect
    Winter = wc.Button(1100, 200, 200, 70, border_colour, (139, 69, 19), screen)
    Winter_button_rect = Winter.rect

    # title text
    choose = wc.Text('Choose your', width/2, height/3 - 175, 'different_screens\Fonts\ANDYB.TTF', 100, (255, 255, 255), screen, bold=True)
    choose_1 = wc.Text('Month', width/2, height/3 - 75, 'different_screens\Fonts\ANDYB.TTF', 100, (255, 255, 255), screen, bold=True)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Springpring_button_rect.collidepoint(event.pos):
                    # Start the game logic here
                    print("Game started!")
                    month = "Spring"
                    sleep(2)

                elif Summer_button_rect.collidepoint(event.pos):
                    # Start the game logic here
                    print("Game started!")
                    month = "Summer"
                    sleep(2)

                elif Fall_button_rect.collidepoint(event.pos):
                    # Start the game logic here
                    print("Game started!")
                    month = "Fall"
                    sleep(2)

                elif Winter_button_rect.collidepoint(event.pos):
                    # Start the game logic here
                    print("Game started!")
                    month = "Winter"
                    sleep(2)
        
        # load the background
        screen.blit(background, (0,0))

        # draw the title
        choose.draw(screen)
        choose_1.draw(screen)

        # draw spring buttons
        Spring.draw(screen)
        Spring.with_text('Spring','Corbel', 35, (255, 215, 0), screen, bold=True)
        Spring.desc_box = True
        Spring.description = 'Easy Difficulty,\n Starting $2000,\n 1.5x selling bonus'
        Spring.update()

        # draw summer buttons
        Summer.draw(screen)
        Summer.with_text('Summer','Corbel', 35, (255, 255, 255), screen, bold=True)
        Summer.desc_box = True
        Summer.description = 'Medium Difficulty,\n Starting $1500,\n 1.25x selling bonus'
        Summer.update()

        # draw fall buttons
        Fall.draw(screen)
        Fall.with_text('Fall','Corbel', 35, (255, 215, 0), screen, bold=True)
        Fall.desc_box = True
        Fall.description = 'Easy Difficulty,\n Starting $2000,\n 1.5x selling bonus'
        Fall.update()

        # draw winter buttons
        Winter.draw(screen)
        Winter.with_text('Winter','Corbel', 35, (255, 255, 255), screen, bold=True)
        Winter.desc_box = True
        Winter.description = 'Hard Difficulty,\n Starting $1000,\n 1x selling bonus'
        Winter.update()

        pygame.display.flip

screen = pygame.display.set_mode(size=(720, 720))
width = screen.get_width()
height = screen.get_height()
month(screen, width, height)