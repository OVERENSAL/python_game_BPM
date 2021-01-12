import pygame
from Display import Display

display_width = Display.display_width
display_height = Display.display_height

display = pygame.display.set_mode((display_width, display_height))

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    hp = 3
    line1 = display_width // 2 - 108
    #line2 = display_width // 2 - 54
    #line3 = display_width // 2
    #line4 = display_width // 2 + 54
    line5 = display_width // 2 + 108

    def moveLeft(self):
        if(self.x != self.line1):
            self.x -= 54 

    def moveRight(self):
        if(self.x != self.line5):
            self.x += 54
