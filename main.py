import pygame
from board import Board





# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

board = Board(WHITE,BLACK,HEIGHT,WIDTH)
board.setUpWindow()
board.setUpBoard()
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    board.setUpPieces(board)






    # Update the display
    pygame.display.flip()

pygame.quit()
