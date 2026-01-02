#This class represents a player (a spaceship)

import pygame
import circleshape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    # A player will look like a triangle, even though I'll use a circle to represent its hitbox.
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt) # How much to rotate a frame


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: #rotate to the left if "a" key was pressed
            self.rotate(-dt)
        if keys[pygame.K_d]: #rotate to the right if "d" key was pressed
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt) #move forward if "w" was pressed
        if keys[pygame.K_s]:
            self.move(-dt) #move backward if "S" was pressed

    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1) #Unit vector pointing straight up from (0,0) to (0,1) 
        rotated_vector = unit_vector.rotate(self.rotation) # Rotating that vector by the player's rotation, so it's pointing in the same direction as the player
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt #By multiplying these values, the vector is the length the player should move during this frame
        self.position += rotated_with_speed_vector #Adding the vector to the player's position to move them



