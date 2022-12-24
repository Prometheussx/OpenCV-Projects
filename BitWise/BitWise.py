# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 23:29:58 2022

@author: erdem
"""
#VE BĞLACI BİTWİSE_AND
#bit and siyahlar 0 beyazlar bir olucak şekilde mantık işlemleri yapar ve mantıksal işlemini uygular
#ve bağlacı 1ve 1 haricindeki bütün işlemleri sıfır yapar
#yani siyah ve beyaz noktalar üst üste geldiğinde 1 ve 0 işlemini uygular buda sonucu 0 yapar yani beyaz ve siyah üst üste gelirse sonuç siyahtır
#beyaz beyazla denk gelirse 1 ve 1 den sonuç 1 dir ve beyaaz kalır
#siyah siyahın üstüne gelirse 0 ve 0 dan sonuç 0 dır yani siyah kalır

#VEYA BİTWİSE_OR
#Veya mantık yapısında 0 veya 0 eşittir 0 bunun haricindeki bütün değerler 1 dir
#yani siyaah beyaz 1 beyaz beyaz 1 dir ama siyah siyah 0 dır yani siyah siyah hariç heryer beyzdır

#YADA BİTWİSE_XOR
#yada işlemi aynı değerlerde 0 döndürür farklı değerlerde ise 1 yani 0yada 0 0 =1 yada 1 =1  0yada1=1

#NOT YAPISI TERSİNİ ALMA

#İÇİNE GİRİLEN FOTOĞRAFIN TERSİNİ ALIR 0 1 YAPAR 1 0 YAPAR
import numpy as np
import cv2

img1=cv2.imread("bitwise_1.png")
img2=cv2.imread("bitwise_2.png")

bit_and =cv2.bitwise_and(img2,img1) #bit düzeyinde ve mantıksal işlemi yapar 
bit_or = cv2.bitwise_or(img2,img1) #BİT DÜZYİNDE VEYA İŞLEMİ YAPAR
bit_xor = cv2.bitwise_xor(img2,img1)#Bit Düzeyinde Yada işlemi Yapar
bit_not = cv2.bitwise_not(img1)
bit_not2 = cv2.bitwise_not(img2)

cv2.imshow("mg1",img1)
cv2.imshow("mg2",img2)
cv2.imshow("BitAnd",bit_and)
cv2.imshow("BitOr",bit_or)
cv2.imshow("BitXOR",bit_xor)
cv2.imshow("BitNOT",bit_not)
cv2.imshow("BitNOT2",bit_not2)
cv2.waitKey(0)
cv2.destroyAllWindows()