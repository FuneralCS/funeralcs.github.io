---
title: "Cebimizdeki Hayat Kurtarıcı: Android Deprem Uyarı Sistemi Nasıl Çalışır?"
date: 2025-10-11 09:00:00 +0300
categories: [teknoloji, bilim, donanımlar, matematik]
tags: [Android, deprem, erken-uyarı, sismoloji, P-dalgası, ivmeölçer, Google, 6Şubat]
author: tunahan
image:
  path: /assets/img/xx-xx-xx-derpem-uyari-sistemi/cover.webp 
  alt: "Akıllı telefonların bir araya gelerek oluşturduğu küresel deprem tespit ağı ve erken uyarı sistemini temsil eden bir görsel."
description: "Telefonunuzun bir deprem sensörüne nasıl dönüştüğünü, Google'ın Android Deprem Uyarı Sistemi'nin (AEA) P dalgalarını algılayarak milyonlarca kişiye nasıl saniyeler kazandırdığını, 6 Şubat depremlerindeki performansını ve güncel iyileştirmeleri inceliyoruz."
toc: true
math: false
mermaid: false
comments: false
pin: false
---

## Giriş
>  3 yıllık çalışma süresi boyunca, sistem Türkiye'de aylık ortalama 312 deprem tespit etti ve bunların büyüklükleri M 1,9 ile M 7,8 arasında değişiyordu. M ≥4,5 büyüklüğündeki depremler için 98 ülkede uyarılar gönderildi; bu, aylık yaklaşık 60 olay ve 18 milyon uyarıya karşılık geliyor. Kullanıcı geri, uyarı alan kişilerin %85'inin sarsıntıyı hissettiğini ve %36, %28 ve %23'ünün sırasıyla sarsıntıdan önce, sarsıntı sırasında ve sarsıntıdan sonra uyarı aldığını göstermektedir. Akıllı telefon tabanlı deprem algılama algoritmalarının nasıl büyük ölçekte uygulanabileceğini ve olay sonrası analizlerle nasıl iyileştirilebileceğini gösteriyoruz ~ Allen et al., Global earthquake detection and warning using Android phones [1]

Deprem gerçeği ülkemizin değişmez kaderi gibi karşımızda duruyor. 6 Şubat depreminin enkazı hâlâ hayatımızın her alanında hissediliyor ve o izler kolay kolay silinmeyecek. Depremleri durduramayız ama önlem almak elimizde. Google, 11 Ağustos 2020’de devreye aldığı bu sistemle, şimdiye kadar geliştirilen en akıllı algoritmalardan birkaçını bir araya getirerek telefonlarımızı birer erken uyarı cihazına dönüştürdü.

> Ancak, hala felaket niteliğinde depremlerle karşı karşıyayız. Bazıları,
   2023 yılında Türkiye ve Fas'ta olduğu gibi binlerce insanı öldürüyor ve yaralıyor; daha fazlası ise yüzlerce insanı yaralıyor ve böylece birçok hayatı altüst ediyor. Güvenli binalar inşa etmek için gerekli bilgi ve kaynaklara erişim, dünyanın birçok yerinde hala sınırlayıcı bir faktör olarak kalmaktadır. Kaynaklar olsa bile, savunmasız binaları yenilemek hala onlarca yıl. ~ Aynı makaleden
   {: .prompt-warning}

Sizlere başlarken bir soru bırakmak istiyorum: Telefonunuz cebinizdeyken aslında bir deprem sensörü olabilir mi?
## Ön bilgi

Deprem, fay hattı boyunca kayaların aniden kırılıp yer değiştirmesiyle ortaya çıkan titreşimlerdir. Bu titreşimler dalgalar halinde yayılarak yeryüzüne ulaşır. Deprem sırasında üç farklı dalga türü oluşur, ancak burada odaklanacağımız dalga türü **P (primary)** dalgalarıdır.

<div style="display: flex; flex-wrap: wrap; align-items: flex-start; gap: 20px;">
    <figure style="flex: 0 0 300px; margin: 0;">
        <img src="assets/img/xx-xx-xx-derpem-uyari-sistemi/p_s.webp"
             alt="P ve S dalgaları için AI üretimi bir temsil"
             width="300" style="max-width: 100%; height: auto;">
        <figcaption>P ve S dalgaları için AI üretimi bir temsil</figcaption>
    </figure>

    <div style="flex: 1; min-width: 250px;">
        <p><strong>P dalgaları</strong>, yani gövde dalgaları, deprem sırasında ortaya çıkan ilk ve en hızlı dalgalardır. 
        Adını “primary” (birincil) kelimesinden alır. Enerji yayılma yönüne paralel şekilde itme–çekme hareketi yaparak ilerlerler 
        ve saniyede <strong>6 ila 8 kilometre</strong> hızla yol alabilirler. Bu özellikleri nedeniyle sismik istasyonlara ulaşan ilk dalgalardır.</p>

        <p>P dalgalarını hayvanlar çoğu zaman hissedebilir, insanlar ise hissedemez. 
        Bu yüzden hayvanların depremi önceden fark ettiği düşünülür. 
        İnsanların algılayamadığı bu titreşimleri telefonlarımız algılayabilir — adeta “cebimizdeki küçük hayvan” gibi davranarak P dalgalarını bizden önce hisseder. 
        İşte bu birkaç saniyelik fark bile hayat kurtarıcı olabilir.</p>
    </div>
