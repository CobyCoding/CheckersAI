import pygame
from .constants import RED, WHITE, SQUARE_SIZE, PADDING, BORDER, GRAY, CROWN

class Piece():
    """This class will hold all the infomation about a certain piece
    """
    
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        self.x = 0
        self.y = 0
        self.calculate_pos()
    
    def move(self, row, col):
        """This function will move the piece to the given row and column

        Args:
            row (int): The row you want to move to
            col (int): The column you want to move to
        """

        self.row = row
        self.col = col
        self.calculate_pos() # Recalculate the x and y positions

    def calculate_pos(self):
        """This function will calculate the x and y position
        by the row and col defined in self
        """

        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2 # Gets the coordinate of the x axis in the middle of the piece
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2 # Gets the coordinate of the y axis in the middle of the piece
    
    def make_king(self):
        """This function will simply make this piece a king
        """
        self.king = True
    
    def draw(self, win):
        radius = SQUARE_SIZE // 2 - PADDING # Calculate the radius of the circle
        pygame.draw.circle(win, GRAY, (self.x, self.y), radius + BORDER)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))
    
    def __repr__(self):
        return str(self.color)