---
title: "CPU Nedir, Ne İşe Yarar"
date: 2025-06-01 15:37:00 +0300
categories: [donanımlar]
tags: [işlemci, bilgisayar, donanım]
author: ibrahim
image:
  path: /assets/img/islemci_dokumani.png
  alt: İşlemci Dökümanı
description: "Python Cuda Tools modülünün dökümanı"
toc: true
math: false
mermaid: false
comments: true
pin: false
---
## İşlemci Nedir?

**İşlemci**, diğer adıyla **merkezi işlem birimi** (Central Processing Unit - CPU), bir bilgisayar sisteminin beyni olarak kabul edilir. Bilgisayarda gerçekleşen tüm işlemlerin temelini oluşturan işlemci; veri işleme, komut yürütme ve kontrol mekanizmalarını yönetir. Bir yazılım ya da donanım bileşeninden gelen talimatları alır, işler ve sonuç üretir.

---

## İşlemcilerin Tarihsel Gelişim Süreci

### İlk İşlemci Kavramı ve Öncesi (1940–1960)

İşlemci kavramı ilk olarak modern bilgisayarların atası sayılan sistemlerin geliştirilmesiyle ortaya çıkmıştır. ENIAC (1945) ve UNIVAC (1951) gibi erken dönemli bilgisayarlar merkezi bir işlemci çipine sahip değildi. Vakum tüpleri ve röleler gibi donanımlar sayesinde hesaplama ve kontrol işlemlerini gerçekleştiriyorlardı. Bu makinelerde işlem birimi, fiziksel olarak dağılmış bir yapıya sahipti. Yani toplama, çarpma, bölme gibi işlemler için özel devre blokları bulunuyordu.

### Mikroişlemcinin Doğuşu

Mikroişlemcilerin temeli aslında **transistör** adı verilen küçük elektronik anahtarlardır. En başta vakum tüpleriyle yapılan işlemler, 1947’de transistörün icadıyla çok daha küçük ve verimli hale gelmiştir. Daha sonrasında 1950–60’larda **entegre devreler** ile birden fazla transistör tek bir çipte toplanabildi. 1970’lerden itibaren transistör boyutlarının küçülmesiyle daha fazla transistör tek bir mikroçip içine yerleştirildi. Bu gelişmeler mikroişlemci teknolojisinin gelişmesinde oldukça önemli yer tutmuştur.

### İlk Mikroişlemciler

#### Intel 4004 (1971)

İşlemci tarihindeki devrim niteliğinde bir teknoloji olan **Intel 4004** ilk ticari mikroişlemcidir. Bu çip, 4 bitlik bir işlemciydi ve 2.300 transistör içeriyordu. İlk kez, tüm işlemci bileşenleri tek bir entegre devre (çip) üzerinde toplanmıştı ve mikroişlemci çağını başlatmıştır.

#### Intel 8008 (1972)

Intel 4004’ün hemen ardından gelen **Intel 8008**, 8 bit’lik bir mikroişlemciydi. 3.500 transistöre sahipti, daha karmaşık hesaplamaları yapabiliyordu ve monitör ve klavye gibi “çevre birimleriyle” etkileşim potansiyeline sahipti.

#### Intel 8086 (1978)

**Intel 8086** mikroişlemci tarihi açısından en önemli dönüm noktalarından biri olmuştur. 16 bit’lik mimarisiyle çok daha güçlüydü. 29.000 transistör içeriyordu. **x86** mimarisinin başlangıç noktası kabul ediliyordu ve IBM PC’lerde kullanılmasıyla birlikte dünya çapında bir standart haline geldi. 8086 işlemcisinin makine dili 8008 gibi Intel’in geçmiş mikroişlemcileriyle kod uyumluydu. Bu cihazlar için yazılmış makine kodları ya çok az düzeltme ile ya da elle düzeltme yapılmaksızın otomatik olarak 8086 koduna dönüştürülebiliyordu.

Intel’in bu işlemcideki başarısı, 1980 ve sonrasında kişisel bilgisayarların hızlı bir şekilde yayılmasının temel nedenlerinden biri olmuştur.

### Kişisel Bilgisayarlar (1980’ler)

