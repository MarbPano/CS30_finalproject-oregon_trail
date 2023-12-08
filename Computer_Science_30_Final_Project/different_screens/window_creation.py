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
    def __init__(self, x, y, width, height, light_colour, dark_colour, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.light_colour = light_colour
        self.dark_colour = dark_colour
        self.screen = screen
        self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def draw(self, screen):
        pygame.draw.rect(screen, self.light_colour, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, self.dark_colour, (self.x + 2, self.y + 2, self.width - 4, self.height - 4))
        
    def with_text(self, text, font, font_size, colour, screen, bold=False):
        if bold == True:
            text_font = pygame.font.SysFont(font, font_size, bold=True)
        else:
            text_font = pygame.font.SysFont(font, font_size)
        text = text_font.render(text, True, colour)
        self.text_rect = text.get_rect(center= (self.x, self.y))

        self.draw(screen)
        self.screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
        
    
    def get_rect_t(self):
        return self.text_rect
    
    def get_rect_b(self):
        return self.button_rect
    
class Rectangle:
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))