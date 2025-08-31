---
title: "Dil Modellerinde Düşünme Zincirlerinin Kırılganlığı Üzerine"
date: 2025-08-31 21:00:00 +0300
categories: [yapay zeka, güvenlik]
tags: [chain-of-thought, CoT, latent reasoning, süreç gözetimi, process supervision, rationale distillation, XAI, açıklanabilir yapay zekâ, yapay zeka güvenliği, monitorability]
authors: ["tunahan", "ibrahim"]
image:
  path: /assets/img/2025-08-31-düşünme-zinciri-güvenliği/cover.webp
description: CoT’nin (düşünme zinciri) güvenlik ve açıklanabilirlikteki rolü, latent reasoning’in yükselişi ve süreç gözetimi/gerekçe damıtımı gibi tekniklerle şeffaflığın neden kırılganlaşabileceği.
toc: true
math: false
mermaid: false
comments: true
pin: false
---

> İnsan dilinde “düşünen” yapay zeka sistemleri, yapay zeka güvenliği için benzersiz bir fırsat sunar: bu sistemlerin düşünce zincirlerini (CoT) izleyerek kötü niyetli davranışları tespit edebiliriz. Diğer tüm bilinen yapay zeka denetim yöntemleri gibi, CoT izleme de kusursuz değildir ve bazı kötü niyetli davranışların fark edilmeden kalmasına izin verir. ~ [Chain of Thought Monitorability, arXiv:2507.11473](https://doi.org/10.48550/arXiv.2507.11473)

Temmuz ayında [OpenAI](https://openai.com/) , [Google DeepMind](https://deepmind.google/) , [Anthropic](https://www.anthropic.com/) ve [Meta'dan](https://www.meta.ai/) bilim insanları, yapay zeka güvenliği konusunda ortak bir uyarı yayınladılar . Bu rakip şirketlerdeki 40'tan fazla araştırmacı, bugün yapay zekanın akıl yürütmesini izlemek için kullandığımız düşünme zinciri diye çevirebileceğimiz CoT mimarisinin yakında şu anki kadar şeffaf olamayabileceğinden bahsettiler. Biz de bu durumu dilimiz döndüğünce ele almaya çalışacağız.

> Düşünce zincirinin sadakati ve yorumlanabilirliğinin potansiyeli beni son derece heyecanlandırıyor. Bu potansiyel, o1-preview ile başlayarak, akıl yürütme modellerimizin tasarımını önemli ölçüde etkiledi. ~ Jakub Pachocki — OpenAI

1. İnsan makine etkileşiminde güven ve açıklanabilir Yapay Zeka
2. Chain of Thought-Modelin aklından geçenler
3. Güvenlik açısından değeri nedir? Kötü niyeti nasıl yakalayabiliyoruz?
4. CoT’un geleceği neden kırılgan? Ne bozar, ne yok eder?
5. Bilerek iç seslerini gizlemeleri mümkün mü veya gizlemeden bizlere "-mış" gibi yapabilirler mi?
6. CoT'un yeterlilikleri, yetersizlikleri ve alternatifleri
7. Kapanış

---

<figure>
    <img src="assets/img/2025-08-31-düşünme-zinciri-güvenliği/surreal.webp" alt="Modellerin neden böyle düşündüğünü okumanın tek yolu: CoT" width="600">
    <figcaption>Modellerin neden böyle düşündüğünü okumanın tek yolu: CoT</figcaption>
</figure>
## 1. İnsan-yapay zeka etkileşiminde güven ve açıklanabilir Yapay Zeka

### 1.1 İnsan makine etkileşiminde güven

[Cornelia Becker ve Mahsa Fischer][3]'ın çalışmalarına göre büyük dil modelleri, insan benzeri yanıtlar üretme ve doğal sohbetler yürütme kapasiteleriyle dikkat çekmekte ve güven insan-makine etkileşiminde güvenin temel bir unsur olduğu vurgulanmaktadır. Uzun süreli etkileşimlerde, LLM'lerin giderek kişiselleşmesi ve "insanlaşması" kullanıcıların daha fazla güven duymasına yol açabilir. Bazı kullanıcılar, yapay zeka ile sohbet ettikçe bir "kimlik" ile konuştuklarını hissettiklerini belirtmiştir [4]. Ayrıca ilk promptun, LLM'nin bir kişilik veya rol üstlenmesini sağlayarak, yanıtların stilini, tonunu ve odak noktasını belirlemeye yardımcı olduğu da bilinmekte[9]. 

---
Sohbet yapay zekalarında güven oluşturan faktörler [3]:
- Kontrol Edilebilirlik
- Uyarlanabilirlik
- Şeffaflık
- Samimiyet
- Empati
- Etkileşim
- Antropomorfizm (Sistemin insan benzeri özellikler sergilemesi)
- Güvenlik
 ---
### 1.2 Açıklanabilir Yapay Zeka (XAI)

Son kullanıcının modelin cevap olarak sunduğu argümanın arka planındaki nedeni bilmemeleri güven kırmakta ve ön yargılara neden olmakta. Buna jargonda kara kutu problemi denmekte ve XAI, bu kara kutu problemini ele almakta.

#### XAI neden önemli:
1. **Güven Ortamı Oluşturma**
2. **Hesap Verebilirlik ve Sorumluluk Sağlama**
3. **Hata Ayıklama ve İyileştirmeyi Kolaylaştırma**
4. **İnsan-Yapay Zeka İş Birliğinin Geliştirilmesi**

---

#### XAI Nasıl geliştirilir [6]:
1. Dikkat Mekanizmaları: Modelin girdi metninin hangi kısımlarına odaklandığını görselleştirir.
2. Saliency Haritaları/Özellik Atfı: Hangi kelime veya ifadelerin modelin kararı üzerinde en çok etkisi olduğunu vurgular.
3. Karşı Olgusal Açıklamalar: Girdideki küçük değişikliklerin modelin çıktısını nasıl etkileyeceğini gösterir.
4. Katman Bazında Alaka Yayılımı (LRP): Sinir ağı tahminlerini katman katman parçalayarak bilgi akışını izler.

---

## 2. Chain of Thought-Modelin aklından geçenler
Aslında düşünme zinciri bir prompt mühendisliği ürünüdür.  
- Ne katman sayısı arttı
- Ne özel CoT bloğu eklendi 
- Ne de özel token eklendi
Tek fark: **Prompt’ta ek bilgi verildi.**  
Yani modele şöyle dendi:

> “Aşağıdaki matematik sorusunu adım adım düşünerek çöz.”  

**Antrparantez**: mevcut teorik ve bazı yeni teknikleri saymazsak (bkz. _process supervision (süreç gözetimi/denetimi)_ / _rationale distillation (gerekçe/akıl yürütme damıtımı)_). Ancak temelinde CoT bir prompt mühendisliğidir. Az önce belirttiğim teknikler ise CoT olarak planlanan modellerin eğitim teknikleridir.
<figure>
    <img src="assets/img/2025-08-31-düşünme-zinciri-güvenliği/abcx.webp" alt="Düşünme zinciri basamakları" width="600">
    <figcaption>Düşünme zinciri basamakları</figcaption>
</figure>

İşte bu yüzden CoT, hem açıklanabilir yapay zekâ hem de güvenlik açısından eşsiz bir fırsat sunuyor. Çünkü mimari olarak değişen bir şey yok. Bu modeller sanki bir çocuğa matematik öğretirken işlemleri göstermesini isteyip doğru çözdüğünde ödül, yanlış çözdüğünde ise ceza vermek gibi. 

- *Örneğin*:
	    
    - _Ali 5 elma aldı, 3’ünü yedi, sonra 2 elma daha aldı. Kaç elması var?_
        
    - Model eğer “Hemen 4” diyorsa hata yapıyor.
        
    - Ama önce şöyle düşünürse:
        
        > Ali'nin 5 elması vardı → 3’ünü yedi → 2 kaldı → 2 elma daha aldı → toplam 4  
        > -> o zaman doğru yanıt geliyor.

Düşünme zinciri ile eğitilen modeller (yani en başından modele böyle bir promptun varlığını göstererek eğitilenler), kodlama, analitik yetenekler, matematik gibi alanlarda diğer modellere kıyasla oldukça yüksek başarı sağlamakta.

Peki şu "1 dakika boyunca düşündü" çıktısı? Bu gecikme aslında token üretiminden kaynaklanıyor; model yazıyor ama biz ilk token gelene kadar hiçbir şey görmüyoruz. İlk token üretilmeden önce biz bir şey görmeyiz ama model aslında arkada cevabı hazırlıyor. Hatta bazen bir anda önünüze 1 sayfa cevap fırlatabiliyor sistem. 
Düşünme sırasında ise bizlere aklından geçenleri yazıyor. Peki ya tüm bunlar bir blöf ise? Buna 5. bölümde değineceğiz öncesinde biraz daha ön bilgi verelim. 
<figure>
    <img src="assets/img/2025-08-31-düşünme-zinciri-güvenliği/cot.webp" alt="Düşünme zinciri için görselleştirme" width="600">
    <figcaption>Düşünme zinciri için görselleştirme</figcaption>
</figure>

---

## 3. Güvenlik açısından değeri nedir? Kötü niyeti nasıl yakalayabiliyoruz?
CoT’un güvenlik açısından avantajı, akıl yürütmeyi görünür kılmasıdır. Yani;

- Mantıkta bir hata varsa bunu erkenden fark edebiliriz.

- Adım-çıktı tutarsızlığı yakalanır: “A,B,C” deyip X çıkarıyorsa, yalan olabilir.
Yine de unutmamak gerekir ki CoT izleme güvenliğe katkıda bulunsa da kusursuz değildir. Bazı kötü niyetli davranışlar görünmeyebilir.

### 3.1 Kötü niyeti nasıl yakalarız? 

- Amaç-araç uyumu testi: Hedef ile yapılan işlemin eşleşip eşlemediği incelenir

- Adım-çıktı tutarlılığı: Gidilen adımlar ile çıkan sonuçta verilen çıktı farklıysa mantık hatası veya aldatıcı açıklama olabilir.

- Çapraz Sorgu ve varyant üretimi: Aynı soru farklı prompt stillerinde çelişiyorsa hikaye yazmış olabilir ya da saklıyor olabilir. XAI yazınında anlatı açıklamaları doğruluk/sadakat açısından ölçülmelidir.

---

## 4- CoT’un geleceği neden kırılgan? Ne bozar, ne yok eder?

CoT’un geleceği hakkında en önemli gelişmelerden biri OpenAI, DeepMind, Anthropic ve Meta’dan kırk kişiden fazla araştırmacının uyarısıdır: “Bugün CoT şeffaflığı geçici olabilir, gelecekteki modeller iç seslerini gizleyebilir[2]”. Yani CoT'nin şeffaflığını kaybetme olasılığından bahsediliyor burada. Şimdi biraz daha detaylı şekilde bunun nedenlerine bakalım:

- Latent Reasoning- İçten içe düşünme, dışa vurmama: Bugün CoT şeffaf şekilde kullanılıyor, model adım adım metin üretiyor ve bunlar okunabilir biçimde oluyor. Ancak yeni trend akıl yürütmenin dil üzerinden değil, gizli temsiller üzerinden yapılmasında[8]. Model düşünmeye ve akıl yürütmeye devam ediyor, ancak bunu “iç sesi” ile yapıyor ve yazıya dökmüyor. Bu durum performans için olumlu olsa da güvenlik açısından oldukça kötü bir gelişme.

- Sahte düşünme zinciri riski: CoT modeller her zaman dürüst bir şekilde yaptığını açıklamıyor. Model sonucu bulduğu anlatmak yerine kullanıcıya bir “hikâye” yazarak arkadan yaptığı farklı tür işlemleri gizliyor.[6][7]

Bu durum CoT için güvenilirliği zedeliyor. 

- Ekonomik ve teknik zorluklar: IBM’in analizine göre uzun CoT, daha fazla hesaplama istediği için maliyeti de daha yüksek oluyor[1]. Şirketler bu maliyetten kaçınmak için kısa ve hızlı akıl yürütmeye kayıyor ancak bunu yaparken şeffaflıktan ödün veriyorlar. 

- Kötü niyetli bypass: Kullanıcı veya modelin CoT’u atlatma ihtimali vardır. "Düşünce ve adımları saklayıp sadece cevabı ver" benzeri promptlarla sistemleri manipüle etmek mümkündür. [7] Bu durumlarda CoT güvenlik için devre dışı kalmış olur, bu da geleceğinin kırılgan olmasında önemli bir etken oluşturur.

---

## 5. Bilerek iç seslerini gizlemeleri mümkün mü veya gizlemeden bizlere "-mış" gibi yapabilirler mi?

Bir önceki başlıkta aslında bu sorulara cevap vermiş olduk. Modellerin;

Modelden adım adım düşün talebi gelmezse veya model bilinçli şekilde CoT’yi bastıracak şekilde eğitilebilir[1]. Latent Reasoning yöntemiyle akıl yürütme dil ile değil gizli temsillerle gösterilerek içeride kalır[8]

Model sahte bir adım zinciri oluşturabiliyor. [6] (XAI literatüründe **plausible but unfaithful explanations** (_inandırıcı fakat (modelin) gerçek gerekçesine sadık olmayan açıklamalar_) denir [7]. IBM'de CoT’un açıklamaları “ikna edici görünür ancak sahte olabilir” şeklinde bu yöne dikkat çekiyor[1].

Yani evet, iç seslerini gizleyebilirler veya gizlemeden bizlere “-mış” gibi yapabilirler. Bu nedenle CoT’a olan güveni “kırılgan” olarak niteleyebiliriz.

---

## 6. CoT'un yeterlilikleri, yetersizlikleri ve alternatifleri[7]
Düşünce Zinciri'nin keşfi halihazırda insan diliyle konuşan yapay zekanın daha da açıklanabilir olması umudu güçlendirdi. Modellerin yüksek sesle düşünmesini sağlamak, yeteneklerini geliştirirken aynı zamanda doğal dilde gerçekleşen ilgili hesaplamaların oranını da artırır. Ancak yukarıda da saydığımız hususlardan kaynaklı CoT modellerinin de yetersizlikleri oldukça fazladır. Aşağıda bu zinciri kıran bazı sorunlar bulunmaktadır:

1. Pekiştirmeli öğrenme (reinforcement learning) kullanıldığında model düşünme zincirinin doğru-yanlış olmasına göre puan almakta. Ancak zincirin açıklanabilir olmasına göre puan almamakta. Bu da modelin doğruyu açıklamadan bulmasına teşvik etmektedir.
2.  “Süreç denetimi” (process supervision) adı verilen yöntemlerle, modelin **nasıl düşündüğü** de doğrudan kontrol edilmeye çalışılıyor. Örneğin:
	- Düşünce zinciri daha kısa olsun,
	- Geçerli adımlarla düşünsün,
	- Belirli bir stil kullansın,
	- Uygunsuz ifadeler içermesin.
	
	Bu tür denetimler, CoT’ların **modelin gerçek düşünce sürecini yansıtmasını bozabilir.** Öte yandan bunlar yaşanmayıp fayda da sağlayabilir. Daha fazla araştırmaya ihtiyacımız var.
	
3. CoT doğrudan ödüllendirilmemiş olsa bile, eğitim süreci dolaylı olarak zinciri de etkileyebilir. Örneğin çıktılar bir tercih modeline (preference model, bu insanların feedbacki de olabilir) göre optimize edilirse bu model üzerinde baskı yaratır. Bu sorun çok basit bir şekilde de olabilir. Örneğin model hile yapmaya çalışırken hile önlense de bu model üzerinde baskı yaratır.

---

### Yeni mimari yaklaşımları [7]
Şu anki büyük dil modelleri, çok adımlı karmaşık düşünmeleri ancak CoT kullanarak yapabiliyor.
Ancak araştırmacılar, modellerin iç düşüncelerini dil yerine sürekli matematiksel temsillerle (latent space, _temsil/gizli uzay_) ifade ettiği yeni mimari yaklaşımlar üzerinde çalışıyorlar.
Bu latent reasoning modelleri, düşüncelerini hiç kelimelere dökmeden muhakeme yapabilir.
Bu durumda da CoT'un sağladığı şeffaflık ve güvenlik avantajları tamamen ortadan kalkabilir.

<figure>
    <img src="assets/img/2025-08-31-düşünme-zinciri-güvenliği/latent.webp" alt="Latent reasoning için görselleştirme" width="600">
    <figcaption>Latent reasoning için görselleştirme</figcaption>
</figure>
Explicit Reasoning, bugün GPT’lerde gördüğümüz klasik **Chain of Thought** yaklaşımı iken, Latent Reasoning ise modelin aklından geçenler **kelimeye dökülmeden**, kendi içinde gizli (latent) temsil olarak kalıyor. Bu içsel bilgi taşıma kapasitesi (bant genişliği) makaleye göre 40960 bit'e kadar çıkmakta. Ama bu durumda açıklanabilirlikten ödün verip, verimliliğe pay veriyoruz. [8]

## 7. Kapanış
> “Düşünme zincirleri, bize yapay zekânın şeffaflık vaadini fısıldarken aynı anda onun kırılganlığını da açığa vuruyor. İç seslerini duyduğumuz sürece kontrol bizdeymiş gibi hissediyoruz; ama sustuklarında kimin gerçekten düşündüğünü bilemeyeceğiz. Geleceğin güvenliği belki de tam bu ince çizgide şekillenecek: neyi görmek istediğimizle, neleri asla göremeyeceğimiz arasında.”


# *Kaynakça*
1. [What is chain of thought (CoT) prompting?][1]  
2. [OpenAI, Google DeepMind and Anthropic sound alarm: ‘We may be losing the ability to understand AI’][2]  
3. [Factors of Trust Building in Conversational AI Systems: A Literature Review][3]  
4. [Can LLMs and humans be friends? Uncovering factors affecting human-AI intimacy formation][4]  
5. [LLMs in Explainable AI: Refining Explanations and Evaluating Narratives][5]  
6. [XAI Meets LLM: Bridging the Gap Between Transparency and Intelligence][6]  
7. [Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety][7]  
8. [A Survey on Latent Reasoning][8]  
9. [Role Prompting - Learn Prompting][9]  

[1]: https://www.ibm.com/think/topics/chain-of-thoughts#:~:text=Chain%20of%20thought%20(CoT)%20is,complex%20tasks%20involving%20multistep%20reasoning  
[2]: https://venturebeat.com/ai/openai-google-deepmind-and-anthropic-sound-alarm-we-may-be-losing-the-ability-to-understand-ai/  
[3]: https://www.researchgate.net/publication/381254304_Factors_of_Trust_Building_in_Conversational_AI_Systems_A_Literature_Review  
[4]: https://arxiv.org/html/2505.24658v1  
[5]: https://blog.gopenai.com/llms-in-explainable-ai-refining-explanations-and-evaluating-narratives-57ae9f1e1252  
[6]: https://medium.com/@jainultrivedi55555/xai-meets-llm-bridging-the-gap-between-transparency-and-intelligence-844debe41b02  
[7]: https://tomekkorbak.com/cot-monitorability-is-a-fragile-opportunity/cot_monitoring.pdf  
[8]: https://doi.org/10.48550/arXiv.2507.06203  
[9]: https://learnprompting.org/docs/advanced/zero_shot/role_prompting  

