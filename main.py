import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    #Initialize pygame
    pygame.init()

    #Getting a new instance of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
        pygame.display.flip() #refresh the screen



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
