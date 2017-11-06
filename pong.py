from tinydb import Query
from tinydb import TinyDB
import random, pygame, sys
from pygame.locals import *
import socket


WIDTH = 800
H_WIDTH = int(WIDTH/2)
HEIGHT = 600
H_HEIGHT = int(HEIGHT/2)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

score1 = 0
score2 = 0

paddle_width = 8
paddle_height = 64

ball_vel = [0, 0]
ball_pos = [0, 0]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]

window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Pong Game by Arkadiusz Biel & Krzysztof Kwietniewski")
play = True

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
#Losowanie kierunku rzutu pilki
L_or_R = random.randint(0, 3)
if L_or_R == 0:
    ball_vel = [-random.uniform(0, 1), -1]
elif L_or_R == 1:
    ball_vel = [-random.uniform(0, 1), 1]
elif L_or_R == 2:
    ball_vel = [random.uniform(0, 1), -1]
elif L_or_R == 3:
    ball_vel = [random.uniform(0, 1), 1]
def addscore():
    global users_table, db, scores
    # lastid
    user_count = len(scores)
    scores.insert({'score': int(v2.get()), 'uid': int(v.get()), 'id': user_count+1})

def seescore():
    global users_table, db, scores
def adduser():
    global users_table, db

def users():
    global users_table, db
    user_count = len(users_table)
    userlist = users_table.all();

    for i in range(0, user_count):
       print(i)

def game_intro():
    intro = True
    window.fill(BLACK)
    largeText = pygame.font.Font('freesansbold.ttf', 70)
    MenuText= pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects("The Pong Game", largeText)

    TextRect.center = ((WIDTH / 2), (HEIGHT / 2))
    window.blit(TextSurf, TextRect)
    pygame.display.update()
    pygame.time.wait(2000)
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                introkey(event)
                intro=False


        print("test");
        window.fill(BLACK)
        TextSurf, TextRect = text_objects("To start offline multiplayer click space", MenuText)

        TextRect.center = ((WIDTH/ 2), (HEIGHT / 2)-120)
        window.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("To start online multiplayer click enter", MenuText)
        TextRect.center = ((WIDTH / 2), (HEIGHT / 2) - 70)
        window.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("To join online multiplayer click J", MenuText)
        TextRect.center = ((WIDTH / 2), (HEIGHT / 2) - 20)
        window.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("To Quit click escape", MenuText)

        TextRect.center = ((WIDTH / 2), (HEIGHT / 2) +30)
        window.blit(TextSurf, TextRect)
        pygame.display.update()
def init():
    global paddle1_pos, paddle2_pos, ball_pos, paddle1_vel, paddle2_vel
    paddle1_pos = [32, H_HEIGHT  - 32]
    paddle2_pos = [WIDTH - 32, H_HEIGHT - 32]
    ball_pos = [H_WIDTH - 8, H_HEIGHT - 8]
    paddle1_vel = 0
    paddle2_vel = 0
def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()
def draw(window):
    global paddle1_pos, paddle2_pos, ball_pos, paddle1_vel, paddle2_vel, score1, score2, play
    if play:
        window.fill(WHITE)
        pygame.draw.rect(window, BLACK, (0, 8, WIDTH, HEIGHT - 16))
        pygame.draw.line(window, WHITE, (H_WIDTH, 0), (H_WIDTH, HEIGHT))
        pygame.draw.rect(window, WHITE, (paddle1_pos[0], paddle1_pos[1], paddle_width, paddle_height))
        pygame.draw.rect(window, WHITE, (paddle2_pos[0], paddle2_pos[1], paddle_width, paddle_height))
        pygame.draw.circle(window, WHITE, (int(ball_pos[0]), int(ball_pos[1])), 16)

        # Fizyka paletka 1
        if paddle1_pos[1] > 8 and paddle1_pos[1] < (HEIGHT - 72):
            paddle1_pos[1] += paddle1_vel
        elif paddle1_pos[1] == 8 and paddle1_vel > 0:
            paddle1_pos[1] += paddle1_vel
        elif paddle1_pos[1] == (HEIGHT - 72) and paddle1_vel < 0:
            paddle1_pos[1] += paddle1_vel

        #Fizyka paletka 2
        if paddle2_pos[1] > 8 and paddle2_pos[1] < (HEIGHT - 72):
            paddle2_pos[1] += paddle2_vel
        elif paddle2_pos[1] == 8 and paddle2_vel > 0:
            paddle2_pos[1] += paddle2_vel
        elif paddle2_pos[1] == (HEIGHT - 72) and paddle2_vel < 0:
            paddle2_pos[1] += paddle2_vel

        #Ruszaie sie pilki
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        #Fizyka pilki
        if ball_pos[1] == 8 or ball_pos[1] == (HEIGHT - 8):
            ball_vel[1] = -ball_vel[1]

        #Odbijanie paletki
        elif int(ball_pos[0]) == 48:
            if ball_pos[1] in range(paddle1_pos[1], paddle1_pos[1] + 64):
                ball_vel[0] = -ball_vel[0]

        elif int(ball_pos[0]) == WIDTH - 40:
            if ball_pos[1] in range(paddle2_pos[1], paddle2_pos[1] + 64):
               ball_vel[0] = -ball_vel[0]
        elif int(ball_pos[0]) == 47:
            score2 += 1
            init()
            play = False
        elif int(ball_pos[0]) == WIDTH - 39:
            score1 += 1
            init()
            play = False

        #Wyniki
        text = pygame.font.SysFont("", 64)
        n2 = len(str(score1)) - len(str(score2))
        n2 = n2 < 0 and 0 or n2
        n = len(str(score2)) - len(str(score1))
        n = n < 0 and 0 or n
        score_text = ("0" * n + str(score1) + " : " + "0" * n2 + str(score2))
        score = text.render(score_text, 1, WHITE)
        player1 = text.render("Player1", 1, WHITE)
        player2 = text.render("Player2", 1, WHITE)
        score_width, score_height = text.size(score_text)
        player2_width, player2_height = text.size("Player2")
        window.blit(player1, (32,32))
        window.blit(player2,  (H_WIDTH*2 - (player2_width+32), 32))
        window.blit(score, (H_WIDTH - score_width / 2, 32))

def keydown(event):
    global paddle1_vel, paddle2_vel, play
    if event.key == K_w:
        paddle1_vel = -2
    elif event.key == K_s:
        paddle1_vel = 2
    elif event.key == K_UP:
        paddle2_vel = -2
    elif event.key == K_DOWN:
        paddle2_vel = 2
    elif event.key == K_SPACE:
        play = True
def introkey(event):
    if event.key == K_SPACE:
        gamemode = 0
    elif event.key == K_KP_ENTER:
        gamemode = 1
def keyup(event):
    global  paddle1_vel, paddle2_vel
    if event.key in (K_w, K_s):
        paddle1_vel = 0
    elif event.key in (K_UP, K_DOWN):
        paddle2_vel = 0
is_intro=True
#game_intro(is_intro)
game_intro()
init()
running = True
while running:
    draw(window)
    pygame.display.update()
    print(str(play))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            keydown(event)
        elif event.type == KEYUP:
            keyup(event)
        elif event.type == QUIT:
            pygame.quit()
            quit()