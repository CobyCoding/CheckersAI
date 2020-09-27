import pygame
from .constants import BLACK, RED, WHITE, ROWS, COLS, SQUARE_SIZE
from .piece import Piece

class Board:
    """This class will deal with the board. This will include

    Drawing itself onto screen
    Deleting pieces of screen
    Keeping track of pieces
    """
    def __init__(self):
        self.board = [] # A 2d list storing a representation of the board
        self.selected_piece = None # The piece the user has selected
        self.red_left = self.white_left = 12 # How many of each teams pieces are still on the board
        self.red_kings = self.white_kings = 0
        self.create_board()

    def get_piece(self, row, col):
        """This function will get the piece object that is at a given row and column

        Args:
            row (int): The row of the piece object you wish to get
            col (int): The column of the piece object you wish to get

        Returns:
            piece object: The piece object at the given row and column
        """
        return self.board[row][col]

    def move(self, piece, row, col):
        """This function will move a piece to the given row and column  

        Args:
            piece (Piece object): The piece you wish to move
            row (int): The row you wish to move to
            col (int): The column you wish to move to
        """
        try:
            self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        except AttributeError:
            return None
        except Exception as e:
            print(e)

        piece.move(row, col)

        if row == ROWS or row == 0:
            piece.make_king() # Make a piece a king
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1

    def draw_squares(self, win):
        """A function that will draw the background of the board

        Args:
            win (Pygame surface): The pygame surface you want to draw on
        """

        win.fill(BLACK) # Fill the screen with black
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    def create_board(self):
        """This function will add all of the standered starting pieces to the board list
        """
        for row in range(ROWS):
            self.board.append([]) # Append new list signifing a new row
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2): # I dont understand go watch this https://youtu.be/LSYj8GZMjWY?t=109
                    if row < 3: # If want to create red piece
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    
    def draw(self, win):
        """This function will draw the board

        Args:
            win (pygame surface): The pygame surface you want the board to be drawed on
        """
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

if __name__ == "__main__":
    pass