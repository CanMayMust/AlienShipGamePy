import sys
import os
import pygame


class Settings:
    """存储所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (135, 206, 250)  # 蓝色天空背景

        self.win_caption = "跟踪KEYDOWN事件"


class KeyPressTracking12_5:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        os.environ["SDL_VIDEO_CENTERED"] = "1"  # 窗口置于屏幕中央
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.win_caption)

    def run_app(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)

            self.screen.fill(self.settings.bg_color)
            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == "__main__":
    KeyPressTrackingApp = KeyPressTracking12_5()
    KeyPressTrackingApp.run_app()
