import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #wepcamden okicaksak 0 başka bir kamera ise 1 / hazır video açıyosan 0 yerine videoismi.mp4 yazıcaksın/ CAP_DSHOW HATA ALMMAK İÇİN EKLENİYOR
filename="c:\asus\OneDrive\Masaüstü\webcam.avi" #kaydetme
codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2') #değerlereforcc.com dan bakanbilirsin video agoritması çözücü
frameRate = 30 #frame oranı
resolution = (640,480)
videoFileOutput = cv2.VideoWriter(filename, codec, frameRate, resolution) #çıktı alma

while True:
    ret, frame = cap.read() #okunmuş verielrin doğruluğunu ve kare gösterir
    frame = cv2.flip(frame, 1) #istenilen görüntüyü istenilen derecede değiştirri
    cv2.imshow("Webcam", frame)
    videoFileOutput.write(frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):  #karelerin ekranda duracağı süre belirler (30 milisaniye)  / 0xFF kodu q basılınca işleme sokması anlamına geliyor klavye bağıntısı için kullanılıyor
        break
videoFileOutput.release()
cap.release() #webcam kapamayı sağlar baişa işlem yapmayı sağlar
cv2.destroyAllWindows() #pencere kapam
