import pygame

display_width = 600
display_height = 600

display = pygame.display.set_mode((display_width, display_width))

class Shot:
    def __init__(self, color, radius, x, y):
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y

    def draw(self, speed):
        if (self.y <= display_height):
            pygame.draw.circle(display, self.color, (self.x, self.y), self.radius)
            self.y += speed
    
    def isRunAway(self):
        if(self.y > display_height):
            return True
        return False

    def isShotTouchPoint(self, pointX, pointY):
        if((pointX - self.x)^2 + (pointY - self.y)^2 == self.radius^2):
            return True
        return False
