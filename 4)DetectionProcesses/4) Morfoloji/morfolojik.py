# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 23:10:54 2022

@author: erdem
"""
#erosion bozulma demektir
import cv2
import numpy as np
kernel =np.ones((5,5),np.uint8)

img = cv2.imread("harf.png",0)
dilation = cv2.dilate(img,kernel,iterations = 1) #beyazalrı arıttır bozar
erosion = cv2.erode(img,kernel,iterations = 1)#siyahları artırır bozarr
 #iteration tekrar asayısı kernelsa bozulma yapısı
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
cv2.imshow("img:",img)
cv2.imshow("erosion:",erosion)
cv2.imshow("dilation:",dilation)
cv2.imshow("Open:",opening)