---
title: "LLM'leri ve Halüsinasyonları Anlamak"
date: 2025-07-13 11:00:00 +0300
categories: [yapay zeka, derin öğrenme, büyük dil modelleri]
tags: [llm, yapay zeka, halüsinasyon, doğal dil işleme, transformer]
author: tunahan
image:
  path: /assets/img/2025-07-13-llmleri-ve-halüsinasyonları-anlamak/cover.webp
description: "Büyük Dil Modellerini (LLM'leri) ile giderek artan etkileşimimizde karşılaştığımız önemli bir sorun olan halüsinasyonları, nedenlerini ve nasıl azaltılabileceğini keşfedin."
toc: true
math: false
mermaid: false
comments: true
pin: false
---

## LLM'ler

Yapay zeka modelleri hayatımızın her alanına girerken, özellikle Büyük Dil Modelleri (LLM'ler) ile etkileşimimiz giderek artıyor. Ancak bu devrimsel teknolojinin ardında, zaman zaman karşımıza çıkan ve kullanıcı deneyimini doğrudan etkileyen önemli bir sorun var: Halüsinasyonlar. Bu yazıda, LLM'lerin derinliklerine inip onları anlamaya çalışacak ve ardından bu "uydurma" davranışın nedenlerini ve nasıl azaltılabileceğini keşfedeceğiz

---
## LLM'leri anlamak

_LLM_'ler devasa verilerle, _NLP_ (Doğal dil işleme) yöntemleri sonucu oluşturulmuş modelleridir [3] .

Dil modellerinin tarihi eskiye dayansa da, günümüzdeki _Büyük Dil Modelleri_ için bir dönüm noktası 2017 yılında Google Brain (günümüzde Google DeepMind) ekibinin yayımladığı "Attention is All You Need" başlıklı makale olmuştur [4] . Bu makale, 
**"Transformers"** adı verilen ve "dikkat" (attention) mekanizmasını kullanan devrimci bir mimariyi tanıttı. Bu mimarinin temelinde, bir metni anlamak için **"encoder" (kodlayıcı)** ve yeni bir metin üretmek için **"decoder" (kod çözücü)** olmak üzere iki ana blok bulunur.

Bu güçlü mimari, zamanla iki farklı yaklaşımın doğmasına neden oldu:

1. **Üretim Odaklı Modeller:** GPT ve türevleri bu yaklaşıma en iyi örnektir. Adından da anlaşılacağı gibi ("_Generative Pretrained Transformer_"), bu modellerin temel amacı metin üretmektir. Bu nedenle Transformer yapısının yalnızca **"decoder" (üretici)** bloğunu kullanırlar [5] .
    
2. **Anlama ve Üretme Odaklı Modeller:** **Google'ın** "_BERT_" modeli gibi diğer yapılar ise metni derinlemesine anlamayı hedefler. Bu amaçla, mimarinin hem **encoder** hem de **decoder** bloklarını çift yönlü (_bidirectional_) bir şekilde kullanırlar. Bu yapı, onları çeviri araçları gibi hem anlamanın hem de üretmenin kritik olduğu görevler için ideal kılar [6] .
<figure>
    <img src="/assets/img/2025-07-13-llmleri-ve-halüsinasyonları-anlamak/transformer.webp" alt="Transformer Mimarisi Diyagramı" width="600">
    <figcaption>Görsel: Transformer Mimarisi</figcaption>
</figure>


Modelin, kavramları bir vektör uzayında nasıl grupladığını anlattık: "_kral_" ve "_prens_" gibi kelimeler bir araya gelirken, "_kraliçe_" ve "_prenses_" başka bir yerde kümelenir. Bu durum akla şu mantıklı soruyu getiriyor: Eğer model matematiksel olarak en yakın vektörleri seçiyorsa, aynı soruya neden her zaman birebir aynı cevabı vermiyor?

Bu sorunun cevabı, modellerden beklentimizde gizli: **yaratıcılık**. Eğer bir model her defasında en olası, en "_doğru_" cevabı verseydi, deterministik ve sıkıcı olurdu. "Ama matematik deterministik değil mi?" diye düşünebilirsiniz. Evet, temelindeki matematik kurallara bağlıdır, ancak _LLM_'ler basit birer hesap makinesi değildir. Onlar, bir sonraki kelimeyi olasılıklara göre tahmin eden dil üreticileridir. İşte bu noktada devreye, modelin davranışına bilinçli olarak eklenen küçük bir **rastgelelik faktörü** giriyor. Bu faktör sayesinde model, her zaman en bariz yolu seçmek yerine, farklı ve yaratıcı metinler üretebiliyor. Meraklısı için "Temperature” ve “Top_p" terimlerine bakabilirler [8].

---

Diyelim ki ChatGPT'ye "İstanbul'un yakaları nelerdir?" dediniz. 

<figure>
    <img src="/assets/img/2025-07-13-llmleri-ve-halüsinasyonları-anlamak/istanbul-yakalar1.webp" alt="ChatGPT'nin İstanbul'un yakaları sorusuna verdiği ilk yanıt." width="600">
    <figcaption>Görsel: ChatGPT'nin İstanbul'un yakaları sorusuna verdiği ilk yanıt.</figcaption>
</figure>

O da böyle bir yanıt verdi. Peki şimdi de "İstanbul'un yakalarından bir hikaye yazar mısın?" diyelim.

<figure>
    <img src="/assets/img/2025-07-13-llmleri-ve-halüsinasyonları-anlamak/istanbul-yakalar2.webp" alt="ChatGPT'nin İstanbul'un yakaları ile ilgili hikaye isteğine verdiği ilk yanıt." width="600">
    <figcaption>Görsel: ChatGPT'nin İstanbul'un yakaları ile ilgili hikaye isteğine verdiği ilk yanıt.</figcaption>
</figure>

Yeni bir sohbette tekrar isteyelim:

<figure>
    <img src="/assets/img/2025-07-13-llmleri-ve-halüsinasyonları-anlamak/istanbul-yakalar3.webp" alt="ChatGPT'nin İstanbul'un yakaları ile ilgili hikaye isteğine yeni sohbette verdiği farklı yanıt." width="600">
    <figcaption>Görsel: ChatGPT'nin İstanbul'un yakaları ile ilgili hikaye isteğine yeni sohbette verdiği farklı yanıt.</figcaption>
</figure>

Beklediğimiz üzere farklı bir çıktı verdi.

Peki tekrar "İstanbul'un yakaları nelerdir?" dediğimizde de mi farklı bir yanıt verecek?
<figure>
    <img src="/assets/img/2025-07-13-llmleri-ve-halüsinasyonları-anlamak/istanbul-yakalar4.webp" alt="ChatGPT'nin İstanbul'un yakaları sorusuna tekrar verdiği aynı yanıt." width="600">
    <figcaption>Görsel: ChatGPT'nin İstanbul'un yakaları sorusuna tekrar verdiği aynı yanıt. </figcaption>
</figure>

Tabii ki de hayır aynı çıktıyı verecek ve vermeli de çünkü İstanbul'un iki yakası sabittir!

Yani bizim rastgelelik dediğimiz şey, sorduğunuz sorunun tipine göre farklılık gösterir. Örneğin, 'İstanbul'un yakaları nelerdir?' gibi net bir soruda rastgelelik daha çok cevabın **nasıl** verildiğini (nitelik) etkilerken; 'Bana bir hikaye anlat' gibi yaratıcı bir istekte ise cevabın **ne** olduğunu (nicelik) tamamen değiştirir

```ChatGPT
Model, kelimeleri vektör uzayında temsil eder ve benzer anlamlara sahip kelimeleri bir araya getirir. Örneğin, erkek, kral, prens ve baba gibi kelimeler birbirine yakın olurken, kadın, kraliçe, prenses ve anne gibi kelimeler de kendi aralarında yakınlaşır. Bu sayede, cinsiyetler, aile üyeleri ve nitelikler gibi kategoriler arasındaki ilişkiler daha net bir şekilde modellenir. Sonuç olarak, derin öğrenme bu tür ilişkileri keşfederek veriler arasında anlamlı bağlantılar kurar.
```
Farkı gördünüz değil mi? Benim yarı bozuk lisanım ChatGPT ile statik ve katı bir yapıya büründü. 

Peki neden her seferinde birebir çıktıyı vermez modeller?
Şöyle açıklayayım:

```
Sizin prompt'ta yazıp yazmadığınız nokta bile çıktıyı değiştirirken 128 tane gizli katmanlı ve bir o kadar da karmaşık bir model mimarisinden her seferinde aynı çıktıyı beklemek? Ütopik açıkçası. 
```
 Bir de tabii biz kasti şekilde rastgelelik sağlamaya çalışıyoruz ancak oralara bu yazıda girmeyeceğim

Ancak şunu eklemeden edemeyeceğim:
Model ne düşündüğünü, hatta çıktı verdiğini, hatta ve hatta çıktı verip vermediğini bile bilmiyor (Ta ki siz yeni prompt girene kadar)
> Ancak araştırılan ve geliştirilen mekanizmalarla bu durum değişebilir (ChatGPT "o" serisi bunun için var [9])

---
# Halüsinasyonları anlamak

Yazıya başlamadan önce hepinizden ChatGPT'de (ama o serisi değil sebebini anlatacağım) yeni bir sohbet açıp ona "Türkiye kelimesinde kaç tane 'e' harfi vardır?" demenizi istiyorum. Biz de deneyelim:

<figure>
    <img src="/assets/img/2025-07-13-llmleri-ve-halüsinasyonları-anlamak/kac-e-var.webp" alt="ChatGPT'nin Türkiye kelimesinde kaç 'e' var sorusuna verdiği müthiş yanıt" width="600">
    <figcaption>Görsel: ChatGPT'nin Türkiye kelimesinde kaç 'e' var sorusuna verdiği müthiş yanıt.</figcaption>
</figure>

Gördüğünüz gibi... Şimdi düşünelim, nasıl olur da çalıştırılması için sunucu kümesi kullanılan ve eğitimi için internette girilmedik kaynak kalmayan bu model, nasıl olur da bunu yapamaz. Sebebi çok basit:
O düşünmüyor ki!
Az önce de anlattım;

```
...Model ne düşündüğünü, hatta çıktı verdiğini, hatta ve hatta çıktı verip vermediğini bile bilmiyor...
```

O sadece varsa internette gördüğü eski bilgisini sizlere açıklıyor. Peki ya görmediyse? Ya yanlışsa? Ya sadece türevini gördüyse ve genelleyemezse?

İşte buna halüsinasyon deniyor.

**Tıpta halüsinasyon**, bir kişinin gerçek olduğuna inandığı ancak gerçek olmayan görüntü, ses, koku gibi duyuları hissetmesidir ^[1] .

LLM'ler ise özellikle geliştikçe kendilerine aşırı güvenerek alakasız, uydurma ve tutarsız içerik üretirler ^[2] . Bu bilgiler tamamen yanlış veya uydurma olabileceği gibi kendini bir anda insan gibi görmeye ve yaşamadığı şeyleri yaşamış gibi anlatmasına da neden olabilir.

---
##  Ai dünyası için halüsinasyon

Elimden geldiğince basitleştirerek anlatmaya çalışacağım. Burada 24 Ocak 2025'de yayımlanan oldukça yoğun bir makaleden yaranlandım [7] .

LLM'lerin halüsinasyonlarını iki ana kategoriye ayırabiliriz: **Gerçeklik Halüsinasyonları** ve **Sadakat Halüsinasyonları**. Gerçeklik halüsinasyonları, modelin gerçekte doğru olan bilgiyi yanlış sunması, yani 'gerçeklik çelişkisi' yaşamasıyla ortaya çıkar. Örneğin, 'Thomas Edison telefonun icadını yaptı' gibi yanlış bir ifade kullanması buna örnektir. Ya da, gerçek bir bilgiye tamamen uydurma, dışarıdan doğrulanamayan eklemeler yapabilir, buna da 'gerçeğe dayalı uydurma' denir. Modelin belirli bir kişi hakkında uydurma atıflar söylemesi bu kategoriye girer.

İkinci ana kategori olan **Sadakat Halüsinasyonları** ise modelin verilen talimatlara veya bağlama sadık kalmamasından kaynaklanır. Buna 'talimat tutarsızlığı' denir; örneğin kullanıcı Türkçe bir şey sorduğunuzda modelin İngilizce yanıt vermesi gibi. 'Bağlam tutarsızlığı' ise bir özet istendiğinde metni hatalı özetlemesiyle kendini gösterir. Son olarak, modelin matematiksel işlemlerde veya mantıksal çıkarımlarda hata yapması da 'mantık uyuşmazlığı' olarak adlandırılır.

Aşağıda bu konuda bir tablo bulabilirsiniz:



| Ana Tür                     | Alt Tür                    | Örnek                                                              |
| :-------------------------- | :------------------------- | :----------------------------------------------------------------- |
| **Gerçeklik Halüsinasyonu** | **Gerçeklik Çelişkisi**    | "Thomas Edison telefonun icadını yaptı." gibi yanlış bir ifade.    |
|                             | **Gerçeğe Dayalı Uydurma** | Modelin bir kişi hakkında uydurma atıflar söylemesi.               |
| **Sadakat Halüsinasyonu**   | **Talimat Tutarsızlığı**   | Kullanıcı Türkçe bir şey sunduğunda modelin İngilizce yanıtlaması. |
|                             | **Bağlam Tutarsızlığı**    | Bir özet istendiğinde modelin metni hatalı özetlemesi.             |
|                             | **Mantık Uyuşmazlığı**     | Matematikte yaptığı işlem hataları veya hatalı çıkarımlar.         |

---
## LLM'ler Neden Bazen "Uydurur"? 

Büyük Dil Modelleri'nin (LLM'ler) zaman zaman "uydurma" olarak tabir ettiğimiz, yani yanlış veya tutarsız bilgiler üretme eğilimi, genellikle üç ana kategoride incelenebilir: **eğitim verilerinden kaynaklanan sorunlar, eğitimin kendisindeki zorluklar ve çıktı üretme sürecindeki hatalar**.

