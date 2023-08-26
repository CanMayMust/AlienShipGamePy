import sys
import pygame

class AlienInvasion:
  """管理游戏资源和行为的类"""
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("外星人入侵")

  def run_game(self):
    """游戏主消息循环"""
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
      pygame.display.flip()

if __name__ == '__main__':
  ai = AlienInvasion()
  ai.run_game()