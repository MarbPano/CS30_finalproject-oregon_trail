import pygame
import window_creation as wc
import shop_screen as sc
import classes_player as cp
from time import sleep
from os import path

def choices(screen, width, height, player_name):
    border_colour = (80, 80, 80)

    img_dir = path.join(path.dirname(__file__), "images")
    background = pygame.image.load(path.join(img_dir, 'Camp-f.png'))

    # creating buttons for each character choice
    Voyaguer = wc.Button(width/2 - 350, height - 360, 200, 70, border_colour, (0, 0, 139), screen)
    Voyaguer_button_rect = Voyaguer.rect
    Hunter = wc.Button(width/2 - 100, height - 360, 200, 70, border_colour, (128, 0, 0), screen)
    Hunter_button_rect = Hunter.rect
    Farmer = wc.Button(width/2 + 150, height - 360, 200, 70, border_colour, (0, 128, 0), screen)
    Farmer_button_rect = Farmer.rect

    # title text
    font_dir = path.join(path.dirname(__file__), "Fonts")
    choose = wc.Text('Choose your', width/2, height/3 - 175, (path.join(font_dir, 'ANDYB.TTF')), 100, (255, 255, 255), screen, bold=True)
    choose_1 = wc.Text('Character', width/2, height/3 - 75, (path.join(font_dir, 'ANDYB.TTF')), 100, (255, 255, 255), screen, bold=True)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            # check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Voyaguer_button_rect.collidepoint(event.pos):
                    # Start the game logic here
                    print("Game started!")
                    char_job = "Voyageur"
                    user = cp.Player(player_name, char_job)
                    money = user.money
                    sc.shop(screen, width, height, money)
                    sleep(2)
                    
                elif Hunter_button_rect.collidepoint(event.pos):
                    # Start the game logic here
                    print("Game started!")
                    char_job = "Hunter"
                    print(player_name)
                    user = cp.Player(player_name, char_job)
                    money = user.money
                    sc.shop(screen, width, height, money)
                    sleep(2)
                    
                elif Farmer_button_rect.collidepoint(event.pos):
                    # Start the game logic here
                    print("Game started!")
                    char_job = "Farmer"
                    user = cp.Player(player_name, char_job)
                    money = user.money
                    sc.shop(screen, width, height, money)
                    sleep(2)
                    
        # load the background
        screen.blit(background, (0,0))

        # draw the title
        choose.draw(screen)
        choose_1.draw(screen)

        # draw voyaguer buttons
        Voyaguer.draw(screen)
        Voyaguer.with_text('Voyageur','Corbel', 35, (255, 215, 0), screen, bold=True)
        Voyaguer.desc_box = True
        Voyaguer.description = 'Easy Difficulty,\n Starting $2000,\n 1.5x selling bonus'
        Voyaguer.update()

        # draw hunter buttons
        Hunter.draw(screen)
        Hunter.with_text('Hunter','Corbel', 35, (255, 255, 255), screen, bold=True)
        Hunter.desc_box = True
        Hunter.description = 'Medium Difficulty,\n Starting $1500,\n 1.25x selling bonus'
        Hunter.update()

        # draw farmer buttons
        Farmer.draw(screen)
        Farmer.with_text('Farmer','Corbel', 35, (139, 69, 19), screen, bold=True)
        Farmer.desc_box = True
        Farmer.description = 'Hard Difficulty,\n Starting $1000,\n 1.0x selling bonus'
        Farmer.update()

        pygame.display.flip()

#screen = pygame.display.set_mode(size=(720, 720))
#width = screen.get_width()
#height = screen.get_height()
#choices(screen, width, height, "Player")