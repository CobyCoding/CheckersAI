# Imports
import pygame
from checkers.constants import WIDTH, HEIGHT, FPS, SQUARE_SIZE, RED
from checkers.game import Game

# Initialize
pygame.init()

# Global Variables Defined In constants.py

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # The pygame window
pygame.display.set_caption("Checkers") # Set the pygame window caption

def row_col_from_mouse(pos):
    """This function will return the row and col that the mouse clicked on

    Args:
        pos (tuple): The mouse click position

    Returns:
        tuple: The row and col that the mouse was clicked on
    """
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    # What we run to run game
    
    run = True # If you want the game to run
    clock = pygame.time.Clock() # The fps speed of the game
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        if game.winner() != None:
            print(f"{game.winner()} has won!!!")
        # The pygame event handler

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If hit red cross on pygame window
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN: # If any button on mouse pressed down
                pos = pygame.mouse.get_pos()
                row, col = row_col_from_mouse(pos)

                game.select(row, col)
        
        game.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()