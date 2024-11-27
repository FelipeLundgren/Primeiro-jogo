import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
def main():
    print(f"Containers are set: {hasattr(Player, 'containers')}")
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField.containers = (updatable,)  # Note the comma to make it a tuple
    asteroid_field = AsteroidField()
    
    
    while True: 
        screen.fill((0, 0, 0))
        
        for item in updatable:
            item.update(dt)

        for circle in asteroids:
            if player.collision(circle):
                print("Game Over!")
                sys.exit()
        
        for imagem in drawable:
            imagem.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        


if __name__ == "__main__":
    main()




