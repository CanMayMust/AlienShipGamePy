import sys
import os
import pygame
from pygame.sprite import Sprite


class Settings:
    """存储所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        self.win_caption = "作业13-1"


class Star(Sprite):
    def __init__(self, star_game):
        super().__init__()
        self.screen = star_game.screen
        self.image = pygame.image.load("images/7star13-1_50X50.png")
        self.rect = self.image.get_rect()

        # 每颗星最初都出现在屏幕的左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储星的精确水平位置
        self.x = float(self.rect.x)


class Star13_1:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        os.environ["SDL_VIDEO_CENTERED"] = "1"  # 窗口置于屏幕中央
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.win_caption)
        self.stars = pygame.sprite.Group()
        self._create_star_line()

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)

        self.stars.draw(self.screen)

        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _create_star_line(self):
        """
        创建星并计算一行可容纳多少个星，星的间距为星的宽度
        """
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2 * star_width)
        number_aliens_x = available_space_x // (2 * star_width)

        available_space_y = self.settings.screen_height - 3 * star_height
        number_rows = available_space_y // (2 * star_height)

        for row_number in range(number_rows):
            for star_number in range(number_aliens_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        star = Star(self)
        star_width, star_heigh = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)


if __name__ == "__main__":
    star_align = Star13_1()
    star_align.run_game()
