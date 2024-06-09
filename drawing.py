import pygame
import sys

class DrawingApp:
    def __init__(self, width=1920, height=1080):
        pygame.init()
        self.WIDTH = width
        self.HEIGHT = height
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.LINE_WIDTH = 90
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Drawing with Mouse")
        
        # Load button images
        self.start_img = pygame.image.load("images/start.png")
        self.pen_inactive_img = pygame.image.load("images/pen_inactive.png")
        self.pen_active_img = pygame.image.load("images/pen_active.png")
        self.eraser_inactive_img = pygame.image.load("images/eraser_inactive.png")
        self.eraser_active_img = pygame.image.load("images/eraser_active.png")
        self.start_rect = self.start_img.get_rect(topleft=(400, 900))
        self.pen_button_rect = self.pen_inactive_img.get_rect(topleft=(40, 40))
        self.eraser_button_rect = self.eraser_inactive_img.get_rect(topleft=(40, 120))
        
        self.drawing = False
        self.last_pos = None
        self.drawing_color = self.BLACK
        self.pen_active = True
        self.eraser_active = False
        
        self.screen.fill(self.WHITE)
        pygame.display.flip()
    
    def draw(self, color, start_pos, end_pos, width):
        pygame.draw.line(self.screen, color, start_pos, end_pos, width)
        pygame.draw.circle(self.screen, color, start_pos, width // 2)

    def clamp_position(self, pos):
        x, y = pos
        x = max(self.LINE_WIDTH // 2, min(self.WIDTH - self.LINE_WIDTH // 2, x))
        y = max(self.LINE_WIDTH // 2, min(self.HEIGHT - self.LINE_WIDTH // 2, y))
        return (x, y)
    
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.pen_button_rect.collidepoint(event.pos):
                self.drawing_color = self.BLACK
                self.pen_active = True
                self.eraser_active = False
            elif self.eraser_button_rect.collidepoint(event.pos):
                self.drawing_color = self.WHITE
                self.pen_active = False
                self.eraser_active = True
            else:
                self.drawing = True
                self.last_pos = self.clamp_position(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            self.drawing = False
            self.last_pos = None
        elif event.type == pygame.MOUSEMOTION:
            if self.drawing:
                current_pos = self.clamp_position(event.pos)
                if self.last_pos is not None:
                    self.draw(self.drawing_color, self.last_pos, current_pos, self.LINE_WIDTH)
                self.last_pos = current_pos

    def update_display(self):
        self.screen.blit(self.pen_active_img if self.pen_active else self.pen_inactive_img, self.pen_button_rect)
        self.screen.blit(self.eraser_active_img if self.eraser_active else self.eraser_inactive_img, self.eraser_button_rect)
        self.screen.blit(self.start_img, self.start_rect)
        pygame.display.flip()
