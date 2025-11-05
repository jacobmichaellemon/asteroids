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

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #TODO: Adjustable screen settings, full screen
    game_running = True
    clock = pygame.time.Clock()
    dt = 0

    #allow us to iterate over objects created
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #these containers are references to any objects being created that we want to track for creation, updating, and deleting easily
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)

    asteroid_field = AsteroidField() #looks unused, gets called to every update because its in the updateable container, see above

    center_screen = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player = Player(center_screen[0], center_screen[1], shots)

    while game_running:
        dt = clock.tick(60)/1000 #60 FPS
        screen.fill("black")

        #TODO: added a score value to window

        updatable.update(dt)
        asteroid_shot = False #flag to avoid cascading shot collisons, once the shot collison happens, break out

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
