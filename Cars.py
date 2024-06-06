import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1920, 1080  # Increased window size
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_WIDTH = 80

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing with Mouse")

# Set the background color
screen.fill(WHITE)
pygame.display.flip()

# Main loop
drawing = False
last_pos = None

def draw(screen, color, start_pos, end_pos, width):
    pygame.draw.line(screen, color, start_pos, end_pos, width)
    pygame.draw.circle(screen, color, start_pos, width // 2)

def clamp_position(pos):
    x, y = pos
    x = max(LINE_WIDTH // 2, min(WIDTH - LINE_WIDTH // 2, x))
    y = max(LINE_WIDTH // 2, min(HEIGHT - LINE_WIDTH // 2, y))
    return (x, y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Start drawing when the mouse button is pressed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = clamp_position(event.pos)
        
        # Stop drawing when the mouse button is released
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None
        
        # Draw lines when the mouse is moved while holding the button
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                current_pos = clamp_position(event.pos)
                if last_pos is not None:
                    draw(screen, BLACK, last_pos, current_pos, LINE_WIDTH)
                last_pos = current_pos
    
    # Update the display
    pygame.display.flip()
