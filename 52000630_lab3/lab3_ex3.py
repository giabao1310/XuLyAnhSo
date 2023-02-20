import numpy as np
import cv2

kernel = np.ones((5, 5), np.uint8)

image = cv2.imread("threshold.png", cv2.IMREAD_GRAYSCALE)

# 3.1 cau a
thresh = 170
maxValue = 255

th, output1 = cv2.threshold(image, thresh, maxValue, cv2.THRESH_BINARY_INV)
output1 = cv2.morphologyEx(output1, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("image_03_01.png", output1)
cv2.imshow("image_03_02.png", output1)

# 3.1 cau b
thresh = 170
maxValue = 255

th, output2 = cv2.threshold(image, thresh, maxValue, cv2.THRESH_TOZERO_INV)
output2 = cv2.morphologyEx(output2, cv2.MORPH_OPEN, kernel)
thresh = 0
maxValue = 255
th, output2 = cv2.threshold(output2, thresh, maxValue, cv2.THRESH_BINARY)
cv2.imwrite(fileOutput2, output2)
cv2.imshow(fileOutput2, output2)

cv2.waitKey(0)
cv2.destroyAllWindows
