import pygame
from piece import Piece




piecesPlayer1 = [[Piece((255, 0, 0)) for _ in range(8)] for _ in range(2)]
piecesPlayer2 = [[Piece((0, 0, 255)) for _ in range(8)] for _ in range(2)]



class Board:

    def __init__(self,WHITE,BLACK,HEIGHT,WIDTH,BOARDSIZE):
        self.WHITE = WHITE
        self.BLACK = BLACK
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.BOARDSIZE = BOARDSIZE


    def setUpWindow(self):
        # Create the game window
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Checkers Game")
        # Clear the screen
        self.screen.fill(self.WHITE)
    
    def setUpBoard(self):
        rectangle = [[0 for _ in range(8)] for _ in range(8)]
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    #screen, color, rectangle(position, dimensions)
                        rectangle[row][col] = pygame.draw.rect(self.screen, self.BLACK, (col * (self.WIDTH // 8)\
                        , row * (self.HEIGHT // self.BOARDSIZE), self.WIDTH // self.BOARDSIZE, self.HEIGHT // self.BOARDSIZE))
                else:
                    #screen, color, rectangle(position, dimensions)
                        rectangle[row][col] = pygame.draw.rect(self.screen, self.WHITE, (col * (self.WIDTH // 8)\
                        , row * (self.HEIGHT // self.BOARDSIZE), self.WIDTH // self.BOARDSIZE, self.HEIGHT // self.BOARDSIZE))        
        return rectangle 


    def setUpPieces(self,board):
        #set up the initial position of the board
        #Example: Drawing a red checker piece in the middle of the first square
        checker_radius = min(self.WIDTH // 8, self.HEIGHT // 8) // 2 - 10
        for row in range(2): # top 2 rows of the board
            for col in range(8):
                piecesPlayer1[row][col].setPiece(board.screen, (col* (self.WIDTH // self.BOARDSIZE) + self.WIDTH //\
                    16, row * (self.HEIGHT // self.BOARDSIZE) + self.HEIGHT // 16), checker_radius) 
        #other player pieces
        for row in [6,7]: # top 2 rows of the board
            for col in range(8):
                piecesPlayer2[row-6][col].setPiece(board.screen, (col* (self.WIDTH // self.BOARDSIZE) + self.WIDTH //\
                    16, row * (self.HEIGHT // self.BOARDSIZE) + self.HEIGHT // 16), checker_radius)

        # print('x',piecesPlayer1[1][5].getPosition()[0], 'y', piecesPlayer1[1][5].getPosition()[1])

        # Add the initial pieces on the board
    def is_valid_move(self, move):
        # Check if a move is valid
        pass
    def normalizePosition(self,x,y):
        row = y//(self.HEIGHT//self.BOARDSIZE)
        col = x//(self.WIDTH//self.BOARDSIZE)
        return (row,col)





    '''
        def make_move(self, move):
            # Make a move on the board
    '''
