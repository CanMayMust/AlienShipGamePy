import sys
import os
import pygame


class Settings:
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕
        self.screen_width = 1024
        self.screen_height = 768
        # self.bg_color = (135, 206, 250)# 蓝色天空背景
        self.bg_color = (0, 0, 0)  # 黑色天空背景
        self.win_caption = "火箭移动"
        self.rocket_speed = 0.8  # 火箭移动速度设置


class Rocket:
    def __init__(self, rocket_game):
        """初始化火箭并设置其初始位置"""
        self.screen = rocket_game.screen
        self.settings = rocket_game.settings
        self.screen_rect = rocket_game.screen.get_rect()

        # 加载火箭并图像并获取其外接矩形
        self.rocket_image = pygame.image.load("images/rocket12-4.bmp")
        self.rect = self.rocket_image.get_rect()

        self.rect.center = self.screen_rect.center

        # 在火箭的属性x/y中存储小数值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整火箭位置"""
        # 更新火箭而不是rect对象的x值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # 根据self.x/y更新rect对象
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制移动"""
        self.screen.blit(self.rocket_image, self.rect)


class Rocket12_4:
    def __init__(self):
        pygame.init()

        # settings
        self.settings = Settings()

        os.environ["SDL_VIDEO_CENTERED"] = "1"  # 窗口置于屏幕中央
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.win_caption)
        self.rocket = Rocket(self)

    def run_game(self):
        """游戏主消息循环"""
        while True:
            self._check_events()
            # 更新火箭位置
            self.rocket.update()
            # 每次循环都要重绘屏幕
            self._update_screen()

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        pygame.display.flip()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False


if __name__ == "__main__":
    rocketApp = Rocket12_4()
    rocketApp.run_game()
