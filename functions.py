from OpenGL.GL import *
from numpy import array, float32, hstack, int32
from pygame import image
import glm

def mesher(node, shader):
  for mesh in node.meshes:
    vertex_data = hstack([
			array(mesh.vertices, dtype=float32),
			array(mesh.normals, dtype=float32),
			array(mesh.texturecoords[0], dtype=float32),
		])
    index_data = hstack(array(mesh.faces, dtype=int32),)
    vertex_buffer_object = glGenVertexArrays(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer_object)
    glBufferData(GL_ARRAY_BUFFER, vertex_data.nbytes, vertex_data, GL_STATIC_DRAW)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 9 * 4, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 9 * 4, ctypes.c_void_p(3 * 4))
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 9 * 4, ctypes.c_void_p(6 * 4))
    glEnableVertexAttribArray(2)
    element_buffer_object = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, element_buffer_object)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, index_data.nbytes, index_data, GL_STATIC_DRAW)
    glUniform3f( glGetUniformLocation(shader, "GL_LIGHT_USAGE"), -80, 185, 0.2 )
    glUniform4f( glGetUniformLocation(shader, "GL_DIFFUSE_USAGE"), 0.7, 0.2, 0, 1 )
    glUniform4f( glGetUniformLocation(shader, "GL_AMBIENT"), 0.2, 0.2, 0.2, 1)
    glDrawElements(GL_TRIANGLES, len(index_data), GL_UNSIGNED_INT, None)
  for child in node.children:
    mesher(child, shader)


def changeText(number, texturesArray):
  surface = image.load(texturesArray[number])
  data = image.tostring(surface, 'RGB')

  x = surface.get_width()
  y = surface.get_height()

  view = glm.mat4(1)
  projection = glm.perspective(glm.radians(45), 800/600, 0.1, 1000.0)
  model = glm.mat4(1)

  texture = glGenTextures(1)
  glBindTexture(GL_TEXTURE_2D, texture)
  glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, x, y, 0, GL_RGB, GL_UNSIGNED_BYTE, data)
  glGenerateMipmap(GL_TEXTURE_2D)
