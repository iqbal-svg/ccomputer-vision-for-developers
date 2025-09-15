import cv2
import numpy as np

## 1. Convert to gray scale

img = cv2.imread('lena.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("Color_img Shape: ", img.shape)
print("img_gray Shape: ", img_gray.shape)
cv2.imshow("Color_img", img)
cv2.imshow("Gray_img", img_gray)
cv2.waitKey(0)