#region Pygame
import pygame
from numpy import array, float32, hstack, int32
#endregion

#region C_HEADERS
import glm
import pyassimp as simp  # Couldn't resist
#endregion

#region CUSTOM
import shaders
import functions
import pygame_functions
from classes import *
import os
#endregion

#region OPENGL
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader   # Instructions that are the same as C++
#endregion

texturesArray = ['./white.png', './models/chief_helm_d.png']

def failedToOpenObj(name):
  raise Exception('Could not open object: %s' % name)

def loadObject(name: str)->object:
  return simp.load(name) 

def setShaders(pgInformation, vertex, fragment):
  try:
    pgInformation.setShaders( 
      compileProgram
      ( 
        compileShader(vertex, GL_VERTEX_SHADER), 
        compileShader(fragment, GL_FRAGMENT_SHADER))
      )
  except Exception as e:
    print(e)
    return False
  return True

def main():
  screen, clock = pygame_functions.initPygame()
  pgInformation = PygameInformation(screen, clock)

  if not setShaders(pgInformation, shaders.GL_VERTEX_NATIVE_SHADER, shaders.GL_VERTEX_NATIVE_FRAGMENT):
    raise Exception('Couldn\'t set Shaders')

  helmet = loadObject('./models/helmet.obj') # Try to load the object
  if helmet is None: failedToOpenObj('Helmet')  # Throw exception if not possible

  camera = Camera(glm.vec3(0.0, 0.0, 1.0), 0.1)

  glViewport(0, 0, 800, 600)
  glEnable(GL_DEPTH_TEST)

  Game = GameManager()

  while Game.isRunning:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(1, 1, 1, 1.0)

    glUseProgram(pgInformation.shaders)

    Game.setMatrix(camera)
    Game.setMatrixLocation(pgInformation.shaders)
    Game.time += 0.01

    uniform = glGetUniformLocation(pgInformation.shaders, 'time')
    glUniform1f(uniform, Game.time)

    glUniformMatrix4fv(Game.matrixLocation, 1, GL_FALSE, glm.value_ptr(Game.matrix))
    # Seen in class
    functions.mesher(helmet.rootnode, pgInformation.shaders)

    pygame.display.flip()

    for event in pygame.event.get():
      etype = event.type
      if etype == pygame.QUIT:
        Game.running = False
      elif etype == pygame.KEYDOWN:
        key = event.key
        if key == pygame.K_a: glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        if key == pygame.K_s: glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        if key == pygame.K_LEFT: camera.vec3.x -= camera.speed
        if key == pygame.K_RIGHT: camera.vec3.x += camera.speed
        if key == pygame.K_UP: camera.vec3.y -= camera.speed
        if key == pygame.K_DOWN: camera.vec3.y += camera.speed
        if key == pygame.K_q: functions.changeText(0, texturesArray)
        if key == pygame.K_w: functions.changeText(1, texturesArray)
        if key == pygame.K_1: 
          if not setShaders(pgInformation, shaders.GL_VERTEX_NATIVE_SHADER, shaders.GL_VERTEX_NATIVE_FRAGMENT):
            raise Exception('Couldn\'t set Shaders')
        if key == pygame.K_2: 
          if not setShaders(pgInformation, shaders.GL_VERTEX_NATIVE_SHADER, shaders.GL_NORMALS):
            raise Exception('Couldn\'t set Shaders')
          glUseProgram(pgInformation.shaders)
        if key == pygame.K_3: 
          if not setShaders(pgInformation, shaders.GL_VERTEX_NATIVE_SHADER, shaders.GL_SCANNER_FIRST_HALO):
            raise Exception('Couldn\'t set Shaders')
          glUseProgram(pgInformation.shaders)
        if key == pygame.K_4: 
          if not setShaders(pgInformation, shaders.GL_VERTEX_NATIVE_SHADER, shaders.GL_SCANNER):
            raise Exception('Couldn\'t set Shaders')
          glUseProgram(pgInformation.shaders)
        if key == pygame.K_5: 
          if not setShaders(pgInformation, shaders.GL_VERTEX_NATIVE_SHADER, shaders.GL_PARTAY):
            raise Exception('Couldn\'t set Shaders')
          glUseProgram(pgInformation.shaders)
        if key == pygame.K_x: Game.executing = not Game.executing
    
    if not Game.executing:
      Game.counter += 1
    pgInformation.clock.tick(0)



main()
  

