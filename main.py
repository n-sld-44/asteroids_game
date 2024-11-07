import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet

def main():
    print("Hello")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()


    Bullet.containers = updatable,drawable,bullets
    Player.containers = updatable,drawable
    Asteroid.containers = updatable,drawable, asteroids
    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        
        for sprite in updatable:
            sprite.update(dt)

        for sprite in asteroids:
            if player.collides_with(sprite):
                print("Game Over")
                return
            for bullet in bullets:
                if sprite.collides_with(bullet):
                    sprite.kill()
                    bullet.kill()
                    break
        
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
