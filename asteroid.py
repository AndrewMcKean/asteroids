import random

import pygame

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
         
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)

        child_one_velocity = self.velocity.rotate(angle)
        
        child_two_velocity = self.velocity.rotate(-angle)

        child_radius = self.radius - ASTEROID_MIN_RADIUS

        child_one_asteroid = Asteroid(self.position.x, self.position.y, child_radius)
        child_two_asteroid = Asteroid(self.position.x, self.position.y, ASTEROID_MIN_RADIUS)

        child_one_asteroid.velocity = child_one_velocity * 1.2
        child_two_asteroid.velocity = child_two_velocity * 1.2

        
