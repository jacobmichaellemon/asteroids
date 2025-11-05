from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.width = 2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, self.width)
    
    def update(self, dt):
        self.position += self.velocity*dt