Intel 8086 IBM PC’lerde kullanılmaya başlandı, kişisel bilgisayarlar yaygınlaştı ve bunun sonucunda işlemci teknolojisinin gelişimi hızlandı. Bu dönemde Motorola 68000 serisi, AMD gibi rakip firmalar ile birlikte işlemci rekabeti artmaya başladı. Bu sayede daha yüksek saat hızları ve gelişmiş önbellek sistemlerinin geliştirilmesi gibi teknolojik ilerlemeler ile işlemci teknolojisi seviye atlamıştır.

### Çok Çekirdekli Mimarilere Geçiş (1990–2000’ler)

1990’lı yıllarda işlemciler güçlendi. Intel Pentium serisi, AMD K6 ve Athlon gibi işlemciler hem rekabeti kızıştırdı hem de daha güçlüydü. Artık 32-bit mimariler standart haline gelmişti ve 64-bit mimarisine geçiş için temeller atılmaya başlandı.

Bu dönemlerde Stanford Üniversitesi’nde Elektrik Mühendisliği ve Bilgisayar Bilimleri profesörü olan Prof. Kunle Olukotun ana odak tek çekirdekli işlemcilerken çok çekirdekli işlemciler ile ilgili çalışmalar yapmıştır. Hydra isimli çok çekirdekli mikroişlemci projesinin lideridir. Bu proje çok çekirdekli işlemcilerin teorik değil uygulanabilir olduğunu göstermiştir.

2000’li yıllarda ise işlemcilerin gelişimine bağlı olarak ısınma ve yüksek enerji tüketimi sorunları odağın çok çekirdekli işlemcilere çevrilmesine neden olmuştur. İşlemci içine birden fazla çekirdek yerleştirmek bu sorunların çözülmesini sağlamıştır. Tek çekirdekli işlemcilerde hızı arttırmak için sürekli olarak “saat hızı” arttırılıyordu ama bu sürdürülebilir bir sistem değildi. Bu yüzden daha düşük frekanslı birden fazla çekirdek koymak gibi bir fikir temel alınmıştır. Hem daha optimize hem daha verimli hem de daha hızlı işlemciler elde etmek mümkün olmuştur.

**IBM POWER4** ile 2001 yılında ilk kez çift çekirdekli bir mikroişlemci tanıttı. Bu işlemci ticari amaçlıydı. Masaüstü için 2005 yılında **Intel Pentium D** ve **AMD Athlon 64 X2** işlemcileri üretildi. Pentium D tam olarak entegre çok çekirdekli bir sistem değildi, iki ayrı Pentium 4 çekirdeğinin tek pakette birleştirilmiş bir tasarımıydı. AMD ise Athlon 64 X2 işlemcisinde ilk entegre çift çekirdekli işlemciyi yapmıştı. Ayrıca bu tasarımla Intel’e göre daha iyi performans ve daha az ısı oluşumu sağladılar.

### Günümüz ve Gelecek (2010’dan günümüze)

Günümüze bakarsak işlemciler sadece dizüstü veya masaüstü bilgisayarlarda değil; akıllı telefonlar, tabletler, sunucular, gömülü sistemler ve yapay zeka altyapıları gibi pek çok farklı alanda kullanılmaktadır. Qualcomm, Apple, MediaTek, Samsung, HiSilicon, NVIDIA, Unisoc, Rockship, Intel, AMD gibi farklı firmalar farklı alanlarda işlemciler üretmekte ve geliştirmektedir. Son yıllarda **ARM tabanlı işlemciler** gibi farklı mimarilerde işlemciler ön plana çıkmıştır. Yapay zeka ve makine öğrenmesi gibi teknolojilere özel olarak tasarlanmış işlemciler bu teknolojinin geleceği için önemli bir yer kaplayacak ve bu geleceği şekillendirecek gibi görünüyor.

---

## İşlemcilerin Temel Bileşenleri

### ALU (Arithmetic Logic Unit – Aritmetik Mantık Birimi)

Aritmetik mantık birimi, aritmetik ve mantık işlemlerini gerçekleştiren bir dijital devredir. En basit işlemciden en güçlü işlemciye kadar tüm işlemcilerin yapıtaşıdır.

### CU (Control Unit - Kontrol Birimi)

Kontrol birimi, bilgisayarda çalışan komutların nasıl işleneceğini belirler. Bellekten aldığı komutları yorumlar ve bu komutların hangi sırayla ve nasıl yürütüleceğini kontrol eder. Diğer ünitelerin çalışmasını zamanlama ve kontrol sinyalleri sağlayarak yönlendirir.

