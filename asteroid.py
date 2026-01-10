import circleshape
import pygame
from constants import LINE_WIDTH
from logger import log_event
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    


    #Draw the asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, LINE_WIDTH)

    
    #move in a straight line at constant speed
    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill() #this asteroid is always destroyed, but maybe we'll spawn new smaller ones, depending on its size

        if self.radius <= ASTEROID_MIN_RADIUS:
            return #it was a small asteroid and I'm done
        
        #I need to spawn 2 new asteroids

        log_event("asteroid_split")
        new_angle = random.uniform(20,50) #generating a random angle between 20 and 50 degrees

        asteroid_1_velocity = self.velocity.rotate(new_angle) #new vector representing the 1st new asteroid movement (velocity vector)
        asteroid_2_velocity = self.velocity.rotate(-new_angle) #new vector representing the 2nd new asteroid movement (velocity vector)


        smaller_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS 

        asteroid_1_object = Asteroid(self.position.x, self.position.y, smaller_asteroid_radius) #new asteroid object 1
        asteroid_2_object = Asteroid(self.position.x, self.position.y, smaller_asteroid_radius) #new asteroid object 2

        asteroid_1_object.velocity = asteroid_1_velocity * 1.2
        asteroid_2_object.velocity = asteroid_2_velocity * 1.2










