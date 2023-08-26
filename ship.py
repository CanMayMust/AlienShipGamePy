import pygame


class Ship:
    """管理飞船的类"""

    """
    Ship的方法__init__()接受两个参数：引用self和指向当前AlienInvasion实例的引用。这让Ship能够访问AlienInvasion 中定义的所有游戏资源
    """

    def __init__(self, ai_game):
        """初始化飞船，并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.ship_image = pygame.image.load("images/ship.bmp")
        self.rect = self.ship_image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.ship_image, self.rect)