İlk olarak, **eğitim verilerinden kaynaklanan sorunlar** halüsinasyonların temelini oluşturabilir. Eğer modelin üzerinde eğitildiği devasa veri setleri yanlış veya eksik bilgiler içeriyorsa, model bu boşlukları kendi kendine "doldurmaya" çalışır ve bu da uydurma bilgilere yol açar. Aynı zamanda, eğitim verilerindeki belirli önyargılar veya kalıplar, modelin gerçekleri çarpıtmasına neden olabilir. Ayrıca, modelin belirli bir görevi veya kullanıcı isteğini tam olarak anlayıp uygulayamaması da, yetersiz yönlendirme nedeniyle yanlış yanıtlar vermesine sebep olabilir.

İkinci kategori olan **eğitimin kendisindeki zorluklar** da halüsinasyonlara zemin hazırlar. Modelin ilk ve genel eğitiminde oluşan bazı "kötü alışkanlıklar", daha sonraki ince ayar aşamalarında da devam edebilir. Modeller, insan geri bildirimleriyle sürekli olarak daha iyi hale getirilir; ancak bu geri bildirimler yetersiz veya yanlış yönlendirilirse, model hala uydurma bilgileri doğru sanabilir.

Son olarak, **çıktı üretme sürecindeki hatalar** da halüsinasyonlara yol açabilir. Modelin en iyi cevabı seçme veya kelimeleri bir araya getirme şeklindeki kusurlar, bazen mantıksız veya yanlış çıktılar doğurabilir. En ilginç durumlardan biri ise modelin aslında emin olmadığı bir konuda bile, çok kendinden emin bir şekilde yanlış bir yanıt vermesi, yani "fazla öz güven" sergilemesidir. Özellikle karmaşık sorulara adım adım cevap vermesi gereken durumlarda, modelin mantık yürütme zincirinde kopukluklar olması da düşünme hatalarına yol açar (eğer düşünme zincirine sahip bir modelse).

