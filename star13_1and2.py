import sys
import os

import pygame


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
