---
title: "CPU Nedir, Ne İşe Yarar"
date: 2025-06-01 15:37:00 +0300
categories: [donanımlar]
tags: [işlemci, bilgisayar, donanım]
author: ibrahim
image:
  path: /assets/img/cpu/islemci_dokumani.webp
  alt: İşlemci Dökümanı
description: "İşlemciler hakkındaki en detaylı içerik"
toc: true
math: false
mermaid: false
comments: true
pin: false
---

# İşlemcilerin Temel Bilgileri ve Tarihsel Gelişimi

**İşlemci (CPU)**, bilgisayar sistemlerinin beyni olarak kabul edilen, veri işleme, komut yürütme ve kontrol mekanizmalarını yöneten merkezi işlem birimidir.

**Tarihsel Gelişim Süreci:**
*   **İlk İşlemci Kavramı (1940-1960):** ENIAC (1945) ve UNIVAC (1951) gibi ilk bilgisayarlar merkezi bir işlemci çipine sahip değildi; hesaplama ve kontrol işlemleri vakum tüpleri ve rölelerle dağıtılmış fiziksel yapıda gerçekleştiriliyordu.
*   **Mikroişlemcinin Doğuşu:** 1947'de **transistörlerin** icadı ve ardından 1950-60'larda **entegre devrelerin** gelişimi, çok sayıda transistörün tek bir çipte toplanmasını sağlayarak mikroişlemci teknolojisinin temelini attı.
*   **İlk Mikroişlemciler:**
    *   **Intel 4004 (1971):** İlk ticari mikroişlemciydi. 4 bitlikti ve tüm işlemci bileşenlerini tek bir entegre devreye topladı, **mikroişlemci çağını başlattı**.
    *   **Intel 8086 (1978):** Mikroişlemci tarihinde önemli bir dönüm noktasıydı. 16 bit mimarisi ve 29.000 transistörüyle **x86 mimarisinin başlangıcı** oldu. IBM PC'lerde kullanılmasıyla dünya çapında bir standart haline geldi. Bu başarı, 1980'lerden sonra kişisel bilgisayarların hızla yayılmasının temel nedeniydi.
*   **Çok Çekirdekli Mimarilere Geçiş (1990-2000’ler):** 1990'larda Intel Pentium ve AMD Athlon gibi işlemciler rekabeti artırırken 32-bit mimariler standartlaştı. 2000'li yıllarda ısınma ve yüksek enerji tüketimi sorunları, **çok çekirdekli işlemcilere** yönelimi hızlandırdı. Tek çekirdekli işlemcilerde saat hızını artırmanın sürdürülebilir olmaması, daha düşük frekanslı birden fazla çekirdek kullanma fikrini temel aldı, bu da daha optimize, verimli ve hızlı işlemciler sağladı.
    *   **IBM POWER4 (2001):** İlk ticari çift çekirdekli mikroişlemciyi tanıttı.
    *   **Masaüstü için (2005):** **Intel Pentium D** (iki ayrı çekirdeği tek pakette birleştirdi) ve **AMD Athlon 64 X2** (ilk entegre çift çekirdekli işlemci) üretildi. AMD'nin tasarımı daha iyi performans ve daha az ısı sağlıyordu.
*   **Günümüz ve Gelecek (2010’dan günümüze):** İşlemciler günümüzde sadece bilgisayarlarda değil; akıllı telefonlar, tabletler, sunucular, gömülü sistemler ve yapay zeka altyapıları gibi birçok alanda kullanılmaktadır. Son yıllarda **ARM tabanlı işlemciler** öne çıkmış, yapay zeka ve makine öğrenmesine özel tasarlanmış işlemciler geleceği şekillendirecek gibi görünüyor.

### İşlemcilerin Temel Bileşenleri

Bir işlemcinin ana bileşenleri şunlardır:
*   **ALU (Arithmetic Logic Unit – Aritmetik Mantık Birimi):** Aritmetik ve mantık işlemlerini gerçekleştiren temel dijital devredir.
*   **CU (Control Unit - Kontrol Birimi):** Komutların nasıl işleneceğini belirler, bellekten aldığı komutları yorumlar ve diğer ünitelerin çalışmasını yönlendirir.
*   **Register (Yazmaç):** CPU içinde yer alan, geçici verileri tutan en hızlı bellek birimidir.
*   **Cache (Önbellek):** İşlemcinin verilere hızlı erişimini sağlayan küçük, katmanlı bir bellek alanıdır (**L1, L2, L3**). Veri bekleme süresini (gecikmeyi) azaltır. İşlemci önce cache'e bakar, yoksa RAM'den alır.
*   **Bus (Veri Yolu):** Bilgisayar bileşenleri arasında veri, adres ve kontrol sinyallerini taşıyan elektronik yollardır. **Data Bus**, **Address Bus** ve **Control Bus** olmak üzere türleri vardır.
*   **Instruction Decoder:** Bellekteki makine komutlarını çözümler ve işlemci bileşenlerini yönlendiren kontrol sinyallerini oluşturur.

