from constants import *
from circleshape import * 
from player import * 

class Shot(CircleShape):
    def __init__(self, position, rotation, radius): 
        super().__init__(position.x, position.y, SHOT_RADIUS) 
        self.rotate = rotation
        self.radius = radius 
        self.velocity = pygame.Vector2(0, 1).rotate(self.rotate)

    def draw(self, screen): 
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)  

    def update(self, dt):
        self.position += (self.velocity * dt * PLAYER_SHOOT_SPEED) 


   # def move(self, dt):
       # forward = pygame.Vector2(0, 1).rotate(self.rotation)
       # self.position += forward * PLAYER_SPEED * dt