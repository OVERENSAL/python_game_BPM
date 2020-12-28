import pygame
from Boss import Boss
from Shot import Shot
from Player import Player
from Display import Display
from Button import Button

pygame.init()

display_width = Display.display_width
display_height = Display.display_height
display = Display.display

pygame.display.set_caption('BPM Shooting')
icon = pygame.image.load('boss1.png')
pygame.display.set_icon(icon)
pygame.mixer.music.load('JohnMurphy-InTheHouseInAHeartbeat.mp3')
pygame.mixer.music.set_volume(0.5)

clock = pygame.time.Clock()

def playerControl(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LSHIFT] & keys[pygame.K_UP]:
        self.moveUp(True)
    elif keys[pygame.K_UP]:
        self.moveUp(False)

    if keys[pygame.K_LSHIFT] & keys[pygame.K_DOWN]:
        self.moveDown(True)
    elif keys[pygame.K_DOWN]:
        self.moveDown(False)

    if keys[pygame.K_LSHIFT] & keys[pygame.K_LEFT]:
        self.moveLeft(True)
    elif keys[pygame.K_LEFT]:
        self.moveLeft(False)

    if keys[pygame.K_LSHIFT] & keys[pygame.K_RIGHT]:
        self.moveRight(True)
    elif keys[pygame.K_RIGHT]:
        self.moveRight(False)

def run_game():
    game = True
    shot = Shot(display_width // 2, 60, 5, 5)
    boss = Boss(display_width // 2, 30, 20, 30)
    player = Player(display_width // 2, display_height - 40, 10, 10)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        playerControl(player)

        display.fill((0, 0, 0))
        pygame.draw.rect(display, (255, 255, 255), (boss.x, boss.y, boss.width, boss.height))
        pygame.draw.rect(display, (0, 0, 255), (player.x, player.y, player.width, player.height))
        Shot.move(shot)
        pygame.display.update()
        clock.tick(100)

def show_menu():
    pygame.mixer.music.play(-1)
    menu_background = pygame.image.load('music.jpg')
    button = Button(100, 50)
    show = True

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.blit(menu_background, (0, 0))
        button.draw(Display.display_width // 2 - 40, Display.display_height // 2 + 50, "Pft,fkj", run_game)
        font_type = pygame.font.Font("Cloister Black Light.ttf", 30)
        text = font_type.render("Start", True, (0, 0, 0))
        display.blit(text, (Display.display_width // 2 - 23, Display.display_height // 2 + 52))


        pygame.display.update()
        clock.tick(60)

show_menu()
