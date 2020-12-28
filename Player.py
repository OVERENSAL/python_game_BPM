import pygame
from Display import Display

display_width = Display.display_width
display_height = Display.display_height

display = pygame.display.set_mode((display_width, display_height))

moveSpeed = 4
slowdownMoveSpeed = moveSpeed // 2

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def moveUp(self, slowdown):
        global moveSpeed, slowdownMoveSpeed
        if (slowdown == True):
            if (self.y - slowdownMoveSpeed > 100):
                self.y -= slowdownMoveSpeed
        else:
            if (self.y - moveSpeed > 100):
                self.y -= moveSpeed

    def moveDown(self, slowdown):
        global moveSpeed, slowdownMoveSpeed
        if (slowdown == True):
            if (self.y + slowdownMoveSpeed < display_height - self.height):
                self.y += slowdownMoveSpeed
        else:
            if (self.y + moveSpeed < display_height - self.height):
                self.y += moveSpeed

    def moveLeft(self, slowdown):
        global moveSpeed, slowdownMoveSpeed
        if (slowdown == True):
            if (self.x - slowdownMoveSpeed > 0):
                self.x -= slowdownMoveSpeed
            else:
                self.x = display_width
        else:
            if (self.x - moveSpeed > 0):
                self.x -= moveSpeed
            else:
                self.x = display_width

    def moveRight(self, slowdown):
        global moveSpeed, slowdownMoveSpeed
        if (slowdown == True):
            if (self.x + slowdownMoveSpeed < display_width - self.width):
                self.x += slowdownMoveSpeed
            else:
                self.x = 0
        else:
            if (self.x + moveSpeed < display_width - self.width):
                self.x += moveSpeed
            else:
                self.x = 0
