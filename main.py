#region Pygame
import pygame
import numpy
#endregion

#region C_HEADERS
import glm
import pyassimp as simp  # Couldn't resist
#endregion

#region CUSTOM
import shaders
import functions
import pygame_functions
import classes
import os
#endregion

#region OPENGL
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader   # Instructions that are the same as C++

#endregion
def failedToOpenObj(name):
  raise Exception('Could not open object: %s' % name)

def loadObject(name: str)->object:
  return simp.load(name) if os.path.exists(name) else None

def main():
  screen, clock = pygame_functions.initPygame()
  pgInformation = classes.PygameInformation(screen, clock)

  pgInformation.setShaders(compileProgram(
    compileShader(shaders.GL_PY_VERTEX_SHADER, GL_VERTEX_SHADER),
    compileShader(shaders.GL_PY_FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
  ))
  helmet = loadObject('./helmet')
  if helmet is None:
    failedToOpenObj('Helmet')



