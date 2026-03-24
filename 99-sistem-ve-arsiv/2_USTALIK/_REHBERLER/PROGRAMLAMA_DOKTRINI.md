# 📜 Programlama Doktrini: Kod Yazma Sanatı

Bu rehber, derslerin ötesinde "iyi kod" yazmanın felsefesini ve pratik adımlarını içerir.

---

## 🏗️ 1. Kod Okunabilirlik Disiplini
Kod, bilgisayarın anlaması için değil, başka bir insanın (veya 6 ay sonraki sizin) anlaması için yazılır.
- **İsimlendirme:** `int x;` yerine `int studentCount;` kullanın. İsimler bir hikaye anlatmalıdır.
- **Fonksiyon Boyutu:** Bir fonksiyon tek bir iş yapmalı (Single Responsibility) ve bir ekran sayfasına sığmalıdır.

## 🛠️ 2. Refaktör: Sürekli İyileştirme
"Çalışıyor" olduğunda işiniz bitmez, işiniz yeni başlar.
- Kodunuzu yazdıktan sonra AI'ya "Bu kodu SOLID prensiplerine göre nasıl daha temiz hale getirebilirim?" diye sorun.
- Tekrar eden kodlardan (DRY - Don't Repeat Yourself) kaçının.

## 📐 3. Tasarım Kalıpları (Design Patterns)
Tekerleği her seferinde yeniden icat etmeyin.
- **Singleton:** Sadece bir örneği olması gereken sınıflar için.
- **Strategy:** Bir işin birden fazla yolu varsa (örn: farklı sıralama algoritmaları), bunları strateji olarak tanımlayın.

## 🧪 4. "Test-Driven" Zihniyeti
Kodunuzun doğru olup olmadığını "deneyerek" değil, "test ederek" ispatlayın.
- Kodunuzu yazmadan önce, o kodun ne yapması gerektiğini tanımlayan bir test senaryosu düşünün.

---
> "Temiz kod, onu yazan kişinin işine duyduğu saygının ilk göstergesidir."