| Ana Kategori                                   | Neden                                                              |
| ---------------------------------------------- | ------------------------------------------------------------------ |
| **1. Eğitim Verilerinden Kaynaklanan Sorunlar**| **Yanlış veya Eksik Bilgiler**                                     |
|                                                | **Yanlı Bakış Açıları**                                            |
|                                                | **Yetersiz Yönlendirme**                                           |
| **2. Eğitimin Kendisindeki Zorluklar**         | **Temel Eğitimden Gelen Sorunlar**                                 |
|                                                | **İnsan Geri Bildirimlerinin Eksikliği veya Yanlış Yönlendirmesi** |
| **3. Çıktı Üretme Sürecindeki Hatalar**        | **Cevap Üretme Yöntemlerindeki Kusurlar**                          |
|                                                | **Fazla Özgüven**                                                  |
|                                                | **Düşünme Hataları**                                               |
|                                                |                                                                    |

---

## Halüsinasyonları Nasıl Azaltırız? (Veya azaltabilir miyiz?)

Bu sorunu çözmek için çeşitli yaklaşımlar bulunmakta olup, bunları üç ana kategoriye ayırabiliriz: **daha iyi veri kullanmak, eğitimi geliştirmek ve çıktı üretme mekanizmalarını iyileştirmek**.

