import random
import pygame, sys
from pygame.locals import *

pygame.init()

def ball_init():

def init():

def draw():

def keydown(event):
    global paddle1_vel, paddle2_vel

    if event.key == K_UP:
        paddle2_vel = -8
    elif event.key == K_DOWN:
        paddle2_vel = 8
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

