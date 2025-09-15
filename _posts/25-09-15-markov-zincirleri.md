---
title: "Markov Zincirleri (Markov Chains)"
date: 2025-09-15 18:00:00 +0300
categories: [yapay zeka, matematik]
tags: [nlp, matematik, yapay zeka, math, science, markov chains, chain]
authors: yusuf-said
image:
  path: /assets/img/2025-09-15-markov-zincirleri/cover.webp
description: Markov Zincirlerinin tarihi ve günümüzde nasıl bir öneme sahip olduğu
toc: true
math: true
mermaid: false
comments: true
pin: false
---

# 1. Markov Zincirleri Nedir? ve Kökeni ve Yapısı

**Markov Zincirleri**, adını Rus matematikçi **Andrey Markov**’dan alır. Bu zincirler, stokastik yapıya sahip matematik ve istatistik tabanlı bir olasılık modelidir. Markov zincirleri, şuanki durumu temel alarak gelecekteki durumların olasılıklarını tahmin etmek için kullanılır. Temel varsayımı şudur: Gelecek yalnızca şuanki duruma bağlıdır, geçmişin doğrudan bir etkisi yoktur. Bu özelliğe **belleksizlik (memorylessness)** denir ve Markov zincirlerinin temelini oluşturur.


<figure>
    <img src="/assets/img/2025-09-15-markov-zincirleri/2.webp" width="600" alt="">
 
</figure>



Temelleri 20. yüzyılın başına dayanmaktadır ve Andrey Markov tarafından ele alınmıştır. Keşfedilme süreci, Pavel Nekrasov’un Büyük Sayılar Yasası’nı dini bir temele oturtarak her şeyin belirli bir düzende gerçekleştiğini ve bağımsız olduğunu iddia etmesiyle başlamıştır. Markov ise bunun böyle olmadığını, olayların tamamen bağımsız değil, aksine şuanki yaşanan durumla bağlantılı ve rastgele bir biçimde birbirine bağlı olduğunu savunmuştur. Bunu ispatlamak içinse **Alexander Puşkin’in “Yevgeni Onegin”** şiirindeki harf ve kelime dağılımlarını incelemiştir. İlk önce şiiri incelemek için ilk yirmi bin kelimesini kendine data olarak hazırlıyor, harfleri **sesliler(V)** ve **sessizler(C)** diye ayırıyor. Bu ayırma sonucunda metnin %43'ünün sesli, %57'sinin sessiz harflerden oluştuğunu tespit ediyor. Daha sonra farklı kombinasyonlarla bir araya gelen(CC, CV, VC, VV) harf çiftleri saymış ve bu rakamlar üzerinden geçiş olasılıkları hesaplarını hesapladı. Örneğin, bir sesli harften sonra tekrar sesli harf gelme olasılığı %13, sessiz harf gelme olasılığı ise %87 olarak bulunmuştur. Benzer biçimde, bir sessiz harften sonra sesli gelme olasılığı yaklaşık %67, tekrar sessiz gelme olasılığı ise %33’tür.

Bu oranlar bir **geçiş matrisi** halinde düzenlenmiş ve böylece iki durumlu bir olasılık modeli, yani bugün “**Markov zinciri**” olarak bilinen yapı kurulmuştur. Markov, bu zinciri kullanarak rastgele başlanan bir harf dizisinin uzun vadede yine metindeki genel dağılıma (%43 sesli, %57 sessiz) yakınsadığını göstermiştir. Bu yapının Nekrasov'un söylediği gibi her şeyin bir düzen içinde değil bir Rastgeliklerin ve bağımlı durumların bir araya gelmesiyle bir yakınsama durumu haline gelebileceğini kanıtlamıştır.

Bir sonraki kısımda matematiksel olarak temel gösterimi anlatmak istedik. Tabii ki burada amacımız matematiksel ispatına veya temsillerine odaklanmak değil sadece felsefi ve sezgisel bir anlatım yapmak.

# 2. Markov Zincirlerinin Matematiksel Temelleri

