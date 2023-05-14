import cv2

def pre_processing(img):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  ret, img_binarized = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
  return img_binarized