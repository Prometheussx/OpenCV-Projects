# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 13:34:37 2022

@author: erdem
"""

import cv2

img = cv2.imread("contour.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours,_ =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt=contours [0]

area=cv2.contourArea(cnt)#alan değerinin kodu

print(area)


M=cv2.moments(cnt)

print(M['m00']) #alan değerinin kodu

perimeter = cv2.arcLength(cnt,True) #çevre bulma
print(perimeter)

"""
cv2.imshow("main",img)
cv2.imshow("thres",thresh)
cv2.imshow("gray",gray)
"""

cv2.waitKey(0)

cv2.destroyAllWindows()