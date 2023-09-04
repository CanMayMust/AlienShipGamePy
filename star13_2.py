import sys
import os

import pygame
from random import randint
from pygame.sprite import Sprite


class Settings:
    """存储所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        self.win_caption = "作业13-2"


if __name__ == "__main__":
    star_rand = Star13_2()
    star_rand.run_game()
