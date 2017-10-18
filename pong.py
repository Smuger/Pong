from tinydb import Query
from tinydb import TinyDB
import random
import pygame, sys
from pygame.locals import *

pygame.init()

#Zmienne
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HEIGHT = 1600
WIDTH = 900
window = pygame.display.set_mode((WIDTH,HEIGHT),0,32)

def ball_init():


def init():
    global paddle1_pos, paddle2_pos

def draw(canvas):
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos
    global l_score, r_score

    pygame.canvas.fill(WHITE,0,0)

def keydown(event):
    global paddle1_vel, paddle2_vel

    if event.key == K_UP:
        paddle2_vel = -8
    elif event.key == K_DOWN:
        paddle2_vel = 80
    elif event.key == K_w:
        paddle1_vel = 8
    elif event.key == K_s:
        paddle1_vel = -8

def keyup(event):

    global paddle1_vel, paddle2_vel

    if event.key (K_UP, K_DOWN):
        paddle2_vel = 0
    elif event.key (K_w, K_s):
        paddle1_vel = 0

