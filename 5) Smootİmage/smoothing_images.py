import cv2
import numpy as np

img_filter = cv2.imread("filter.png")
img_median = cv2.imread("median.png")
img_bilateral = cv2.imread("bilateral.png")
blur =cv2.blur(img_filter,(11,11)) #içeri girilen değer bulanıklık oranıdır ve sadece pozitif tek sayılar iş yapıyor
blur_g=cv2.GaussianBlur(img_filter,(5,5),cv2.BORDER_DEFAULT)
blur_m = cv2.medianBlur(img_median,5) #karıncalı yapar
blur_b = cv2.bilateralFilter(img_bilateral,9,95,95)#yumuşatma efekti yapıyor
cv2.imshow("original2",img_bilateral)
cv2.imshow("original",img_filter)
cv2.imshow("blur",blur)
cv2.imshow("blur_g",blur_g)
cv2.imshow("blur_m",blur_m)
cv2.imshow("blur_b",blur_b)
cv2.waitKey(0)
cv2.destroyAllWindows()
