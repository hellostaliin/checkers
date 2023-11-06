import pygame
from board import Board
from piece import PIECE




# Initialize Pygame
pygame.init()





# Constants
WIDTH, HEIGHT = 800, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BOARDSIZE = 8

board = Board(WHITE,BLACK,HEIGHT,WIDTH,BOARDSIZE)
board.setUpWindow()
rectangle = board.setUpBoard()
# print(len(rectangle)) # number rows
# print(len(rectangle[0])) # number colms
# print(rectangle[0][1].x,rectangle[0][1].y)
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    board.setUpPieces(board)
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        x, y = pygame.mouse.get_pos()
        # print(x,y)  
        # Calculate the square (row, col) clicked
        rowClick = board.normalizePosition(x,y)[0]#not so good : its bcz i force the board size to be 800..
        colClick = board.normalizePosition(x,y)[1]
        
        for piece in 
        # Check if there is a piece in the clicked square
        # if rectangle[row][col] is not None:
        #     print("Piece clicked at row", row, "col", col)





    # Update the display
    pygame.display.flip()

pygame.quit()
