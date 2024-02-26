import pygame
import sys
from button import ImageButton
from Bankbuttons import Numbutton
pygame.init()
MAX_FPS = 60
WIDTH=1280
HEIGHT=720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Bank game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
#Создание картинок:)
bg = pygame.image.load('images/Bankicon.png')
Bankomat=pygame.image.load('images/Bankomatik.png')
Bankomat=pygame.transform.scale(Bankomat,(450,800))
card=pygame.image.load('images/card.png')
card=pygame.transform.scale(card,(60,60))
numbutton=pygame.image.load('images/buttons.png')
numbutton=pygame.transform.scale(numbutton, (300, 300))
bg_sound = pygame.mixer.Sound('sounds/Bs.mp3')
#bg_sound.play()
clock = pygame.time.Clock()

cursor = pygame.image.load("images/cursor.png")
cursor =pygame.transform.scale(cursor,(30,30))
hand = pygame.image.load("images/hand.png")
hand =pygame.transform.scale(hand,(30,30))
pygame.mouse.set_visible(False)

def main_menu():
    start_button = ImageButton(800, 352, 74, "Start", "images/button.png","images/hbutton.png", "sounds/button.mp3")
    settings_button = ImageButton(800, 452, 10,  "Settings", "images/button.png","images/hbutton.png", "sounds/button.mp3")
    exit_button = ImageButton(800, 552, 10, "Quit", "images/button.png","images/hbutton.png", "sounds/button.mp3")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        # pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.USEREVENT and event.button == start_button:
                print("Кнопка 'Start' была нажата!")
                fade()
                start_menu()
            if event.type == pygame.USEREVENT and event.button == settings_button:
                print("Кнопка 'Настройки' была нажата!")
                fade()
                settings_menu()
            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()
            for btn in [start_button,settings_button,exit_button]:
                btn.handle_event(event)
        for btn in [start_button,settings_button,exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        x,y =pygame.mouse.get_pos()
        screen.blit(cursor,(x-2,y-2))


        pygame.display.flip()
def settings_menu():
    audio_button = ImageButton(800, 352, 74, "audio", "images/button.png","images/button.png" ,"sounds/button.mp3")
    video_button = ImageButton(800, 452, 10, "video", "images/button.png","images/button.png", "sounds/button.mp3")
    back_button = ImageButton(800, 552, 10, "back", "images/button.png","images/button.png", "sounds/button.mp3")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        # pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.USEREVENT and event.button == video_button:
                fade()
                videosettings_menu()
            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False
            for btn in [audio_button,video_button,back_button]:
                btn.handle_event(event)

        for btn in [audio_button,video_button,back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))
        pygame.display.flip()
def change_videomode(w,h,fullscreen =0,):
    global WIDTH, HEIGHT, screen,bg
    WIDTH,HEIGHT = w,h
    screen = pygame.display.set_mode((WIDTH, HEIGHT),fullscreen)
    bg = pygame.image.load('images/Bankicon.png')

def videosettings_menu():
    video_button = ImageButton(800, 252, 74, "1280-720", "images/button.png", "images/button.png", "sounds/button.mp3")
    video1_button = ImageButton(800, 352, 10, "1280-800", "images/button.png", "images/button.png", "sounds/button.mp3")
    video2_button = ImageButton(800, 452, 10, "FULL HD", "images/button.png", "images/button.png", "sounds/button.mp3")
    back_button = ImageButton(800, 552, 10, "back", "images/button.png", "images/button.png", "sounds/button.mp3")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        # pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.USEREVENT and event.button == video_button:
                WIDTH = 1280
                HEIGHT = 720
                fade()
                running=False
            if event.type == pygame.USEREVENT and event.button == video1_button:
                change_videomode(1600, 720)
                WIDTH = 1600
                HEIGHT = 720
                fade()
                running=False
            if event.type == pygame.USEREVENT and event.button == video2_button:
                change_videomode(1920, 1080,pygame.FULLSCREEN)
                fade()
                running=False
            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False
            for btn in [video_button, video1_button,video2_button, back_button]:
                btn.handle_event(event)

        for btn in [video_button, video1_button,video2_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))
        pygame.display.flip()

def start_menu():
    bankomat_button = ImageButton(500, 452, 74, "Bankomat", "images/button.png", "sounds/button.mp3")
    back_button = ImageButton(500, 552, 74, "Back", "images/button.png", "sounds/button.mp3")
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == bankomat_button:
                print("Кнопка банкомат была нажата")
                fade()
                running = False
                bankomat1()
            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False
            for btn in [bankomat_button,back_button]:
                btn.handle_event(event)

        for btn in [back_button,bankomat_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x - 2, y - 2))
        pygame.display.flip()
def bankomat1():

    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(Bankomat, (430, -40))
        card_button = Numbutton(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.USEREVENT and event.Bankbuttons == card_button:
                print("OK")
                fade()
                bank_buttons()
            for btn in [card_button]:
                btn.handle_event(event)
        pos_x,pos_y = Pos(str(pygame.mouse.get_pos()),"x"), Pos(str(pygame.mouse.get_pos()),"y")
        print(pos_x,pos_y)
        x, y = pygame.mouse.get_pos()
        screen.blit(hand, (x - 2, y - 2))
        pygame.display.flip()


def bank_buttons():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(Bankomat, (430, -40))
        screen.blit(card, (772, 327))
        screen.blit(numbutton, (500,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        x, y = pygame.mouse.get_pos()
        screen.blit(hand, (x - 2, y - 2))
        pygame.display.flip()


def loading():
    running = True
    while running:
        screen.fill((0, 0, 0))

        screen.blit(player,(300,250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        x, y = pygame.mouse.get_pos()
        screen.blit(hand, (x - 2, y - 2))
        pygame.display.flip()


def fade():
    running= True
    fade_alpha = 0

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        fade_surface = pygame.Surface((1280,720))
        fade_surface.fill((0,0,0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface,(0,0))

        fade_alpha +=5
        if fade_alpha>= 105:
            fade_alpha = 255
            running = False

        pygame.display.flip()
        clock.tick(MAX_FPS)
def Pos(pos,xy):
    pos_x,pos_y="",""
    bool_x,bool_y= False,False
    for i in range(len(pos)):
        if pos[i] == "(" and xy =="x":
            bool_x=True
        elif bool_x == True and pos[i]!="," and xy =="x":
            pos_x +=pos[i]
        elif pos[i] =="," and xy == "x":
            bool_x = False
        elif pos[i] == " " and xy == "y":
            bool_y = True
        elif bool_y == True and pos[i] != ")" and xy == "y":
            pos_y += pos[i]
        elif pos[i]== ")" and xy == "y":
            bool_y = False
    if xy =="x":
        return int(pos_x)
    elif xy == "y":
        return int(pos_y)
if __name__=="__main__":
    main_menu()



