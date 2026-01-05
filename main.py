import pygame
import sys
import player
import asteroid
import asteroidfield
import shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event

def main():
    #Initialize pygame
    pygame.init()

    #Getting a new instance of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    #New clock object
    clock = pygame.time.Clock()


    
    #Creating new empty groups 
    updatable = pygame.sprite.Group() #This will hold all the objects that can be updated
    drawable = pygame.sprite.Group() #This will hold all the objects that can be drawn
    asteroids = pygame.sprite.Group() #This will hold all the objects from Asteroid
    shots = pygame.sprite.Group() #This will hold all the objects from Shot


    player.Player.containers = (updatable, drawable) #Adding the Player class to updatable and drawable groups
    asteroid.Asteroid.containers = (asteroids, updatable, drawable) #Ensuring that every instance of the Asteroid class is automatically added to these groups upon creation
    asteroidfield.AsteroidField.containers = (updatable) #Ensuring that every instance of the AsteroidField class is automatically added to this group upon creation
    shot.Shot.containers = (shots, updatable, drawable) #Ensuring that every instance of the Shot class is automatically added to these groups upon creation



    #New player object
    my_player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    #New AsteroidField object
    my_asteroid_field = asteroidfield.AsteroidField()

    

    """
    Delta Time
     It represents the amount of time that has passed since the last frame was drawn.
     This value is useful to decouple the game's speed from the speed it's being drawn to the screen.
    """
    dt = 0





    #Game Loop
    while True:
        log_state()



        """
        Check if the user has closed the window, and exit the game loop if they do.
        It will make the window's close button actually work.
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        



        screen.fill("black") #fill the screen with a solid black color


        #Rotate/move the player
        updatable.update(dt)


        #Check if any asteroid collides with the player
        for asteroid_instace in asteroids:
            if asteroid_instace.collides_with(my_player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()


        #Re-render the player on the screen each frame
        for instance in drawable:
            instance.draw(screen)

        

        pygame.display.flip() #refresh the screen




        """
        It will pause the game loop until 1/60th of a second has passed.
        It returns the amount of time that has passed since the last time it was called.
        and convert from milisenconds to seconds.
        """
        
        dt = clock.tick(60) / 1000

 

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")





    

"""
 This line ensures that the main function is called only when this file is run directly;
 it won't run if it's imported as a module. It's considered the "Pythonic" 
 way to structure an executable program in Python.

"""
if __name__ == "__main__":
    main()
