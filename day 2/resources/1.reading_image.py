import cv2
# #read image
# img=cv2.imread("lena.png")
# print(img)
# print(img.shape)

# print("OpenCV version:", cv2.__version__)
# cv2.imshow("Image",img)
# cv2.waitKey(0)

# reading videos

# cap = cv2.VideoCapture("elon.mp4")

# while True:
#     success, img = cap.read()
#     print(img.shape)
#     cv2.imshow("Output", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#reading web cam
cap = cv2.VideoCapture(0)

cap.set(3, 640) # set width
cap.set(4, 480) # set height

while True:
    success, img = cap.read()
    print(img.shape)
    cv2.imshow("Output", img)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 