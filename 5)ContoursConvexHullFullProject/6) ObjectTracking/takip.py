# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 18:20:17 2022

@author: erdem
"""

import cv2
import numpy as np

cap = cv2.VideoCapture("dog.mp4")

while(1):
    _,frame=cap.read() #_kod bozulmasın diye gereksiz atamayı doldurmak için avr
    
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #Hsv  rgb renk paletinin 3 BOyutlu Soft geçişli şekilde şekillenmiş halidir
    sensitivity = 15 #uygunluk için hasaslık ayarı
    lowe_white=np.array([0,0,250-sensitivity]) #en düşük beyaz oranı
    upper_white=np.array([255,sensitivity,255])
    #farklı renkler için hsv cor red şeklinde aratabilriz
    
    mask=cv2.inRange(hsv,lowe_white,upper_white) #maskeleme yapısı hangi değerler arasında alıcağını belritiyoruz
    res=cv2.bitwise_and(frame,frame,mask=mask) # Görüntü Bölgesinin Alımı:
    # bu algoritmada değerler ikişerkere çünki asıl video ve işlenmiş video aynı anda var ve kazıyarak işleme sokuyor
    
    cv2.imshow("frame",frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("result",res)
    
    if cv2.waitKey(5) & 0xFF ==ord('q'):
        break
   
    
cv2.destroyAllWindows()
    
    
    
    