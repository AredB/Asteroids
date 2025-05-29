import pygame
import random

from constants import *
from circleshape import *
from explosion import *

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        displacement = self.velocity * dt
        self.position += displacement
    
    def split(self):
        Explosion(self.position)
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        new_radius = self.radius / 2

        offset = pygame.Vector2(new_radius, 0)

        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        asteroid1 = Asteroid(self.position.x + offset.x, self.position.y + offset.y, new_radius)
        asteroid1.velocity = velocity1

        asteroid2 = Asteroid(self.position.x - offset.x, self.position.y - offset.y, new_radius)
        asteroid2.velocity = velocity2