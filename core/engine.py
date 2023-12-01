import numpy as np

class Camera:
  def __init__(self, hx, hy, d, c, n, v):
    self.view_plane = (hx, hy)
    self.d = d
    self.c = np.array(c)
    self.n = np.array(n)
    self.v = np.array(v)
    self.v_ = self.v - np.dot(self.v, self.n) / np.dot(self.n, self.n) * self.n
    self.u = np.cross(self.n, self.v_)
    self._base = np.array([
      self.normalize(self.u), self.normalize(self.v_), self.normalize(self.n)
    ])

  def normalize(self, v):
    return v / np.linalg.norm(v)

  def change_base(self, v):
    return np.dot(self._base, v - self.c)

class Object3D:
  def __init__(self, vertices, triangles):
    self.vertices = vertices
    self.triangles = triangles
  
  def __repr__(self):
    return f'Object3D({len(self.vertices)},{len(self.triangles)})'

  def triangle(self, index: int):
    return [self.vertices[i-1] for i in self.triangles[index]]

  def __iter__(self):
    return iter(self.triangles)
