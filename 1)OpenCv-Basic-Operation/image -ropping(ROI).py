#ROI ==> region of interest ==> ilgi alanı
import cv2

img = cv2.imread("D:\opencvders\Temelislemler\deneme.jpg")
#print(img.shape[:2])

roi = img[180:380, 30:420]
cv2.imshow("deneme",img)
cv2.imshow("roi",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
