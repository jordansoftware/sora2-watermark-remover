import cv2
import numpy as np

def remove_watermark(input_path: str, output_path: str):
    """
    Supprime le watermark d'une vidéo en appliquant un inpainting sur la zone définie.
    Les coordonnées du watermark doivent être ajustées selon ta vidéo.
    """
    # Coordonnées du watermark (à adapter)
    wm_x, wm_y, wm_w, wm_h = 50, 50, 150, 50  # exemple, à changer

    # Ouvrir la vidéo
    cap = cv2.VideoCapture(input_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Créer le writer pour la vidéo de sortie
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Créer le masque binaire sur la zone du watermark
        mask = np.zeros(frame.shape[:2], np.uint8)
        mask[wm_y:wm_y+wm_h, wm_x:wm_x+wm_w] = 255

        # === Bloc de vérification : rectangle rouge ===
        cv2.rectangle(frame, (wm_x, wm_y), (wm_x + wm_w, wm_y + wm_h), (0, 0, 255), 2)
        cv2.imshow("Vérification watermark", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # ===========================================

        # Appliquer l'inpainting
        frame_inpaint = cv2.inpaint(frame, mask, 3, cv2.INPAINT_TELEA)

        # Écrire la frame traitée dans la vidéo de sortie
        out.write(frame_inpaint)
        frame_count += 1

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"✅ Traitement terminé : {frame_count} images traitées")
