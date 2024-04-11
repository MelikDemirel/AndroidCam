# OpenCV kütüphanesini içe aktar
import cv2
# NumPy kütüphanesini içe aktar
import numpy as np
# Requests kütüphanesini içe aktar
import requests

# IP kameradan alınacak görüntülerin bulunduğu URL'yi belirt
url = ""

# Sonsuz bir döngü başlat
while True:
    # URL üzerinden görüntü al
    img_resp = requests.get(url)
    
    # Gelen veriyi bir diziye dönüştür
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    
    # Diziyi bir görüntü olarak çöz
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    
    # Görüntüyü belirtilen boyuta yeniden boyutlandır
    img = cv2.resize(img, (640, 480))
    
    # Görüntüyü ekranda göster
    cv2.imshow("Android Camera", img)
    
    # Eğer kullanıcı klavyeden 'ESC' tuşuna basarsa, döngüden çık
    if cv2.waitKey(1) == 27:
        break

# Tüm açık pencereleri kapat
cv2.destroyAllWindows()
