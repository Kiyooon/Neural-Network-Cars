import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1920, 1080  # Increased window size
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_WIDTH = 80

# Load button images
pen_inactive_img = pygame.image.load("images/pen_inactive.png")
pen_active_img = pygame.image.load("images/pen_active.png")
eraser_inactive_img = pygame.image.load("images/eraser_inactive.png")
eraser_active_img = pygame.image.load("images/eraser_active.png")
pen_button_rect = pen_inactive_img.get_rect(topleft=(40, 40))
eraser_button_rect = eraser_inactive_img.get_rect(topleft=(40, 120))

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing with Mouse")

screen.fill(WHITE)
pygame.display.flip()

drawing = False
last_pos = None
drawing_color = BLACK  
pen_active = True  
eraser_active = False  

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
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pen_button_rect.collidepoint(event.pos):
                drawing_color = BLACK
                pen_active = True
                eraser_active = False
            elif eraser_button_rect.collidepoint(event.pos):
                drawing_color = WHITE
                pen_active = False
                eraser_active = True
            else:
                drawing = True
                last_pos = clamp_position(event.pos)
        
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None
        
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                current_pos = clamp_position(event.pos)
                if last_pos is not None:
                    draw(screen, drawing_color, last_pos, current_pos, LINE_WIDTH)
                last_pos = current_pos
    
    screen.blit(pen_active_img if pen_active else pen_inactive_img, pen_button_rect)
    screen.blit(eraser_active_img if eraser_active else eraser_inactive_img, eraser_button_rect)
    
    pygame.display.flip()
