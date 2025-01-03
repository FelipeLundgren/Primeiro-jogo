from circleshape import *
from constants import *
from circleshape import CircleShape
from Shot import *

class Player (CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.add_to_containers()
        self.shoot_timer = 0
    
    def add_to_containers(self):
        for group in self.containers:
            group.add(self)
    
    
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
    
    def update(self, dt):
        print(f"Updating Player with dt: {dt}")
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        self.shoot_key()
    
        self.shoot_timer = max(0, self.shoot_timer - dt)
    def draw(self, screen):
        pygame.draw.polygon(screen,"white", self.triangle(),2)
    
   

    def shoot(self):
        if self.shoot_timer == 0:
            shot = Shot(self.position.x, self.position.y)
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            forward = forward * PLAYER_SHOOT_SPEED
            shot.velocity = forward
            self.shoot_timer = 0.3
        
    
    def shoot_key (self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.shoot()


