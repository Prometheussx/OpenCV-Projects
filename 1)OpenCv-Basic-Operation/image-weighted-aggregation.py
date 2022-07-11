#Ağırlıklı Toplamanın Matamatiksel Açılımı

''' f(x,y) = x*a + y*b+ c ==> x değerini a yoğunluğunda y değerini b yoğunluğunda toplıyarak sabit sayı eklersek yeni çıktı oluştururz'''


#Kütüphaneler
import cv2
import numpy as np

#Yuvarlak Çizdirmek
circle= np.zeros((512,512,3),np.uint8)+255
cv2.circle(circle,(256,256),60,(255,0,0),-1)

#Dikdörtgen Çizdirmek
rectangle= np.zeros((512,512,3),np.uint8)+255
cv2.rectangle(rectangle,(150,150),(350,350),(0,0,255),-1)
# Ağırlıklı toplama kodları
dst = cv2.addWeighted(circle , 0.7 , rectangle , 0.3 , 0)   # 0.3 yüzde 30 0.7 yüzde 70 demektir sondaki 0 sabit sayıdır
''' ilk önce ekliyeceğimizi resmi yazıyoruz sonrasında o resmi 
 kaç yoğunluğunda ekliyeceğimizi yazıyoruz sonra diğer fotoğrafı kaç yoğunluğunda ekliyeceğimizi yazıyoruz '''





#resimleri çalıştırma fonksiyonları
cv2.imshow("daire",circle)
cv2.imshow("dikdortgen",rectangle)
cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
