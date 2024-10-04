import pygame
from pygame.draw import *

from random import randint

import math

pygame.init()

FPS = 30
#screen
screen = pygame.display.set_mode((600, 400))
#colours
RED=(255,0,0)
GREEN=(0,255,0)
SKY_BLUE = (0,255,255)
LIGHT_GRAY = (200,200,200)
BLACK=(0,0,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
BROWN=(150,40,0)
ORANGE=(255,100,10)
FOREST_GREEN=(0,50,0)
#sky
screen.fill(SKY_BLUE)
#grass
rect(screen, GREEN, (0, 200, 600, 200))
#house
rect(screen, BROWN, (100, 150, 160, 120))
aalines(screen, BLACK, True, [[100,150],[260,150],
                              [260,270],[100,270],
                              [100,150]])
#roof
polygon(screen, RED, [[100,150],[180,90],[260,150]])
aalines(screen, BLACK, True, [[100,150],[180,90],[260,150]])
#window
rect(screen, BLUE, (160, 190, 40, 40))
aalines(screen, ORANGE, True, [[160,190],[200,190],
                              [200,230],[160,230],
                              [160,190]])
#cloud
for i in range(15):
    x=randint(320,420)
    y=randint(40,70)
    circle(screen, LIGHT_GRAY, (x,y),30)
#tree
rect(screen, BROWN, (470, 130, 20, 120))
for i in range(13):
    x=randint(450,500)
    y=randint(90,170)
    circle(screen, FOREST_GREEN, (x,y),30)
#sun
angle=0
x=530
y=40
circle(screen,(YELLOW),(530,40),20)
for i in range(12):
    angle_rad=2*math.pi*i /12
    end_x=x+20*2*math.cos(angle_rad)
    end_y=y+20*2*math.sin(angle_rad)
    polygon(screen,YELLOW,
        [(x,y), (end_x,end_y),
         (x+ 20 * math.cos(angle_rad+math.pi/12),
          y+ 20 * math.sin(angle_rad+math.pi/12))])
    
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
