import cv2
from cvzone.HandTrackingModule import HandDetector

# Inisialisasi kamera dan detektor tangan
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

print("Program berjalan. Tekan 'q' pada keyboard untuk keluar.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Efek cermin
    frame = cv2.flip(frame, 1)

    # PERBAIKAN: Tangkap dua variabel (hands dan frame) sekaligus
    hands, frame = detector.findHands(frame, draw=False)

    is_peace_sign = False

    if hands:
        hand = hands[0]
        # Ambil status jari (1 = tegak, 0 = tekuk)
        fingers = detector.fingersUp(hand)

        # Logika Peace Sign ✌️: Telunjuk & Tengah tegak, sisanya menekuk
        if fingers == [0, 1, 1, 0, 0]:
            is_peace_sign = True

    # Jika memunculkan ✌️, langsung blur seluruh layar
    if is_peace_sign:
        frame = cv2.GaussianBlur(frame, (99, 99), 0)

    # Tampilkan hasil kamera yang bersih
    cv2.imshow("Camera", frame)

    # Keluar jika menekan tombol 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()