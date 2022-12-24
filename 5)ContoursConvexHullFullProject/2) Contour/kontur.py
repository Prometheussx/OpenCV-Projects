# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 17:42:43 2022

@author: erdem
"""

import cv2

img = cv2.imread("contour1.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #kordinatları tutar 

print(contours)

cv2.drawContours(img, contours,1,(0,0,255),3) #-1 hepsini 0 dış bükeyli      gemoetrik yapı 1 iç bükeyli yapı
#kullanılacak resim ikinci kordinatlar  3. olarak -1 4. oalrak renk 5. olarak kalınlık






cv2.imshow("img",img)


cv2.waitKey(0)

cv2.destroyerAllWindows()