## 2.1. Tanım
Bir **Markov zinciri**, ayrık zamanlı bir stokastik süreçtir:

$$
\{X_n\}_{n \ge 0},\quad X_n \in S
$$

Burada:
- $S$ = durumlar kümesi (sonlu veya sayılabilir).
- $X_n$ = $n$’inci zamanda sistemin bulunduğu durum.

**Markov özelliği (belleksizlik):**
$$
P(X_{n+1}=j \mid X_n=i, X_{n-1},\dots,X_0) = P(X_{n+1}=j \mid X_n=i)
$$

Yani gelecek sadece bugüne bağlıdır; geçmişin etkisi yoktur.

---

## 2.2. Geçiş Olasılıkları
Geçişler bir **geçiş matrisi** $P$ ile tanımlanır:
$$
P = [p_{ij}],\qquad p_{ij} = P(X_{n+1}=j \mid X_n=i)
$$

Koşullar:
$$
p_{ij} \ge 0,\qquad \sum_j p_{ij} = 1
$$

**Örnek (2 durumlu sistem):**
$$
P=\begin{bmatrix}
0.8 & 0.2\\
0.4 & 0.6
\end{bmatrix}
$$

- Bugün güneşli ise: yarın %80 güneşli, %20 yağmurlu.  
- Bugün yağmurlu ise: yarın %40 güneşli, %60 yağmurlu.

---

## 2.3. Başlangıç Dağılımı
Başlangıçtaki olasılık dağılımı:
$$
\boldsymbol{\pi}^{(0)}=[\pi^{(0)}_1,\pi^{(0)}_2,\dots,\pi^{(0)}_m],\qquad \sum_i \pi^{(0)}_i=1
$$

$n$ adım sonraki dağılım:
$$
\boldsymbol{\pi}^{(n)}=\boldsymbol{\pi}^{(0)}P^n
$$

---

## 2.4. Durağan Dağılım
Markov Zincirleri belirli sayıda tekrarlandıktan sonra sabit bir dağılıma ulaşır. BU dağılım $\boldsymbol{\pi}$, **durağan (denge)** dağılımdır.
Eğer aşağıdaki denklem çözülürse bir genel dağılım ve stabil değer elde edilir. :
$$
\boldsymbol{\pi}=\boldsymbol{\pi}P,\qquad \sum_i \pi_i=1
$$

**Örnek:**
Yukarıdaki $P$ için çözüm:
$$
\boldsymbol{\pi}=\begin{bmatrix}\tfrac{2}{3} & \tfrac{1}{3}\end{bmatrix}
$$
Yani uzun vadede günlerin yaklaşık %67’si güneşli, %33’ü yağmurlu olur.


# 3.Markov Zincirlerinin Kullanım alanları
## 3.1 Fizik ve Atom altı parçacıklar:
<figure>
    <img src="/assets/img/2025-09-15-markov-zincirleri/1.webp" alt="" width="600">
</figure>

Markov zincirleri, atom altı parçacıkların nasıl davrandığı ve nasıl olasılıklar içinde hangi orbitalden hangi orbitale atlama olasılıklarını simüle etmek için kullanılır. Ayriyeten çekirdekteki saçılma ve enerji durumlarını tespit etmek için de kullanılır.
 Örneğin; 
II. Dünya Savaşı döneminde John von Neumann, Stanislaw Ulam ile birlikte **Monte Carlo yöntemini** geliştirmiş ve Manhattan Projesi kapsamında nötron taşınımı ile zincirleme reaksiyonların modellenmesinde kullanmıştır. Bu süreçte, nötronların bağımsız hareket etmediği, her adımın bir önceki duruma bağlı olduğu fark edilmiş ve bu nedenle sürecin **Markov zincirleri** üzerinden modellenmesi gerektiği ortaya çıkmıştır. Von Neumann ve Stanislaw Ulam, bu zincirleri **ENIAC** üzerinde simüle ederek Monte Carlo metodunu bulmuşlardır. Bununla beraber ilerideki yıllarda bu araştırmaların üzerinde giderek Monte Carlo ve Markov Zincirlerinin birleştirilmiş hali olan MCMC keşfedilmiştir.