İlk olarak, **daha iyi veri kullanmak** halüsinasyon riskini önemli ölçüde azaltabilir. Modelleri eğitmek için mümkün olduğunca doğru, güncel ve yanlılıktan arındırılmış veri kümeleri kullanmak esastır. Ayrıca, modelin bilmediği konularda "emin değilim" diyebilmesini veya yalnızca bildiği konularda konuşmasını sağlamak, yani bilgi sınırlarını belirlemek kritik öneme sahiptir. Kullanıcıların ne istediğini daha iyi anlaması ve buna göre doğru cevaplar üretmesi için modele daha net ve kaliteli "eğitim örnekleri" sağlanması da halüsinasyonları engellemeye yardımcı olur.

İkinci olarak, **eğitimi geliştirmek** de çözümün önemli bir parçasıdır. Modelin temel eğitim ve ince ayar (özel görevler için eğitilme) aşamalarını, halüsinasyon riskini en aza indirecek şekilde tasarlamak gerekir. Bununla birlikte, modelin yanlış veya uydurma yanıtlar verdiğinde bunu anlayacak ve kendini düzeltecek daha akıllı geri bildirim mekanizmaları kullanmak, modelin zamanla daha güvenilir olmasını sağlar.

Son olarak, **çıktı üretme mekanizmalarını iyileştirmek** de halüsinasyonlarla mücadelede etkilidir. Modelin bir soruya cevap verirken en doğru ve mantıklı seçeneği belirlemesini sağlayacak gelişmiş teknikler kullanmak (örneğin, belirli bir "sıcaklık" ayarıyla daha tahmin edilebilir cevaplar üretmek) daha akıllı cevap seçme yöntemlerini içerir. Bu noktada öne çıkan bir yöntem, **Harici Bilgilerle Destekleme (RAG - Retrieval Augmented Generation)** yaklaşımıdır. Bu yöntemde model, sadece öğrendiklerine dayanmak yerine, bir nevi "kütüphaneye danışarak" cevap verir. Güvenilir kaynaklardan bilgi çekerek uydurma olasılığını büyük ölçüde azaltır. Ayrıca, modelin ürettiği yanıtların doğru ve kendi içinde tutarlı olup olmadığını kontrol eden ek mekanizmalar eklemek ve karmaşık problemleri çözerken insan gibi adım adım düşünmesini ve plan yapmasını sağlayan teknikler kullanmak (Chain-of-Thought prompting gibi) daha iyi düşünme becerileri geliştirmesine yardımcı olur.

