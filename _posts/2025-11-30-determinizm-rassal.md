---
title: "Determinizim ve Rassal Sayılar Üzerine"
date: 2025-11-30 14:30:00 +0300
categories: [rastgelelik, fizik]
tags: [rastgele, determinizm, deterministik, fizik, random, bilgisayar, matematik, rand(), seed(), minecraft, random.h, süperdeterminizm, bilgisayar bilimi, aritmetik, fonksiyon]
author: vladimirdelvis
image:
  path: /assets/img/2025-11-30-determinizm-rassal/banner.webp
description: "Determinizm ve Rassal Sayılar Üzerine. Günümüzdeki bilgisayarların nasıl rastgele sayı ürettiklerini anlayın."
toc: true
math: true
mermaid: false
comments: true
pin: false
lang: tr
---
## 1. Giriş

Rastgelelik kavramı insanlığın başlangıcından beri insanların zihninde yer almıştır. Eski çağlardan günümüzdeki kuantum fiziğine kadar rastgele sayıların öngörülemez olduğu savunulmuştur. Ancak klasik fizik bunun tam aksini rastgele olayların deterministik olduğunu öne sürmüştür. Örneğin bir para atma deneyinde, eğer gerekli tüm sabitler (havanın sürtünmesi, rüzgarın hızı, paranın atılış hızı, paranın dönüş hızı, paranın atılış açısı...) bilinirse ilgili denklemler kullanılarak paranın hangi yüzünün geleceği hesap edilebilir ve tüm bu sabitler değiştirilmezse para hep aynı yüzü üste gelecek şekilde duracaktır.

Bilgisayarlar deterministik makinelerdir. Bir bilgisayar aynı girdi üzerinde aynı sonucu üretecektir. Ancak biz bazen sürekli farklı sonuç üretmesini isteriz. İşte insanlar bu sorunun altından sözde rastgele sayı üreticileri (PRNG) veya gerçek rastgele sayı üreticileri (TRNG) ile çözmüşlerdir.

>TRNG'ler fiziksel olaylar kullanılarak hesaplanan sayılardır. Örneğin bomboş bir atmosferik gürültü veya lavarand gibi teknolojiler ile olur. PRNG'ler ise bir sayıdan (seed) başka bir sayı üreten ve hep aynı sayıyı üreten fonksiyonlardır. Zaten yazının ilerleyen kısımlarında bunlara daha iyi değineceğiz.

>Not: Ancak yazının başında dedigim gibi klasik fizik aslında doğa olaylarının zaten deterministik olduğunu söyler. Ancak TRNG'lerin kullandığı kaynaklar gerçekten hesaplanması çok güç sistemlerdir. Tüm o değişkenleri bilmek imkansızdır. Bu yüzden adı gerçek rastgele sayı üreticisidir.

---

## 2. Makineler Nasıl "Zar Atar"?

Dijital sistemlerde rastgelelik üretimi, iki ana paradigma üzerine kuruludur: Yazılımsal algoritmalarla üretilen Sözde Rastgele Sayı Üreteçleri (PRNG) ve fiziksel süreçlerden beslenen Gerçek Rastgele Sayı Üreteçleri (TRNG).

### 2.1. Sözde Rastgele Sayı Üreteçleri (PRNG: Pseudo-Random Number Generators)

PRNG'ler, deterministik bir algoritma kullanarak, dışarıdan bakıldığında rastgele gibi görünen ancak aslında tamamen matematiksel bir formüle dayalı sayı dizileri üretmeye yarar. Bu sistemlerin en belirleyici özelliği ise başlangıç durumu bilindiğinde, tüm dizinin yeniden üretilebilmesidir. Bu algoritmaların en çok kullanılanılanları LCG, MT19937, PCG...

#### 2.1.1 Seedleme

