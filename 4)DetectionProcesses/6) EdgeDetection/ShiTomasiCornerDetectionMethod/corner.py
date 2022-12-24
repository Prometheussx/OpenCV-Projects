# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 20:26:58 2022

@author: erdem
"""

import cv2
import numpy as np

img = cv2.imread("text.png")
img1= cv2.imread("contour.png")

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)#grayin corners ta kullanılması için float 32 tipine dönmelidir burda onu yaptık
corners= cv2.goodFeaturesToTrack(gray,200,0.01,10)#4adet paremetre alır ilki renk paremetresi yani gray ikincis max köşe sayisi bulucağını girerirz
#üçüncü olarak quality value dür kalite değeridir bu en mükemmel köşeyi alır 
#bu sebeple nekadar ufak köşe alıcaksak sayıyı okadar azaltıcaz nekadar belirgin köş alıcaksak okadar yükselticez ve 0 ile1 arası değer alır
# 0.01 girilebilir  
#4.olarak min distance yani köşe arası min uzaklık                  

corners = np.int0(corners) #her köşeye çember bırkıcağımız için float değerlere çember bırakılmaz bu sebeble corners'ı int tipine çeviriyoruz
for corner in corners:
    x,y=corner.ravel() #cornera corners tarafından gelicek değerler tek boyuttlu değildir bu sebbele tek byutta indirgenir 
    cv2.circle(img,(x,y),3,(0,0,255),-1) #x,y merkez noktası seçildi
    
cv2.imshow("Corner",img)
cv2.waitKey(0)
cv2.destroyAllwindows()