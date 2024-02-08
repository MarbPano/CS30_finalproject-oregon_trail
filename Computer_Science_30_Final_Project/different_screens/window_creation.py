import pygame
pygame.init()

class Line():
    def __init__(self, x1, y1, x2, y2, line_width, line_colour, screen):
        # initialize the line object with its properties
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.line_width = line_width
        self.line_colour = line_colour
        self.screen = screen
    
    def draw(self, screen):
        # draw the line
        pygame.draw.line(screen, self.line_colour, (self.x1, self.y1), (self.x2, self.y2), self.line_width)
    
class Text():
    def __init__(self, text, x, y, font, font_size, colour, screen, bold=False):
        # initialize the text object with its properties
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.font_size = font_size
        self.colour = colour
        self.bold = False
        self.screen = screen
    
    def draw(self, screen): 
        # draw the text       
        if self.bold == True:
            font = pygame.font.Font(self.font, self.font_size, bold=True)
        else:
            font = pygame.font.Font(self.font, self.font_size)
        text = font.render(self.text, True, self.colour)
        self.rect = text.get_rect(center=(self.x, self.y)) 
        screen = self.screen
        screen.blit(text, self.rect.topleft)
    
class Button():
    def __init__(self, x, y, width, height, border_colour, button_colour, screen):
        # initialize the button object with its properties
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.border_colour = border_colour
        self.button_colour = button_colour
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.original = self.create(screen, self.border_colour, self.button_colour)
        self.hover = self.create(screen, self.border_colour, (
    self.button_colour[0] + 20,
    self.button_colour[1] + 20,
    self.button_colour[2] + 20
    ))
        self.filled = self.original
        self.isclicked = False

        
        #self.clicked = self.create(screen, self.border_colour, (
    #self.button_colour[0] - 50,
    #self.button_colour[1] - 50,
    #self.button_colour[2] - 50
    #    ))
        self.desc_box = False
        if self.desc_box == True:
            self.description = None 

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            isclicked = True   
    

    def create(self, screen, border_colour, button_colour):
        # create the button surface
        button_surface = pygame.Surface((self.width, self.height))
        button_surface.fill(border_colour)

        pygame.draw.rect(button_surface, button_colour, (2, 2, self.width - 4, self.height - 4))

        return button_surface
    
    def with_text(self, text, font, font_size, colour, screen, bold=False):
        # draw the button with text
        if bold == True:
            self.text_font = pygame.font.SysFont(font, font_size, bold=True)
        else:
            self.text_font = pygame.font.SysFont(font, font_size)
        text = self.text_font.render(text, True, colour)
        self.text_rect = text.get_rect(center= (self.x, self.y))
        self.screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
    
    def update(self):
        # update the button's state based on mouse position
        pos = pygame.mouse.get_pos() 
        if self.rect.collidepoint(pos):
            self.filled = self.hover
            #self.hover_desc(self.screen, self.description, pos)
        else:
            self.filled = self.original


        if self.isclicked:
            self.filled = self.clicked

        if self.desc_box == True:
            self.hover_desc(self.screen, self.description, pos)
            
    def draw(self, screen):
        # draw the button
        screen.blit(self.filled, self.rect)

    def hover_desc(self, screen, text, pos):
        # draw the description box
        GRAY = (200, 200, 200, 200)
        x, y = pos
        button_rect = self.rect
        if button_rect.collidepoint(x, y):
            font = pygame.font.SysFont('Corbel', 10, bold=True)
            lines = text.split('\n')
            line_height = font.get_linesize()
            box_width = max(font.size(line)[0] for line in lines) + 10
            box_height = len(lines) * line_height + 20
            box_rect = pygame.Rect(x, y - box_height, box_width, box_height)
            pygame.draw.rect(screen, GRAY, box_rect)
            #screen.blit(description_text, (x + 5, y - 25))
            for i, line in enumerate(lines):
                line_text = font.render(line, True, (0, 0, 0))
                screen.blit(line_text, (x + 5, y - box_height + 5 + i * 20))
    
    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class Rectangle:
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))

class Confirm:
    def __init__(self, screen):
        self.text = "Are you sure?"
        self.width = 300
        self.height = 180
        self.x = screen.get_width() / 2
        self.y = screen.get_height() / 2
        self.colour = (54, 54, 54)
        self.border_c = (80, 80, 80)
        self.button_c = (101, 67, 33)
        self.screen = screen
        
        
    
    def create(self, screen):
        
        #create rectangle for the confirmation box and two buttons in the box bellow the text
        confirmation_box = Rectangle(self.x - self.width/2, self.y - self.height/2, self.width, self.height, self.colour)
        confirmation_box.draw(screen)

        # add the text
        font = pygame.font.SysFont('Corbel', 30, bold=True)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.x, self.y - 50))
        screen.blit(text, text_rect)

        # Create yes and no buttons in the box below the text but on the same x axis
        yes_button = Button(self.x - self.width/2 + 15, self.y + self.height/2 - 60, 100, 50, self.border_c, self.button_c, screen)
        self.yes_rect = yes_button.rect
        yes_button.draw(screen)
        yes_button.with_text('Yes', 'Corbel', 30, (255, 255, 255), screen, bold=True)
        yes_button.update()  # Add this line to update the state of the "Yes" button

        no_button = Button(self.x + self.width/2 - 115, self.y + self.height/2 - 60, 100, 50, self.border_c, self.button_c, screen)
        self.no_rect = no_button.rect
        no_button.draw(screen)
        no_button.with_text('No', 'Corbel', 30, (255, 255, 255), screen, bold=True)
        no_button.update()  # Add this line to update the state of the "No" button

    def collide(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.yes_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.display.update()
                    return 'Yes'
                elif self.no_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.display.update()
                    return 'No'



