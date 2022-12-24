# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 20:47:42 2022

@author: erdem
"""

#cv2.Canny(input,minThreshold,maxThreshold)

import cv2

cap = cv2.VideoCapture(0)

while 1:
    ret,frame = cap.read()
    
    frame = cv2.flip(frame,1) #ters gelen yansımayı düze çevirtiyor y eksenine göre yapıyor yani sağ el aklakrsa yansıamdada sağ aklakr
    
    edges = cv2.Canny(frame,10,20) #ilk değer min th ve bu değer altı alınmaz 2. değer max th ve üstündekiler kesin alınır
    
    cv2.imshow("Frame",frame)
    cv2.imshow("Edge",edges)
    
    if cv2.waitKey(5) & 0xFF ==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()