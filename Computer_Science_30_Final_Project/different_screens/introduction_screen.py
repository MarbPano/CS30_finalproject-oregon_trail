import pygame
from os import path
import time
import window_creation as wc
import character_screen as cs

# Initialize Pygame
pygame.init()

class Family:
    def __init__(self, screen, width, height):
        # initialize the family object with its properties
        self.screen = screen
        self.width = width
        self.height = height
        self.spacing = 65 # spacing between names
        # use shopscreen background
        img_dir = path.join(path.dirname(__file__), "images")
        self.background = pygame.image.load(path.join(img_dir, "Camp-f.png"))
        # create family title
        self.create_family_title(screen)
        # create family members
        self.leader = self.naming(screen, width, height, width // 2 - 305, height - (5 * self.spacing), "Leader's name:")
        self.player = "" # saves player name
        self.member2 = self.naming(screen, width, height, width // 2 - 305, height - (4 * self.spacing), "Wife's name:")
        self.member3 = self.naming(screen, width, height, width // 2 - 305, height - (3 * self.spacing), "Kid 1's name:")
        self.member4 = self.naming(screen, width, height, width // 2 - 305, height - (2 * self.spacing), "Kid 2's name:")
        self.member5 = self.naming(screen, width, height, width // 2 - 305, height - self.spacing, "Kid 3's name:")

 


    

    def create_family_title(self, screen):
        # create the title 
        screen.blit(self.background,(0,0))
        font_dir = path.join(path.dirname(__file__), "Fonts")
        # loading and rendering the title font
        title_font = pygame.font.Font(path.join(font_dir, 'ANDYB.TTF'), 60)
        family_title = title_font.render("Name Your Family", True, (255, 255, 255))
        title_rect = family_title.get_rect(center=(self.width // 2, self.height // 8))
        screen.blit(family_title, title_rect)
        pygame.display.flip()

    def naming(self, screen, width, height, x, y, title):
        # creating input fields for naming family members
        font_dir = path.join(path.dirname(__file__), "Fonts")
        # loading and rendering the title font
        font = pygame.font.Font(path.join(font_dir, 'ANDYB.TTF'), 50)
        input_text = "" # saves input text
        input_font = pygame.font.Font(path.join(font_dir, 'ANDYB.TTF'), 35)
        title_font = pygame.font.Font(path.join(font_dir, 'ANDYB.TTF'), 50)

        # render title text
        title_img = title_font.render(title, True, (255, 255, 255))
        title_rect = title_img.get_rect()
        title_rect.topleft = (x, y)

        # rectangle for input area
        input_rect = pygame.Rect(x + title_rect.width + 10, title_rect.top, 200, title_rect.height)
        input_surface = pygame.Surface((input_rect.size), pygame.SRCALPHA)
        input_surface.fill(pygame.Color(0, 0, 0, 128))
        screen.blit(input_surface, input_rect.topleft)

        # cursor variables
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
                    elif event.key == pygame.K_RETURN:
                        if input_text:
                            if title == "Leader's name:": # saves player name
                                self.player = input_text
                                print(self.player)
                                return input_text
                            if title == "Kid 3's name:": # runs confirmation after last name
                                self.show_confirmation(screen)
                                return input_text
                            else:
                                return input_text

            # fill inpu tusrface with transparent black
            input_surface.fill(pygame.Color(0, 0, 0, 128))

            # render input text
            screen.blit(input_surface, input_rect.topleft)

            img = input_font.render(input_text, True, (255, 255, 255))
            rect = img.get_rect()
            rect.topleft = (x + title_rect.width + 10, title_rect.top)  

            # controling cursor visibility
            if time.time() - cursor_timer > 0.5:
                cursor_visible = not cursor_visible
                cursor_timer = time.time()

            # draw cursor if visisble
            if cursor_visible:
                cursor_rect = pygame.Rect(rect.topright, (3, rect.height))
                pygame.draw.rect(screen, (255, 255, 255), cursor_rect)

            screen.blit(img, rect)
            screen.blit(title_img, title_rect)
            pygame.display.flip()

    def show_confirmation(self, screen):
        # define confirmation variables
        font_dir = path.join(path.dirname(__file__), "Fonts")
        confirmation_font = pygame.font.Font(path.join(font_dir, 'ANDYB.TTF'), 40)
        confirmation_text = confirmation_font.render(f"Is spelling correct for Family Members?", True, (255, 255, 255))
        text_rect = confirmation_text.get_rect(center=(self.width // 2, self.height - (8 * self.spacing)))
        screen.blit(confirmation_text, text_rect)

        # define colours
        border_colour = (80, 80, 80)
        button_colour = (101, 67, 33)
        
        # Create yes and no buttons using wc
        yes_button = wc.Button(self.width // 3 - 60, self.height - (7 * self.spacing), 150, 50, border_colour, button_colour, screen)
        yes_button_rect = yes_button.rect
        no_button = wc.Button(2 * self.width // 3, self.height - (7 * self.spacing), 150, 50, border_colour, button_colour, screen)
        no_button_rect = no_button.rect

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
                # check for mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if yes_button_rect.collidepoint(event.pos):
                        print("Yes button clicked")
                        print(self.player)
                        cs.choices(screen, self.width, self.height, self.player)
                        time.sleep(2)
                    elif no_button_rect.collidepoint(event.pos):
                        print("No button clicked")
                        self.rerun(screen)

            # Draw the buttons
            yes_button.draw(screen)
            yes_button.with_text('Yes', 'Corbel', 30, (255, 255, 255), screen, bold=True)
            yes_button.update()
            no_button.draw(screen)
            no_button.with_text('No', 'Corbel', 30, (255, 255, 255), screen, bold=True)
            no_button.update()

            pygame.display.flip()

    def rerun(self, screen):
        # Fill the screen with black
        screen.fill((0, 0, 0))
        # Recreate the Family instance
        family = Family(screen, self.width, self.height)

# Create a Pygame screen
#screen = pygame.display.set_mode((720, 720))
#width = screen.get_width()
#height = screen.get_height()
#family = Family(screen, width, height)

# Run the Pygame event loop
#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False


