# import pygame 
# import sys
# from os import path
# from time import sleep
# import window_creation as wc
# import character_screen as cs
# 
# pygame.init()
# 
# #screen resoultion
# width = 720
# height = 720
# res = ((width // 2) * 1.5, ((height // 2) * 1.35) - 50)
# 
# #open the window
# screen = pygame.display.set_mode(size=(res))
# #font color of button 
# border_colour = (80, 80, 80)
# button_colour = (101, 67, 33)
# 
# #width and height of screen
# width = screen.get_width()
# height = screen.get_height()
# 
# 
# 
# 
# start_button = wc.Button(width/2 - 100, height - 250, 225, 60, border_colour, button_colour, screen)
# start_button_rect = start_button.rect
# 
# quit_button = wc.Button(width/2 - 100, height - 175, 225, 60, border_colour, button_colour, screen)
# quit_button_rect = quit_button.rect
# 
# #be able to use the mouse
# pos = pygame.mouse().get_pos()
# 
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         
#         # check for mouse click
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if start_button_rect.collidepoint(event.pos):
#                 # Start the game logic here
#                 print("Game started!")
#                 sleep(2)
#                 cs.choices(screen, width, height)
#             elif quit_button_rect.collidepoint(event.pos):
#                 pygame.quit()
#                 sys.exit()
#          
# 
#     #fill background with the title_background
#     screen.blit((title_background), (0,0))
#     
#     # draw the texts
#     title_text.draw(screen)
#     start_button.draw(screen)
#     start_button.with_text('Start Game','Corbel', 35, text_colour, screen, bold=True)
#     start_button.update()
#     quit_button.draw(screen)
#     quit_button.with_text('Quit Game','Corbel', 35, text_colour, screen, bold=True)
#     quit_button.update()
# 
# 
#     # update display
#     pygame.display.flip()


import pygame
import sys
from os import path
from time import sleep
import window_creation as wc


pygame.init()

img_dir = path.join(path.dirname(__file__), "images")
title_background = pygame.image.load(path.join(img_dir, "Title-f.png"))

# screen resolution

res = ((760 // 2) *1.5, ((760 // 2) * 1.35) - 50)

# open the window
screen = pygame.display.set_mode(size=(res))#, flags=pygame.FULLSCREEN)

# font colour
text_colour = (255, 248, 220)
title_colour = (0, 100, 0)

# shades for button
border_colour = (80, 80, 80)
button_colour = (101, 67, 33)

# width of screen
width = screen.get_width()

# height of screen
height = screen.get_height()

# creating text and buttons


food_button = wc.Button(width/2 - 100, height - 250, 225, 60, border_colour, button_colour, screen)

parts_button = wc.Button(width/2 - 100, height - 175, 225, 60, border_colour, button_colour, screen)


# mouse position
pos = pygame.mouse.get_pos()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if food_button.collidepoint(event.pos):
                print("added food") 
                sleep(2)
                
            elif parts_button.collidepoint(event.pos):
                print("added parts")
                
    
         

    
  
    
    # draw the texts
    
    food_button.draw(screen)
    food_button.with_text('Food','Corbel', 35, text_colour, screen, bold=True)
    food_button.update()
    
    parts_button.draw(screen)
    parts_button.with_text('Spare Parts','Corbel', 35, text_colour, screen, bold=True)
    parts_button.update()
    
#     horses_button.draw(screen)
#     horses_button.with_text('Horses','Corbel', 35, text_colour, screen, bold=True)
#     horses_button.update()
#     
#     bullets_button.draw(screen)
#     bullets_button.with_text('Bullets','Corbel', 35, text_colour, screen, bold=True)
#     bullets_button.update()
#     
#     medicine_button.draw(screen)
#     medicine_button.with_text('Medicine','Corbel', 35, text_colour, screen, bold=True)
#     medicine_button.update()


    # update display
    pygame.display.flip()







