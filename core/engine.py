class Vertice3D:
  def __init__(self, x, y=None, z=None):
    if type(x) == tuple or type(x) == list and len(x) == 3:
      self.x, self.y, self.z = x
    else:
      self.x, self.y, self.z = x, y, z
  
  def __repr__(self):
    return f'Vector3D({self.x},{self.y},{self.z})'

class Object3D:
  def __init__(self, vertices, triangles):
    self.vertices = vertices
    self.triangles = triangles
  
  def __repr__(self):
    return f'Object3D({len(self.vertices)},{len(self.triangles)})'
