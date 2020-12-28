import pygame
from Display import Display

class Button:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (x < mouse[0] < x + self.width) & (y < mouse[1] < y + self.height):
            pygame.draw.rect(Display.display, (23, 204, 58), (x, y, self.width, self.height))

            if click[0] == 1 and action is not None:
                action() #добавить звук нажатия кнопки

        else:
            pygame.draw.rect(Display.display, (190, 253, 170), (x, y, self.width, self.height))

        #self.b
