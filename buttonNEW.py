import pygame

class ButtonNew:
    def __init__(self, color, a_color, x,y,width,height, text=''):
        self.color = color
        self.a_color = a_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,action=None):
        #Call this method to draw the button on the screen
        mouse = pygame.mouse.get_pos()
        # if outline:
        #     pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
        if (self.x < mouse[0] < self.x + self.width) & (self.y < mouse[1] < self.y + self.height):
            pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        else:
            pygame.draw.rect(win, self.a_color, (self.x,self.y,self.width,self.height),0)
    
        if self.text != '':
            #font = pygame.font.SysFont('comicsans', 30)
            #text = font.render(self.text, 1, (0,0,0))
            font_type = pygame.font.Font("Cloister Black Light.ttf", 30)
            text = font_type.render(self.text, True, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True
        return False