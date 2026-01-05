#This class represents a bullet
import circleshape
import pygame
from constants import LINE_WIDTH


class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    

    #move in a straight line at constant speed
    def update(self, dt):
        self.position += self.velocity * dt

    
    #Draw the bullet
    def draw(self, screen):
        pygame.draw.circle(screen, "orange", self.position, self.radius, LINE_WIDTH)




