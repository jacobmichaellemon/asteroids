import pygame
from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, radius, shot_speed, ship_rotation):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 1).rotate(ship_rotation) * shot_speed

    def draw(self, screen):
        x = int(self.position.x)
        y = int(self.position.y)
        pygame.draw.circle(screen, "white", (x, y), self.radius)

    def update(self, dt):
        self.position += self.velocity*dt