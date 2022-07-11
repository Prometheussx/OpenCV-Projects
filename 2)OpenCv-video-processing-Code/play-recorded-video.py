import cv2

cap = cv2.VideoCapture(0) #wepcamden okicaksak 0 başka bir kamera ise 1 / hazır video açıyosan 0 yerine videoismi.mp4 yazıcaksın
while True:
    ret, frame = cap.read() #okunmuş verielrin doğruluğunu ve kare gösterir
    frame = cv2.flip(frame, 1) #istenilen görüntüyü istenilen derecede değiştirri
    cv2.imshow("Webcam", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):  #karelerin ekranda duracağı süre belirler (30 milisaniye)  / 0xFF kodu q basılınca işleme sokması anlamına geliyor klavye bağıntısı için kullanılıyor
        break
cap.release() #webcam kapamayı sağlar baişa işlem yapmayı sağlar
cv2.destroyAllWindows() #pencere kapam
