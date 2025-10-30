import cv2

# Chemin vers ta vidéo
input_video = r"uploads/test.mp4"

cap = cv2.VideoCapture(input_video)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Affiche la frame
    cv2.imshow("Frame", frame)

    # Arrêt avec la touche 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
