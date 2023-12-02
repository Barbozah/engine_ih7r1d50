import tkinter as tk
from tkinter.filedialog import askopenfilename
import numpy as np
from core.engine import equation
from core.io import load_objects_byu

class PixelDrawer:
  def __init__(self, width=800, height=600):
    self.wh = width, height
    self.root = tk.Tk()
    self.canvas = tk.Canvas(self.root, width=width, height=height, background="black")
    self.canvas.pack()

  def draw_pixel(self, x, y, color="white"):
    x = int(x)
    y = int(y)
    self.canvas.create_line(x, y, x+1, y, fill=color)
  
  def clear(self):
    self.canvas.delete("all")
  
  def rasterize(self, triangle: list[np.ndarray]):
    triangle = sorted(triangle, key=lambda v: v[1])
    if triangle[0][1] == triangle[1][1]:
      self._rasterize_flat_bottom_triangle(triangle)
    elif triangle[1][1] == triangle[2][1]:
      self._rasterize_flat_top_triangle(triangle)
    else:
      x = triangle[0][0] + (triangle[1][1] - triangle[0][1]) / (triangle[2][1] - triangle[0][1]) * (triangle[2][0] - triangle[0][0])
      self._rasterize_flat_bottom_triangle([triangle[0], triangle[1], np.array([x, triangle[1][1]])])
      self._rasterize_flat_top_triangle([triangle[1], np.array([x, triangle[1][1]]), triangle[2]])
  
  def _rasterize_flat_bottom_triangle(self, triangle: list[np.ndarray]):
    m1 = equation(triangle[0], triangle[2])
    m2 = equation(triangle[1], triangle[2])
    for y in range(int(triangle[0][1]), int(triangle[1][1])+1):
      x1 = m1(y)
      x2 = m2(y)
      for x in range(int(x1), int(x2)+1):
        self.draw_pixel(x, y)
  
  def _rasterize_flat_top_triangle(self, triangle: list[np.ndarray]):
    m1 = equation(triangle[0], triangle[1])
    m2 = equation(triangle[0], triangle[2])
    for y in range(int(triangle[0][1]), int(triangle[2][1])+1):
      x1 = m1(y)
      x2 = m2(y)
      for x in range(int(x1), int(x2)+1):
        self.draw_pixel(x, y)

  def run(self, camera, rasterize=False):
    filename = askopenfilename(defaultextension='byu', title="Selecione um arquivo .byu")
    objects = list(load_objects_byu(filename))
    for obj in objects:
      for i in range(len(obj.triangles)):
        if rasterize:
          self.rasterize(obj.triangle(i, camera, self.wh))
        else:
          for v in obj.triangle(i, camera, self.wh):
            self.draw_pixel(*v)
    self.root.deiconify()
    self.root.mainloop()
