# 🎨 AR Virtual Painter (AI Hand-Tracking)

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.9-orange.svg)

[🇹🇷 Türkçe Açıklama Aşağıdadır](#-türkçe-açıklama)

An Augmented Reality (AR) drawing application built with Python, OpenCV, and MediaPipe. This project allows users to draw on their screen simply by waving their fingers in the air, without any physical hardware (like an iPad or stylus). It features real-time hand landmark detection and multiple gesture controls.

## ✨ Features
* **Hovering AR Canvas:** Drawings stay fixed on the screen while the live camera feed runs in the background.
* **Hand Skeleton Overlay:** Real-time visual feedback showing the detected 21 hand landmarks and connections.
* **Gesture Controls:**
  * ☝️ **1 Finger (Index):** Draw on the canvas.
  * ✌️ **2 Fingers (Index + Middle):** Selection Mode / Navigate menu to change colors.
  
* **Color Palette & Clear Function:** Built-in UI to switch between Neon Purple, Green, Blue, or clear the entire canvas.

## ⚙️ Requirements & Installation
> **⚠️ Important Note for Apple Silicon (M1/M2/M3/M4) Users:** It is highly recommended to use **Python 3.11**. Newer versions (like 3.12+) might cause `protobuf` conflicts with MediaPipe.

1. Clone the repository:
   ```bash
   git clone [https://github.com/KNCn23/AR-Virtual-Painter.git](https://github.com/yourusername/AR-Virtual-Painter.git)
   cd AR-Virtual-Painter
   
Create and activate a virtual environment:

Bash
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
python main.py


🇹🇷 Türkçe Açıklama
Python, OpenCV ve MediaPipe kullanılarak geliştirilmiş bir Artırılmış Gerçeklik (AR) çizim uygulamasıdır. Bu proje, kullanıcıların herhangi bir fiziksel donanıma (tablet veya dijital kalem) ihtiyaç duymadan, sadece parmaklarını havada hareket ettirerek ekrana çizim yapmalarına olanak tanır. Gerçek zamanlı el iskeleti takibi ve el hareketi (gesture) kontrolleri içerir.

✨ Özellikler
AR Tuvali: Canlı kamera görüntüsü arka planda akarken çizimler ekranın üzerinde havada asılı kalır.

El İskeleti Görünümü: Tespit edilen 21 eklem noktasını (landmark) ve aralarındaki bağlantıları anlık olarak ekranda gösterir.

Parmak Hareketleri ile Kontrol:

☝️ 1 Parmak (İşaret): Çizim Modu.

✌️ 2 Parmak (İşaret + Orta): Seçim Modu (Çizmeden renk paletinde gezinme).


Renk Paleti: Ekranın üst kısmındaki arayüz sayesinde Neon Mor, Yeşil, Mavi renklere geçiş yapılabilir veya ekran tamamen temizlenebilir.

⚙️ Kurulum ve Gereksinimler
⚠️ Apple Silicon (M1/M2/M3/M4) Kullanıcıları İçin Önemli Not: Projenin sorunsuz çalışması için Python 3.11 kullanılması şiddetle tavsiye edilir. Daha yeni sürümlerde MediaPipe kaynaklı protobuf uyuşmazlıkları yaşanabilmektedir.

Projeyi bilgisayarınıza indirin:

Bash
git clone [https://github.com/KNCn23/AR-Virtual-Painter.git](https://github.com/KULLANICI_ADIN/AR-Virtual-Painter.git)
cd AR-Virtual-Painter

Sanal ortam (virtual environment) oluşturun ve aktif edin:

Bash
python3.11 -m venv venv
source venv/bin/activate

Windows için: venv\Scripts\activate
Gerekli kütüphaneleri yükleyin:

Bash
pip install -r requirements.txt

Uygulamayı çalıştırın:

Bash
python main.py
