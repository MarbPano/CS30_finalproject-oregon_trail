import pygame
pygame.init()

class Line():
    def __init__(self, x1, y1, x2, y2, line_width, line_colour, screen):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.line_width = line_width
        self.line_colour = line_colour
        self.screen = screen
    
    def draw(self, screen):
        pygame.draw.line(screen, self.line_colour, (self.x1, self.y1), (self.x2, self.y2), self.line_width)
    
class Text():
    def __init__(self, text, x, y, font, font_size, colour, screen, bold=False):
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.font_size = font_size
        self.colour = colour
        self.bold = False
        self.screen = screen
    
    def draw(self, screen):        
        if self.bold == True:
            font = pygame.font.Font(self.font, self.font_size, bold=True)
        else:
            font = pygame.font.Font(self.font, self.font_size)
        text = font.render(self.text, True, self.colour)
        self.rect = text.get_rect(center=(self.x, self.y)) 
        screen = self.screen
        screen.blit(text, self.rect.topleft)
    
    def get_rect(self):
        return self.rect

class Button():
    def __init__(self, x, y, width, height, border_colour, button_colour, screen):
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
        button_surface = pygame.Surface((self.width, self.height))
        button_surface.fill(border_colour)

        pygame.draw.rect(button_surface, button_colour, (2, 2, self.width - 4, self.height - 4))

        return button_surface
    
    def with_text(self, text, font, font_size, colour, screen, bold=False):
        if bold == True:
            self.text_font = pygame.font.SysFont(font, font_size, bold=True)
        else:
            self.text_font = pygame.font.SysFont(font, font_size)
        text = self.text_font.render(text, True, colour)
        self.text_rect = text.get_rect(center= (self.x, self.y))
        self.screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
    
    def update(self):
        pos = pygame.mouse.get_pos() 
        if self.rect.collidepoint(pos):
            self.filled = self.hover
            #self.hover_desc(self.screen, self.description, pos)
        else:
            self.filled = self.original
        
        if self.desc_box == True:
            self.hover_desc(self.screen, self.description, pos)
    def draw(self, screen):
        screen.blit(self.filled, self.rect)

    def hover_desc(self, screen, text, pos):
        GRAY = (200, 200, 200, 200)
        x, y = pos
        button_rect = self.rect
        if button_rect.collidepoint(x, y):
            font = pygame.font.SysFont('Corbel', 10)
            description_text = font.render(text, True, (0, 0, 0))
            box_rect = pygame.Rect(x, y - 30, description_text.get_width() + 10, description_text.get_height() + 10)
            pygame.draw.rect(screen, GRAY, box_rect)
            screen.blit(description_text, (x + 5, y - 25))
            pygame.display.flip()
    


        

    
class Rectangle:
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))