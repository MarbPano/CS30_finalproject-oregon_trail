import pygame

class Button:
    def __init__(self, color, color_hover, rect, text=''):
        self.text = text
        tmp_rect = pygame.Rect(0, 0, *rect.size)
        self.org = self._create_image(color, text, tmp_rect)
        self.hov = self._create_image(color_hover, text, tmp_rect)
        self.image = self.org
        self.rect = rect

    def _create_image(self, color, text, rect):
        img = pygame.Surface(rect.size)
        img.fill(color)
        if text != '':
            font = pygame.font.Font(None, 24)
            text_surf = font.render(text, 1, pygame.Color('black'))
            text_rect = text_surf.get_rect(center=rect.center)
            img.blit(text_surf, text_rect)
        return img

    def update(self):
        pos = pygame.mouse.get_pos()
        self.image = self.hov if self.rect.collidepoint(pos) else self.org

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Create a button
button = Button(pygame.Color('green'), pygame.Color('red'), pygame.Rect(50, 50, 200, 60), 'Hover me!')

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the button
    button.update()

    # Draw everything
    screen.fill((255, 255, 255))
    button.draw(screen)
    pygame.display.flip()

pygame.quit()
