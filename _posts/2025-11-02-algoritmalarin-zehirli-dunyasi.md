---
title: "Algoritmaların Zehirli Dünyası"
date: 2025-11-02 11:00:00 +0300
categories: [yapay zeka, hukuk,bankacılık]
tags: [hukuk, reklam, yapay zeka, science, bias, data-driven,data,bigdata, sigorta,sosyal eşitlik]
authors: yusuf-said
image:
  path: /assets/img/2025-11-02-algoritmalarin-zehirli-dunyasi/cover.webp
description: Günümüzde Algoritmaların topluma ve bireye verdiği zararlar.
toc: true
math: true
mermaid: false
comments: true
pin: false
lang: tr
---

Bu yazımızda kullandığımız teknolojilerin kalbinde yatan algoritmalar ve bunların bize olan zararlarını ele alacağız.

Yazıda, genel olarak 21.yy'da yaşanmış olayları ele alarak günümüze ve güncel yaşananlara odaklanacağız. Hazırsanız başlayalım. İlk olarak algoritma nedir? Ve genel tanımlara odaklanalım.

## 1. Algoritma ve Genel Tanımlar
### 1.1 Algoritma Nedir?
İsmini ünlü Pers Matematikçi **[Harezmi](https://en.wikipedia.org/wiki/Al-Khwarizmi)**'den alan algoritma kavramı, genellikle _bilgisayar bilimleri_, matematik ve günlük hayatta karşımıza çıkar. Bir problemin çözümünün adımlarının basitleştirilmiş ve açık şekilde anlatılmasına genellikle **[algoritma](https://www.youtube.com/watch?v=cDA3_5982h8)** deriz. Algoritmalar bir yazılımın veya programın kalbini oluşturan esas parçadır. Algoritmalar sayesinde çözümü istenen problemi doğal dilden dijital sistemlere aktararak günümüzde bilgisayarlar vb. sistemleri günlük hayata uyarlamamızı ve kullanmamızı sağlar.

### 1.2 Genel Tanımlar
#### **Bias (Ön yargı)**:
Algoritmaların -özellikle yapay zekanın- belirli grup veya sosyal olarak dezavantajı olan gruplara (kadın, çocuk ,engelli, azınlık gruplar vb.) karşı ön yargı geliştirmesi. Örneğin engelli veya kadınların iş başvurularında geriye düşmesi.

#### **Filtre Balonu (Filter Bubble)**:
Algoritmaların kişisel tercihlere dayanarak kullanıcıyı belirli içeriklere hapsetmesi. Örneğin aramalara dayanarak reklam gösterilmesi.

#### **[BlackBox Algoritmaları](https://www.arimetrics.com/en/digital-glossary/black-box-algorithm)**:
Kullanıcıların algoritmaların nasıl çalıştığı veya neye göre karar verdiğinin bilememesi ve şeffaf ve rekabet karşı olan algoritma türü. Örneğin bankalarda veya finans sistemlerinde kredi limit veya kredi/sigorta başvurularının reddedilmesi.

#### **Ekran Süresi(Screen Time)**: 
Kullanıcıların teknolojik cihazlarla(telefon, bilgisayar, TV vb.) ne kadar süre geçirdiğini anlatan ölçüt. Ekran süresinin ergin bireyler için 1.30-2 saat arası olması öneriliyor.

Genel tanımları verdiğimize göre yazının geri kalanında algoritmaların yarattığı olayları sınıflandırıp detaylara geçeceğiz.

#### **Cookie**: 
İnternet sitelerinin, kullanıcıların tarayıcılarına kaydettiği küçük veri dosyalarıdır. Kullanıcı tercihlerini hatırlamak ve oturum bilgilerini saklamanın yanı sıra, **reklam ve pazarlama amaçlı kullanıcı davranışlarını takip ederek hedeflenmiş reklamlar sunmak** için de kullanılır.

## 2. Algoritmanın Yarattığı Problemler


### Ayrımcılık ve Sosyal Adaletsizlik

#### Amazon'un İşe Alım Süreçleri
<figure>
    <img src="/assets/img/2025-11-02-algoritmalarin-zehirli-dunyasi/resim2.webp" width="600" alt="resim1">
 
</figure>
2015'te Amazon'un yazılım ekibi, iş başvurularına gelen özgeçmişleri inceleyen bir yapay zeka sistemine geçti. Yapay zeka modeli on yıllık verileri ele alarak eğitilmişti. Bundan dolayı yazılım/bilgisayar alanı gibi hızlı değişim ve cinsiyet eşitsizliğini olduğu bir alanda dengesiz bir veri üzerinden eğitilmişti. Bundan dolayı kadın olarak işe başvuran bireyleri erkek bireylere göre daha az tercih edecek şekilde bir ön yargı geliştirmişti. Ön yargı konusunda bir erkek başvuranın özgeçmişinde "Kadın Satranç Kulübü Kaptanı" yazmasından dolayı kriterleri sağlamasına rağmen elemiştir. Bu olay 2015'e sürmüş olup Amazon'da çalışan mühendisler bu olaya müdahale ederek durmuştur. Ama ne kadar bir önlem alındığı veya ne kadar önüne geçilebileceği bir muamma olup sorunlar olduğundan dolayı bu uygulamayı 2017'de sona erdirmişler.[1]



#### ABD'de Yargı Üzerinden Irkçılık
Amerikalı Mahkemelerde [COMPAS](https://en.wikipedia.org/wiki/COMPAS_(software)) ve LSI-R adlarına sahip veri-tabanlı  karar verme sistemi kullanılıyordu. COMPAS özel bir şirket tarafından geliştirilen bir sistemdi ve blackbox algoritmaya sahipti . Suçluların daha sonra tekrar suç işleyip işlememe durumlarını ele alması için tasarlanmıştı. Diğer tarafta LSI-R adlı bir istatistik yöntemi vardı.[2] Bu yöntem akademisyenler tarafından tasarlanmıştı. Bu iki yöntemin ortak noktası da ön yargıya karşı problemli olmasıydı. Bu sistemler insanların yaşadığı bölgeyi, akrabalarının ve kendisinin adli sicil kayıtlarını, eğitim ve maddi durumlarını değerlendirerek suça ne kadar eğilimli veya bir suçun onun tarafından mı işlendiğini tespit etmek için Amerikalı Mahkemeler tarafından kullanılan bir sistemlerdi. Bu sistemler sosyo-ekonomik veya sosyolojik yapıların dengesizliği göz ardı edip Siyahi bireylerin mahkeme tarafından cezalandırılmasına ve ayrımcılığa sebep oluyordu. Bu olayların fark edilmesi sonucunda mahkemelerde kullanılma zorunluluğu kaldırıldı ve kullanımının uyarılara ve belirli şartlara bağlanılması istendi. [3]


### Otoriterlik ve Siyasi Kontrol

#### Cambridge Analytica ve Facebook Faciası

<figure>
    <img src="/assets/img/2025-11-02-algoritmalarin-zehirli-dunyasi/resim3.webp" width="600" alt="resim2">
 
</figure>

2018'de ortaya çıkan bilgilere göre İngiltere Merkezli şirket olan Cambridge-Analytica, 2014 yılında Facebook üzerinden bir uygulama sunuyor. Uygulamanın adı _thisisyourdigitallife_. Bu uygulama aracılığıyla kişiler kişisel bilgilerini ve arkadaşlık verilerini girerek bir karakter testi yapıyor. Bu testin illegal olarak veri toplayıp 2016-ABD seçimleri ve 2018-Brexit seçimlerinde kişilere siyasi-hedefli reklam verme amacıyla kullandığı ortaya çıkıyor. Bu durumu 2015'te fark eden Facebook hiçbir önlem almıyor. 2018'de bu yapı ortaya çıktıktan sonra, FTC incelemeler yapıp Facebook'a gerekli önlemleri almadığında dolayı 5 Milyar USD ceza veriyor. Cambridge Analytica'nın yaklaşık 50 milyon kişinin verisini çektiği tespit edilmiş. Bu olayların başında fonlayan kili Trump'ın danışmanı Steve Bunnon ve Cambridge Üniversitesinde bu verileri toplayan  ve işleyerek araştırmalar yapan Aleksandr Kogan olduğu biliniyor. [4] [5]
[6]


#### Çin Yüz Tanıma Sistemleri

Çin, kişi başına düşen güvenlik kamerası sayısında dünya birincisi[7]. Bu kameralar sayesinde yüz tanıma teknolojileri kullanılarak insanların kimliği tespit edilebiliyor ve hareketleri takip edilebiliyor. Sistem genel güvenlik amacıyla kullanılsa da, özellikle Uygur Müslümanlar gibi azınlık grupların fişlenmesi ve sürekli gözetim altında tutulması için de kullanıldığı bildiriliyor[8]. Bu uygulamalar, Çin’in Uygur halkına yönelik yıllardır süregelen baskı ve asimilasyon politikalarının bir parçası olarak görülüyor.

Bunun yanı sıra bu kameralar ve yüz tanıma sistemleri toplum üzerinde de baskı oluşturuyor. Sürekli gözetim altında olmak, insanların davranışlarını kısıtlamasına, daha içine kapanmasına ve ifade özgürlüğünü sınırlamasına yol açıyor[8]. Böylece sistem sadece suç önleme aracı değil, aynı zamanda sosyal kontrol ve otoriter güç aracı olarak işlev görüyor.

### Sosyal Medya Platformlarının Etik Kaygısının Olmaması

#### Elon Musk'ın Twitter'ı Satın Alması

<figure>
    <img src="/assets/img/2025-11-02-algoritmalarin-zehirli-dunyasi/resim4.webp" width="600" alt="resim3">
 
</figure>
Kasım 2022'de Elon Musk Twitter'ı 45 Milyar USD'ye satın aldı. Ve satın almasının amacının ifade özgürlüğünü ve şeffaflığı artırmak için olduğunu söylemişti. Ama alındıktan kısa süre sonra platformda bir takım problemler meydana geldi. Bot ve zararlı içeriğin engellenemesi, ırkçı ve nefret söyleminin artması, mavi tik üzerinden kazanç vaadiyle ölü internet teorisini doğrulayan bir platforma dönüştürdü. Ve mavi tıka sahip olan hesaplarının önerilerde daha fazla önerilmesini ve öne çıkmasını sağlamıştır. 2024 Amerika Seçimlerinde Trump'ın yanında yer alması platformun bağımsız ve tarafsızlığına gölge düşürdü. Ayrıyeten öneri algoritmasının şeffaf olmaması en büyük problemlerden birisi. Fransa Mahkemeleri, X'in otomatik veri işleme sisteminin şeffaf olmaması gerekçesiyle soruşturma başlattı. Soruşturmada algoritmanın bağımsız bir önerme yapmadığı genellikle aşırı sağ ve ırkçı gönderilerinin öne çıkarıldığını iddia edilmiştir.
Grok'un ise kontrolden çıkıp nefret söyleminde bulunması da ayrı bir olaydır.[8] [9] [10][11]

### Kişiselleştirilmiş Öneriler

#### Kısa Videolar ve Dikkat Süresinin Azalması
<figure>
    <img src="/assets/img/2025-11-02-algoritmalarin-zehirli-dunyasi/resim5.webp" width="600" alt="resim4">
 
</figure>
Belki de aralarında en çok maruz kaldığımız ve bize en çok zarar veren algoritma sistemleri sosyal medya kısa video öneri sistemler... İlk türevleri Vine-2013'e dayansa da özellikle Çinli sosyal medya platformu TikTokun 2018'de piyasaya girmesiyle ön plana çıktı. Kullanıcıların 15-30 saniyelik videolar izlemesiyle dopamin reseptörlerinin bozulmasına bağımlılık geliştirmesine ve dikkat süresinin azalmasında belirgin sebep olmuştur.[12] Bu tür algoritmalar kişinin sadece dikkat süresini ve dopamin reseptörlerini bozmakla kalmıyor. Ayrıca uyku düzenini , benmerkezcil algısını, özgüvenini de yıkıyor. Bireylerin daha fazla ekrana bağlı kalıp hiçbir şey yapmadığı ve çevresiyle zayıf iletişimi olan pasif bir bireye dönüştürüyor. 

#### Kişileştirilmiş Reklamlar

Yazının bu kısmında kişiselleştirilmiş reklam algoritmalarını ele alacağız. Kişiselleştirilmiş reklamlar kişilerin internet aramaları, sosyal medya paylaşımları ve gezinti geçmişiniz toplayarak size bir dijital-reklam kimliği oluşturur.[13] Dijital-reklam kimlikleri ayrıyeten izleme sistemleri olan [cookie](https://en.wikipedia.org/wiki/HTTP_cookie)leri kullanır. Bu sayede birden fazla reklam sisteminde kişisel bilgileriniz bulunur. Kişiselleştirilmiş reklamlar sizin harcama eğilimlerinizi hedeflediği birinci olarak cebinizin düşmanı, ikinci olaraksa mahremiyetinizin düşmanı. Bu verilerin ne kadar ve ne amaçla tutulduğu da muamma. 
Bu yüzden cookie kullanımı azaltmak ve [reklam engelleyicileri](https://en.wikipedia.org/wiki/Ad_blocking) hayatınıza dahil ederek hem temiz bir internet hem de mahremiyet dostu bir deneyim elde edersiniz.

### Finansal Sistemler
<figure>
    <img src="/assets/img/2025-11-02-algoritmalarin-zehirli-dunyasi/resim6.webp" width="600" alt="resim5">
 
</figure>Bankalar ve sigorta şirketleri, müşterilerine kredi vermek, risklerini hesaplamak ve finansal ürünler sunmak için  makine öğrenmesi algoritmaları kullanıyor. Bu algoritmalar veriyi çok hızlı işleyip karar vermeyi kolaylaştırsa da birtakım sorunları ve hatalara sebep olabiliyor.
### Algoritmaların Riskleri

1. **Hatalı karar ve model riski**  
    Algoritmalar geçmiş veriler üzerinden eğitildiği için, eksik veya hatalı bilgiler yanlış sonuçlar doğurabilir. Örneğin bir kişinin kredi notu düşük görünmesine rağmen ödeme kapasitesi yüksek olabilir. Bu tür hatalar, sadece bireysel değil sistemsel olarak finansal güvenliği de tehdit edebilir.[14]
    
2. **Ön yargı ve ayrımcılık**
    Algoritmalar geçmiş verilere dayandığından, bazı gruplar değişen ortamda  dezavantajlı hale gelebilir. Örneğin kadınlar, azınlıklar veya düşük gelirli gruplar kredi başvurularında haksız şekilde reddedilebilir. [15]
    
3. **Şeffaflık eksikliği**  
    Bankaların ve sigorta şirketlerinin kullandığı algoritmalar genellikle blackbox algoritma şeklindedir.  Müşteriler ve bazen deneten kişiler bile algoritmanın neden belirli kararlar verdiğini tam olarak göremez. Bu durum hatalı veya haksız kararların tespit edilmesini zorlaştırır.[16]

4. **Toplumsal ve ekonomik etkiler**  
    Algoritmaların yanlış veya ön yargılı çalışması ekonomik ve sosyal eşitsizliği artırabilir. Bireyler veya belirli gruplar sürekli dezavantajlı duruma düşerse finansal sistemin adil ve güvenilir olması tartışmalı hale gelir.

## Tartışma: LLM'ler ve AI'da Durumlar Nasıl?

Bu kısımda ise Neural Network gibi veri-tabanlı sistemler üzerine tartışacağız.
LLM ve NN'ler bildiğiniz üzere veriler üzerinden eğitilen ve geliştirilenh algoritmalardır. 
Özelllikle günümüzde ChatGPT,Gemini vb. dil modellerinin prompt injection yapılarak modellerdeki sansürün kaldırıldığına şahit oluyoruz. Bu sansürün kaldırılması ile dil modellerinden yasal olmayan konular hakkında bilgiler alınabiliyor. Bu başlıca problemlerden birisi. Ama diğer problemler ise dil modellerinin eğitildiği kaynakların ve verilerin, ne kadar özenle seçilirse seçilsin ön yargıya sahip olabileceği. Örneğin Grok'un sistem komutlarının birkaçının değiştirilerek ırkçı ve politik doğruluk yapablieceğini gördük.[16][17]
Bir başka problem ise İmage-Gen teknolojileri. Bunlar üzerinden realistik fotoğraf üretimi ile sosyal medyada dezenformasyona sebep olabiliyor. Sadece resim/video ile değil bu durum. Ses klonlanması-Deepfake gibi sistemlerde dolandırıcılık  dezenformasyon, kişisel verilerin tehlikeye girmesi gibi durumlara sebep olabliyor. Peki sizin yapay zeka teknolojilerine karşı tutumunuz nasıl?

## Sonuç 
Göreceğiniz üzere algoritmaların ne kadar insanlık yararına katkıları olsa da günümüzde hem ayrımcılığa hem yalan bilgiye sebep olabiliyorlar. Kişisel verilerimizde ayrıyeten bir tehdit. Bunun için bu sistemleri kullanırken dikkatli olmalıyız. Kişisel verilerin paylaşımına dikkat etmeli ve sosyal medya platformlarını kısıtlı ve dikkatli kullanmalıyız.

## İleri Okumalar
* Cal Newport - Pürdikkat
* Johann Hari - Çalınan Dikkat
* Cathy O'Neil - Matematiksel İmha Silahları





## Kaynakça
1. [Jeffrey Dastin, Amazon scraps secret AI recruiting tool that showed bias against women][1]
2. [Cathy O’Neil, Matematiksel İmha Silahları: Büyük Veri, Eşitsizliği Nasıl Artırıyor ve Demokrasiyi Nasıl Tehdit Ediyor?][2]
3. [National Legal Research Group, Criminal Law: Use of Risk Assessment Tools in Sentencing Upheld... for Now][3]
4. [Carole Cadwalladr & Emma Graham-Harrison, Revealed: 50 million Facebook profiles harvested for Cambridge Analytica in major data breach][4]
5. [Wikipedia contributors, Aleksandr Kogan (scientist)][5]
6. [Federal Trade Commission, FTC imposes $5 billion penalty and sweeping new privacy restrictions on Facebook][6]
7. [Emin Aytekin, Çin, yüz tanıma teknolojisinin kullanımına düzenleme getirecek][7]
8. [Drew Harwell, In China, facial recognition, public shaming, and control go hand in hand][8]
9. [Damien Leloup, Martin Untersinger, & Aurore Defer, French prosecutors open investigation into X’s algorithms][9]
10. [Yash Vekaria, Zubair Shafiq, & Savvas Zannettou, Before Blue Birds Became X-tinct: Understanding the Effect of Regime Change on Twitter's Advertising and Compliance of Advertising Policies][10]
11. [Wikipedia contributors, Twitter under Elon Musk][11]
12. [Yan Qin, Bouchra Omar, & Alessandro Musetti, The addiction behavior of short-form video app TikTok: The information quality and system quality perspective][12]
13. [Google Play Developer Support, Reklam kimliği (Advertising ID) hakkında][13]
14. [BIS, Financial Stability Institute Insights No. 63: Machine learning in financial services][14]
15. [BFA Global, Algorithmic Risk in Financial Services][15]
16. [MDPI, Algorithmic Decision-Making in Finance][16]
17. [Jeffrey Dastin, Chatbot Grok doesn’t glitch — it reflects X][17]
18. [Drew Harwell, Grok Is Spewing Antisemitic Garbage on X][18]

[1]: https://www.reuters.com/article/world/insight-amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK0AG/
[2]: https://www.google.com
[3]: https://www.nlrg.com/criminal-law-legal-research/criminal-law-use-of-risk-assessment-tools-in-sentencing-upheld-.-.-.-for-now
[4]: https://www.theguardian.com/news/2018/mar/17/cambridge-analytica-facebook-influence-us-election
[5]: https://en.wikipedia.org/wiki/Aleksandr_Kogan_%28scientist%29
[6]: https://www.ftc.gov/news-events/news/press-releases/2019/07/ftc-imposes-5-billion-penalty-sweeping-new-privacy-restrictions-facebook
[7]: https://www.aa.com.tr/tr/bilim-teknoloji/cin-yuz-tanima-teknolojisinin-kullanimina-duzenleme-getirecek-/2963871/
[8]: https://www.cnet.com/news/politics/in-china-facial-recognition-public-shaming-and-control-go-hand-in-hand/
[9]: https://www.lemonde.fr/en/pixels/article/2025/02/07/paris-prosecutors-open-investigation-into-x-s-algorithms_6737910_13.html
[10]: https://arxiv.org/abs/2309.12591
[11]: https://en.wikipedia.org/wiki/Twitter_under_Elon_Musk
[12]: https://doi.org/10.3389/fpsyg.2022.932805
[13]: https://support.google.com/googleplay/android-developer/answer/6048248?hl=tr
[14]: https://www.bis.org/fsi/publ/insights63.pdf
[15]: https://bfaglobal.com/wp-content/uploads/2020/01/R2AWhitePaper-1.pdf
[16]: https://www.mdpi.com/2227-9091/7/1/29
[17]: https://techpolicy.press/chatbot-grok-doesnt-glitch-it-reflects-x
[18]: https://www.wired.com/story/grok-antisemitic-posts-x-xai/
