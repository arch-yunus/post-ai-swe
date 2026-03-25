# 01 - Agentic Workflow Design

## 🤖 Giriş: Otomasyondan Otonomiye

Geleneksel "Script" (Betik) mantığı, belirli girdilere belirli çıktılar verir. "Agentic Workflow" (Ajan Akışı) ise, bir hedefe ulaşmak için kendi alt görevlerini belirleyen ve hata durumunda rotasını düzelten dinamik yapılardır.

## 🗝️ Akış Tasarımı Bileşenleri

### 1. Planning (Planlama)
Ajanın karmaşık bir görevi atomik adımlara bölmesi.
- **Internal Monologue:** Ajanın adım atmadan önce kurduğu mantık.
- **Task Decomposition:** Büyük resmi küçük parçalara ayırma.

### 2. Tools (Araçlar)
Ajanın dünyaya dokunduğu elleri. Terminal, tarayıcı, API'ler.

### 3. Feedback Loops (Geri Bildirim Döngüleri)
"Hata yaptım mı?" denetimi. Unit testlerin otonom çalıştırılması ve sonucuna göre kodun düzeltilmesi.

## 🛰️ PAISE Perspektifi: Orchestration over Coding
Bir mimar olarak sizin göreviniz kod yazmak değil, bu ajanların birbiriyle uyumlu çalıştığı "Hattı" (Pipeline) tasarlamaktır.

---
*PAISE Institute - Technical Forge*
