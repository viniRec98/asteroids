import circleshape
import pygame
from constants import LINE_WIDTH


class Asteroid(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    


    #Draw the asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, LINE_WIDTH)

    
    #move in a straight line at constant speed
    def update(self, dt):
        self.position += self.velocity * dt