</div>

Depremin bir diğer dalga türü **S (secondary)** dalgalardır. Daha yavaş hareket ederler ama yıkıcı etkileri çok daha fazladır. Aslında biz insanların “deprem oldu” diye hissettiği şey çoğunlukla S dalgalarıdır.

---

***Artık AEA sistemine geçebiliriz.***
## Sistemin mantığı
Öncelikle sizlere Dave Burke'un Tweetini göstermek istiyorum az sonra anlatacaklarım için. Kendisi şu anda **Arc Institute’te CTO** ve hâlâ **Google’da danışman (Google Advisor)**

<blockquote class="twitter-tweet" data-theme="dark">
<p lang="en" dir="ltr">Android phones and <a href="https://twitter.com/hashtag/USGS?src=hash&amp;ref_src=twsrc%5Etfw">#USGS</a> gave Southern California residents an early warning to the 4.5 earthquake last night Here&#39;s what the phones&#39; sensors, acting as seismometers, detected. Yellow and red concentric circles are expected locations of the P and S waves. <a href="https://t.co/duKZnnIjE3">https://t.co/duKZnnIjE3</a> <a href="https://t.co/9q4GLvLm9O">pic.twitter.com/9q4GLvLm9O</a></p>&mdash; Dave Burke (@davey_burke) <a href="https://twitter.com/davey_burke/status/1307395583338885120?ref_src=twsrc%5Etfw">September 19, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Android Deprem Uyarı Sistemi (AEA), aslında klasik sismoloji prensiplerini kullanıyor ama bunu herkesin cebinde taşıdığı **ivmeölçer** sensörleri üzerinden yapıyor.
> Akıllı telefon sensörleri arasında ivmeölçer, en eski ve en yaygın olanlardan biridir. Son nesil akıllı telefonlar, varsayılan olarak MEMS tabanlı ivmeölçer sensörleri içerir. İvmeölçer sensörü, cihazı üç eksende (x, y ve z) etkileyen sabit (yerçekimi), zamanla değişen (titreşimler) ve yarı statik (eğim) ivme kuvvetlerini metre/saniye kare (m/sn²) cinsinden ölçer. ~Grouios el al. 2023 [2]

- **Telefon hareketsizken** → ivmeölçer, ani hızlanmaları algılıyor.
- Bu tür bir hızlanma **P ve S dalgalarının** yarattığı sarsıntıya benziyorsa → telefon Google sunucularına “küçük bir sinyal” gönderiyor.
- Google sunucuları → farklı telefonlardan gelen sinyalleri bir araya getiriyor, zaman-mekân dağılımına bakıyor.
- Eğer bu dağılım bir deprem kaynağına uyuyorsa → sistem “deprem oldu” diyor ve depremin **büyüklüğünü, merkezini ve oluş zamanını** tahmin ediyor.
Bu sayede telefonlar, aslında cebimizde taşıdığımız minik birer sismograf gibi davranıyor

<figure>
    <img src="assets/img/xx-xx-xx-derpem-uyari-sistemi/bulut.webp" 
         alt="Sistem" width="512">
    <figcaption>Sistem</figcaption>
</figure>  

---

## Sistemin Yaygınlığı ve İlk Kullanımı

> AEA’nın yaygınlaştırılması, 11 Ağustos 2020’de Kaliforniya’da **ShakeAlert** tarafından üretilen uyarıların iletilmesiyle başladı. Android telefonlarının kendi tespitlerine dayalı uyarılar ise ilk olarak **28 Nisan 2021’de Yeni Zelanda ve Yunanistan’da** devreye girdi, ardından **15 Haziran 2021’de Türkiye, Filipinler ve Orta Asya’ya** genişletildi. 2022’de sistem, uyarıların verilmesine izin verilen diğer yüksek riskli ülkelere de yayıldı. 2022 sonunda **93 ülkede**, 2023 sonunda ise **98 ülkede** AEA uyarıları gönderiliyordu. ~ Makaleden

<figure>
    <img src="assets/img/xx-xx-xx-derpem-uyari-sistemi/harita.webp" 
         alt="Tespit edilen ve uyarı verilen depremlerin küresel dağılımı." width="600">
    <figcaption>Tespit edilen ve uyarı verilen depremlerin küresel dağılımı</figcaption>
