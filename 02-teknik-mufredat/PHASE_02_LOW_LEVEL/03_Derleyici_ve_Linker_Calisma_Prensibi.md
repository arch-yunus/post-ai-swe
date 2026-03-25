# 03 - Derleyici ve Linker Çalışma Prensibi

## ⚙️ Soyutlamanın Altına İniş

Kodun makine diline dönüşüm süreci, bir mimarın sistemin sınırlarını anlaması için kritiktir.

### 1. Pre-processing (Önişleme)
`#include`, `#define` gibi makroların çözüldüğü aşama.

### 2. Compilation (Derleme)
Yüksek seviyeli dilin (C, C++, Rust), Assembly koduna dönüştürülmesi.

### 3. Assembly
Assembly kodunun makine koduna (Object file `.o` / `.obj`) çevrilmesi.

### 4. Linking (Bağlama)
Farklı object dosyalarının ve kütüphanelerin birleştirilerek çalıştırılabilir (`executable`) hale getirilmesi.

## 🔍 Mimari Denetim: Static vs Dynamic Linking
- **Static Linking:** Kütüphaneler executable içine gömülür. Daha büyük dosya boyutu, taşınabilirlik kolaylığı.
- **Dynamic Linking:** Kütüphaneler çalışma zamanında yüklenir (`.so`, `.dll`). Daha küçük dosya boyutu, kütüphane güncellemeleri kolaylığı.

---
*PAISE Institute - Technical Forge*
