import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类calss represent individual alien"""
    """试一试能不能上传GitHub"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("images/alien_small.bmp")
        self.rect = self.image.get_rect()

        # 每个外星人最初都出现在屏幕的左上角附近each alien appears on screen's top-left nearby
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置store aliens' horizon position precisely
        self.x = float(self.rect.x)
