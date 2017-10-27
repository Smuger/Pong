#from tinydb import Query
#from tinydb import TinyDB
import random, pygame, sys
from pygame.locals import *

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
pygame.display.set_caption("Kwietniewski")
play = True

pygame.init()
pygame.font.init()

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

def init():
    global paddle1_pos, paddle2_pos, ball_pos, paddle1_vel, paddle2_vel
    paddle1_pos = [32, H_HEIGHT - 32]
    paddle2_pos = [WIDTH - 32, H_HEIGHT - 32]
    ball_pos = [H_WIDTH - 8, H_HEIGHT - 8]
    paddle1_vel = 0
    paddle2_vel = 0

def draw(window):
    global paddle1_pos, paddle2_pos, ball_pos, paddle1_vel, paddle2_vel, score1, score2, play
    if play:
        window.fill(WHITE)
        pygame.draw.rect(window, BLACK, (0, 8, WIDTH, HEIGHT - 16))
        pygame.draw.line(window, WHITE, (H_WIDTH, 0), (H_WIDTH, HEIGHT))
        pygame.draw.rect(window, WHITE, (paddle1_pos[0], paddle1_pos[1], paddle_width, paddle_height))
        pygame.draw.rect(window, WHITE, (paddle2_pos[0], paddle2_pos[1], paddle_width, paddle_height))
        pygame.draw.circle(window, WHITE, (int(ball_pos[0]), int(ball_pos[1])), 16)

        #Fizyka paletka 1
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
        score = text.render(str(score1) + " : " + str(score2), 1, WHITE)
        score_width, score_height = text.size((str(score1) + " : " + str(score2)))
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

def keyup(event):
    global  paddle1_vel, paddle2_vel
    if event.key in (K_w, K_s):
        paddle1_vel = 0
    elif event.key in (K_UP, K_DOWN):
        paddle2_vel = 0

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