| Ana Kategori                                     | Çözüm                                  |
| ------------------------------------------------ | -------------------------------------- |
| **1. Daha İyi Veriler Kullanmak**                | **Doğru ve Temiz Veri**                |
|                                                  | **Bilgi Sınırlarını Belirleme**        |
|                                                  | **Daha İyi Yönlendirme Verileri**      |
| **2. Eğitimi Geliştirmek**                       | **Eğitim Süreçlerini Optimize Etmek**  |
|                                                  | **Akıllı Geri Bildirim Sistemleri**    |
| **3. Çıktı Üretme Mekanizmalarını İyileştirmek** | **Daha Akıllı Cevap Seçme Yöntemleri** |
|                                                  | **Harici Bilgilerle Destekleme (RAG)** |
|                                                  | **Cevapları Kontrol Etme**             |
|                                                  | **Daha İyi Düşünme Becerileri**        |

<figure>
    <img src="/assets/img/2025-07-13-llmleri-ve-halüsinasyonları-anlamak/chain.webp" alt="Chain-of-Thought Mimarisi" width="600">
    <figcaption>Görsel: Chain-of-Thought Mimarisi [10] .</figcaption>
</figure>

---

> "Bu büyük dil modelleri, bizlere hem bilginin sonsuzluğunu hem de yanılgının kaçınılmazlığını gösteriyor. Onlarla kurduğumuz diyalog, aslında kendi "doğruluk" arayışımızın bir yansımasıdır; geleceğin dijital dünyasında bilgelik, bu sorgulamadan doğacaktır."



