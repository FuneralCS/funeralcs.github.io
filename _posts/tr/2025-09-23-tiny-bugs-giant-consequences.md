---
title: "Küçük Hatalar, Dev Sonuçlar"
date: 2025-09-23 03:43:00 +0300
categories: [teknoloji, tarih]
tags: [software bug, case study, software engineering, system failure]
author: kerim
image:
  path: /assets/img/2025-09-23-tiny-bugs-giant-consequences/kapak-fotografi.webp
  alt: ""
description: "Tarihin en kötü yazılım hatalarından Therac-25, Patriot Füze ve Mars Climate Orbiter'ı derinlemesine inceleyerek, bunlardan çıkarabileceğimiz dersleri ele alıyoruz."
toc: true
math: true
mermaid: false
comments: true
pin: false
lang: tr
---

## Tiny Bugs, Giant Consequences  
English version 🇬🇧 ➤ [Tiny Bugs, Giant Consequences](https://funeralcs.com/en/posts/tiny-bugs-giant-consequences/)

Yazılımlar nadiren tek bir satırlık hatalı koddan dolayı çöker. Asıl çöküş; insan faktörleri, eksik güvenlik kilitleri, sessiz kullanıcı arayüzleri ve test edilmemiş varsayımlar bu kodun etkisini bir felakete dönüştürdüğünde yaşanır. Aşağıda, en küçük dijital hataların gerçek dünyada nasıl en büyük sonuçlara yol açabileceğini görmek için üç gerçek olayı ele alacağız: Therac-25, Patriot füzesinin zaman kayması ve Mars Climate Orbiter.

### Vaka Çalışması: Arıza 54: Ölümcül Hale Gelen Hata Kodu

> 1985 ile 1987 yılları arasında, THERAC-25 adlı son teknoloji radyasyon tedavisi makinesi, en az altı hastaya aşırı dozda radyasyon vererek ölümcül sonuçlara yol açtı. Bu olayın arkasındaki hikaye, güvenlik göz ardı edildiğinde basit bir yazılım hatasının nasıl ölümcül hale gelebileceğine dair mükemmel bir ders niteliğindedir.
{: .prompt-info }

<figure>
    <img src="/assets/img/2025-09-23-tiny-bugs-giant-consequences/Kennestone-Hospital.webp" width="650" alt="Kennestone Hastanesi">
</figure>

<figure>
    <img src="/assets/img/2025-09-23-tiny-bugs-giant-consequences/THERAC-25.webp" width="650" alt="THERAC-25 Cihazı">
</figure>

#### Temel Neden: Gizli Yazılım Hataları

Makinenin kodunun derinliklerinde, iki kritik hata ortaya çıkmayı bekliyordu. Bunları bu kadar ölümcül kılan şey, Therac-25'in tamamen yazılıma dayalı olarak tasarlanmış olmasıydı. Eski modellerde bu tür kazaları önleyecek fiziksel güvenlik kilitleri vardı, ancak bunlar kaldırılmıştı.

<figure>
    <img src="/assets/img/2025-09-23-tiny-bugs-giant-consequences/Therac-25-2-modes.webp" width="650" alt="Therac-25'in iki çalışma modu">
</figure>

> Peki, tam olarak ne oldu?
{: .prompt-info }

**1. “Çok Hızlı” Hata (Race Condition):** Makinenin iki modu vardı: düşük güçlü, hassas bir Elektron Işını ve 100 kat daha güçlü, metal kalkan gerektiren bir X-Işını. Deneyimli bir operatör yazarken hata yapıp 8 saniye içinde düzelttiğinde, bir kusur ortaya çıkıyordu:

- **Ekran**, güvenli, düşük güçlü ayarı gösterirdi.  
- Ancak **makinenin donanımı**, kalkan olmadan tam güçlü X-ışını ateşlemeye hala hazırdı.  

Yazılım, ekran ve donanımın senkronize olup olmadığını karşılıklı olarak asla kontrol etmiyordu.

**2. “Sıfırlanma” Hatası (Integer Overflow):** Yazılımdaki bir sayaç, operatörün yaptığı ayarlamaları takip ediyordu. Ancak sayaç çok küçüktü; tıpkı 255'e kadar çıkabilen ve sonra 0'a dönen bir araba kilometre sayacı gibi. 

<figure>
    <img src="/assets/img/2025-09-23-tiny-bugs-giant-consequences/overflow.webp" width="650" alt="Integer overflow canlandırması">
</figure>

> Programcılar ölümcül bir hata yaptılar: “Ateşleme Güvenli!” sinyali olarak 0 rakamını kullandılar.
{: .prompt-danger }

Operatör, sayacın 255'ten 0'a dönmesi için yeterli ayarlamaları yaparsa, yazılım yanlışlıkla “sıfır, güvenli olduğu anlamına gelir!” diye düşünür ve herhangi bir güvenlik kalkanı olmadan ışını ateşlerdi. Bu özel hata, belgelenen son aşırı dozun sorumlusuydu.

#### Bir Hata Nasıl Felakete Dönüştü: Başarısızlık Zinciri

Bu hatalar tehlikeyi yarattı, ancak bir dizi kötü tasarım tercihi bunların ölümcül hale gelmesine izin verdi.

<figure>
    <img src="/assets/img/2025-09-23-tiny-bugs-giant-consequences/Therac-25-simulation.webp" width="650" alt="Therac-25 hata canlandırması">
</figure>

> Therac-25'in ölümcül yazılım hatasının bir canlandırması
{: .prompt-warning }
 - **Uyarı İşe Yaramazdı:** Makine tehlikeli bir duruma girdiğinde, kırmızı “TEHLİKE” işareti yanıp sönmedi. Sadece “Arıza 54” gibi anlaşılmaz bir mesaj görüntüledi. Kullanım kılavuzunda bunun ne anlama geldiği bile açıklanmamıştı.  
 - **Operatörler Hataları Görmezden Gelmeye Alışmıştı:** Makine o kadar güvenilmezdi ki, her gün düzinelerce anlamsız hata mesajı gösteriyordu. Operatörler, “çözümün” her zaman aynı olduğunu öğrendiler: Devam etmek için sadece “P” tuşuna basmak. Makine, kısacası, tek bir rutin tuş basışıyla ölümcül bir hatayı geçersiz kılmalarına izin veriyordu.  
 - **Üretici Sorunu İnkar Etti:** Hastaneler ilk korkunç yaralanmaları bildirdiğinde, üretici AECL, makinelerinin mükemmel olduğunu ve aşırı dozun “imkansız” olduğunu ısrarla savundu. Bu inkar, kritik düzeltmelerin gecikmesine ve daha fazla hastanın tehlikeye atılmasına neden oldu.  


Sonuçta, Therac-25 trajedisi sadece kötü koddan ibaret değildi. Tasarım, güvenlik ve sorumluluk açısından bir başarısızlıktı ve yazılım dünyasında nelerin tehlikede olduğunu hatırlatan tüyler ürpertici bir uyarıydı.

---

### Vaka Çalışması: 600 Metrelik Hesap Hatası

> 1991 yılında, Körfez Savaşı sırasında, bir Amerikan Patriot füze bataryası, gelen bir Irak Scud füzesini önleyemedi. Scud, bir ABD Ordusu kışlasını vurdu, 28 Amerikan askeri öldü ve yaklaşık 100 kişi yaralandı. Ardından yapılan soruşturma, şok edici bir nedeni ortaya çıkardı: bu facia, düşmanın sinyal bozma veya mekanik bir arıza nedeniyle değil, sistemin yazılımındaki küçük, biriken bir hata nedeniyle meydana gelmişti.
{: .prompt-info }

<figure>
    <img src="/assets/img/2025-09-23-tiny-bugs-giant-consequences/Correctly-Calculated-Missile.webp" width="650" alt="Doğru hesaplanmış füze yörüngesi">
</figure>

> Patriot Radar Sistemi'nin normalde bu şekilde çalışması gerekiyordu.
{: .prompt-info }

#### Temel Neden: İkili Sayı Sistemindeki Bir Kusur

Patriot sisteminin yazılımı, açıldığı andan itibaren zamanı takip etmek üzere tasarlanmıştır. Dahili saati her saniyenin onda birinde bir tik atmaktadır. Sorun burada başlamıştır:

- **Ondalık-İkili Sorunu:** `1/10` sayısını `0.1` olarak yazmak bizim için kolaydır. Ancak, bilgisayarın ana dili olan ikili (2 tabanlı) sistemde `0.1` sayısı sonsuz, tekrar eden bir kesir haline gelir.  
- **Kırpma Hatası:** Sistemin bilgisayarı bu değer için yalnızca sınırlı sayıda bit depolayabilirdi. Bu nedenle, tekrar eden kesrin sonunu “kesmek” zorundaydı. Bu basit işlem, saatin her tikinde yaklaşık 0,000000095 saniyelik mikroskobik bir hata yarattı.  

> Bilgisayarların ondalık sayıları temsil etme şeklinin bir sonucu olan bu küçük hata, arızanın temel nedeniydi.
{: .prompt-danger }

#### Mikroskobik Bir Hata Nasıl Bir Felakete Dönüştü?

Tek başına bu kadar küçük bir hata tamamen önemsizdir. Ancak, bu tür sayısal hataların asıl tehlikesi, zamanla birikerek büyüme potansiyelleridir.

- **Birikim:** Patriot bataryası 100 saatten fazla süreyle kesintisiz çalışıyordu. 100 saat boyunca saniyenin her onda birinde, bu küçük hata saatin toplam süresine eklendi.  
- **Sapma:** 100 saatten fazla bir süre boyunca birikerek, hatalar sistemin dahili saatinin yaklaşık 0,34 saniye geri kalmasına neden oldu.  

<figure>
    <img src="/assets/img/2025-09-23-tiny-bugs-giant-consequences/Incorrectly-calculated-missile.webp" width="650" alt="Yanlış hesaplanmış füze yörüngesi">
</figure>

<figure>
    <img src="/assets/img/2025-09-23-tiny-bugs-giant-consequences/Alpha-Battery-new.webp" width="650" alt="Alpha Bataryası'nın konumu">
</figure>

Bir insan için saniyenin üçte biri hiçbir şey ifade etmez. Ancak, saatte yaklaşık 6.000 km hızla hareket eden bir hedefi takip eden bir hava savunma sistemi için bu çok büyük bir farktır. Sistem Scud füzesini doğru bir şekilde tespit etti, ancak iç saati saptığı için hedefin gelecekteki konumuna ilişkin hesaplaması hatalıydı.

Scud'un olacağı yerin son tahmini 600 metreden fazla sapmıştı. Sistem, hedefi gökyüzünün yanlış bir bölgesinde aradı, tehdit olmadığı sonucuna vardı ve önleyici füzesini hiç fırlatmadı. Zamanla biriken mikroskobik bir yazılım yuvarlama hatası, doğrudan feci bir arızaya yol açtı.

---

### Vaka Çalışması: Bir Görevi Yok Eden Birim Hatası

> Eylül 1999'da, NASA'nın 125 milyon dolarlık Mars Climate Orbiter'ı dokuz aylık bir yolculuğun ardından kızıl gezegene ulaştı, ancak iz bırakmadan ortadan kayboldu. Görev tamamen başarısız olarak ilan edildi. Ardından yapılan soruşturma şaşırtıcı bir neden ortaya çıkardı: uzay aracı, bir motor patlaması veya donanım arızası yüzünden değil, yer kontrol yazılımındaki basit ve utanç verici bir karışıklık nedeniyle kaybolmuştu.
{: .prompt-info }

<div style="display: flex; justify-content: center; align-items: center; gap: 8px;">
  <img src="./assets/img/2025-09-23-tiny-bugs-giant-consequences/Mars_Climate_Orbiter_-_launch_configuration.webp" alt="Mars Climate Orbiter Diagramı" style="width: 350px; height: 390px; object-fit: cover;">
  <img src="./assets/img/2025-09-23-tiny-bugs-giant-consequences/Mars-Climate-Orbiter-launch.webp" alt="Mars Climate Orbiter Fırlatma Anı" style="width: 350px; height: 390px; object-fit: cover;">
</div>

#### Temel Neden: Birimlerdeki Basit Bir Uyumsuzluk

Görev bir iş birliğiydi. Yüklenici Lockheed Martin, Mars Climate Orbiter'ın iticilerini kontrol eden yer yazılımını geliştirirken, NASA'nın Jet Propulsion Laboratory (JPL) ekibi navigasyonu yönetiyordu. Tüm görevi baltalayan asıl hata, aralarındaki iletişim boşluğundan kaynaklandı.

> **Birim Uyumsuzluğu (Sistem Entegrasyon Hatası):** Lockheed Martin'in yazılımı itici gücü **pound-force** cinsinden hesaplarken, NASA'nın yazılımı bu veriyi **newton** cinsinden bekliyordu. 
>
> $$\Large {1 \mathit{\ pound\ force} = 4.44822162 \mathit{\ newtons}}$$
{: .prompt-danger }

<figure>
    <img src="/assets/img/2025-09-23-tiny-bugs-giant-consequences/Mars_Climate_Orbiter_-_mishap_diagram.webp" width="650" alt="Mars Climate Orbiter yörünge hatası diyagramı">
</figure>

#### Bir Hata Nasıl Felakete Dönüştü: Başarısızlıklar Zinciri

- **Biriken Hata:** NASA'nın yaptığı her hesaplama 4,45 kat hatalıydı. Küçük düzeltmeler yaptıklarını sanıyorlardı, ancak aslında uzay aracını her ateşlemede rotasından daha da uzaklaştırıyorlardı.  
- **“Uçtan Uca” Testin Yapılmaması:** Ekipler, iki yazılım sistemini hiçbir zaman birlikte test etmediler. Basit bir entegrasyon testi bu hatayı anında ortaya çıkarabilirdi.  
- **Uyarılar Gözden Kaçırıldı:** Mühendisler sapmayı fark ettiler, ancak bunu yeterince hızlı bir şekilde üstlerine bildirmediler. 9 ay sonra, hata katlanarak büyüdü ve sonunda uzay aracı kayboldu.  


 >***Sonuç:** Basit bir birim dönüştürme hatası nedeniyle tüm görev başarısız oldu. Bu olay, kapsamlı testlerin ve net iletişimin önemini gösteren unutulmaz bir ders niteliğindedir.*
 {: .prompt-warning }
 
Bu hikayelerin ortak bir noktası vardır: En büyük felaketlere yol açan başarısızlıklar genellikle en küçük ve en “insani” hatalarla başlar. Bunlar kötü niyetli hackerlar veya kontrolden çıkmış yapay zekalar tarafından değil, basit gözden kaçırmalar, hatalı varsayımlar ve iletişim kopuklukları nedeniyle meydana geldi. Bu olaylar, yazılım mühendisliğindeki en büyük zorluğun sadece bir şeyleri çalıştırmak olmadığını güçlü bir şekilde hatırlatıyor. Asıl zorluk, işler kaçınılmaz olarak ters gittiğinde bunu öngörmek ve güvenli bir şekilde yönetmektir. 
 
Bunlar, işlevsel kodun sadece başlangıç noktası olduğunu kanıtlıyor; bir sistemin gücünün gerçek ölçüsü, kendi kaçınılmaz kusurlarıyla ne kadar ustalıkla başa çıktığıdır. 

---

### Kaynakça & İleri Okuma

THERAC-25:  
- [Death and Denial: The Failure of the THERAC-25, A Medical Linear Accelerator](https://users.csc.calpoly.edu/~jdalbey/SWE/Papers/THERAC25.html)
  
- [History's Worst Software Error - Youtube](https://www.youtube.com/watch?v=Ap0orGCiou8)  

- [The Tragic Race Condition - Team Codereliant](https://www.codereliant.io/p/the-most-tragic-bug)  

The Patriot Missile:  
- [PATRIOT MISSILE DEFENSE Software Problem Led to System Failure at Dhahran, 
Saudi Arabia](https://www.gao.gov/assets/imtec-92-26.pdf)  

Mars Climate Orbiter:  
- [NASA Mars Climate Orbiter Project Failure (1999) REPORT](https://www.researchgate.net/publication/345858885_NASA_Mars_Climate_Orbiter_Project_Failure_1999_REPORT)

- [They didn’t check the Software | The NASA Mars Climate Orbiter Incident - Youtube
](https://www.youtube.com/watch?v=i8slVQJe0n4)

- [Mars Climate Orbiter - Wikipedia](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter)  
