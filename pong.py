#from tinydb import Query
#from tinydb import TinyDB
import random
import pygame, sys
from pygame.locals import *

HEIGHT = 600
WIDTH = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
H_WIDTH = int(WIDTH/2)
H_HEIGHT = int(HEIGHT/2)
score1 = 0
score2 = 0
paddle1_vel = 0
paddle2_vel = 0
L_or_R = random.randint(0, 1)

if L_or_R == 0:
    ball_vel = [random.uniform(-1, -0.5), random.uniform(-1, 1)]
else:
   ball_vel = [random.uniform(0.5, 1), random.uniform(-1, 1)]


pygame.init()
pygame.font.init()
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("siusiak")


def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos
    global score1, score2
    paddle1_pos = [32, H_HEIGHT - 32]
    paddle2_pos = [WIDTH - 48, H_HEIGHT - 32]
    ball_pos = [H_WIDTH, H_HEIGHT]


def draw(window):
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel
    window.fill(WHITE)
    pygame.draw.rect(window, BLACK, (0, 8, WIDTH, HEIGHT - 16))
    pygame.draw.line(window, WHITE, (H_WIDTH, 0), (H_WIDTH, HEIGHT))
    pygame.draw.rect(window, WHITE, (paddle1_pos[0], paddle1_pos[1], 16, 64))
    pygame.draw.rect(window, WHITE, (paddle2_pos[0], paddle2_pos[1], 16, 64))
    pygame.draw.circle(window, WHITE, (int(ball_pos[0]), int(ball_pos[1])), 10, 0)

    if paddle1_pos[1] > 8 and paddle1_pos[1] < (HEIGHT - 72):
        paddle1_pos[1] += paddle1_vel
    elif paddle1_pos[1] == 8 and paddle1_vel > 0:
        paddle1_pos[1] += paddle1_vel
    elif paddle1_pos[1] == (HEIGHT - 72) and paddle1_vel < 0:
        paddle1_pos[1] += paddle1_vel
    if paddle2_pos[1] > 8 and paddle2_pos[1] < (HEIGHT - 72):
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == 8 and paddle2_vel > 0:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == (HEIGHT - 72) and paddle2_vel < 0:
        paddle2_pos[1] += paddle2_vel

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    if ball_pos[1] < 19 or ball_pos[1] > (HEIGHT - 18):
        ball_vel[1] = -ball_vel[1]

    elif ball_pos[0] == 48 and ball_pos[1] >= paddle1_pos[1] and ball_pos[1] <= (paddle1_pos[1] + 64):
        ball_vel[0] = -ball_vel[0]
    elif ball_pos[0] == 752 and ball_pos[1] >= paddle2_pos[1] and ball_pos[1] <= (paddle2_pos[1] + 64):
        ball_vel[0] = -ball_vel[0]

    text = pygame.font.SysFont("", 64)
    score = text.render( (str(score1) + " : " + str(score2)), 1, WHITE)

    score_width, score_height = text.size((str(score1) + " : " + str(score2)))
    window.blit(score, (H_WIDTH - score_width/2, 32))

def keydown(event):
    global paddle1_vel, paddle2_vel
    if event.key == K_w:
        paddle1_vel = -2
    elif event.key == K_s:
        paddle1_vel = 2
    elif event.key == K_UP:
        paddle2_vel = -2
    elif event.key == K_DOWN:
        paddle2_vel = 2

def keyup(event):
    global paddle1_vel, paddle2_vel
    if event.key in (K_w, K_s):
        paddle1_vel = 0
    elif event.key in (K_UP, K_DOWN):
        paddle2_vel = 0

init()

running = True

while running:

    draw(window)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            keydown(event)
        elif event.type == KEYUP:
            keyup(event)
        elif event.type == pygame.QUIT:
            running = False
    pygame.display.update()

