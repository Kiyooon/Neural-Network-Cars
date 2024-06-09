import pygame
import sys
from drawing import DrawingApp
from car import CarSimulation

def main():
    pygame.init()
    app = DrawingApp()
    sim = CarSimulation()

    running = True
    drawing_mode = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                drawing_mode = not drawing_mode
                if not drawing_mode:
                    pygame.image.save(app.screen, "images/map.png")
                    sim.run_simulation()
            if drawing_mode:
                app.handle_event(event)
        
        if drawing_mode:
            app.update_display()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
