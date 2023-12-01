import tkinter as tk
import numpy as np

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
  
  def draw_line(self, x1, y1, x2, y2, color="white"):
    if x1 > x2:
      x1, x2 = x2, x1
      y1, y2 = y2, y1
    deltaX = abs(x2 - x1)
    deltaY = abs(y2 - y1)
    error = 0
    deltaErr = abs(deltaY / deltaX)
    y = y1
    for x in range(x1, x2):
      self.draw_pixel(x, y, color=color)
      error = error + deltaErr
      while error >= 0.5:
        self.draw_pixel(x, y, color=color)
        y = y + np.sign(y2 - y1)
        error = error - 1.0

  def run(self):
    self.root.mainloop()