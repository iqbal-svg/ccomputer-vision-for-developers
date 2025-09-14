import cv2
img=cv2.imread("lena.png")
print(img)
print(img.shape)

print("OpenCV version:", cv2.__version__)
cv2.imshow("Image",img)
cv2.waitKey(0)