## 3.2 NLP (Doğal Dil İşleme)

<figure>
    <img src="https://media.geeksforgeeks.org/wp-content/uploads/20230503183646/Markov-Chains-in-NLP.webp" alt="Düşünme zinciri basamakları" width="600">
    <figcaption> Markov Chains in NLP(görsel 1)</figcaption>
</figure>



Markov Zincirleri, NLP'nin temelini oluşturur. İlkel NLP modellerinde olasılık hesapları yani bir kelimeden sonra hangi kelimenin geleceği veya basit metin üretimi için kullanılmıştır. Ama Markov Zincirleri kısa bellekli olduğu için günümüzde n-gram(Markov zincirlerinin gelişmiş hali) ve Transformers mimarisi, Markov zincirlerinin yerine almıştır.


## 3.3 Google Aramaları ve PageRank

PageRank, Google'ın arama algoritmasının temeli olan ve web sayfalarının önem derecesini belirlemek için 1996'da geliştirilen bir algoritmadır.

Web sitelerini gezen hayali bir rastgele kullanıcıyı düşünelim. Bu kullanıcı herhangi bir sayfaya girer ve sayfada bulunan bağlantılardan birini seçerek diğer sayfaya geçer. Bu geçişler yalnızca web sitelerinin bağlantı yapısına dayanır. Elde edilen bu geçişler ve web siteleri bir **graf yapısı** üzerinde modellenir. Graf üzerindeki her düğüm birer **state (durum)** olarak Markov zincirine eklenir. Bu durum defalarca tekrarlandığı zaman zincir, zamanla **durağan-stabil bir hale** ulaşır. Bu elde edilen durum , günümüzde Google gibi arama motorlarının temelini oluşturan **PageRank algoritmasının** ortaya çıkmasını sağladı.

## 3.4 Biyoinformatik ve Biyolojik Yapıların Modellenmesi

Markov zincirleri biyoinformatikte yaygın olarak DNA, RNA ve protein dizilerindeki istatistiksel bağıntıları modellemek için kullanılır. Gen tahmini, dizilerde motif arama, protein ailelerinin belirlenmesi, splice site tespiti ve filogenetik analizlerde önemli rol oynarlar. Ayrıca gizli Markov modelleri (HMM) ["gizli bağlanltıları ve ilişkileri yakalamak için özelleşmiş markov zincirleri"] özellikle genom anotasyonu ve protein dizilerinin sınıflandırılmasında temel yöntemlerden biridir.
## Yapay Zeka
Markov Zincirleri NLP'de kullanıldığından bahsetmiştik. Yapay zekanın çeşitli kısımlarında kullanımı mevcuttur. Örneğin Reinforcement Learning'de (Markov Decision Process, Partially Observable MDP), Görüntü İşleme(Markov Random Fields), Zaman Serileri(Markov Switch Models), Bayesian Metotlarda kullanılır.
# 4.Markov Zincirlerinin Zayıflıkları 