</figure>  

---

## Prensip ve Performans
Prensipten az önce de bahsetmiştim klasik sismoloji ile birebir aynı mantıkta, sistem P dalgasını algılıyor "binlerce sismograftan" ve uyarı gönderiyor. Gizlilik açısından merak edenler olursa konum verisi "bulanık" gönderiliyor tamamen anonim biçimde. Zaten telefon pazarının %70 Android olduğunu düşünürsek yaklaşık bir konum bile yeterli

### 1 Nisan 2021 – 31 Mart 2024 Arasında:
- **11.231 deprem** tespit edildi.
- Bunların %85’i geleneksel kataloglarla eşleşti.
- Büyüklük (magnitüd) aralığı ise: **M 1.9 (Japonya) – M 7.8 (Türkiye)**.
- Sistem özellikle kıta içi ve kıyıdaki depremleri yakalayabiliyor; okyanus ortasındaki depremler pek algılanamıyor -sebebini söylememe gerek yok diye düşünüyorum-
- M4.5 büyüklüğündeki depremler ~100 km açıkta dahi algılanabiliyor.   
- Global “magnitüd tamlık değeri” (Mc): **4.9** → yani dünya genelinde sistem M4.9 ve üstü depremleri güvenilir biçimde tespit ediyor.
- En kritik zorluk: **magnitüdün hızlı tahmini** (çünkü büyüklük geç bulunursa uyarı da geç kalır).

**_3 yıl içinde hatalar ciddi biçimde düştü:_**
- İlk büyüklük tahminindeki **ortalama hata yarı yarıya azalmış** → 0.50’den 0.25’e düşmüş. (deprem ilerledikçe daha fazla telefondan sinyal alınıyor ancak deprem öncesi erken aşamada hesaplamak veri azlığı ve diğer sebeplerden ötürü daha zor oluyor)
- En kötü %10’luk durumlarda (yani “en büyük hataların” görüldüğü uç vakalarda) hata **1.02’den 0.70’e gerilemiş**.
İyileşme nedeni ise **bölgesel tahmin modelleri** olarak yazılmış makalede. (farklı tektonik koşullar, zemin türleri, bina tipleri ve telefon modellerine göre ayarlamalar).

<figure>
    <img src="assets/img/xx-xx-xx-derpem-uyari-sistemi/hata.webp" 
         alt="AEA Hata oranları" width="600">
    <figcaption>AEA Hata oranları. Türkçeye çevirmek gerekirse:
- <b>Number of events</b>: İncelenen deprem sayısı  
- <b>1st magnitude estimate</b>: İlk büyüklük tahmini  
- <b>Max magnitude estimate</b>: Maksimum (son) büyüklük tahmini  
- <b>Absolute error</b>: Mutlak hata (tahmin ile gerçek değer arasındaki fark)  
- <b>Median</b>: Ortanca değer (tam ortadaki)  
- <b>90th percentile</b>: En kötü %10’luk olaylardaki hata  
- <b>Mean</b>: Ortalama değer  
 </figcaption>
</figure>  

---

## Uyarı türleri
> **MMI (Modified Mercalli Intensity)**: Depremin büyüklüğünü değil, sizin hissettiğiniz şiddeti anlatır.
>→ **Büyüklük (Magnitude)**, depremin ürettiği toplam enerjiye verilen isimdir. Nerede olursanız olun, o deprem aynı büyüklüktedir. 
>→  **Şiddet (Intensity)** ise bulunduğunuz yere göre değişir. Yani depremi ne kadar kuvvetli hissettiğinizdir.
>→  Örneğin: Belgrad Ormanı’nda olan biriyle Avcılar’daki biri aynı depremi yaşar. Depremin **büyüklüğü** herkes için aynıdır, ama Avcılar’daki kişi çok daha şiddetli hisseder. Çünkü şiddet, merkez üssüne uzaklığa ve zeminin yapısına göre değişir.

- **TakeAction** → MMI ≥5 beklenen bölgeler, acil ve intrusif (sessiz modu bozuyor).
- **BeAware** → MMI 3–4 beklenen bölgeler, daha hafif bildirim.
- Örnek: M5.5 deprem (20 km derinlik) için en yakın 8 km’ye TakeAction bildirimi gönderilirken, 197 km çapına BeAware gönderilir..
- M6.5 deprem için ise 78 km TakeAction, 442 km'ye kadar BeAware gönderilir.
### Diğer uyarı sistemleri ile karşılaştırma:
AEA, ABD ShakeAlert ve Japonya JMA ile karşılaştırılmış.
Hata oranları **benzer**, ama AEA:
- Daha düşük hata (ilk tahmin ortanca hata 0.3)
- Çok daha fazla sayıda uyarı (binlerce olay).
## 6 Şubat depremlerinde AEA
- Sistem ilk olarak **7,1 saniye** sonra büyüklüğü 4.5 olarak tahmin etmiş.
    - **18,7 saniye** sonra en fazla 4.9 olarak güncelleyebilmiş.
    - **512.411 BeAware bildirimi** gönderilmiş, 64 km’ye kadar.
