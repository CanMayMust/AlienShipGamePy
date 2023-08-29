import sys
import os
import pygame
from pygame.sprite import Sprite


class Settings:
    def __init__(self):
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (255, 255, 255)
        self.win_caption = "F22横移"
        self.f22_speed = 0.7
        # 导弹设置
        self.missile_speed = 0.5
        self.missile_width = 15
        self.missile_height = 3
        self.missile_color = (60, 60, 60)
        self.missiles_allowed = 3


class FighterJet22:
    def __init__(self, f22_game):
        self.screen = f22_game.screen
        self.settings = f22_game.settings
        self.screen_rect = f22_game.screen.get_rect()

        # 加载F22并图像并获取其外接矩形
        self.f22_image = pygame.image.load("images/F22-Jet_turn.png")
        self.rect = self.f22_image.get_rect()

        # self.rect.center = self.screen_rect.center
        self.rect.midleft = self.screen_rect.midleft

        # 在F22的属性y中存储小数值
        self.y = float(self.rect.y)

        # 移动标志
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整F22位置"""
        # 更新F22而不是rect对象的y值
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.f22_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.f22_speed

        # 根据self.y更新rect对象
        self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制移动"""
        self.screen.blit(self.f22_image, self.rect)


class Missile(Sprite):
    def __init__(self, f22_game):
        """在f22当前位置创建一个导弹对象"""
        super().__init__()
        self.screen = f22_game.screen
        self.settings = f22_game.settings
        self.color = self.settings.missile_color

        # 在（0,0）处创建一个表示导弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(
            0, 0, self.settings.missile_width, self.settings.missile_height
        )
        self.rect.midright = f22_game.f22.rect.midright

        # 存储用小数表示的子弹位置
        self.x = float(self.rect.x)

    def update(self):
        """向右移动导弹"""
        # 更新表示导弹位置的小数值
        self.x += self.settings.missile_speed
        # 更新表示导弹的rect的位置
        self.rect.x = self.x

    def draw_missile(self):
        """在屏幕上绘制导弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)


class F22_12_6:
    def __init__(self):
        pygame.init()

        # settings
        self.settings = Settings()

        os.environ["SDL_VIDEO_CENTERED"] = "1"  # 窗口置于屏幕中央
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.win_caption)
        self.f22 = FighterJet22(self)

        # 用于存储导弹的编组
        self.missiles = pygame.sprite.Group()

    def run_game(self):
        """游戏主消息循环"""
        while True:
            self._check_events()
            # 更新f22位置
            self.f22.update()
            self.missiles.update()
            self._update_missiles()
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

    def _update_missiles(self):
        """更新导弹的位置并删除消失的导弹 refresh the missiles pos and delete missiles missing"""
        self.missiles.update()
        for missile in self.missiles.copy():
            if missile.rect.left > self.screen.get_rect().right:
                self.missiles.remove(missile)
        # print(len(self.missiles))#显示当前还有多少颗导弹presents missiles availiable

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.f22.blitme()
        for missile in self.missiles.sprites():
            missile.draw_missile()
        pygame.display.flip()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.f22.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.f22.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_missile()
        elif event.key == pygame.K_q:
            sys.exit()

    def _fire_missile(self):
        """创建一颗导弹，并将其加入编组missiles中"""
        if len(self.missiles) < self.settings.missiles_allowed:
            new_missile = Missile(self)
            self.missiles.add(new_missile)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.f22.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.f22.moving_down = False


if __name__ == "__main__":
    f22App = F22_12_6()
    f22App.run_game()
