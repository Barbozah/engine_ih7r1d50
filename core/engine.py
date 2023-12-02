import numpy as np

def normalize(v):
  return v / np.linalg.norm(v)

def equation(v1, v2):
  if v1[1] == v2[1]:
    return lambda _: v1[0]
  a = (v1 - v2)[0]/(v1 - v2)[1]
  b = v1[0] - a*v1[1]
  return lambda x: a*x + b

class Camera:
  def __init__(self, hx, hy, d, c, n, v):
    self.h = np.array([hx, hy])
    self.d = d
    self.nvp = d / self.h
    self.c = np.array(c)
    self.n = np.array(n)
    self.v = np.array(v)
    self.v_ = self.v - np.dot(self.v, self.n) / np.dot(self.n, self.n) * self.n
    self.u = np.cross(self.n, self.v_)
    self._base = np.array([
      normalize(self.u), normalize(self.v_), normalize(self.n)
    ])

  def change_base(self, v):
    return np.dot(self._base, v - self.c)

  def __eq__(self, __value: object) -> bool:
    if not isinstance(__value, Camera):
      return False
    return np.all(self.h == __value.h) and \
      self.d == __value.d and \
      np.all(self.c == __value.c) and \
      np.all(self.n == __value.n) and \
      np.all(self.v == __value.v)

class Object3D:
  def __init__(self, vertices, triangles):
    self.vertices = vertices
    self.triangles = triangles
    self.projected = None
  
  def __repr__(self):
    return f'Object3D({len(self.vertices)},{len(self.triangles)})'

  def triangle(self, index: int, camera: Camera, screen: tuple = None):
    if self.projected is None or self.projected[0] != camera:
      self.project(camera, screen)
    return [self.projected[1][i-1] for i in self.triangles[index]]

  def project(self, camera: Camera, screen: tuple = None):
    vertices = [camera.change_base(v) for v in self.vertices]
    x = camera.nvp[0] * np.array([v[0] / v[2] for v in vertices])
    y = camera.nvp[1] * np.array([v[1] / v[2] for v in vertices])
    if screen is not None:
      x = (x+1)/2 * screen[0] + .5
      y = screen[1] - (y+1)/2 * screen[1] + .5
    self.projected = camera, np.array([x, y]).T
  
  def __getitem__(self, index: int):
    return self.triangle(index)

  def __iter__(self):
    return iter(self.triangles)
  
  def __len__(self):
    return len(self.triangles)
