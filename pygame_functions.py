from pygame.display import set_mode
from pygame.time import Clock
import pygame


def initPygame(height: int = 800, width: int = 600)->object:
  try:
    pygame.init()
    screen = set_mode((height, width), pygame.OPENGL | pygame.DOUBLEBUF)
    clock = Clock()
  except Exception as e:
    print(e)
    return None, None
  return screen, clock