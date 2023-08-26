import sys
import pygame

from settings import Settings

class AlienInvasion:
  """管理游戏资源和行为的类"""
  def __init__(self):
    pygame.init()
    self.settings = Settings()
    self.screen = pygame.display.set_mode(
      (self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption(self.settings.win_caption)

  def run_game(self):
    """游戏主消息循环"""
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
      # 每次循环都要重绘屏幕
      self.screen.fill(self.settings.bg_color)
      pygame.display.flip()

if __name__ == '__main__':
  ai = AlienInvasion()
  ai.run_game()