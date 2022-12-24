# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:01:19 2022

@author: erdem
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("smile.jpg")#np.zeros siyah ekran oluşturur 
#uint8 ise 8 bitlik pozitif tamsayı tutan tip. [0, 255] arası değer tutabilir.RGB İçin Gereklidir
#cv2.rectangle(img,(0,60),(200,150),(255,255,255),-1) #,ilk değer kenarların başlangıç değerleri 2.değer kenarların bitiş değeri 3.değer renk 4.değer iç doluluğu

r,g,b=cv2.split(img) #renk değerlerini ayrı ayrı atama





cv2.imshow("img",img)#histagram tek bir değer satırı haline gelen renk değerlerini grafik tablosunda gösterir
#img.ravel 500x500lük rersmimimizi tek bir satır haline getiriyor 
#2.girdi kaç değer olduğu [0,256] ise değer arlağını yani 0 dahil 255 e kadar olucak değeri belritir
#Sonuç Olarak 250000 Adet Pixelin Renk Değerini gösterirr
plt.hist(r.ravel(),256,[0,256])#çizdirme
plt.hist(g.ravel(),256,[0,256])
plt.hist(b.ravel(),256,[0,256])



plt.show()



cv2.waitKey(0)
cv2.destroyAllwindows()
