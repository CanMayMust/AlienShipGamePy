import sys
import os

import pygame
from random import randint
from pygame.sprite import Sprite


pygame.init()
myScreen = pygame.display.set_mode((1200, 768))
pygame.display.set_caption("作业13-2")


def runWindow():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        myScreen.fill((255, 255, 255))
        pygame.display.flip()


if __name__ == "__main__":
    runWindow()
