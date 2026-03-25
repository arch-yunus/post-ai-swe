# 02 - Rust ve Güvenli Sistem Mühendisliği

## 🦀 Giriş: Güvenliğin Yeni Standardı

Rust, "Memory Safety without Garbage Collection" (Çöp toplayıcı olmadan bellek güvenliği) vaadiyle modern sistem programlamanın zirvesidir. Post-AI döneminde, AI tarafından üretilen kodun "doğuştan güvenli" olması için Rust en ideal mimari tercihtir.

## 🗝️ PAISE Perspektifi: Ownership & Borrowing

Rust'un en güçlü yanı, bellek hatalarını **derleme zamanında (compile-time)** yakalamasıdır.

### 1. Ownership (Sahiplik)
Her verinin tek bir sahibi vardır. Sahibi kapsam dışına (out of scope) çıktığında veri otomatik olarak silinir.

### 2. Borrowing (Ödünç Alma)
Veriyi kopyalamak yerine referansını paylaşma:
- `&T` (Immutable reference): Sadece oku.
- `&mut T` (Mutable reference): Değiştir ama tek bir tane olsun.

## 🤖 AI ile Rust Sinerjisi
AI, Rust'un katı kuralları (Borrow Checker) sayesinde daha az "sessiz bug" içeren kod üretir. Rust'un derleyicisi, AI'nın yaptığı hataları size en açıklayıcı şekilde raporlar.

---
*PAISE Institute - Technical Forge*
