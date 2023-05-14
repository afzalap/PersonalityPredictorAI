import numpy as np

def calculate_zone_heights(binary_image):
    rows, columns = binary_image.shape
    black_pixel_count = [sum(row) for row in binary_image]
    max_horizontal_frequency = max(black_pixel_count)
    T = max_horizontal_frequency // 3
    r1 = None
    for i in range(rows-1, -1, -1):
        if black_pixel_count[i] > T:
            r1 = i
            break
    r2 = None
    for i in range(rows):
        if black_pixel_count[i] > T:
            r2 = i
            break
    upper_zone_height = r2
    middle_zone_height = r1 - r2
    lower_zone_height = rows - 1 - r1
    return upper_zone_height, middle_zone_height, lower_zone_height

def extract_letter_size(words):
  upper_zone_heights = []
  middle_zone_heights = []
  lower_zone_heights = []
  for word in words:
    upper_zone_height, middle_zone_height, lower_zone_height = calculate_zone_heights(word)

    upper_zone_heights.append(upper_zone_height)
    middle_zone_heights.append(middle_zone_height)
    lower_zone_heights.append(lower_zone_height)

  upper_zone_height = np.mean(upper_zone_heights)
  middle_zone_height = np.mean(middle_zone_heights)

  lower_zone_height = np.mean(lower_zone_heights)

  return upper_zone_height, middle_zone_height, lower_zone_height