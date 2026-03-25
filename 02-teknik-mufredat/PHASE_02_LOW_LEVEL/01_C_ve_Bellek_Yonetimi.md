# 01 - C Programlama ve Bellek Yönetimi (Memory Management)

## 🏛️ Giriş: Neden Post-AI Çağında C?

Yapay zeka modelleri kod yazmayı kolaylaştırsa da, "alt katman" (low-level) sistemlerin nasıl çalıştığını bilmeyen bir mimar, AI'nın ürettiği kodun performans ve güvenlik açıklarını denetleyemez. C, bilgisayar mimarisine en yakın, "yüksek seviyeli" dillerin atasıdır.

## 🧠 Temel Kavramlar

### 1. Stack vs Heat: Bellek Bölümleri
- **Stack (Yığın):** Yerel değişkenlerin tutulduğu, hızlı erişimli ama sınırlı alan. LIFO (Last-In-First-Out) prensibiyle çalışır.
- **Heap (Öbek):** `malloc()`, `calloc()` ile çalışma zamanında (runtime) ayrılan, daha büyük ama manuel yönetim gerektiren alan.

### 2. Pointer (İşaretçi) Mekaniği
Pointer'lar, bir verinin değerini değil, bellekteki **adresini** tutan değişkenlerdir.
```c
int x = 10;
int *ptr = &x; // ptr, x'in adresini tutar
```

## 🛡️ AI Destekli Geliştirmede Denetim Soruları
AI bir C kodu ürettiğinde şu 3 soruyu sormalısınız:
1. **Memory Leak Control:** `malloc` edilen her alan `free` edildi mi?
2. **Buffer Overflow:** Array sınırları kontrol ediliyor mu?
3. **Null Pointer Check:** Manuel ayrılan bellek başarılı oldu mu?

## 🚀 Uygulama: Manuel Bellek Yönetimi Simülasyonu
(Bu bölümdeki örnekler `PHASE_02_LOW_LEVEL/examples` dizininde bulunabilir.)

---
*PAISE Institute - Technical Forge*
