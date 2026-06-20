💻 Cara Penggunaan
Unduh atau salin kode program ke dalam file bernama fotokitablur.py.

Jalankan program melalui terminal Anda dengan perintah:

Bash
python fotokitablur.py
Jendela kamera bernama "Camera" akan terbuka.

Angkat tangan Anda ke arah kamera dan tunjukkan gestur Peace Sign (✌️) untuk melihat layar berubah menjadi blur.

Lepaskan gestur tangan untuk mengembalikan layar menjadi jernih kembali.

Tekan tombol 'q' pada keyboard Anda untuk menutup program dan keluar dengan aman.

📁 Struktur File Proyek
Plaintext
├── fotokitablur.py  # Script utama program Python
└── README.md        # Dokumentasi panduan proyek (File ini)
🛠️ Logika Kode (Cara Kerja)
Program ini memanfaatkan fungsi .fingersUp() dari cvzone. Fungsi ini mengembalikan sebuah array biner berisi 5 elemen yang merepresentasikan status setiap jari dari jempol hingga kelingking ([jempol, telunjuk, tengah, manis, kelingking]):

1 berarti jari dalam posisi tegak/lurus.

0 berarti jari dalam posisi tertekuk/mengepal.

Logika deteksi untuk gestur Peace Sign (✌️) diatur pada kondisi berikut:

Python
if fingers == [0, 1, 1, 0, 0]:
    # Hanya jari telunjuk dan tengah yang tegak, picu GaussianBlur!
Dibuat dengan ❤️ menggunakan Python dan OpenCV. Silakan gunakan, modifikasi, atau kembangkan proyek ini sesuka Anda!
"""
