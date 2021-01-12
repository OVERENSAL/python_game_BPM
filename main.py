import pygame
from Boss import Boss
from Shot import Shot
from Player import Player
from Display import Display
from Button import Button
from buttonNEW import ButtonNew
    
def run_game():
    game = True
    speed = 3
    line1 = display_width // 2 - 108
    line2 = display_width // 2 - 54
    line3 = display_width // 2
    line4 = display_width // 2 + 54
    line5 = display_width // 2 + 108
    shotes = [
        Shot((255, 0, 0), 25, line1, 0),
        Shot((255, 0, 0), 25, line2, 0),
        Shot((255, 0, 0), 25, line3, 0),
        Shot((255, 0, 0), 25, line4, 0),
        Shot((255, 0, 0), 25, line5, 0),
    ]
    #boss = Boss(display_width // 2, 30, 20, 30)
    player = Player(display_width // 2, display_height - 40, 15, 15)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.moveLeft()
                if event.key == pygame.K_RIGHT:
                    player.moveRight()     

        display.fill((0, 0, 0))
        #pygame.draw.rect(display, (255, 255, 255), (boss.x, boss.y, boss.width, boss.height))
        pygame.draw.rect(display, (0, 0, 255), (player.x, player.y, player.width, player.height))
        shotes[0].draw(speed)
        if(shotes[0].isRunAway()):
            shotes[1].draw(speed)
        if(shotes[1].isRunAway()):
            shotes[2].draw(speed)
        if(shotes[2].isRunAway()):
            shotes[3].draw(speed)
        if(shotes[3].isRunAway()):
            shotes[4].draw(speed)
        if(shotes[4].isRunAway()):
            shotes[0].draw(speed)
        pygame.display.update()

        for shot in shotes:
            if(shot.isShotTouchPoint(player.x, player.y)):
                player.hp-=1
                
                    

        clock.tick(100)

def show_menu():
    pygame.mixer.music.load('JohnMurphy-InTheHouseInAHeartbeat.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    menu_background = pygame.image.load('music.jpg')
    #button = Button(100, 50)
    buttonq = ButtonNew((190, 253, 170), (23, 204, 58), Display.display_width // 2-40, Display.display_height // 2 + 50, 100, 50, 'hello')
    show = True

    while show:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            if(event.type == pygame.MOUSEBUTTONUP):
                if(buttonq.isOver(pygame.mouse.get_pos())):
                    pygame.mixer.music.unload()
                    return
        display.blit(menu_background, (0, 0))
        buttonq.draw(display)
        #if(buttonq.isClicked(pygame.mouse.get_pos())):

        pygame.display.update()
        clock.tick(60)
pygame.init()
    

display_width = Display.display_width
display_height = Display.display_height
display = Display.display

pygame.display.set_caption('BPM Shooting')
icon = pygame.image.load('boss1.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

show_menu()
run_game()
while(game_over()):
    run_game()