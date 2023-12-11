import pygame
import window_creation as wc
from time import sleep

def choices(screen, width, height):
    #make 3 character choices, each with a button, voyageur, hunter and farmer
    #make each button have a different image

    border_colour = (80, 80, 80)
#Voyageur:

#Button Color (Dark Blue): RGB(0, 0, 139)
#Text Color (Gold/Yellow): RGB(255, 215, 0)
#Farmer:

#Button Color (Green): RGB(0, 128, 0)
#Text Color (Brown): RGB(139, 69, 19)
#Hunter:

#Button Color (Dark Red/Maroon): RGB(128, 0, 0)
#Text Color (White/Silver): RGB(255, 255, 255)

    pos = pygame.mouse.get_pos()

    Voyaguer = wc.Button(width/2 - 130, height - 450, 280, 70, border_colour, (0, 0, 139), screen)
    Voyaguer_button_rect = Voyaguer.rect
    Hunter = wc.Button(width/2 - 130, height - 360, 280, 70, border_colour, (128, 0, 0), screen)
    Hunter_button_rect = Hunter.rect
    Farmer = wc.Button(width/2 - 130, height - 270, 280, 70, border_colour, (0, 128, 0), screen)
    Farmer_button_rect = Farmer.rect

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Voyaguer_button_rect.collidepoint(event.pos):
                    # Start the game logic here
                    print("Game started!")
                    char_job = "Voyageur"
                    sleep(2)
                    
                elif Hunter_button_rect.collidepoint(event.pos):
                    # Start the game logic here
                    print("Game started!")
                    char_job = "Hunter"
                    sleep(2)
                    
                elif Farmer_button_rect.collidepoint(event.pos):
                    # Start the game logic here
                    print("Game started!")
                    char_job = "Farmer"
                    sleep(2)
                    
        
        screen.blit(pygame.image.load('different_screens\images\Camp-f.png'), (0,0))

        # draw voyaguer buttons
        Voyaguer.draw(screen)
        Voyaguer.with_text('Voyageur','Corbel', 35, (255, 215, 0), screen, bold=True)
        Voyaguer.desc_box = True
        Voyaguer.description = 'Easy Difficulty,\n x amount of money,\n 1.5x selling bonus'
    
        Voyaguer.update()

        # draw hunter buttons
        Hunter.draw(screen)
        Hunter.with_text('Hunter','Corbel', 35, (255, 255, 255), screen, bold=True)
        Hunter.desc_box = True
        Hunter.description = 'Medium Difficulty,\n x amount of money,\n 1.25x selling bonus'
        Hunter.update()

        # draw farmer buttons
        Farmer.draw(screen)
        Farmer.with_text('Farmer','Corbel', 35, (139, 69, 19), screen, bold=True)
        Farmer.desc_box = True
        Farmer.description = 'Hard Difficulty,\n x amount of money,\n 1x selling bonus'
        Farmer.update()

        pygame.display.flip()

screen = pygame.display.set_mode(size=(720, 720))
width = screen.get_width()
height = screen.get_height()
choices(screen, width, height)