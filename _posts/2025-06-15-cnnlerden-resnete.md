---
title: "Sıfırdan CNN’ler: LeNet’ten ResNet’e"
date: 2025-06-15 09:00:00 +0300
categories: [Derin Öğrenme, ResNet, LeNet, Görüntü İşleme]
tags: [derin öğrenme, resnet, lenet, yazılım, görüntü işleme]
author: tunahan
image:
  path: /assets/img/cv/cv.webp
description: "Bugün CNN’lerin doğuşundan itibaren ResNet mimarisine nasıl geldik. Tüm bunlara değineceğiz"
toc: true
math: false
mermaid: false
comments: true
pin: false
lang: tr
---
# Sıfırdan CNN’ler: LeNet’ten ResNet’e

Herkese selamlar!  Bu yazıda size bilgisayarlı görünün (Computer Vision) ilkel yöntemlerinden ResNet gibi derin öğrenme devlerine uzanan yolculuğumuzu anlatacağım.

Hiç teknik karmaşaya girmeden, basitçe konuşacağız. Her şeyin en anlaşılır hâliyle burada olduğunu göreceksiniz!

> Not: Bu yazı ResNet’e kadar olan kısmı kapsamaktadır. DenseNet, EfficientNet, Vision Transformer gibi yeni mimarileri ilerleyen haftalarda işleyeceğim.

##  Bilgisayarlı Görü Nedir?

Bugün hemen hemen her araçta şerit takip sistemi ve hatta otonom sürüş özellikleri bulunuyor. Peki bu nasıl mümkün oldu?

1960-1970’lerde ilk görüntü işleme denemeleri başladı. O zamanlar görüntü, sadece piksel dizileri olarak işleniyordu. Mesela günümüzde kullandığımız 1080p görüntüler (RGB formatında 3×1920×1080) devasa boyutlarda verilerdir. Ama ilk deneylerde MNIST gibi 28×28 boyutunda, sadece siyah beyaz görüntüler kullanılıyordu.

Amaç neydi? O dönemlerde hedef çok daha basitti: görüntülerde sadece kenar, köşe gibi temel özellikleri tanımak.

###  Piksel Nedir?
Piksel, görüntünün en küçük yapı birimi. RGB renk temasında kırmızı (R), yeşil (G) ve mavi (B) kanallarından oluşur. RGB’den önce ise grayscale (gri tonlama) kullanılıyordu.

###  Histogram Nedir?
Görüntüdeki parlaklık dağılımının ölçütüdür. Bir fotoğraftaki karanlık ve aydınlık alanları gösterir.

---

## İlk Filtreler ve Kenar Algılama

İlk görüntü işleme filtreleri Sobel, Prewitt ve Roberts operatörleriydi. Bu filtreler görüntü üzerindeki parlaklık farklarını belirleyerek "kenarları" ortaya çıkarıyordu.

Bu işlem basitti:

1. Görüntü gri tonlamaya çevrilir.
2. 3×3'lük küçük bir pencere (kernel) tüm görüntü üzerinde kaydırılır.
3. Her pikselde, çevresinin ağırlıklı toplamı alınarak kenar haritası oluşturulur.

---

## Özellik Çıkarımı ve Temsiller

Elle tasarlanan çeşitli teknikler vardı:

- **Nokta Özellikleri (Keypoints)**: 
  - **SIFT ve SURF**: Görüntüdeki belirgin noktaları tespit eder ve bu noktaların özelliklerini çıkarır.

- **HOG (Histogram of Oriented Gradients)**: 
  - Görüntüyü küçük hücrelere bölüp her hücrede kenar yönlerini histogramla tutar.
  - Özellikle insan ve araç tanımada kullanılır.

- **Haar benzeri özellikler**:
  - Dikdörtgen filtrelerle parlaklık farkları tespit edilir.
  - Viola–Jones yüz tanıma algoritmasında kullanıldı.

Bu yöntemlerin sorunu neydi? Hepsi insan eliyle tasarlanıyordu. Bir görüntüden elle filtrelerle özellik çıkarmak ve onları SVM, k-NN, Random Forest gibi klasik makine öğrenme yöntemleriyle sınıflandırmak gerekiyordu. Bu, zor ve sınırlayıcıydı.

---

## Derin Öğrenme ve LeNet’in Doğuşu

**İhtiyaç:** Elle özellik çıkarma yerine, özellikleri otomatik öğrenen sistemler geliştirmek. İşte bu yüzden **CNN’ler (Convolutional Neural Networks)** doğdu.

**Amaç:** MNIST veri setindeki 60 bin el yazısı rakamı otomatik sınıflandırmak.

---

##  Derin Öğrenme Nedir?

Derin öğrenme, insan beyninin çalışma prensiplerinden esinlenilerek geliştirilmiş yapay sinir ağlarını temel alan makine öğrenmesinin bir alt alanıdır.

1940’larda başlayan yapay sinir ağı çalışmaları, 1980’lerde geri yayılım (backpropagation) algoritmasının bulunmasıyla hız kazandı. 2000’lerde büyük verinin ve güçlü donanımların ortaya çıkmasıyla gerçek anlamda derin öğrenme dönemi başladı.

Temel derin öğrenme türleri:

- Yapay Sinir Ağları (ANN)
- Evrişimli Sinir Ağları (CNN) – Bugün konuştuğumuz
- Tekrarlayan Sinir Ağları (RNN)
- Uzun Kısa Vadeli Bellek (LSTM)
- Üretken Çekişmeli Ağlar (GAN)

Derin öğrenmede kullanılan teknikler:

- Geri yayılım (Backpropagation)
- Aktivasyon fonksiyonları (ReLU, sigmoid, vb.)
- Dropout ve düzenleştirme
- Stokastik Gradyan İnişi (SGD), Adam optimizasyonu vb.

Bu arada not düşelim: Yapay sinir ağlarının babası sayılan Geoffrey Hinton, 2024 yılında Nobel Fizik Ödülü’nü aldı.

---

## LeNet-5 Mimarisi (1998)

LeNet, CNN'lerin atasıdır. Katmanlarını yakından tanıyalım:

- **Konvolüsyon**: Görüntü üzerinde küçük filtreler gezdirilerek desenler yakalanır.
- **Aktivasyon (ReLU)**: Negatif değerleri sıfırlayarak doğrusal olmayanlık sağlar.
- **Normalizasyon (BatchNorm)**: Ağın daha hızlı ve dengeli öğrenmesini sağlar.
- **Havuzlama (Pooling)**: Boyut küçültülerek hesaplama maliyetini azaltır ve özet bilgi üretir.
- **Tam Bağlı (Fully Connected)**: Son aşamada özellikleri sınıflandırır.
> Convolution: Görüntüdeki lokal desenleri bulmak için kayan pencere.
> Stride: Filtrenin kaç piksel atlayarak hareket ettiğini belirtir.
> Padding: Görüntünün kenarlarına sıfır eklenerek boyutun korunması sağlanır.
> Flatten: 2D veriyi 1D hale getirerek Fully Connected katmana geçiş sağlar.

**LeNet Yapısı:**
- Giriş: 32×32 gri görüntü
- 2×(Konvolüsyon + Havuzlama) → Tam bağlı katmanlar → Softmax (10 sınıf)
- MNIST verisinde yüksek doğruluk sağladı ve CNN dönemini başlattı.

> LeNet: İlk gerçek CNN, elle çıkarılan özellik dönemini kapattı.
> ResNet: Derinlik sorununu çözerek modern derin ağların kapısını açtı. Transformer’lar bile bu anlayıştan beslendi. (Attention)

---

## LeNet Sonrası Önemli Modeller

### 🔸 **AlexNet (2012)**
Geoffrey Hinton danışmanlığında Alex Krizhevsky tarafından geliştirildi. 60 milyon parametre içeriyordu. GPU kullanımını başlatıp ImageNet yarışmasını ezici farkla kazanarak derin öğrenme devrimini başlattı.

### 🔸 **ZFNet (2013)**
AlexNet’in iyileştirilmiş versiyonu; filtre boyutlarını küçültüp ağın öğrenme şekillerini görselleştirdi.

### 🔸 **VGGNet (2014)**
Sadece 3×3 konvolüsyonlar kullanarak 16–19 katmana ulaştı. Çok parametre içerdi (~138 milyon) ama sadeliğiyle ünlendi.

### 🔸 **GoogLeNet/Inception (2014)**
Aynı anda farklı boyutlardaki filtreleri kullanarak hem derin hem geniş bir ağ oluşturdu. Parametre sayısını (~6 milyon) düşük tutmayı başardı.

---

## ResNet (2015): Derinliğin Gerçek Çözümü

Derin ağlarda öğrenme zorlaşır. Çünkü gradyan kaybolur veya bozulur. İşte ResNet bunu çözdü:

Normalde bir katmanın çıktısı şöyle hesaplanır:

```
Çıktı = F(x)
```
ResNet ise çıktı ile girdi arasında doğrudan bağlantı kurar:
```
Çıktı = F(x) + x
```

Bu "skip connection" sayesinde ağ, farkları öğrenmeye odaklanır.  
>  Basitçe: Toplamayı biliyorsan çarpma öğrenmek daha kolaydır. Model için de aynısı geçerli. Yani çarpmayı öğreteceksek önce toplamayı öğretiyoruz yani iki sayının etkileşimini, ardından çarpmanın genelini artık bağlantı adıyla modele tekrar veriyoruz.

**ResNet-18 Yapısı**:
- Giriş: RGB görüntü (3×224×224)
- İlk katman: Conv → BatchNorm → ReLU → MaxPool (64×56×56)
- Ardından 4 adet Residual Layer:
  - Layer1: 64 kanal
  - Layer2: 128 kanal
  - Layer3: 256 kanal
  - Layer4: 512 kanal
- Son katmanlar: AvgPool → Flatten → Fully Connected → Sonuç

---

## Sonuç ve Özet

Bilgisayarlı görüde LeNet'ten ResNet'e gelene kadar uzun bir yol katettik. Bugün ulaştığımız nokta, yapay zeka devriminin gerçek anlamda başladığı yerdir.

Umarım bu yazı sizin için aydınlatıcı ve öğretici olmuştur.

Bir sonraki yazıda görüşmek üzere, hoşça kalın! 