### İşlemci Çalışma Modları

İşlemcinin çalışma modları, yazılımların donanıma erişim yetkilerini ve işlemcinin yetki seviyesini belirler:
*   **Real Mode (Gerçek Mod):** Eski işlemciler için geçerli, 1 MB bellek sınırı olan, korumasız bir moddur. Modern sistemlerde sadece başlatma sırasında kullanılır.
*   **Protected Mode (Korumalı Mod):** Modern işletim sistemlerinin çalıştığı moddur. Bellek koruması, çoklu görev ve kullanıcı-çekirdek ayrımı sağlar.
*   **User Mode (Kullanıcı Modu):** Uygulama programlarının (oyunlar, ofis yazılımları) çalıştığı, sınırlı yetkilere sahip güvenli moddur. Donanıma doğrudan erişemez.
*   **Kernel Mode (Çekirdek Modu / Supervisor Mode):** İşletim sistemi çekirdeğinin çalıştığı, tüm sistem kaynaklarına sınırsız erişime sahip moddur. Kritik sistem işlemleri burada yürütülür.
*   **Virtual Mode (Sanal Mod / VM86):** Protected Mode altında çalışarak eski gerçek mod programlarının (DOS gibi) modern sistemlerde sanal ortamda çalışmasını sağlar.

### Komut Setleri ve Mimariler

**Komut seti**, işlemcinin anlayabildiği makine komutlarının listesidir. **Mimari**, işlemcinin tasarım ve çalışma yapısını belirler.
*   **CISC (Complex Instruction Set Computing):** Çok sayıda karmaşık komut içeren mimaridir. Donanımın karmaşık işleri üstlenmesi amaçlanır, daha az komutla işlem yapılabilir ama daha fazla güç tüketimi olabilir.
*   **RISC (Reduced Instruction Set Computing):** Daha az ve daha basit komutlar kullanan bir mimaridir. Her komut genellikle tek bir saat döngüsünde çalışır. Donanım basit tutularak daha az enerji tüketir, ancak aynı işlem için daha fazla komut gerekebilir.
*   **SIMD (Single Instruction, Multiple Data):** Aynı komutla birden fazla veriyi aynı anda işleyebilen paralel hesaplama modelidir. Özellikle grafik, ses, video, yapay zeka gibi çoklu veri işlemlerinde kullanılır.
    *   **MMX (1996):** Intel'in multimedya uygulamaları için ilk SIMD uzantısı.
    *   **SSE:** MMX'in geliştirilmişi, kayan nokta (ondalıklı sayı) işlemlerini de destekler.
    *   **AVX:** SSE'nin daha gelişmişi, 256-bit ve 512-bit geniş veri blokları üzerinde çalışır, bilimsel ve yapay zeka hesaplamalarında hız kazandırır.
    *   **FPU (Floating Point Unit):** İşlemcinin ondalıklı sayılarla işlem yapmasını sağlayan özel birimdir.
*   **ARM vs x86:** ARM (RISC mimarisi) düşük güç tüketimi ve yüksek verimlilik sunarken mobil ve gömülü sistemlerde yaygındır. x86 (CISC mimarisi) ise yüksek ham performans sunar ve PC, sunucu alanlarında kullanılır.

### Bellek Yönetimi ve Sanal Bellek

**Bellek yönetimi**, RAM'in verimli ve güvenli kullanımını sağlar. **Sanal bellek**, fiziksel belleğin yetersiz kaldığı durumlarda sabit disk üzerinde ek bellek alanı kullanarak işlemlerin çalışmasını sağlayan bir tekniktir.
*   **Paging (Sayfalama):** Bellek sabit boyutlu sayfalara bölünür. Sanal adresler, sayfa tablosu ile fiziksel adreslere çevrilir. Bellek parçalanmasını azaltır.
*   **Segmentation (Segmentleme):** Bellek mantıksal bölümlere (kod, veri, yığın) ayrılır. Eski x86 mimarilerinde yaygındır.
*   **TLB (Translation Lookaside Buffer):** Sanal adresten fiziksel adrese dönüşümü hızlandıran, işlemci içindeki önbellektir.
*   **Heap ve Stack Yönetimi:** Belleğin kullanım alanlarını belirler. **Stack** LIFO (Last In First Out) prensibiyle otomatik yönetilirken, **Heap** geliştirici tarafından dinamik olarak yönetilir.
*   **MMU (Memory Management Unit):** İşlemcinin bir parçası olup sanal adresleri fiziksel adreslere çeviren donanım birimidir; sanal bellek sistemi MMU olmadan çalışamaz.

### Çalıştırma Seviyeleri (Ring Levels)

İşlemcinin yazılımlara verdiği yetki seviyelerini tanımlar:
*   **Ring 0 (Kernel Modu):** En yetkili seviyedir. İşletim sistemi çekirdeği burada çalışır ve donanıma doğrudan erişim sağlar.
*   **Ring 3 (Kullanıcı Modu):** Uygulama yazılımlarının çalıştığı seviyedir. Donanıma doğrudan erişim yetkisi sınırlıdır, güvenlik için bu modda çalışır.
*   **Ring -1 (Hypervisor Modu):** Sanallaştırma destekli işlemcilerde bulunur. Hypervisor bu modda çalışır ve işletim sistemlerini yönetebilir, Ring 0'ın da üstünde yer alır.