Bir PRNG için seed değeri aslında algoritma için en önemli değerdir. Algoritma bu sayı ile bir başka sayı (veya bir şey üretir) ve yeni üretilen bu sayı ise algoritmanın yeni seed değeri olur. Bu şekilde algoritma devam eder. Bu algoritmalar TRNG'lere göre çok hızlıdır bu yüzden oyunlarda ve simülasyonlarda sıkça kullanılır. *bknz. Minecraft* Bilgisayarlar çoğunlukla bu başlangıç seedi için unix zamanını kullanırlar.

### 2.2 Gerçek Rastgele Sayı Üreteçleri (TRNG: True Random Number Generators)

PRNG'lerin deterministik doğasının yarattığı güvenlik açıklarını kapatmak için, fiziksel dünyadaki kaotik veya kuantum süreçlerden veri toplayan TRNG'ler kullanılır.

#### 2.2.1 TRNG'lerin kullandığı kaynaklar

- **Termal Gürültü (Johnson-Nyquist Gürültüsü):** Bir iletkendeki elektronların ısıya bağlı rastgele hareketleri. Modern işlemcilerin (CPU) içine entegre edilen TRNG devreleri genellikle bu prensibi kullanır.
- **Atmosferik Gürültü:** Radyo alıcıları tarafından yakalanan statik parazit. Random.org gibi servisler, atmosferdeki yıldırımların yarattığı elektromanyetik gürültüyü kullanır.
- **Kuantum Olayları:** Radyoaktif bir izotopun bozunma anı veya bir fotonun yarı geçirgen bir aynadan geçip geçmediği gibi, kuantum mekaniği gereği doğası gereği belirsiz olan olaylar. Bu, teorik olarak "kanıtlanabilir" tek rastgelelik kaynağıdır.

#### 2.2.2 Lav Lambası Duvarı

Cloudflare, "Lavarand" adlı bir rastgele sayı üretmek için lav lambası duvarı geliştirmiştir. Bu duvarda 100 adet lav lambası sürekli çalışır. Tam karşılaşılarındaki kamera aracılığı ile lav lambalarının içindeki sıvının kaotik hareketi, ışık yansımaları, odadan geçen insanlar ve kameranın sensöründeki gürültü birleşerek çok yüksek entropiye sahip bir havuz oluşturur.

---

## 3. İnsan Zihni ve Rastgelelik

Makineler rastgeleliği sağlamak için muazzam bir hesaplama yapar ancak beyni bunu şıp diye seçer. Ancak insan zihninin seçtiği bu sayı gerçekten rastgele midir? Hayır tabiki de. İnsanlar bu konuda berbattır.

### 3.1 Tekrardan Kaçınma ve Negatif Bitişiklik

İnsan zihni, "gerçek" rastlantısallığı tekrarsız olduğunu sanarlar mesela yazı-tura deneyinde "yazı-yazı-yazı-yazı-yazı" gelmesini rastgele değil diye değerlendirir. Ancak "yazı-tura-yazı-tura-yazı" gelmesi insanlara rastgele gelir. Ama bu iki dizinin gelme olasılığı aynıdır. İnsanlar kendi dizilerini oluştururken, ardışık tekrarları bilinçsizce bastırır. Buna "Negatif Bitişiklik Etkisi" (Negative Recency Effect) denir. Örneğin, 1 ile 10 arasında sayı söylerken, bir kişi "5" dedikten sonra bir sonraki sayının "5" olmama ihtimalini yapay olarak artırır.

>Mavi-Yedi Fenomeni: İnsanlara tek haneli bir sayı tutun dendiğinde insanların çoğu '7' rakamını, bir renk tutun dendiğinde 'mavi' rengini söylemişlerdir.

<figure>
    <img src="/assets/img/2025-11-30-determinizm-rassal/insan-rastgele.webp" width="650" alt="Görsel: İnsan Zihni ve Bilgisayarın Rastgele Sayı Dağılımı">
</figure>

---

## 4. Oyunlarda rastgelelik

Oyun endüstrisi rastgele sayı üretme sistemlerini çok sık kullanırlar. Ancak saf rastgele sayı üreticiler oyuncular tarafından çok sert ve acımasız olarak algılandığından, geliştiriciler bazen rastgelelik algoritmaların kasten entropisini azaltabilir.

