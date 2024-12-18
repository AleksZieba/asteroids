from constants import *
from circleshape import * 
import random 
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)  
     
        self.radius = radius 

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)  

    def update(self, dt):
        self.position += (self.velocity * dt)

    def collision_check(self, shots):
        if (self.position.distance_to(shots.position)) < self.radius + shots.radius:
            return True
        else: 
            return False 

    def split(self): 
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else: 
            angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid = Asteroid(self.position.x, self.position.y, new_radius) 
            asteroid.velocity = self.velocity.rotate(angle) * 1.6
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)  
            asteroid.velocity = self.velocity.rotate(-angle) * 1.6

          #  asteroid1.containers = (updatable, drawable, asteroids) 
          #  asteroid2.containers = (updatable, drawable, asteroids) 
