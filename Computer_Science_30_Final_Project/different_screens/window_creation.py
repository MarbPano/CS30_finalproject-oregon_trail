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
        self.desc_box = False
        if self.desc_box == True:
            self.description = None 
    

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

class Rectangle:
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))