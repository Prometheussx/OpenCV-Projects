# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 11:10:08 2022

@author: erdem
"""

import cv2
import numpy as np

img =cv2.imread("line.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,75,150)


#cv2.HoughLines()Daha Çok  cpu yer
"""
ilk değer keknarı bulunmuş fotoğraf sonrasında row ve 
teta değerlerini giriyoruz buda 1 ve np.pi/180 dir ardındn 
trashold değeri girilir örnek 50"
"""
#lineları belirleme
#maxlinegap line araı boşlukları doldurur
lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=250)#daha az cpu yer
#linler değer tutar x1y1 başlangıç x2y2 bitiş değerleridir çziginin
print(lines)

#line linesın içinde gezdiriyoruz ve başlangıç bitiş 
#noktlaarı lines datasında 0.noktada olduğu için sıfırdan 
#başlangıç bitişleri çekiyoruz
#ardından onları çizgi olarak oluşturuyruz


for line in lines:
    x1,y1,x2,y2 = line[0]
    #başlangıç bitiş noktaları renk ve kalınlık dğerleri
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    


cv2.imshow("img",img)
cv2.imshow("gray",gray)
cv2.imshow("edges",edges)

"""
NOT:Lines datası 
[[[ 46  57 119  57]]

 [[162  62 234  62]]

 [[441 325 608 325]]

 [[442 320 603 320]]  

Bu şekilde olduğu için ve bu setlerin her satırının sadece 
0. elemanı bizim başlangıç biitş noktasını verdiği için
x1,y1,x2,y2=line[0] dedik bu sayede
çizginin başlangıç noktası olan x1,y1 = [46,162] oldu
çizginin bitiş noktası olan x2,y2 ise = [441,442] oldu

"""






