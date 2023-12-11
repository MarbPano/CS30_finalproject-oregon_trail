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

    Voyaguer = wc.Button(width/2 - 100, height - 250, 225, 60, border_colour, (0, 0, 139), screen)
    Voyaguer_button_rect = Voyaguer.rect
    Hunter = wc.Button(width/2 - 100, height - 175, 225, 60, border_colour, (128, 0, 0), screen)
    Hunter_button_rect = Hunter.rect
    Farmer = wc.Button(width/2 - 100, height - 100, 225, 60, border_colour, (0, 128, 0), screen)
    Farmer_button_rect = Farmer.rect

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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
        Voyaguer.update()

        # draw hunter buttons
        Hunter.draw(screen)
        Hunter.with_text('Hunter','Corbel', 35, (255, 255, 255), screen, bold=True)
        Hunter.update()

        # draw farmer buttons
        Farmer.draw(screen)
        Farmer.with_text('Farmer','Corbel', 35, (139, 69, 19), screen, bold=True)
        Farmer.update()

        pygame.display.flip()


