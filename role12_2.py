import pygame


class Role12_2:
    def __init__(self, ai_game):
        """初始化角色，并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载角色图像并获取其外接矩形
        self.role_image = pygame.image.load("images/12-2角色big彩.bmp")
        self.rect = self.role_image.get_rect()

        # self.rect.midbottom = self.screen_rect.midbottom
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """在指定位置绘制角色，窗口中央"""
        self.screen.blit(self.role_image, self.rect)