# Kaynakça

1. [Memorial Sağlık Grubu - Halüsinasyon ve Varsanı Nedir?][1]  
2. [Lakera.ai - The Beginner’s Guide to Hallucinations in Large Language Models][2]  
3. [Google Cloud - Large Language Models powered by world-class Google AI][3]  
4. [Vaswani, A., et al. (2017). *Attention is all you need*. NeurIPS][4]  
5. [OpenAI — Understand Foundational Concepts of ChatGPT and cool stuff you can explore!][5]  
6. [Devlin, J., et al. (2018). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*][6]  
7. [Huang et al., 2024. _A Survey on Hallucination in Large Language Models_][7]  
8. [Understanding OpenAI’s “Temperature” and “Top_p” Parameters in Language Models][8]  
9. [Wei et al., 2023. *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*][9]  
10. [The Delegated Chain of Thought Architecture][10]  

[1]: https://www.memorial.com.tr/hastaliklar/halusinasyon-varsani-nedir-belirtileri-nelerdir
[2]: https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models
[3]: https://cloud.google.com/ai/llms
[4]: https://arxiv.org/abs/1706.03762
[5]: https://medium.com/@amol-wagh/open-ai-understand-foundational-concepts-of-chatgpt-and-cool-stuff-you-can-explore-a7a77baf0ee3#:~:text=OpenAI%20%E2%80%94%20Understand%20Foundational%20Concepts%20of%20ChatGPT%20and%20cool%20stuff%20you%20can%20explore!
[6]: https://arxiv.org/abs/1810.04805
[7]: https://doi.org/10.1145/3703155
[8]: https://medium.com/@1511425435311/understanding-openais-temperature-and-top-p-parameters-in-language-models-d2066504684f
[9]: https://arxiv.org/abs/2201.11903
[10]: https://lab.scub.net/the-delegated-chain-of-thought-architecture-5dd5ab9ca88e
