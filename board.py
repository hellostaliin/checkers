import pygame


class Board:

    def __init__(self,WHITE,BLACK,HEIGHT,WIDTH):
        # Initialize the board and set up the initial piece positions
        #self.grid = [[None for _ in range(8)] for _ in range(8)]
        #self.screen = screen
        self.WHITE = WHITE
        self.BLACK = BLACK
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH

    def setUpWindow(self):
        # Create the game window
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Checkers Game")
        # Clear the screen
        self.screen.fill(self.WHITE)
    
    def setUpBoard(self):
        for row in range(8):
                for col in range(8):
                    if (row + col) % 2 == 0:
                        #screen, color, rectangle(position, dimensions)
                        pygame.draw.rect(self.screen, self.BLACK, (col * (self.WIDTH // 8)\
                            , row * (self.HEIGHT // 8), self.WIDTH // 8, self.HEIGHT // 8))



    def setUpPieces(self,board):
        #set up the initial position of the board
        #Example: Drawing a red checker piece in the middle of the first square
        checker_radius = min(self.WIDTH // 8, self.HEIGHT // 8) // 2 - 10
        for row in range(2): # top 2 rows of the board
            for col in range(8):
                pygame.draw.circle(board.screen, (255, 0, 0), (col* (self.WIDTH // 8) + self.WIDTH //\
                    16, row * (self.HEIGHT // 8) + self.HEIGHT // 16), checker_radius) 
        #other player pieces
        for row in [6,7]: # top 2 rows of the board
            for col in range(8):
                pygame.draw.circle(board.screen, (0, 0, 255), (col* (self.WIDTH // 8) + self.WIDTH //\
                    16, row * (self.HEIGHT // 8) + self.HEIGHT // 16), checker_radius) 

        # Add the initial pieces on the board
    def is_valid_move(self, move):
        # Check if a move is valid
        pass
    '''
        def make_move(self, move):
            # Make a move on the board
    '''
