import cv2
import numpy as np

img = cv2.imread("map.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray,(3,3)) #blur değeri 3 e 3
ret,thresh = cv2.threshold(blur,40,255,cv2.THRESH_BINARY)


cv2.imshow("gray",gray)
cv2.imshow("Threshold",thresh)

cv2.imshow("blur",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