### Register (Yazmaç)

Registerlar, CPU’nun çalışırken ihtiyaç duyduğu geçici verileri tutar. Register, CPU içinde yer alan en hızlı bellek birimidir. Diğer hafıza türlerinden çok daha hızlı çalışır çünkü doğrudan işlemci içinde yer alır.

### Cache

Cache, işlemcinin verilerini ve komutlarını saklamak, gerektiğinde ise onlara kolayca erişmek için kullanılan küçük bir bellek alanıdır. **L1, L2, L3** olmak üzere katmanlı çalışır. Cache bellek, işlemcinin veri bekleme süresini (gecikmeyi) azaltmak için tasarlanmıştır. RAM'den veri almak, cache'e göre çok daha yavaştır. Bu yüzden işlemci:

* İlk olarak cache'e bakar.
* Gerekli veri varsa (**cache hit**) hemen işler.
* Yoksa (**cache miss**), RAM’den alır ve cache'e koyar.

#### L1 Cache

Doğrudan işlemcinin içinde yer alır, en hızlı çalışan katmandır, veri saklama kapasitesi en küçük olandır.

#### L2 Cache

Çekirdek içinde veya hemen yakınında yer alır, diğer katmanların arasında bir hıza ve veri saklama kapasitesine sahiptir.

#### L3 Cache

Çok çekirdekli sistemlerde yaygındır, tüm işlemciler arasında paylaşımlıdır. Hız olarak en yavaştır.

### Bus

Bus, bilgisayarın bileşenleri arasında veri alışverişi yapılabilmesi için kullanılan elektronik yolların genel adıdır. İşlemcide bus verileri taşır, adresleri iletir, kontrol sinyalleri gönderir.

#### Bus Türleri

* **Data Bus (Veri Yolu)**: CPU ve RAM arası çift yönlü olarak verileri taşır.
* **Address Bus (Adres Yolu)**: Bellek adreslerini taşıyarak CPU‘nun hangi bellek adresine erişeceğini belirtir.
* **Control Bus (Kontrol Yolu)**: Oku, yaz, başlat, dur gibi komutları yani kontrol sinyallerini taşır.

### Instruction Decoder

