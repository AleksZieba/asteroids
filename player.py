from constants import *
from circleshape import * 
from shot import *

class Player(CircleShape): 
    def __init__(self, x, y, PLAYER_RADIUS):
        super().__init__(x, y, PLAYER_RADIUS) 
        self.rotation = 0 
        self.x = x 
        self.y = y 
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c] 
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt): 
        self.rotation += PLAYER_TURN_SPEED * dt 

    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)  

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt) 

        if keys[pygame.K_SPACE]:
            if self.shoot_timer <= 0:
                self.shoot(Shot, SHOT_RADIUS)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, Shot, SHOT_RADIUS):
        shot = Shot(self.position, self.rotation, SHOT_RADIUS) 
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
    
