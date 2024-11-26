from circleshape import *
from constants import *


class Player (CircleShape):
    def __init__(self,x,y):
        self.rotation = 0
        
        super().__init__(x,y,PLAYER_RADIUS)
        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def move(self,dt):  
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
