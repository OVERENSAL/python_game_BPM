import pygame
import scipy
import scipy.io.wavfile
import scipy.signal
import time
import random
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from subprocess import call
from Boss import Boss
from Shot import Shot
from Player import Player
from Display import Display
from Button import Button
from buttonNEW import ButtonNew

def checkCollision(shots, i, lines):
    for shot in shots:
        if shot.x == lines[i]:
            if shot.y <= shot.radius * 3:
                return False
    return True

def draw_hp_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, (0, 255, 0), fill_rect)
    pygame.draw.rect(surf, (255, 255, 255), outline_rect, 2)

def run_game(file_path):

    music_file_name = file_path
    songs_file = ''
    lame_path = 'lame.exe'
    screen_w = display_width
    screen_h = display_height
    percentage_displayed_f = 0.007                                                                              #Percentage of frequencies to show (Removes higher frequencies) Range = [0, 1]
    max_height_percentile = 80
    fftlength = 2048
    entertainment = False

    while True:                                                                                                 #While no valid file
        if music_file_name[len(music_file_name)-4:] == '.mp3' and Path(lame_path).is_file():                #if mp3, convert if possible
            print('Attempting to convert mp3 file into wav')
            call(["lame", "--decode", music_file_name, music_file_name[:len(music_file_name)-4]+'.wav'], shell=True)
            music_file_name = music_file_name[:len(music_file_name)-4]+'.wav'
        elif music_file_name[len(music_file_name)-4:] != '.wav':
            music_file_name += '.wav'

        if songs_file != '':
            music_file_name = songs_file + "//" + music_file_name

        sr, original_signal = scipy.io.wavfile.read(music_file_name)
        break

    print("Found File!")
    print("Stereo to Mono Conversion")
    music = scipy.mean(original_signal, axis=1)                                                                 #Combining both ears (computationally intensive)

    print('Fourier Transform')                                                                                  #f, t are axis, Sxx is 2d array
    f, t, Sxx = scipy.signal.spectrogram(music, sr,nperseg=fftlength)                                           #Sxx[frequency][time]
    no_of_displayed_f = int(len(f)*percentage_displayed_f+0.5)
    Sxx = Sxx[:no_of_displayed_f-2].transpose()                                                                 #Sxx[time][frequency] Last Frequency at 10163.671875
    f = f[:no_of_displayed_f-2]

    print("Playing...")
    pygame.init()
    screen = pygame.display.set_mode((screen_w, screen_h))                                                      #creates main screen surface
    rect_scale_factor = screen_h/scipy.percentile(Sxx, max_height_percentile)
    done = False
    dt= t[1] - t[0]

    #Printing clock and title on bottom right
    pygame.font.init()
    myfont = pygame.font.SysFont('Verdana', 20)
    title = myfont.render(music_file_name, False, (0, 255, 255))

    #Initialising colour array for rectangles
    colours = []
    colour_f = 0.05                                                                                             #Colour Frequency
    for i in range(no_of_displayed_f):
        colours.append((225, 0, 0))

    #Initialising timer and music
    start_time = time.time()
    song = pygame.mixer.Sound(file_path)
    pygame.mixer.music.load(music_file_name)                                                                    #Load and play music
    pygame.mixer.music.play(1)

    #Precalulations to make animation smoother
    Sxx_len = len(Sxx)
    rect_width = screen_w/no_of_displayed_f
    done = False
    #Animation Loop

    game = True
    lines = [
        display_width // 2 - 108 -12,
        display_width // 2 - 54 -12,
        display_width // 2 -12,
        display_width // 2 + 54 -12,
        display_width // 2 + 108 -12
    ]
    shots0 = []
    shots1 = []
    shots2 = []
    shots3 = []
    shots4 = []
    #boss = Boss(display_width // 2, 30, 20, 30)
    player = Player(display_width // 2 - 7, display_height - 40, 14, 15)

    firstLineNodeNumber = 100
    secondLineNodeNumber = 100
    thirdLineNodeNumber = 100
    foursLineNodeNumber = 100
    fivesLineNodeNumber = 100

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
        if (not pygame.mixer.music.get_busy()):
            return player.hp

        display.fill((0, 0, 0))
        #pygame.draw.rect(display, (255, 255, 255), (boss.x, boss.y, boss.width, boss.height))
        pygame.draw.rect(display, (0, 0, 255), (player.x, player.y, player.width, player.height))

        for shot in shots0:
            if not(shot.isRunAway()):
                shot.draw(random.randint(3, 5))
                if shot.isShotTouchPoint(player.x, player.y):
                    player.hp-=5
                    shots0.remove(shot)
                    if player.hp == 0:
                        return 0
            else:
                shots0.remove(shot)
        for shot in shots1:
            if not(shot.isRunAway()):
                shot.draw(random.randint(3, 6))
                if shot.isShotTouchPoint(player.x, player.y):
                    player.hp-=5
                    shots1.remove(shot)
                    if player.hp == 0:
                        return 0             
            else:
                shots1.remove(shot)
        for shot in shots2:
            if not(shot.isRunAway()):
                shot.draw(random.randint(3, 6))
                if shot.isShotTouchPoint(player.x, player.y):
                    player.hp-=5
                    shots2.remove(shot)
                    if player.hp == 0:
                        return 0             
            else:
                shots2.remove(shot)
        for shot in shots3:
            if not(shot.isRunAway()):
                shot.draw(random.randint(3, 4))
                if shot.isShotTouchPoint(player.x, player.y):
                    player.hp-=5
                    shots3.remove(shot)
                    if player.hp == 0:
                        return 0            
            else:
                shots3.remove(shot)
        for shot in shots4:
            if not(shot.isRunAway()):
                shot.draw(random.randint(3, 5))
                if shot.isShotTouchPoint(player.x, player.y):
                    player.hp-=5
                    shots4.remove(shot)
                    if player.hp == 0:
                        return 0             
            else:
                shots4.remove(shot)

        draw_hp_bar(display, 10, 10, player.hp)


        pygame.display.update()

        clock.tick(100)

        cur_time = time.time() - start_time

        timer = myfont.render(str(int(cur_time))+ "s", False, (0, 255, 255))                                #Timer
                                                                                                            #Puts timer on screen                                                             #Puts sound file name on screen

        main_time_index = int(cur_time//dt)
        
        if int(cur_time) != int(song.get_length()):
            for index, frequency in enumerate(Sxx[(main_time_index)]):
                
                proportion_of_tleft = main_time_index - (main_time_index)
                height = max(proportion_of_tleft*frequency + (1- proportion_of_tleft)*Sxx[(main_time_index)+1][index], 2/rect_scale_factor)
                #Draws rectangles where height combines 2 nearest time bins by proportion for each frequency (height of 2px if no amplitude)
                if (index == 0):
                    if (height * rect_scale_factor > firstLineNodeNumber):
                        if (checkCollision(shots0, 0, lines)):
                            shots0.append(Shot((255, 0, 0), 24, lines[0], 0))
                        firstLineNodeNumber += 150
                    else:
                        if (firstLineNodeNumber > 600):
                            firstLineNodeNumber -= 5
                        firstLineNodeNumber -= 0.8
                if (index == 1):
                    if (height * rect_scale_factor > secondLineNodeNumber):
                        if (checkCollision(shots1, 1, lines)):
                            shots1.append(Shot((255, 0, 0), 24, lines[1], 0))
                        secondLineNodeNumber += 200
                    else:
                        if (secondLineNodeNumber > 1000):
                            secondLineNodeNumber -= 7
                        secondLineNodeNumber -= 1
                if (index == 2):
                    if (height * rect_scale_factor > thirdLineNodeNumber):
                        if (checkCollision(shots2, 2, lines)):
                            shots2.append(Shot((255, 0, 0), 24, lines[2], 0))
                        thirdLineNodeNumber += 300
                    else:
                        if (thirdLineNodeNumber > 700):
                            thirdLineNodeNumber -= 5
                        thirdLineNodeNumber -= 0.7
                if (index == 3):
                    if (height * rect_scale_factor > foursLineNodeNumber):
                        if (checkCollision(shots3, 3, lines)):
                            shots3.append(Shot((255, 0, 0), 24, lines[3], 0))
                        foursLineNodeNumber += 200
                    else:
                        if (foursLineNodeNumber > 1300):
                            foursLineNodeNumber -= 6
                        foursLineNodeNumber -= 0.7
                if (index == 4):
                    if (height * rect_scale_factor > fivesLineNodeNumber):
                        if (checkCollision(shots4, 4, lines)):
                            shots4.append(Shot((255, 0, 0), 24, lines[4], 0))
                        fivesLineNodeNumber += 100
                    else:
                        if (fivesLineNodeNumber > 800):
                            fivesLineNodeNumber -= 4
                        fivesLineNodeNumber -= 0.3


def show_menu(file_path):
    pygame.mixer.music.load('JohnMurphy-InTheHouseInAHeartbeat.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    menu_background = pygame.image.load('music.jpg')
    #button = Button(100, 50)
    buttonq = ButtonNew((190, 253, 170), (23, 204, 58), Display.display_width // 2-40, Display.display_height // 2 + 50, 100, 50, 'Start')

    show = True

    selectMusicBut = ButtonNew((190, 253, 170), (23, 204, 58), Display.display_width // 2-75, Display.display_height // 2 + 120, 170, 50, 'Select music')

    while show:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            if(event.type == pygame.MOUSEBUTTONUP):
                if(buttonq.isOver(pygame.mouse.get_pos())):
                    pygame.mixer.music.unload()
                    return file_path
                if (selectMusicBut.isOver(pygame.mouse.get_pos())):
                    root = tk.Tk()
                    root.withdraw()
                    file_path = filedialog.askopenfilename()
        display.blit(menu_background, (0, 0))
        buttonq.draw(display)
        selectMusicBut.draw(display)
        #if(buttonq.isClicked(pygame.mouse.get_pos())):

        pygame.display.update()
        clock.tick(60)

def game_over(file_path, hp):
    pygame.mixer.music.load('JohnMurphy-InTheHouseInAHeartbeat.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    menu_background = pygame.image.load('music.jpg')
    #button = Button(100, 50)
    mark = 'S'
    if(hp < 80):
        mark = 'A'
    if(hp < 60):
        mark = 'B'
    if(hp < 40):
        mark = 'C'
    if(hp < 20):
        mark = 'D'
    if hp == 0:
        result_game = ButtonNew((23, 204, 58), (23, 204, 58), Display.display_width // 2-75, Display.display_height // 2 - 50, 170, 50, 'LOOSER!!!')
    else:
        result_game = ButtonNew((23, 204, 58), (23, 204, 58), Display.display_width // 2-175, Display.display_height // 2 - 50, 350, 50, 'WINNER! \n Your mark:' + mark)

    restart_btn = ButtonNew((190, 253, 170), (23, 204, 58), Display.display_width // 2-40, Display.display_height // 2 + 50, 100, 50, 'Restart')
    show = True

    selectMusicBut = ButtonNew((190, 253, 170), (23, 204, 58), Display.display_width // 2-75, Display.display_height // 2 + 120, 170, 50, 'Select music')

    while show:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            if(event.type == pygame.MOUSEBUTTONUP):
                if(restart_btn.isOver(pygame.mouse.get_pos())):
                    pygame.mixer.music.unload()
                    return file_path
                if (selectMusicBut.isOver(pygame.mouse.get_pos())):
                    root = tk.Tk()
                    root.withdraw()
                    file_path = filedialog.askopenfilename()
        display.blit(menu_background, (0, 0))
        result_game.draw(display)
        restart_btn.draw(display)
        selectMusicBut.draw(display)
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

file_path = "1234.wav"
file_path = show_menu(file_path)
result = run_game(file_path)
while(True):
    file_path = game_over(file_path, result)
    result = run_game(file_path)
