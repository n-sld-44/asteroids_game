import pygame 
from constants import * 
import random
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(random.uniform(-200,200), random.uniform(-200,200))


    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255), self.position, self.radius, 2 )

    def update(self, dt):
        self.position += self.velocity * dt

        