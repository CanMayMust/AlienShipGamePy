import sys
import os
import math
import time

import pygame
import numpy as np
from random import randint

# from pygame.sprite import Sprite


pygame.init()
myScreen = pygame.display.set_mode((1200, 768))
pygame.display.set_caption("Homework13-2")
os.environ["SDL_VIDEO_CENTERED"] = "1"  # center the window to the screen

starImage = pygame.image.load("images/7star13-2_50X50.png")
starRect = starImage.get_rect()  # the star rectangle

# how many star the screen can contain, storage the positions into a numpy array
# margin: top&bottom--starRect.width, left&right--starRect.height
# interval: half of starRect.height and half of starRect.width
# horizontal: (myScreen.get_width() - 2 * starRect.width) / (starRect.width * 1.5)
# vertical: (myScreen.get_height() - 2 * starRect.height) / (starRect.height * 1.5)
# calc position in advanced
posCol = math.floor(
    (myScreen.get_width() - 2 * starRect.width) / (starRect.width * 1.5)
)
posRow = math.floor(
    (myScreen.get_height() - 2 * starRect.height) / (starRect.height * 1.5)
)
starPosArr = np.zeros(shape=(posRow, posCol), dtype="i, i")
for row in range(posRow):
    for col in range(posCol):
        starPosArr[row, col] = (
            starRect.width + col * starRect.width * 1.5,
            starRect.height + row * starRect.height * 1.5,
        )


def runWindow():
    rand_stars_posList = list()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        myScreen.fill((255, 255, 255))

        rand_stars_posList.clear()
        rand_stars = randint(1, 7)

        for randMe in range(rand_stars):
            rand_stars_posList.append(
                starPosArr[randint(0, posRow - 1), randint(0, posCol - 1)]
            )

        for rand_star in rand_stars_posList:
            starRect.x = rand_star[0]
            starRect.y = rand_star[1]
            myScreen.blit(starImage, starRect)

        time.sleep(1)
        pygame.display.flip()


if __name__ == "__main__":
    runWindow()
