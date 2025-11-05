import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_running = True

    while game_running:
        screen.fill("black")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.flip()


if __name__ == "__main__":
    main()
