import sys
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_running = True
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)

    asteroid_field = AsteroidField()

    center_screen = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player = Player(center_screen[0], center_screen[1], shots)

    while game_running:
        dt = clock.tick(60)/1000
        screen.fill("black")

        updatable.update(dt)
        asteroid_shot = False

        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game over!")
                sys.exit()
            for shot in player.shots:
                if asteroid.check_collisions(shot):
                    shot.kill()
                    player.shots.remove(shot)
                    asteroid.split()
                    asteroid_shot == True
                    break
            if asteroid_shot == True:
                break


        for item in drawable:
             item.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.flip()


if __name__ == "__main__":
    main()