- **M7.5 Elbistan depremi** (9 saat sonra):
    - İlk tahmin **24,4 saniye** sonra M6.1 olarak yapılmış.
    - 5,2 saniye içinde 6.3’e güncellenmiş.
    - **3,9 milyon BeAware bildirimi** gönderilmiş.
    - Uyarı süreleri bazı yerlerde birkaç saniyeden **bir dakikanın üzerine** çıkmış.

**Diğer uygulamalarda ise**
 EQN, M7.8 Pazarcık’ı **12,1 saniye sonra** algılamış ve **63.539 kullanıcıya** uyarı göndermiş.
 Ancak **M7.5 Elbistan’ı hiç tespit edememiş**.
### Sonradan yapılan analiz (neden yetersiz kaldı?)

1. **Algoritma sınırları**: O sırada sistem, tespitten sonra sadece 10 saniyelik güncelleme yapıyordu → büyük depremlerde bu çok kısa kaldı.
2. **Gürültülü telefonlar**: Çok sayıda “*noisy*” telefon yanlış tetikleme yaptı, özellikle M7.8’de geç algılandı. (Noisy veri biliminde yanıltıcı anlamında kullanılır örneğin otobüs sarsıntısı yanıltıcıdır gibi)
3. **Titreşim çakışması**: Uyarı alan telefonların titreşimleri, diğer telefonların gerçek deprem titreşimini algılamasını engelledi.

**Bu sorunlar daha sonra düzeltilmiş:**
- Güncelleme süresi 30 saniyeye çıkarıldı.
- Gürültülü telefonlar artık otomatik eleniyor.
- Uyarı titreşimleri, ölçüm yapan telefonları etkilemiyor.

---

### Yeni algoritma ile simülasyon

Aynı veriler bugünkü sistemle işlendiğinde:
- İlk büyüklük tahmini **6,3 saniye** sonra M4.6.
- 24 saniye içinde büyüklük **M7.4**’e kadar güncelleniyor.
- **TakeAction uyarıları** 158 km’ye kadar (10 milyon telefon).
- **BeAware uyarıları** 604 km’ye kadar (67 milyon telefon).
- Antakya gibi ağır hasar gören yerlerde bile **35 saniyelik uyarı** mümkün olurdu.
- Daha uzak bölgelerde **2,5 dakika önceden uyarı** sağlanabilirdi.

>Yani makale diyor ki: **O günkü algoritma yetersizdi, ama bugünkü geliştirilmiş sistem olsaydı milyonlarca kişi çok daha erken uyarı alabilirdi.** Oldukça üzücü...

---

## Kapanış

Depremler gerçeğimiz, acılarıyla ve kayıplarıyla hep içimizde. Bilim ve teknoloji bize saniyeler kazandırabilir, hayatlar kurtarabilir. Ama unutmamalıyız ki ölüm de hayatın bir parçası. Bizim görevimiz, bu dünyada yaşarken birbirimizin hayatına sahip çıkmak, böylesi felaketleri bir daha yaşamamak. Deprem gerçeğini değiştiremeyiz ama bilgiyi paylaşarak, bilimi yayarak ve teknolojiyi kullanarak daha güvenli bir gelecek kurabiliriz. Okumak okutmak, yaşamak ve yaşatmak...

<figure>
    <img src="assets/img/xx-xx-xx-derpem-uyari-sistemi/grafikler.webp" 
         alt="Tespit edilen ve uyarı verilen depremlerin küresel dağılımı." width="600">
    <figcaption>Uyarı alan kullanıcıların geri bildirimleri. 5 Şubat 2023 ile 30 Nisan 2024 tarihleri arasında kullanıcı anketine toplam 1.555.006 yanıt toplandı. Bu süre zarfında, AEA tarafından tespit edilen 1042 deprem için uyarılar yayınlandı. </figcaption>
</figure>  

# Kaynakça
1. [Richard M. Allen et al. ,Global earthquake detection and warning using Android phones][1]
2. [Cebimizdeki İvmeölçerler: Akıllı Telefon İvmeölçer Teknolojisi Doğru Veriler Sağlıyor mu?][2]
3. [Speed of Sound through the Earth][3]

[1]: https://www.science.org/doi/10.1126/science.ads4779
[2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9824767/
[3]: https://hypertextbook.com/facts/2001/PamelaSpiegel.shtml
