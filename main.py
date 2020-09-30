import pygame
from Boss import Boss
from Shot import Shot
from Player import Player

pygame.init()
display_width = 600
display_height = 600

display = pygame.display.set_mode((display_width, display_width))
pygame.display.set_caption('BPM Shooting')
icon = pygame.image.load('boss1.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

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

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LSHIFT] & keys[pygame.K_w]:
            player.moveUp(True)
        elif keys[pygame.K_w]:
            player.moveUp(False)

        if keys[pygame.K_LSHIFT] & keys[pygame.K_s]:
            player.moveDown(True)
        elif keys[pygame.K_s]:
            player.moveDown(False)

        if keys[pygame.K_LSHIFT] & keys[pygame.K_a]:
            player.moveLeft(True)
        elif keys[pygame.K_a]:
            player.moveLeft(False)

        if keys[pygame.K_LSHIFT] & keys[pygame.K_d]:
            player.moveRight(True)
        elif keys[pygame.K_d]:
            player.moveRight(False)

        display.fill((0, 0, 0))
        pygame.draw.rect(display, (255, 255, 255), (boss.x, boss.y, boss.width, boss.height))
        pygame.draw.rect(display, (0, 0, 255), (player.x, player.y, player.width, player.height))
        Shot.move(shot)
        pygame.display.update()
        clock.tick(100)



run_game()