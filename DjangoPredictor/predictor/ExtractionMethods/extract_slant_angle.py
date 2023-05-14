import cv2
import numpy as np

def detect_slant_angle(image):
    # perform affine transformation
    rows, cols = image.shape
    shear_factors = [i for i in np.arange(-0.5, 0.5, 0.01)]
    max_vertical_frequency = 0
    best_shear_factor = 0
    for shear_factor in shear_factors:
        M = np.float32([[1, shear_factor, 0],[0, 1, 0]])
        sheared_image = cv2.warpAffine(image, M, (cols, rows))

        # calculate vertical projection profile

        vertical_projection = np.sum(sheared_image, axis=0)
        current_vertical_frequency = np.max(vertical_projection)

        # find the maximum vertical frequency
        if current_vertical_frequency > max_vertical_frequency:
            max_vertical_frequency = current_vertical_frequency
            best_shear_factor = shear_factor

    # calculate the slant angle
    slant_angle = np.arctan(best_shear_factor)

     # in radians
    slant_angle = np.arctan(best_shear_factor)

    # coverting it to radians
    slant_angle = np.degrees(slant_angle)

    
    M = np.float32([[1, best_shear_factor, 0],[0, 1, 0]])
    sheared_image = cv2.warpAffine(image, M, (cols, rows))
    # return slant_angle
    return sheared_image, slant_angle

# def extract_slant():
#   slant_angles = []
#   for word in words:
#     slant = detect_slant_angle(word)
#     slant_angles.append(slant)
#   slant = np.mean(slant_angles)


def extract_slant(lines):
  slant_angles = []
  lines_in = []
  for line in lines:
    sheared_image,slant = detect_slant_angle(line)
    slant_angles.append(slant)
    lines_in.append(sheared_image)

  slant = np.mean(slant_angles)

  return lines_in, slant