### 4.1 "Adil" hissedilen raslantısallık: Sözde Rastgele Dağılım (PRD)

Rekabetçi oyunlarda belli başlı özellikler örneğin: kritik vuruş, sersemletme gibi özellikler şansa dayalıdır ancak bu özelliklerin saf rastgelelikle çalışması sorun olur. Çünkü yine bir örnek üzerinden açıklayalım %25 ihtimalle kritik vuran bir karakter, şans eseri arka arkaya 10 kere kritik vurabilir veya 30 kere üst üste hiç kritik vuramayabilir. Bunu kontrol altına almak için Sözde Rastgele Dağılım kullanılır.

#### PRD Devam

PRD sisteminde, bir olayın gerçekleşme olasılığı her başarısız sonuçta artar. Örneğin, ilk önce küçük bir olasılık seçelim %5 gibi bu ihtimalle deneyi yapalım. Başarısız olursak yeni başarı olma ihtimali 2x%5 olacaktır. Yine başarısız olursak başarılı olma ihtimali 3x%5 olacaktır bu düzen bu şekilde devam eder. Ancak bir kere başarılı olduğumuz an ihtimal tekrardan %5 e düşecektir.

>Ek Bilgi: PRD'ye benzer rastgeliliği insan zihninin refahı için bozan sistemler: Oyunlardaki ödül mekanizması, Müzik dinleme platformların shuffle algoritması...

---

## 5. Sonuç

Göreceğiniz gibi insan beyni rastgele sayı üretmekte berbat bir durumdadır. Ancak makineler bu işi sanıldığından daha iyi yapabilir. Yazının en başında dediğim gibi klasik fizik her fiziksel olayın deterministik olduğunu söyler ki bu da lav lambaları veya gürültülerle çelişir gibi gözüküyor. Ancak bu fenomenlerin nasıl gerçekleşeceğini hesaplamak evrenin bir sonraki anını hesaplamak kadar zordur bu yüzden TRNG sistemleri pratikte indeterministik bir yapıda diyebiliriz. Şuanki bildiğimiz bilgiler gerçek rastgeleliğin sadece kuantum dünyasında meydana geldiğini anlatır. Onun dışındaki tüm rastgele olan olgular aslında rastgele gibi gözüken olgulardır. Ek olarak şuanki bildiğimiz şeyler kuantum dünyasının çok az bir kısmı dolayısı ile bildiğimiz kuantum evreni de bir veya birden fazla değişkene bağlı olabilir ama biz bunu henüz bilmiyoruz. (Süperdeterminizm)

---

## Kaynakça & İleri Okuma

1. [RANDOM NUMBER GENERATOR - FREECODECAMP](https://www.freecodecamp.org/news/random-number-generator/)
2. [DIFFERENCE BETWEEN TRNG AND PRNG - WOLFSSL](https://www.wolfssl.com/difference_between_pseudorandom_number_generators_and_true_random_number_generators/)
3. [DIFFERENCE BETWEEN TRNG AND PRNG - RESEARCHGATE](https://www.researchgate.net/post/Difference_between_TRNG_or_PRNG)
4. [PSEUDORANDOM VS TRULY RANDOM NUMBERS - SUPERUSER](https://superuser.com/questions/712551/how-are-pseudorandom-and-truly-random-numbers-different-and-why-does-it-matter)
5. [MERSENNE TWISTER - WIKIPEDIA](https://en.wikipedia.org/wiki/Mersenne_Twister)
6. [MAVI YEDI FENOMENI - WIKIPEDIA](https://en.wikipedia.org/wiki/Blue%E2%80%93seven_phenomenon)
7. [LAVARAND - CLOUDFLARE](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/)
8. [PRD - FANDOM](https://dota2.fandom.com/wiki/Random_Distribution)

## Görsel Kaynakça

1. <https://miro.medium.com/v2/resize:fit:954/format:webp/1*YNnKwfUnLo4NKrqEJoAtww.gif>