* **Belleksizlik**: Markov Zincirleri sadece şuanki zamanı hesapladığı geçmişin önemli olduğu durumlarda olasılık hesaplarını imkansız kılar.
* **Sınırlı Açıklama Yeteneği**: Markov zincirleri olayların neden ve niçin olduğunu açıklayamaz. Sadece olayların sonucunu tahmin etmemizi sağlar. Bu durum tıp ve mühendislikteki sorunların temeline inmeyi ve açıklamamızı engeller.
* **Büyük olasılık uzayları**: Büyük olasılıkları hesaplamak için çok fazla hesaplama gücüne ve veriye ihtiyacımız var. Birden fazla durumlarda daha fazla veri ve daha hesaplama gücü anlamına gelir. 
* **Gizli Durumların Yetersizliği**:Normal Markov Zincirleri olayları doğrudan gözlenmesi için kullanılır.  Bu bazı olaylardaki aradaki ilgili bağlantıların yakalanmaması  ve gizli bağların değerlendirilmemesine sebep olur. Bunun için Markov Zincirlerin güçlendirilmiş hali olan **Gizli Markov Zincirleri** wkullanılır. Örneğin konuşma tanıma sistemlerinde sadece kelimeyle olan bağlantılar değil kelimelerin nasıl çıktığı, hangi ses tonuyla çıktığı da önemlidir. Bunları normal Markov zincirleriyle yakalamıyoruz. Bunun yerine gizli markov zincirleri kullanıyoruz.
* **Stabilite**: Markov Zincirleri bir yerden sonra stabil dağılıma ulaştığı için uzun vadeli kullanıcı davranışlarını modellemek için yeteriz kalabilir.

## 5. Markov Zincirlerinin Gelişmiş ve Özelleşmiş Modelleri

## Monte Carlo Markov Zincirleri (MCMC)
Daha önce yukarıda bu MCMC'lerden bahsetmiştik. MCMC'lerin özellikleri doğrudan yakalanması ve modellenmesi zor ilişkileri modellleyerek ve hesaplayarak olasılıkların ortaya koyulmasını sağlar. 1953 yılında Metropolis algoritmasıyla beraber geliştirilmiştir. Atom altı parçacık davranışlarının modellemesi için kullanılır.

## Gizli Markov Modeli (HMM)
**Gizli Markov Modelleri (HMM)**, gözlenemeyen (gizli) durumların ve bu durumlara bağlı olarak ortaya çıkan gözlemlerin bulunduğu olasılıksal modellerdir. Temelinde Markov zincirine dayanır, her bir gizli durum yalnızca bir önceki duruma bağlıdır. Ancak bu gizli durumlar doğrudan gözlemlenmez. Onların etkisi, gözlenebilir çıktılar üzerinden dolaylı şekilde görülür. Konuşma tanıma, biyoinformatik ve finans gibi alanlarda  kullanılır.

## Markov Zincirlerini İçeren Tablo

|Model|Açıklama|Kullanım Alanları|
|---|---|---|
|**Hidden Markov Models (HMM)**|Gizli durumlar ile gözlemlerin olasılıksal ilişkisini kurar. Durum doğrudan gözlenmez, sadece çıktılar üzerinden tahmin edilir.|Konuşma tanıma, dil işleme, biyoinformatik, finans|
|**Markov Chain Monte Carlo (MCMC)**|Markov zincirleriyle hedef dağılımdan örnekler üretir. Uzun vadede dağılım istenen olasılık dağılımına yaklaşır.|Bayesian istatistik, makine öğrenmesi, fiziksel simülasyonlar|
|**Semi-Markov Models**|Durumda kalma süresi sadece geometrik/exponential değil, farklı dağılımlarla da tanımlanır.|Kuyruk teorisi, güvenilirlik analizi|
|**Markov Random Fields (MRF)**|Zincir yerine graf yapısında Markov özelliğini uygular. Komşuluk ilişkileriyle bağımlılığı modeller.|Görüntü işleme, bilgisayarlı görü, istatistiksel fizik|
|**Markov Decision Processes (MDP)**|Markov zincirine aksiyon ve ödül eklenmiş halidir.|Pekiştirmeli öğrenme, optimizasyon|
|**Partially Observable MDP (POMDP)**|MDP’nin durumu tam gözlenemeyen versiyonu. Belirsizlik altında karar verme sağlar.|Robotik, oyun, otonom sistemler|
|**Absorbing Markov Chains**|Bazı durumlara girildiğinde çıkış yapılamaz (absorbe edilir).|Oyun teorisi, risk analizi|
|**Ergodik / İrredüktibl Zincirler**|Tüm durumlara erişim mümkün, uzun vadede tek bir durağan dağılım vardır.|Teorik analiz, istatistiksel modelleme|
|**Kalman Filter (Linear-Gaussian State Space Model)**|HMM’nin lineer ve Gauss dağılımlı özel hali.|Sensör füzyonu, robotik, finans|
|**Particle Filters**|Sürekli ve karmaşık durumları partiküllerle yaklaşık olarak takip eder.|Non-lineer, non-Gaussian sistemlerde izleme|

