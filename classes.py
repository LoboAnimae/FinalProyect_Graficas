import glm
from OpenGL.GL import *

class PygameInformation:
  def __init__(self, screen = None, clock = None, shaders = None):
    if screen is None: raise Exception('Can\'t assign a NULL value to screen!')
    if clock is None: raise Exception('Can\'t assign a NULL value to clock!')
    self.screen = screen
    self.clock = clock

  def getScreen(self):
    return self.screen
  
  def getClock(self):
    return self.clock

  def setShaders(self, shaders):
    self.shaders = shaders

  def __str__(self):
    return 'Screen: %s\nClock: %s\nShaders: %s\n' % (self.screen, self.clock, self.shaders)

class Camera:
  def __init__(self, coord, speed):
    self.vec3 = coord
    self.speed = speed
class V3:
  def __init__(self, coords: tuple, speed: float)->None:
    self.x, self.y, self.z = coords
    self.speed = speed
  
  def __str__(self)->str:
    return 'V3(%s, %s, %s): CAMERA_SPEED(%s)' % (self.x, self.y, self.z, self.speed)
  
  def dot(self, v1)->float:
    return self.x * v1.x + self.y * v1.y + self.z * v1.z
  
  def __mul__(self, v1):
    return V3(self.x * v1.x, self.y * v1.y, self.z * v1.z)

  def __add__(self, v1):
    return V3(self.x + v1.x, self.y + v1.y, self.z + v1.z)
  
  def __sub__(self, v1):
    return V3(self.x - v1.x, self.y - v1.y, self.z - v1.z)
  
class GameManager:
  def __init__(self, executing = False, running = True, counter = 0, time = 0, i = glm.mat4()):
    self.executing = executing
    self.running = running
    self.counter = counter
    self.time = time
    self.i = i

  def isRunning(self)->bool:
    return self.running
  
  def isExecuting(self)->bool:
    return self.executing
  
  def getCounter(self)->int:
    return int(self.counter)

  def getTime(self):
    return self.time
  
  def setMatrix(self, camera):
    translate = glm.translate(self.i, glm.vec3(0, 0, 0))
    rotate = glm.rotate(self.i, glm.radians(self.counter), glm.vec3(0, 1, 0))
    scale = glm.scale(self.i, glm.vec3(1, 1, 1))

    model = translate * rotate * scale
    view = glm.lookAt(camera.vec3, glm.vec3(0, 0, 0), glm.vec3(0, 1, 0))
    projection = glm.perspective(glm.radians(45), 800/600, 0.1, 1000)
    self.matrix = projection * view * model
  
  def setMatrixLocation(self, shaders):
    self.matrixLocation = glGetUniformLocation(shaders, 'theMatrix')


