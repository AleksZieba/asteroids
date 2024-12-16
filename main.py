import pygame 
from constants import *
from player import *
from asteroid import * 
from asteroidfield import *
from shot import *

def main():
    pygame.init() 
    clock = pygame.time.Clock() 
    dt = 0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
   #x = SCREEN_WIDTH / 2 
   #y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids) 
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for instance in updatable: 
            instance.update(dt)
        #player.update(dt)

        for instance in asteroids: 
            if player.collision_check(instance) == True:
                print("Game Over!")
                return

        screen.fill((0,0,0)) 

        for instance in drawable: 
            instance.draw(screen)
        #player.draw(screen)
        pygame.display.flip()  

        dt = clock.tick(60) / 1000 

if __name__ == "__main__":
    main() 