import sys
import pygame

class AlienInvasion:
  """管理游戏资源和行为的类"""
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((1200, 800))

print("Hello World!")