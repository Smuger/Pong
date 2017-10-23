from tinydb import Query
from tinydb import TinyDB
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
pygame.init()
pygame.font.init()

def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2

window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("siusiak")
window.fill(WHITE)
pygame.draw.rect(window, BLACK, (0, 8, WIDTH, HEIGHT - 16))
pygame.draw.rect(window, WHITE, (32, H_HEIGHT - 32, 16, 64))
pygame.draw.rect(window, WHITE, (WIDTH - 48, H_HEIGHT - 32, 16, 64))
pygame.draw.circle(window, WHITE, (H_WIDTH, H_HEIGHT), 10, 0)
pygame.draw.line(window, WHITE, (H_WIDTH, 0), (H_WIDTH, HEIGHT))

text = pygame.font.SysFont("", 64)
score = text.render( (str(score1) + " : " + str(score2)), 1, WHITE)

score_width, score_height = text.size((str(score1) + " : " + str(score2)))
window.blit(score, (H_WIDTH - score_width/2, 32))

def keydown(event):
    global paddle1_vel, paddle2_vel
    if event.key == K_w:
        paddle1_vel = -10
    elif event.key == K_s:
        paddle1_vel = 10
    elif event.key == K_UP:
        paddle2_vel = -10
    elif event.key == K_DOWN:
        paddle2_vel = 10

def keyup(event):
    global paddle1_vel, paddle2_vel
    if event.key in (K_w, K_s):
        paddle1_vel = 0
    elif event.key in (K_UP, K_DOWN):
        paddle2_vel = 0

pygame.display.update()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