# Kapanış

Markov Zincirleri halen kullanılmakta olan en etkileyici istatistik metotlarından biridir. Kelimelerden atoma insanlığın ve doğanın yapısını anlamamızı ve gerçeklere farklı boyutta algılamamızı sağlıyor.

Okuduğunuz için teşekkürler!


# Kaynakça

- Eckhardt, R. (1987). *Stan Ulam, John von Neumann, and the Monte Carlo method*. Los Alamos Science, (15), 131–141. Los Alamos National Laboratory.  
  Erişim: [PDF](https://mcnp.lanl.gov/pdf_files/Article_1987_LAS_Eckhardt_131--141.pdf)

- Johoblogs. (2021, Şubat 24). *All you need to know about Markov chains*. Medium.  
  Erişim: [https://johoblogs.medium.com/all-you-need-to-know-about-markov-chains-d96e77988a63](https://johoblogs.medium.com/all-you-need-to-know-about-markov-chains-d96e77988a63)

- Math LibreTexts. (2022). *Markov chains and Google’s PageRank algorithm*. In *Understanding Linear Algebra (Austin)*.  
  Erişim: [https://math.libretexts.org/Bookshelves/Linear_Algebra/Understanding_Linear_Algebra_(Austin)/04%3A_Eigenvalues_and_eigenvectors/4.05%3A_Markov_chains_and_Google's_PageRank_algorithm](https://math.libretexts.org/Bookshelves/Linear_Algebra/Understanding_Linear_Algebra_(Austin)/04%3A_Eigenvalues_and_eigenvectors/4.05%3A_Markov_chains_and_Google's_PageRank_algorithm)

- Page, L., Brin, S., Motwani, R., & Winograd, T. (1999). *The PageRank citation ranking: Bringing order to the web*. Stanford InfoLab Technical Report.  
  Erişim: http://infolab.stanford.edu/~backrub/google.html](http://infolab.stanford.edu/~backrub/google.html

- StackExchange. (2015). *Markov Chains vs HMM*. Cross Validated (StackExchange).  
  Erişim: [https://stats.stackexchange.com/questions/148023/markov-chains-vs-hmm](https://stats.stackexchange.com/questions/148023/markov-chains-vs-hmm)

- Wikipedia contributors. (2025). *Monte Carlo method*. In *Wikipedia*.  
  Erişim: [https://en.wikipedia.org/wiki/Monte_Carlo_method](https://en.wikipedia.org/wiki/Monte_Carlo_method)

- Wikipedia contributors. (2025). *Hidden Markov model*. In *Wikipedia*.  
  Erişim: [https://en.wikipedia.org/wiki/Hidden_Markov_model](https://en.wikipedia.org/wiki/Hidden_Markov_model)

- Wikipedia contributors. (2025). *PageRank*. In *Wikipedia*.  
  Erişim: [https://tr.wikipedia.org/wiki/PageRank](https://tr.wikipedia.org/wiki/PageRank)

- Veritasium. (2025, Temmuz 29). *The Strange Math That Predicts (Almost) Anything – Markov Chains* [Video]. YouTube.  
  Erişim: [https://www.youtube.com/watch?v=KZeIEiBrT_w](https://www.youtube.com/watch?v=KZeIEiBrT_w)

- Görsel 1: GeeksforGeeks. (2023). *Markov Chains in NLP* [Görsel].  
  Erişim: [https://media.geeksforgeeks.org/wp-content/uploads/20230503183646/Markov-Chains-in-NLP.webp](https://media.geeksforgeeks.org/wp-content/uploads/20230503183646/Markov-Chains-in-NLP.webp)
