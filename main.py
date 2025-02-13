import pygame
from constants import *

def __init_game():
    sucesses, failures = pygame.init()
    pygame.init()
    print(f"""
PYGAME START RESULTS
___________________________________________
         
SUCCESSES: {sucesses}, FAILURES: {failures}
___________________________________________
            """)

def __game_start():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}") 

def game_running():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        screen.fill((32, 31, 30))
        pygame.display.flip()
    

def main():
    __init_game()
    __game_start()
    game_running()
    
    

if __name__ == "__main__":
    main()