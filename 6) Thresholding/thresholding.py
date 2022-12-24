# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 03:25:50 2022

@author: erdem
"""

#thresholding bir fotoğrafın şahsına özel detaylarını almamızı sağlıyan onu sınıflandırmamızı sağlayan bir yapıddır
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("foto.jpg",0)#greyscale ettik

cv2.imshow("img",img)

ret,th1 =cv2.threshold(img,150,200,cv2.THRESH_BINARY) #◘girilen sayısal verilerle en düzgün ayrıştırılabilir görsel eldedilmeye çalışılır
th2 =cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,2) 
#girilen son iki değerin birbirin bölümünden kalan 1 olmak zorundadır
#Gsonda girilen değerlerden ilki nekadar artarsa çizgi kalınlıklarıda okadar artıyor

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2)

cv2.imshow("img-th1",th1)
cv2.imshow("TH2",th2)
cv2.imshow("TH3",th3)
cv2.waitKey(0)
cv2.destroyerAllWindows()



#TH1 EN KABA DETAYSIZ
#TH2 DAHA DETAYLI
#TH3 İSE EN DETAYLI VE İNCE AYRITLAR OLUŞTURUR