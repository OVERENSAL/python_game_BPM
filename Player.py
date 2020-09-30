import pygame

display_width = 600
display_height = 600

display = pygame.display.set_mode((display_width, display_width))

moveSpeed = 2
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
            if (self.x - moveSpeed > 0):
                self.x -= moveSpeed

    def moveRight(self, slowdown):
        global moveSpeed, slowdownMoveSpeed
        if (slowdown == True):
            if (self.x + slowdownMoveSpeed < display_width - self.width):
                self.x += slowdownMoveSpeed
        else:
            if (self.x + moveSpeed < display_width - self.width):
                self.x += moveSpeed
