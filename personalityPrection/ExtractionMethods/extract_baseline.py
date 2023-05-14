import cv2
import numpy as np
from .pre_process import *

def detect_and_correct_baseline(img, rotation_angle=1):
    # for clockwise rotation of the image
    imgcpy = img.copy()
    
    img_binarized = pre_processing(imgcpy)

    U = 0
    skew_angle = 0
    horizontal = np.sum(img_binarized, axis=1)
    U = np.max(horizontal)


    u_prev = 0 
    skew = 0
    u_max = U
  
    while skew_angle > -40:
        M = cv2.getRotationMatrix2D((img_binarized.shape[1] // 2, img_binarized.shape[0] // 2), -rotation_angle, 1)
        img_binarized = cv2.warpAffine(img_binarized, M, (img_binarized.shape[1], img_binarized.shape[0]), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

        skew_angle -= rotation_angle
        u_prev = U
        horizontal = np.sum(img_binarized, axis=1)
        U =  np.max(horizontal)

        if U > u_max:
            u_max = U
            skew = skew_angle

    skew_clockwise = skew
    hmax_clockwise = u_max

    # for anrti-clockwise rotation of the image
    imgcpy = img.copy()

    img_binarized = pre_processing(imgcpy)

    U = 0
    skew_angle = 0
    horizontal = np.sum(img_binarized, axis=1)
    U = np.max(horizontal)

    u_prev = 0 
    skew = 0
    u_max = U
  
    while skew_angle < 40:
        M = cv2.getRotationMatrix2D((img_binarized.shape[1] // 2, img_binarized.shape[0] // 2), rotation_angle, 1)
        img_binarized = cv2.warpAffine(img_binarized, M, (img_binarized.shape[1], img_binarized.shape[0]), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

        skew_angle += rotation_angle
        u_prev = U
        horizontal = np.sum(img_binarized, axis=1)
        U =  np.max(horizontal)

        if U > u_max:
            u_max = U
            skew = skew_angle


    skew_anticlockwise = skew
    hmax_anticlockwise = u_max

    

    if(hmax_clockwise > hmax_anticlockwise):
      skew_max = skew_clockwise
    else:
      skew_max = skew_anticlockwise

    
  
    M = cv2.getRotationMatrix2D((imgcpy.shape[1] // 2, imgcpy.shape[0] // 2), skew_max, 1)
    rotated = cv2.warpAffine(imgcpy, M, (imgcpy.shape[1], imgcpy.shape[0]), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)


    return rotated, skew_max