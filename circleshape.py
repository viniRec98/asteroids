import pygame
from constants import LINE_WIDTH

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    #Draw the player
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)


    def update(self, dt):
        # must override
        pass


    #collision logic
    """
    Detecting a collision between two circles:

    1. Calculate the distance between the center of the two circles: "distance"
    2. Calculate the radius of each circle: r1 and r2.
    3. If distance is less than or equal to r1 + r2, the circles are colliding. If not, they aren't!
    
    """
    def collides_with(self, circle_shape_object):
        distance = self.position.distance_to(circle_shape_object.position)
        r1 = self.radius
        r2 = circle_shape_object.radius

        if distance <= (r1 + r2):
            return True
        return False
    

