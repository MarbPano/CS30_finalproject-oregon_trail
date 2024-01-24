import pygame

pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200, 200)

# Initialize the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hover Description Box")

# Create a font object
font = pygame.font.Font(None, 30)

def draw_description_box(mouse_pos, button_rect):
    x, y = mouse_pos
    if button_rect.collidepoint(x, y):
        description_text = font.render("This is a description box", True, BLACK)
        description_box_rect = pygame.Rect(x, y - 30, description_text.get_width() + 10, description_text.get_height() + 10)
        pygame.draw.rect(screen, GRAY, description_box_rect)
        screen.blit(description_text, (x + 5, y - 25))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Create a button
    button_rect = pygame.Rect(200, 200, 200, 100)
    pygame.draw.rect(screen, BLACK, button_rect)

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Draw the description box
    draw_description_box(mouse_pos, button_rect)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()