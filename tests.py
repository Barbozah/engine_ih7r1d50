from core import io
from core.engine import Camera
import numpy as np

objects = list(io.load_objects_byu('assets/objects/triangulo.byu'))

camera = Camera(
  hx=1,
  hy=1,
  d=1,
  c=[1, 1, 2],
  n=[-1, -1, -1],
  v=[0, 0, 1]
)

print(camera.change_base(np.array([1, -3, -5])))
