import cv2

url = "http://202.142.10.11/nphMotionJpeg?Resolution=640x480&Quality=Clarity"
cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)  # Força o uso do codec FFMPEG

if not cap.isOpened():
    print("Não foi possível acessar o stream.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Falha ao ler o frame.")
        break

    cv2.imshow("Câmera ao vivo", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()