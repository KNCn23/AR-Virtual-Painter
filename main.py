import cv2
import numpy as np
import mediapipe as mp

# --- AYARLAR ---
brush_thickness = 15
eraser_thickness = 80

# Neon Renkler (AR hissi için parlak renkler)
draw_color = (255, 0, 255)  # Varsayılan: Neon Mor
# Renk Listesi: Mor, Yeşil, Mavi
colors = [(255, 0, 255), (0, 255, 0), (255, 255, 0)]

# Kamera Ayarları
cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

# Çizim Katmanı (Sanal Cam)
# Video ile aynı boyutta simsiyah, boş bir resim oluşturuyoruz.
img_canvas = np.zeros((720, 1280, 3), np.uint8)

# MediaPipe Ayarları
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8)
mp_draw = mp.solutions.drawing_utils

# Önceki koordinatlar (Yumuşak çizim için)
xp, yp = 0, 0

print("AR Modu Başlatıldı... Çıkış için 'q' basın.")

while True:
    # 1. Görüntüyü Al
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Aynalama (Doğal hissetmek için şart)

    # 2. El Tespiti Yap
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            # Koordinatları Çek
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id, cx, cy])

            if len(lm_list) != 0:
                # Parmak Uçları
                x1, y1 = lm_list[8][1], lm_list[8][2]  # İşaret
                x2, y2 = lm_list[12][1], lm_list[12][2]  # Orta

                # Parmak Durum Kontrolü
                fingers = []
                # Baş parmak (x ekseni kontrolü - Sağ el için)
                if lm_list[4][1] < lm_list[3][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                # Diğer 4 parmak (y ekseni kontrolü)
                for tip in [8, 12, 16, 20]:
                    if lm_list[tip][2] < lm_list[tip - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                # --- MODLAR ---

                # A) SEÇİM MODU (İşaret + Orta Parmak Havada) -> Çizim yapmaz, imleç gezdirir
                if fingers[1] and fingers[2]:
                    xp, yp = 0, 0  # Çizgiyi kopar
                    # Ekrana sadece bir "hedef" imleci koyalım
                    cv2.rectangle(
                        img,
                        (x1 - 15, y1 - 15),
                        (x2 + 15, y2 + 15),
                        draw_color,
                        cv2.FILLED,
                    )

                    # Renk Değiştirme Mantığı (Ekranın üstüne dokunursa)
                    if y1 < 100:
                        if 0 < x1 < 200:
                            draw_color = colors[0]  # Mor
                        elif 200 < x1 < 400:
                            draw_color = colors[1]  # Yeşil
                        elif 400 < x1 < 600:
                            draw_color = colors[2]  # Sarı
                        elif 1000 < x1 < 1280:
                            img_canvas = np.zeros((720, 1280, 3), np.uint8)  # Temizle

                # B) ÇİZİM MODU (Sadece İşaret Parmağı Havada) -> Yazar
                elif fingers[1] and not fingers[2]:
                    cv2.circle(
                        img, (x1, y1), 15, draw_color, cv2.FILLED
                    )  # Parmağın ucuna nokta koy

                    if xp == 0 and yp == 0:
                        xp, yp = x1, y1

                    # DİKKAT: Çizimi 'img' (kamera) üzerine değil, 'img_canvas' (sanal katman) üzerine yapıyoruz
                    cv2.line(
                        img_canvas, (xp, yp), (x1, y1), draw_color, brush_thickness
                    )
                    xp, yp = x1, y1

                # C) SİLGİ (Tüm parmaklar havada)
                elif all(fingers):
                    # Siyah renkle boyamak = Silmek (Maskeleme mantığı gereği)
                    cv2.circle(
                        img, (x1, y1), eraser_thickness, (0, 0, 0), cv2.FILLED
                    )  # Ekranda silgi dairesi
                    cv2.circle(
                        img_canvas, (x1, y1), eraser_thickness, (0, 0, 0), cv2.FILLED
                    )  # Canvas'tan sil
                    xp, yp = 0, 0

                else:
                    xp, yp = 0, 0  # El indiğinde veya başka harekette çizimi kes

    # --- AR BİRLEŞTİRME (EN ÖNEMLİ KISIM) ---

    # Adım 1: Canvas'ı gri tona çevir
    img_gray = cv2.cvtColor(img_canvas, cv2.COLOR_BGR2GRAY)

    # Adım 2: Bir Maske oluştur (Dolu olan yerler Beyaz, Boş yerler Siyah olsun)
    _, img_inv = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)

    # Adım 3: Maskeyi tersine çevir (Dolu yerler Siyah, Boş yerler Beyaz)
    # Bu bize "Videonun neresini kesip atacağımızı" söyleyecek.
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)

    # Adım 4: Video görüntüsünden, çizim yapılacak yerleri "kesip at" (Siyah yap)
    # Mantık: Video (Renkli) AND Maske (Siyah delikli beyaz kağıt)
    img = cv2.bitwise_and(img, img_inv)

    # Adım 5: Siyah boşluklara, renkli Canvas çizimini yerleştir.
    # Mantık: Kesik Video OR Renkli Çizim
    img = cv2.bitwise_or(img, img_canvas)

    # --- MENÜYÜ ÇİZ (En üste) ---
    # Kullanıcı nereye dokunacağını bilsin
    cv2.rectangle(img, (0, 0), (200, 80), colors[0], -1)  # Mor Kutu
    cv2.rectangle(img, (200, 0), (400, 80), colors[1], -1)  # Yeşil Kutu
    cv2.rectangle(img, (400, 0), (600, 80), colors[2], -1)  # Sarı Kutu
    cv2.rectangle(img, (1080, 0), (1280, 80), (100, 100, 100), -1)  # Sil Kutusu
    cv2.putText(
        img, "TEMIZLE", (1100, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2
    )

    cv2.imshow("AR Yazi Tahtasi", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
