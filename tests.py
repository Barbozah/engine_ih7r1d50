from core.io import load_objects_byu
from core.engine import Camera
from graphics.tk import PixelDrawer

objects = list(load_objects_byu('assets/objects/vaso.byu'))

camera = Camera(
  hx=2,
  hy=2,
  d=5,
  c=[0, -500, 500],
  n=[0, 1, -1],
  v=[0, -1, -1]
)

screen = PixelDrawer(800, 600)
screen.draw_line(0, 0, 800, 600)
screen.run()
