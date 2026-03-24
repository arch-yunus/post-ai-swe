# 🧠 INTELLIGENCE BRIEF: OPERATING SYSTEMS (OS)

**Mission:** Bilgisayarın çekirdeğine (kernel) hükmetmek.

---

## 🏛️ 1. THE KERNEL: THE OVERSEER (Denetçi)
Sistemdeki tüm kaynakların (CPU, Bellek, I/O) yegane hakimi çekirdektir. 
- **Mastery:** User Mode vs Kernel Mode ayrımını anlayın. Bir sistem çağrısı (syscall) yapıldığında ne olduğunu bilmek, yazılımın gerçek "context"ini anlamaktır.

## 🧵 2. CONCURRENCY: THE PARALLEL WAR
Threads ve Processes arasındaki farkı bilmek yetmez; onları senkronize etme disiplinine (Locks, Mutexes, Semaphores) sahip olmalısınız.
- **Mastery:** Yarış durumu (Race Condition) ve Ölü Lokma (Deadlock) kavramlarını teoride değil, kodunuzun her satırında bir tehdit olarak görün ve önleyin.

## 🗄️ 3. MEMORY VIRTUALIZATION
RAM sınırlıdır, ama hayallerimiz değil. Sanal bellek, size devasa bir alan sunar.
- **Mastery:** Paging ve Segmentasyon mimarisini bilmek, yazdığınız kodun bellekte nasıl "sayfalandığını" ve neden \`Segmentation Fault\` aldığınızı anlamanızı sağlar.

---
\`SIGNAL: KERNEL_INTELLIGENCE_LOCKED\`

