import numpy as np
import cv2

image = cv2.imread("lab3_img1.png")
mask1 = np.zeros(image.shape[:2], dtype="uint8")
mask2 = np.zeros(image.shape[:2], dtype="uint8")
mask3 = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask1 , (145 , 200) , 100 , 255 , -1)
cv2.circle(mask2 , (420 , 180) , 100 , 255 , -1)
cv2.circle(mask3 , (650 , 250) , 100 , 255 , -1)

output = cv2.bitwise_or(mask1 , mask2)
output = cv2.bitwise_or(output , mask3)
output = cv2.bitwise_and(image , image , mask= output)

cv2.imshow("Mask applied to image: " , output)

cv2.waitKey(0)
cv2.destroyAllWindows