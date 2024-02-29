import window_creation as wc
import pygame
import time
import main_screen as ms
import math as m
from os import path


# a button menu system located at the bottom third of the screen
# make the rectangle for it using wc
def menu(screen):
    # rectangle coords
    rect_width = screen.get_width() 
    rect_height = int(screen.get_height() * (2/7))
    rect_x = 0
    rect_y = int((screen.get_height() * (2/3))+ 33)

    # detail rectangle
    details_width = screen.get_width() * (4/13)
    details_height = int(screen.get_height() * (3/11))
    details_x = 5
    details_y = int((screen.get_height() * (2/3))+ 38)
    
    # event rectangle
    events_width = screen.get_width() * (10/16)
    events_height = int(screen.get_height() * (1/12))
    events_x = 250
    events_y = int((screen.get_height() * (2/3)))

    # event rectangle border
    event_bord_width = screen.get_width() * (10/16) + 10
    event_bord_height = int(screen.get_height() * (1/12)) + 10
    event_bord_x = 245
    event_bord_y = int((screen.get_height() * (2/3))- 5)

    #buttons
    border_colour = (80, 80, 80)
    on_button = wc.Button(260, 560, 200, 50, (border_colour), (191, 134, 93), screen)
    on_button_rect = on_button.rect
    off_button = wc.Button(260, 560, 200, 50, (border_colour), (191, 134, 93), screen)
    off_button_rect = off_button.rect
    toggle = False

    hunt_button = wc.Button(500, 560, 200, 50, (border_colour), (191, 134, 93), screen)
    hunt_button_rect = hunt_button.rect

    interact_button = wc.Button(260, 650, 200, 50, (border_colour), (191, 134, 93), screen)
    interact_button_rect = interact_button.rect

    # details button toggles
    details_1 = wc.Button(500, 650, (200/3), 50, (border_colour), (191, 134, 93), screen)
    details_1_rect = details_1.rect
    details_2 = wc.Button(565.9, 650, (200/3), 50, (border_colour), (191, 134, 93), screen)
    details_2_rect = details_2.rect
    details_3 = wc.Button(630.9, 650, (200/3), 50, (border_colour), (191, 134, 93), screen)
    details_3_rect = details_3.rect

    clock = pygame.time.Clock()
    FPS = 60
    

    width, height, screen_x , screen_y = get_remaining_area(screen)
    scrolling_backgrounds =['grass', 'mountains']
    # define game variables

    scroll = 0

    while True: 
        clock.tick(FPS)
       
        # draw the scrolling background
        for background in scrolling_backgrounds:
            if background == 'grass':
                image, width, tiles =ms.grass(screen, width, height, screen_x, screen_y)
                image_rect = image.get_rect()
                for i in range(0, tiles):
                    screen.blit((image), (i * width + scroll, 0))
                    # visualize what's happening
                    image_rect.x = i * width + scroll
            
                    # scroll background
                    scroll -= 5
            
                    # reset scroll
                    if abs(scroll) > width:
                        scroll = 0
            if background == 'mountains':
                image, width, tiles =ms.mountains(screen, width, height, screen_x, screen_y)
                image_rect = image.get_rect()
                for i in range(0, tiles):
                    screen.blit((image), (i * width + scroll, 0))
                    # visualize what's happening
                    image_rect.x = i * width + scroll
            
                    # scroll background
                    scroll -= 5
            
                    # reset scroll
                    if abs(scroll) > width:
                        scroll = 0

            #if background == 'mountains':
            #    mountains, total_width = ms.mountains(screen, width, height, screen_x, screen_y)
            #        # Scroll background and cycle through the images
            #    for x in range(0, width, total_width):
            #        #for image in mountains:
            #            screen.blit(image, (x + scroll, 0))
            #            x += image.get_width()
            #        #
            #
            #        # Update scroll position
            #        scroll -= 1
            #        if scroll <= -total_width:
            #            scroll = 0
            #        
            #        # Reset scroll position once the last image goes off the screen
            #    if scroll <= -total_width:
            #        scroll = 0


        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #if mini_game == True:
            # something happens when you clickk p
                if event.key == pygame.K_p:
                    # this is for pausing
                    pass
                

            if event.type == pygame.MOUSEBUTTONDOWN:
                # changes the face of the on/off buttons
                if on_button_rect.collidepoint(event.pos) and not toggle: 
                    print('toggle on')
                    toggle = True
                elif off_button_rect.collidepoint(event.pos) and toggle: 
                    print('toggle off')
                    toggle = False

                elif hunt_button_rect.collidepoint(event.pos):
                    pass # add hunting function here
                elif interact_button_rect.collidepoint(event.pos):
                    pass # add interacting function here

                # changes the face of interact buttons
                elif details_1_rect.collidepoint(event.pos): 
                    details_1.isclicked = True
                    details_2.isclicked = False
                    details_3.isclicked = False
                elif details_2_rect.collidepoint(event.pos):
                    details_1.isclicked = False
                    details_2.isclicked = True
                    details_3.isclicked = False
                elif details_3_rect.collidepoint(event.pos):
                    details_1.isclicked = False
                    details_2.isclicked = False
                    details_3.isclicked = True

        
        # draw the rectangles
        base = wc.Rectangle(rect_x, rect_y, rect_width, rect_height, (152, 100, 63))
        base.draw(screen)
        details = wc.Rectangle(details_x, details_y, details_width, details_height, (80, 80, 80))
        details.draw(screen)
        event_bord = wc.Rectangle(event_bord_x, event_bord_y, event_bord_width, event_bord_height, (152, 100, 63))
        event_bord.draw(screen)
        events = wc.Rectangle(events_x, events_y, events_width, events_height, (80, 80, 80))
        events.draw(screen)

        # on/off toggles
        if toggle == False:
            on_button.draw(screen)
            on_button.with_text('On', 'Corbel', 30, (255, 255, 255), screen, bold=True)
            on_button.desc_box = True
            on_button.description = 'Toggle traveling'
            on_button.update()

        else:
            off_button.draw(screen)
            off_button.with_text('Off', 'Corbel', 30, (255, 255, 255), screen, bold=True)
            off_button.desc_box = True
            off_button.description = 'Toggle traveling'
            off_button.update()
        
        # details buttons
        details_3.draw(screen)
        details_3.with_text('3', 'Corbel', 30, (255, 255, 255), screen, bold=True)
        details_3.desc_box = True
        details_3.description = 'View family details'
        details_3.update()

        details_2.draw(screen)
        details_2.with_text('2', 'Corbel', 30, (255, 255, 255), screen, bold=True)
        details_2.desc_box = True
        details_2.description = 'View inventory details'
        details_2.update()

        details_1.draw(screen)
        details_1.with_text('1', 'Corbel', 30, (255, 255, 255), screen, bold=True)
        details_1.desc_box = True
        details_1.description = 'View travel details'
        details_1.update()

        hunt_button.draw(screen)
        hunt_button.with_text('Hunt', 'Corbel', 30, (255, 255, 255), screen, bold=True)
        hunt_button.desc_box = True
        hunt_button.description = 'Click to hunt'
        hunt_button.update()

        interact_button.draw(screen)
        interact_button.with_text('Interact', 'Corbel', 30, (255, 255, 255), screen, bold=True)
        interact_button.desc_box = True
        interact_button.description = 'Click to view interact options'
        interact_button.update()

        
        

        pygame.display.flip()

def get_remaining_area(screen): # get the remaining area of the screen after the menu_bar
    # existing area
    rect_width = screen.get_width()
    rect_height = int(screen.get_height() * (2/7))
    rect_x = 0
    rect_y = int((screen.get_height() * (2/3))+ 33)
    
    # remaining area
    remaining_width = screen.get_width()
    remaining_height = screen.get_height() - rect_height
    remaining_x = 0
    remaining_y = 0 #if rect_y == 0 else rect_y + rect_height

    return remaining_width, remaining_height, remaining_x, remaining_y


def main_background(screen):
    width, height, screen_x , screen_y = get_remaining_area(screen)
    main_screen(screen, width, height, screen_x, screen_y)


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





















screen = pygame.display.set_mode((720, 720))
width = screen.get_width()
height = screen.get_height()
menu(screen)
#main_background(screen)