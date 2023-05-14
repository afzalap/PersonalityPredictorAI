import numpy as np
from .pre_process import *

def extract_lines(img):
  # Perform horizontal projection to get the sum of white pixels in each row
  binary_img = pre_processing(img)
  rows, cols = binary_img.shape
  horizontal_sum = np.zeros(rows, dtype=int)
  for i in range(rows):
      for j in range(cols):
          if binary_img[i, j] == 255:
              horizontal_sum[i] += 1

  # Get the starting and ending row of each handwriting line
  start = []
  end = []
  in_line = False
  for i in range(rows):
      if horizontal_sum[i] > 50 and not in_line:
          start.append(i)
          in_line = True
      if horizontal_sum[i] < 50 and in_line:
          end.append(i)
          in_line = False
  # Set the minimum height for a line
  min_line_height = 10

  # Extract each handwriting line as a separate image
  line_spacing = []
  lines = []
  for i in range(len(start)):
      try:  
        line_height = end[i] - start[i]
      except IndexError:
            line_height = 0
      if line_height >= min_line_height:
          line_img = binary_img[start[i]:end[i],:]
          lines.append(line_img)
          if i > 0:
              line_spacing.append(start[i] - end[i-1])

  # Calculate the average line spacing
  if len(line_spacing) == 0:
    avg_line_spacing = 0
  else:
    avg_line_spacing = sum(line_spacing) / len(line_spacing)

  return lines, avg_line_spacing