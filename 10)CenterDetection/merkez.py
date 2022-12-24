# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 13:02:24 2022

@author: erdem
"""

import cv2

img = cv2.imread("contour.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

M = cv2.moments(thresh) #burdan gelen değerlerle resim ağırlık merkezi bulunabiliyor

x = int(M["m10"]/M["m00"]) #x değerlerini çekmek için kullanırız int alma sebebimiz floatlar ile kayma ayı olmaması
y=int(M["m01"]/M["m00"])

cv2.circle(img,(x,y),5,(0,0,255),-1) #♣ağırlık merkezine nokta koyduk



cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
