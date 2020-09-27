import pygame
from .board import Board
from .constants import RED, WHITE, BLUE, SQUARE_SIZE

class Game:
    """This class will handle everything from the board to events from

    Instead of our main.py main function doing it
    """
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        """This function will update the display of the game
        """
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
    
    def _init(self):
        """This function will initialize the game and set all the variables
        """
        self.selected = None # The piece the user has selected
        self.board = Board()
        self.turn = RED
        self.valid_moves = {} # What the current valid moves are

    def reset(self):
        """This function will reset the game
        """
        self._init()
    
    def draw_valid_moves(self, moves):
        """This function will draw the valid moves

        Args:
            moves (dict): The dict of all the valid moves
        """
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    def select(self, row, col):
        """This function will atempt to either move or select a piece depending on whether you have previously
        selected a piece.

        Args:
            row (int): The row to select
            col (int): The col to select

        Returns:
            bool: Whether the selection was successful
        """

        if self.selected: # If something is selected
            result = self._move(row, col) # If alread selected atempt to move the previously selected to the row and col given
            if not result: # If not valid
                self.selected = None # reset selection
                self.select(row, col) # reselect row col passed in

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn: # If the selected piece is the same color as whos tunr it is
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece) # Generate a dict of valid moves
            return True
        
        return False
    
    def winner(self):
        return self.board.winner()

    def _move(self, row, col):
        """This function will check whether a move is valid if so make the move

        Args:
            row (int): The row to move to
            col (int): The col to move to

        Returns:
            bool: Weather the move was successful
        """
        piece = self.board.get_piece(row, col)
        # If we selected a piece and that move is a valid move and the position to move to does not have a piece on it
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            # Capturing pieces
            
            skipped = self.valid_moves[(row, col)] # Get the piece the move skipped over
            if skipped: # If it did skip over a piece
                self.board.remove(skipped) # Remove the piece from the board

            self.change_turn()
        else:
            return False
        
        return True
    
    def change_turn(self):
        """This function will change whos  turn it is
        """
        self.valid_moves = {}
        self.turn = RED if self.turn == WHITE else WHITE
