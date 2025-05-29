# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import Asteroid
from asteroidfield import *
from shot import *
from explosion import *

def draw_score(screen, score):
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    explosions = pygame.sprite.Group()

    score = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    Explosion.containers = (explosions, updatable, drawable)
    
    
    player = Player(x,y)
    asteroid_field = AsteroidField()
    pygame.font.init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:  # assuming you have a bullets group
                if asteroid.collides(shot):
                    asteroid.split()
                    shot.kill()
                    score += int(asteroid.radius * 10)
                    
            if player.collides(asteroid):
                print("Game over!")
                pygame.quit()
                return

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        draw_score(screen, score)

        pygame.display.flip()
        
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()