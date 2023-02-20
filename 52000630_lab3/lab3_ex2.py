import numpy as np
import cv2

HumanImage = cv2.imread("lab3_img1.png")
LogoImage = cv2.imread("lab3_img2.png")

LogoImage = cv2.resize(LogoImage, HumanImage.shape[1::-1])

output = cv2.addWeighted(HumanImage, 0.5, LogoImage, 0.5, 0)

cv2.imshow("2", output)
cv2.waitKey(0)
cv2.destroyAllWindows

