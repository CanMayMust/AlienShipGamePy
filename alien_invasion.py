import sys
import os
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

# from role12_2 import Role12_2


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        os.environ["SDL_VIDEO_CENTERED"] = "1"  # 窗口置于屏幕中央
        # self.play_in_fullscreen()  # 全屏模式
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.win_caption)

        self.ship = Ship(self)  # self指向的是当前AlienInvasion实例

        # self.role = Role12_2(self)#练习12-2

        # 用于存储子弹的编组
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """游戏主消息循环"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()

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

    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹 refresh the bullets pos and delete bullets missing"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))#显示当前还有多少颗子弹presents bullets availiable

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # self.role.blitme()#练习12-2
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def play_in_fullscreen(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
