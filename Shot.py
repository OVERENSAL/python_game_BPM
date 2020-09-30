import pygame

display_width = 600
display_height = 600

display = pygame.display.set_mode((display_width, display_width))

class Shot:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self):
        if (self.y <= display_height):
            pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height))
            self.y += 3
        else:
            self.y = 50

