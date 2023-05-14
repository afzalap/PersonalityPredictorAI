import numpy as np
from .pre_process import *

def top_margin(img):
  image = pre_processing(img)
  rows, cols = image.shape
  horizontal_projection = np.zeros(rows, dtype=int)
  for i in range(rows):
      for j in range(cols):
          if image[i, j] == 255:
              horizontal_projection[i] += 1


  # Find the first black pixel
  top_margin = 0
  for i in range(rows):
      if horizontal_projection[i] != 0:
          top_margin = i
          break

  return (top_margin/rows)*100