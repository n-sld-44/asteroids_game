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

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
           
            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius // 2)
            asteroid1.velocity = self.velocity.rotate(random.randint(20, 50))

            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius // 2)
            asteroid2.velocity = self.velocity.rotate(random.randint(-50, -20))*1.2
        else:
            return

        