Bellekte saklanan makine komutlarını alır ve bu komutların hangi işlem olduğunu çözümler. Ardından, gerekli kontrol sinyallerini oluşturarak diğer işlemci bileşenlerini (ALU, register'lar, kontrol birimi vb.) yönlendirir.

---

## İşlemci Çalışma Modları

İşlemcinin çalışma modları, işletim sisteminin ve programların donanım kaynaklarına nasıl erişebileceğini ve işlemcinin hangi seviyede yetkiye sahip olduğunu belirleyen farklı durumlarıdır. Şimdi farklı çalışma modlarına bakalım.

### 1- Real Mode (Gerçek Mod)

* Eski işlemciler (örneğin 8086) için geçerli.
* 1 MB adreslenebilir bellek sınırı.
* Korumasızdır, doğrudan donanım ve bellek erişimi yapılabilir.
* Genellikle modern sistemlerde sadece boot (başlangıç) sırasında kullanılır.
* Sadece x86 mimarilerde geçerlidir.

### 2- Protected Mode (Korumalı Mod)

* Modern işletim sistemlerinin çalıştığı moddur.
* Bellek koruması, çoklu görev, kullanıcı ve çekirdek ayrımı sağlar.
* Gelişmiş bellek yönetimi yapılabilir (sanal bellek gibi).

### 3- User Mode (Kullanıcı Modu)

* Uygulama programları bu modda çalışır (örneğin oyunlar, ofis yazılımları).
* Sınırlı yetkilere sahiptir.
* Donanım doğrudan kontrol edilemez.
* Belleğe, sadece kendi alanı üzerinden erişebilir.
* Güvenlik için bu modda çalışır; sistemin geri kalanı zarar görmez.

### 4- Kernel Mode (Çekirdek Modu / Supervisor Mode)

* İşletim sistemi çekirdeği bu modda çalışır.
* Tüm sistem kaynaklarına sınırsız erişim vardır.
* Donanım, bellek, CPU talimatları tamamen kontrol altındadır.
* Kritik sistem işlemleri burada yürütülür (dosya sistemine erişim, sürücü işlemleri vb.).

### 5- Virtual Mode (Sanal Mod / VM86)

* Protected Mode altında çalışır.
* Eski gerçek mod (DOS gibi) programların modern sistemlerde çalışabilmesi için sanal ortam sağlar.

---

## Komut Setleri ve Mimariler

**Komut seti**, işlemcinin anlayabildiği ve çalıştırabildiği tüm makine komutlarının listesidir. Bu komutlar, işlemciye ne yapması gerektiğini söyler.
**Mimari**, işlemcinin nasıl tasarlandığını ve çalıştığını belirleyen yapıdır. Hem donanım hem yazılım düzeyinde işlemcinin genel özelliklerini tanımlar.

### 1- CISC (Complex Instruction Set Computing)

CISC, çok sayıda karmaşık komutu içeren bir işlemci mimarisidir. Tek bir komut, birden fazla düşük seviye işlemi (yükleme, hesaplama, depolama) gerçekleştirebilir. Amaç donanımın karmaşık işleri üstlenmesi ve yazılımın basit kalmasıdır. Bu sayede daha az makine komutuyla işlem yapılabilir ancak karmaşık donanım sebebiyle daha fazla güç tüketimi olur.

### 2- RISC (Reduced Instruction Set Computing)

RISC, daha az ama daha basit komutlar kullanan bir mimaridir. Her komut, genellikle tek bir saat döngüsünde çalışır. Amaç CISC mimarisinin tersidir. Donanım basit tutularak yazılım ile daha fazla kontrol sağlanır. Bu sayede hem daha hızlı çalışır hem de daha az enerji tüketir ancak aynı işlem için daha fazla komut gerekebilir.

### 3- SIMD (Single Instruction, Multiple Data)

Aynı komutla birden fazla veriyi aynı anda işleyebilen paralel hesaplama modelidir. Özellikle grafik, ses, video gibi çoklu veri işlemlerinde kullanılır. Görüntü işleme, bilimsel hesaplama ve yapay zeka işlemlerinde kullanılır.

#### Destekleyen Teknolojiler:

* **MMX (MultiMedia eXtension)**: Intel tarafından 1996’da multimedya uygulamalarını hızlandırmak amacıyla tanıtılmış ilk SIMD uzantısıdır. Görüntü, ses, video gibi medya verilerini aynı anda, paralel olarak işleme yeteneğine sahiptir. Sadece tam sayılar (integer) ile çalışır. Ondalıklı sayılar için yeterli değildir. Günümüzde MMX yerine daha gelişmiş uzantılar (SSE, AVX) kullanılır.
* **SSE (Streaming SIMD Extensions)**: MMX’in geliştirilmiş halidir. SIMD yaklaşımıyla çalışır ve kayan nokta (float - ondalıklı sayı) işlemleri de destekler. Ses/video kodlama, 3D oyunlar, fizik hesaplamaları, sinyal işleme gibi işlemleri hızlandırır.
* **AVX (Advanced Vector Extensions)**: SSE’nin daha da gelişmiş halidir. 256-bit (ve AVX-512 ile 512-bit) geniş veri blokları üzerinde çalışabilir. Bilimsel hesaplamalar, yapay zeka işlemleri, kriptografi, büyük veri kümeleri üzerinde müthiş hız kazandırır. Aynı anda 8 adet float veya 4 adet double işlemi yapılabilir. AVX2, AVX-512 gibi sürümleri vardır. Bunlar daha yüksek paralellik sağlar.
* **FPU (Floating Point Unit – Kayan Nokta İşlem Birimi)**: FPU, işlemcinin ondalıklı sayılarla (kayan nokta sayılarla) işlem yapmasını sağlayan özel birimidir. Bilimsel hesaplamalar, grafik uygulamaları ve mühendislik programlarında çok kullanılır. Oyun motorları, fizik simülasyonları, 3D grafik hesaplamaları gibi alanlarda kullanılır.

### 4- VLIW (Very Long Instruction Word)

Tek bir çok uzun komut sözcüğü içinde birden fazla bağımsız işlem barındıran mimaridir. Paralel işlemeyi yazılım belirler. Donanım karmaşıklığı azalır ancak derleyicinin karmaşıklığı artar.

### 5- EPIC (Explicitly Parallel Instruction Computing)

VLIW'nin geliştirilmiş halidir. Derleyici, paralel çalışacak işlemleri açıkça belirtir. Instruction-level parallelism (ILP) hedeflenir. Çok yüksek paralellik potansiyeli gösterir. Ancak karmaşık yazılıma sahiptir ve geriye uyumluluğu düşüktür.

### 6- ARM vs x86

| Özellik           | ARM (RISC)                 | x86 (CISC)                |
| :---------------- | :------------------------- | :------------------------ |
| Komut Seti        | Az ve basit                | Geniş ve karmaşık         |
| Güç Tüketimi      | Düşük (mobil cihazlar)     | Yüksek (masaüstü)         |
| Performans        | Enerji verimli             | Yüksek ham performans    |
| Kullanım Alanı    | Mobil, gömülü sistemler    | PC, sunucu, dizüstü       |
| Üreticiler        | ARM Ltd., Apple, Qualcomm | Intel, AMD                |

---

## Bellek Yönetimi ve Sanal Bellek

**Bellek yönetimi**, işletim sistemi ve işlemcinin bilgisayar belleğini (RAM) en verimli ve güvenli şekilde kullanmasını sağlayan işlemlerdir.
**Sanal bellek**, fiziksel belleğin yetersiz kaldığı durumlarda sabit disk üzerinde bellek gibi davranan ek bir alan kullanarak işlemlerin sorunsuz çalışmasını sağlayan bir tekniktir.

### 1- Adresleme Modları

Bellekte bir veriye nasıl ulaşılacağını belirler. İşlemci komutları, veri adreslerine bu modlarla erişir:

* **Doğrudan (Direct)**: Adres komutta doğrudan yazılır.
* **Dolaylı (Indirect)**: Adres, başka bir bellek konumunda bulunur.
* **Göreceli (Relative)**: Adres geçerli konuma göre hesaplanır.
* **Register Adresleme**: Veri doğrudan register içindedir.
* **Endeksli (Indexed)**: Temel adres + offset (Offset başlangıç noktasından ne kadar ileri ya da geri gidileceğini belirtir.)

### 2- Paging ve Segmentation

Modern işletim sistemleri, belleği daha verimli ve güvenli kullanmak için bu iki tekniği kullanır.

#### Paging (Sayfalama)

* Bellek, sabit boyutlu sayfalara bölünür (örneğin 4 KB).
* Her işlem kendi sanal sayfalarını kullanır.
* Gerçekte hangi fiziksel belleğe karşılık geldiğini işletim sistemi belirler.
* **Sayfa tablosu (Page Table)** ile sanal → fiziksel adres çevrimi yapılır.
* **Avantajı**: Belleğin parçalanmasını azaltır, bellek paylaşımını kolaylaştırır.

#### Segmentation (Segmentleme)

* Bellek, mantıksal bölümlere ayrılır: kod, veri, yığın (stack) vs.
* Her segment farklı boyutta olabilir.
* Eski x86 mimarilerde daha yaygındır.
* **Avantajı**: Kod ve verinin ayrı segmentlerde olması güvenlik sağlar.

### 3- TLB (Translation Lookaside Buffer)

TLB, sanal adresten fiziksel adrese dönüşümü hızlandırmak için işlemci içinde bulunan önbellektir.
Sayfa tablosuna gitmek yavaş bir işlemdir. Bu nedenle dönüşümler TLB’ye kaydedilir; aynı adres tekrar istendiğinde çok daha hızlı alınır.

### 4- Heap ve Stack Yönetimi

Belleğin nasıl kullanıldığını anlatan iki temel alandır:

* **Stack**, **LIFO** yani Last In First Out mantığıyla çalışır. Temel mantığı: depolanacak son öğe ilk işlenir.
* **Heap**, geliştirici tarafından dinamik olarak yönetilir. `malloc` gibi işlemlerle bellek ayırtılır.

Stack otomatik yönetilir; Heap manuel olarak ayrılır ve serbest bırakılır.

### 5- MMU (Memory Management Unit)

MMU, işlemcinin bir parçasıdır ve sanal adresleri fiziksel adreslere çeviren donanım birimidir.
**MMU olmadan sanal bellek sistemi çalışamaz.**

* Sanal bellek adreslerini fiziksel belleğe çevirir.
* Sayfalama ve segmentleme işlemlerini yürütür.
* TLB’yi yönetir.
* Bellek erişimlerini kontrol eder.

---

## Çalıştırma Seviyeleri (Ring Levels)

**Ring Levels**, işlemcinin yazılımlara verdiği yetki seviyelerini tanımlar. Amaç, sistemi güvenli, kararlı ve kontrollü hale getirmektir.

### Ring 0: Kernel Modu (Çekirdek Seviyesi)

* Çalıştırma seviyeleri arasında en yetkili olan seviyedir.
* İşletim sistemi çekirdeği burada çalışır ve donanımlara doğrudan erişim sağlanır.
* Burada kodda yapılacak bir hata tüm sistemin çökmesine neden olabilir.
* Bellek yönetimi, işlemci kontrolü ve sürücü yönetimi gibi işlemleri yapabilme imkanı tanır.

### Ring 1 ve Ring 2: Ara Seviyeler

* Sürücüler veya çekirdek moduna yakın ama tam yetkili olmayan yazılımlar için ayrılmıştır.
* Genelde modern işletim sistemlerinde kullanılmaz.
* Çoğu modern OS (Windows, Linux) bu seviyeleri Ring 0 ve Ring 3 arasında geçirimsiz kabul eder.
* Yani herhangi iki seviye birbirine doğrudan geçemez.

### Ring 3: Kullanıcı Modu (User Mode)

* Uygulama yazılımlarının çalıştığı seviyedir.
* Donanıma doğrudan erişme yetkisi yoktur ve bellek erişimi sınırlıdır.
* Sistem çağrıları yaparak Ring 0’daki işlemleri dolaylı çalıştırır.
* Hatalı çalışırsa sadece program çöker, sistem çökmez.
* Tarayıcı, oyun, Word, Photoshop gibi kullanıcı programları bu seviyede çalışır.

### Ring -1: Hypervisor Modu (VMX Root Mode)

* Hypervisor (sanal makine yöneticisi) bu modda çalışır.
* Sanallaştırma destekli işlemcilerde bulunur.
* Ring 0’ın da üstünde çalışır.
* Bu sayede işletim sistemlerini yönetebilir.
* Sanal makineler Ring 0’da çalışıyormuş gibi olur ancak gerçek donanıma erişemezler.

---

## Çok Çekirdekli ve Çok İş Parçacıklı (Multithreading) İşlemciler

**Çok çekirdekli işlemciler**, bir işlemci yongası üzerinde birden fazla çekirdeğin bulunmasıdır. Her çekirdek bağımsız bir işlem birimi gibi çalışır.
**Çok iş parçacıklı** ise bir çekirdeğin birden fazla iş parçacığını çalıştırabilmesidir.
(Örneğin bir tarayıcının aynı anda birden fazla işi; yani video oynatma, sayfa yükleme, reklam güncelleme gibi her işin her biri farklı iş parçacığı olarak çalışır.)

### 1- SMT (Simultaneous Multithreading)

Aynı anda birden fazla iş parçacığını tek çekirdekte yürütme teknolojisidir.

* **Fiziksel çekirdek**: İşlemci üzerindeki gerçek donanım.
* **Mantıksal çekirdek (Thread)**: Fiziksel çekirdeğin birden fazla iş parçacığını aynı anda çalıştırabilmesini sağlayan yazılımsal görünüm.

SMT ile her fiziksel çekirdek, 2 mantıksal çekirdek gibi davranabilir.

### 2- Hyper-Threading Teknolojisi (Intel)

Intel’in geliştirdiği bir SMT teknolojisidir.
Bir fiziksel çekirdek, iki mantıksal çekirdek gibi davranır.
Yani 4 fiziksel çekirdek 8 iş parçacığı aynı anda çalışabilir gibi görünür.
Çalışma şekli:

* Aynı donanım, boşta kalan kaynakları ikinci bir iş parçacığına verir.
* Bu sayede performans %15–30 civarında artar.

### 3- NUMA (Non-Uniform Memory Access)

NUMA, çok işlemcili sistemlerde her işlemcinin (ya da işlemci grubunun) kendi yerel belleğine sahip olduğu bir bellek mimarisi modelidir.
Ancak her işlemci, diğer işlemcilerin belleğine de erişebilir; sadece bu erişim daha yavaş olur.
Yani bellek erişim süreleri tüm çekirdekler için eşit değildir.

* Her işlemci (ya da işlemci kümesi) kendi RAM’ine doğrudan bağlıdır (yerel bellek).
* Diğer işlemcilerin RAM’lerine erişmek için ara bağlantılar kullanılır (uzak bellek).

---

## İşlemci Performans Metodolojileri

Bu, işlemcinin ne kadar hızlı, verimli ve etkili çalıştığını ölçen yöntemlerin ve kavramların bütünüdür.

### 1- IPC (Instructions Per Cycle)

IPC, bir işlemcinin bir saat döngüsünde kaç adet komutu tamamlayabildiğini gösterir. IPC, verimlilik ölçüsüdür.
**Örnek**:
İşlemci 1 GHz ise ve 1 cycle'da 2 komut tamamlıyorsa → IPC = 2 olur.
Ayrıca 4 GHz ama IPC’si 1 olan CPU, 2 GHz ve IPC’si 3 olan CPU'dan daha yavaş olabilir.
**Yüksek saat hızı yüksek performans demek değildir.**
Gerçek performans için **IPC × Frekans** önemlidir.

### 2- Frekans (GHz) ve Overclocking

#### Frekans

* İşlemcinin saniyede kaç milyon/milyar işlem döngüsü yaptığıdır.
* Ölçü birimi GHz’dir.
* 1 GHz = 1 milyar cycle/saniye

#### Overclocking (Hız Aşırtma)

* İşlemcinin fabrika ayarı frekansının üstüne çıkarılmasıdır.
* Bu sayede daha yüksek performans elde edilebilir.
* **Ancak**:
    * Fazla ısınma
    * Sistem kararsızlığı
    * Artan güç tüketimi
    * gibi riskleri de beraberinde getirir.

### 3- Benchmark Testleri

**Benchmark**, işlemcinin belirli görevlerde gerçek dünyadaki performansını ölçen testlerdir.
Farklı senaryolarda işlemcinin:

* Ne kadar hızlı işlem yaptığı
* Kaç iş parçacığıyla çalıştığı
* Bellek ve I/O erişimlerini ne kadar etkili yönettiği
* gibi değerler ölçülür.

**Örnek Benchmark Araçları**:

* **Cinebench**: Çok çekirdekli performans, video işleme, render testi
* **Geekbench**: Tek ve çok çekirdekli genel sistem testi
* **SPEC CPU**: Akademik ve endüstriyel kıyaslama (bilimsel uygulamalar)
* **PassMark**: Genel kullanıcı sistem karşılaştırması testidir

### 4- Gecikme (Latency) ve Bant Genişliği (Bandwidth)

#### Latency (Gecikme)

* Bir işlemin veya verinin başlaması ile tamamlanması arasındaki süredir.
* **Örnek**: bir komutun tamamlanması, bellekten veri getirme süresi, ağ cevabı...

#### Bandwidth (Bant Genişliği)

* Belirli bir sürede ne kadar veri taşınabildiğidir.
* Genellikle MB/s veya GB/s olarak ölçülür.
* **Örnekler**:
    * Bellek bandwidth: Saniyede kaç GB veri RAM'den CPU’ya taşınabilir?
    * SSD bandwidth: Diskin veri aktarım hızı

---

## Güç Yönetimi ve Termal Tasarım

**Güç yönetimi**, işlemcinin (ve diğer donanımların) güç tüketimini kontrol ederek, hem ısı üretimini azaltmak hem de performansı dengelemek amacıyla yapılan tüm teknolojileri kapsar.
**Termal tasarım** ise, bu ısının nasıl kontrol edildiğini, ne kadar ısıya tolerans gösterilebileceğini ve sistemin buna göre nasıl soğutulması gerektiğini belirler.

### 1- TDP (Thermal Design Power)

**TDP**, işlemcinin yoğun yük altında çalışırken yayabileceği maksimum ısı miktarını ifade eder.
Ölçü birimi: Watt
Bu değer, soğutma sistemi (fan, sıvı soğutma) tasarlanırken dikkate alınır.
Örneğin 65W TDP işlemci ortalama yükte 65 watt ısı yayar, buna göre bir soğutucu gerekir.
**Bu, işlemcinin gerçek tükettiği güç demek değildir.**
**TDP ≠ Güç Tüketimi**
TDP, soğutma kapasitesi ihtiyacıdır.

### 2- DVS (Dynamic Voltage Scaling)

**İşlemci yük durumuna göre gerilimini (voltaj) ve frekansını dinamik olarak artırıp azaltabilir.**
Amaç, gerektiğinde işlemciyi hızlandırıp, boşta iken tasarruf yapmasını sağlamaktır.

* Düşük yükte → daha az voltaj → daha az ısı ve daha az güç tüketimi
* Yük arttığında → voltaj yükselir → performans artar

**Bu teknoloji özellikle dizüstü bilgisayarlarda daha sessiz çalışma ve daha uzun pil ömrü sağlar.**

### 3- Turbo Boost (Intel) / Precision Boost (AMD)

Bu teknolojiler, işlemcinin geçici olarak normal saat hızının üstüne çıkmasına olanak tanır.

* İşlemci sıcaklığı, güç limiti ve çekirdek durumu uygunsa → frekans artırılır
* İşlem bitince veya ısı artınca → frekans normale döner

**Bu bir overclock değildir.**
İşlemci üreticisinin belirlediği güvenli sınırlar içinde yapılan otomatik hız artışıdır.

### 4- Throttle (Termal Sıkma) ve Isı Yönetimi

#### Throttle (Termal Sıkma):

İşlemci çok ısındığında, zarar görmemesi için performansını bilinçli olarak düşürür:

* Frekans düşer
* Voltaj azalır
* Performans yavaşlar

Amaç, işlemciyi korumaktır.
**Sistem kapanmadan önce kendini otomatik olarak soğutmaya alır.**
Bu durum genellikle:

* Soğutucu yetersizse
* Ortam sıcaklığı çok yüksekse
* Uzun süre tam yükte çalışılıyorsa
* gibi senaryolarda görülür.

---

## Modern İşlemciler ve Özel Kullanım Senaryoları

### 1- HPC – High-Performance Computing (Yüksek Başarımlı Hesaplama)

HPC, karmaşık bilimsel, mühendislik ve akademik problemleri çözmek için kullanılan çok güçlü sistemler ve işlemciler anlamına gelir.

#### Kullanım Alanları:

* Hava tahmini
* Nükleer simülasyonlar
* Genetik analiz
* Fizik/moleküler modelleme

#### Özellikleri:

* Çok çekirdekli işlemcilere sahiptirler (64+ core)
* NUMA yapıları bulunur
* Büyük bellek erişimleri vardır (TB düzeyinde RAM)
* Genellikle sunucu sınıfı işlemciler: AMD EPYC, Intel Xeon

### 2- AI ve Makine Öğrenmesi için İşlemciler

Yapay zeka ve derin öğrenme işlemleri için özel olarak optimize edilmiş işlemcilerdir.

#### Neden özel işlemci gerek?

* AI işlemleri matris çarpımları içerir.
* Çok yüksek veri paralelliği gerekir.
* Klasik CPU’lar yetersiz kalabilir.

#### Kullanım Senaryoları:

* **CPU**: Küçük ölçekli makine öğrenmesi
* **GPU**: Büyük model eğitimi
* **TPU**: TensorFlow özel işlemlerinde

### 3- ARM İşlemciler ve Mobil Teknoloji

**ARM**, düşük güç tüketimi ve yüksek verimlilik için tasarlanmış RISC mimarili işlemcilerdir.

#### Kullanım Alanları:

* Akıllı telefonlar
* Tabletler
* Akıllı saatler
* Raspberry Pi
* Apple M1, M2 gibi masaüstü ARM CPU’ları

#### Özellikleri:

* Düşük TDP (Termal güç): pil dostu
* Yüksek verimlilik
* ARMv8, ARMv9 komut seti
* Genellikle SoC (System-on-Chip) içinde çalışır (GPU, NPU, RAM dahil)

### 4- Oyun ve Grafik İşlemcileri

Oyunlarda hem CPU hem GPU birlikte çalışır ama görevleri farklıdır:

* **CPU**: Oyunun akışını yönetir (karakter hareketleri, yapay zeka, olaylar)
* **GPU**: Sahnenin görüntüsünü oluşturur (ışık, gölge, doku, çözünürlük)

**Bu iş yükü paylaşımı sayesinde oyunlar hem akıcı çalışır hem de daha gerçekçi görseller üretilebilir.**
