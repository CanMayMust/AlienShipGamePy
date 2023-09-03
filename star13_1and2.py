import sys
import os

import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, star_game):
        self.screen = star_game.screen
        self.image = pygame.image.load("images/7star13-1_50X50.png")
        self.rect = self.image.get_rect()

        # 每个外星人最初都出现在屏幕的左上角附近each alien appears on screen's top-left nearby
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置store aliens' horizon position precisely
        self.x = float(self.rect.x)


class Star13_1and2:
    def __init__(self):
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.win_caption = "作业13-1和13-2"

        os.environ["SDL_VIDEO_CENTERED"] = "1"  # 窗口置于屏幕中央
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(self.win_caption)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == "__main__":
    ai = Star13_1and2()
    ai.run_game()
