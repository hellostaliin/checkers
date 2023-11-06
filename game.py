import pygame
from piece import Piece

class Game:
    #def __init__(self):
        

    def switch_player(self):
        # Switch to the other player

    def play(self):
        # Implement the game loop
        pass
    def checkMouseClick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Check for left mouse button click
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Now, check if the click was within the boundaries of your object
                if object_rect.collidepoint(mouse_x, mouse_y):
                    # The click was on the object
                    print("Object clicked")


    