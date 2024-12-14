import pygame 
from constants import *
from player import *

def main():
    pygame.init() 
    clock = pygame.time.Clock() 
    dt = 0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
    x = SCREEN_WIDTH / 2 
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group() 
    Player.containers = (updatable, drawable)

# Change the game loop to use the new groups instead of the Player object directly. 
# In other words, iterate over all "updatables" and .update() them, 
# then iterate over all "drawables" and .draw() them.

    player = Player(x, y, PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for instance in updatable: 
            instance.update(dt)
        #player.update(dt)

        screen.fill((0,0,0)) 

        for instance in drawable: 
            instance.draw(screen)
        #player.draw(screen)
        pygame.display.flip()  

        dt = clock.tick(60) / 1000 

if __name__ == "__main__":
    main() 