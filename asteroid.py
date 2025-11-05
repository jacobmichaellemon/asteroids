import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.width = 2

    def split(self):   
        # store old asteroid info for later
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        x = self.position.x
        y = self.position.y
        angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(angle) * 1.2
        velocity2 = self.velocity.rotate(-angle) * 1.2

        self.kill() # removes astroid from the group

        #simply destroy the smallest asteroids
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        #if not a small asteroid, split new smaller ones based on the old asteroid
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, self.width)
    
    def update(self, dt):
        self.position += self.velocity*dt