### Çok Çekirdekli ve Çok İş Parçacıklı İşlemciler

*   **Çok Çekirdekli İşlemciler:** Bir işlemci yongasında birden fazla bağımsız işlem birimi (çekirdek) bulunmasıdır.
*   **Çok İş Parçacıklı (Multithreading):** Bir çekirdeğin birden fazla iş parçacığını çalıştırabilmesidir.
    *   **SMT (Simultaneous Multithreading):** Tek bir fiziksel çekirdeğin aynı anda birden fazla iş parçacığını yürütmesini sağlar, fiziksel çekirdek mantıksal çekirdek (thread) gibi davranabilir.
    *   **Hyper-Threading (Intel):** Intel'in geliştirdiği bir SMT teknolojisidir. Bir fiziksel çekirdek iki mantıksal çekirdek gibi çalışır, performansı %15-30 artırabilir.
*   **NUMA (Non-Uniform Memory Access):** Çok işlemcili sistemlerde her işlemcinin kendi yerel belleğine sahip olduğu, ancak diğer işlemcilerin belleğine erişimin daha yavaş olduğu bir bellek mimarisidir.

### İşlemci Performans Metodolojileri

İşlemcinin hızını, verimliliğini ve etkinliğini ölçen yöntemlerdir:
*   **IPC (Instructions Per Cycle):** Bir saat döngüsünde tamamlanan komut sayısını gösterir, işlemcinin verimlilik ölçüsüdür. **Gerçek performans için IPC × Frekans önemlidir**.
*   **Frekans (GHz) ve Overclocking:** Frekans, işlemcinin saniyedeki işlem döngüsü sayısıdır. **Overclocking**, fabrika ayarı frekansının üstüne çıkarılarak daha yüksek performans elde etme işlemidir, ancak ısınma ve sistem kararsızlığı gibi riskleri vardır.
*   **Benchmark Testleri:** İşlemcinin belirli görevlerdeki gerçek dünya performansını ölçen testlerdir (örn. Cinebench, Geekbench).
*   **Gecikme (Latency) ve Bant Genişliği (Bandwidth):** **Gecikme**, bir işlemin başlama ile tamamlanma süresidir. **Bant genişliği**, belirli bir sürede taşınabilen veri miktarıdır (örn. MB/s, GB/s).

### Güç Yönetimi ve Termal Tasarım

*   **TDP (Thermal Design Power):** İşlemcinin yoğun yük altında yayabileceği **maksimum ısı miktarını** ifade eder. Soğutma sistemi bu değere göre tasarlanır ve **işlemcinin gerçek güç tüketimi demek değildir**.
*   **DVS (Dynamic Voltage Scaling):** İşlemci yük durumuna göre voltajını ve frekansını dinamik olarak artırıp azaltabilir. Daha düşük yükte daha az güç tüketimi sağlar.
*   **Turbo Boost (Intel) / Precision Boost (AMD):** İşlemcinin geçici olarak normal saat hızının üstüne çıkmasına olanak tanıyan otomatik hız artırma teknolojileridir.
*   **Throttle (Termal Sıkma):** İşlemci çok ısındığında, zarar görmemesi için performansını (frekansını/voltajını) bilinçli olarak düşürmesidir. Genellikle soğutucu yetersizse veya ortam sıcaklığı yüksekse görülür.

### Modern İşlemciler ve Özel Kullanım Senaryoları

*   **HPC (High-Performance Computing):** Karmaşık bilimsel ve mühendislik problemleri için kullanılan, çok çekirdekli (64+ core), büyük belleğe sahip güçlü sistemlerdir (örn. AMD EPYC, Intel Xeon).
*   **AI ve Makine Öğrenmesi için İşlemciler:** Yapay zeka işlemleri için optimize edilmiş işlemcilerdir. Genellikle matris çarpımları ve yüksek veri paralelliği gerektirdiğinden klasik CPU'lar yetersiz kalabilir. **CPU** küçük ölçekli, **GPU** büyük model eğitimi, **TPU** ise TensorFlow özel işlemlerinde kullanılır.
*   **ARM İşlemciler ve Mobil Teknoloji:** Düşük güç tüketimi ve yüksek verimlilik için tasarlanmış RISC mimarili işlemcilerdir. Akıllı telefonlar, tabletler ve yeni nesil masaüstü bilgisayarlarda (Apple M serisi) kullanılır.
*   **Oyun ve Grafik İşlemcileri:** Oyunlarda **CPU** oyunun akışını (AI, olaylar) yönetirken, **GPU** sahnenin görüntüsünü (ışık, gölge, doku) oluşturur. Bu iş yükü paylaşımı akıcı ve gerçekçi görseller sağlar.
