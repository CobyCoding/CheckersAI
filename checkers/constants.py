import pygame

# Global Variables

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS
FPS = 60
PADDING = 15
BORDER = 2

# Colors
# rgb

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0 , 255)
GRAY = (128, 128, 128)

# Images

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (45, 25))
