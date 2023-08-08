import pygame, sys
from pygame.locals import QUIT

import random
import time

import settings

import obj
from obj import ball
from obj import wall



### hyperparams ###

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500

###################



pygame.init()
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CENTER = pygame.Vector2(WINDOW.get_width() / 2, WINDOW.get_height() / 2)
clock = pygame.time.Clock()

bounceBall = ball(3, CENTER, pygame.Vector2(0, 0), 'bounceBall', 'red')

topWall = wall((WINDOW.get_width(), WINDOW.get_height() / 20), (0, 0), 'topWall', 'black')
bottomWall = wall((WINDOW.get_width(), WINDOW.get_height() / 20), (0, WINDOW.get_height() - (WINDOW.get_height() / 20)), 'bottomWall', 'black')
leftWall = wall((WINDOW.get_width() / 20, WINDOW.get_height()), (0, 0), 'leftWall', 'black')
rightWall = wall((WINDOW.get_width() / 20, WINDOW.get_height()), (WINDOW.get_width() - (WINDOW.get_width() / 20), 0), 'leftWall', 'black')
objList = [bounceBall, topWall, leftWall, rightWall, bottomWall]


def simulation():

    for obj in objList:
        try:
            obj.update()
        except:
            continue


def draw():

    for obj in objList:
        try:
            obj.render(WINDOW)
        except:
            continue

    pygame.display.update()


def main():
    run = True

    while run:

        for event in pygame.event.get():

            if event.type == QUIT:
                run = False
                pygame.quit()
                sys.exit()

        WINDOW.fill('white')
        
        simulation()
        draw()

        clock.tick(settings.MAX_FRAMERATE)


if __name__ == '__main__':
    main()