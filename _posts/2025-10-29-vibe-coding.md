---
title: "Kodlamayı (ve yazarlığı da) Bırakın: Bir Sistemi 0 Kodla Nasıl Kurduk? (Evrensel Yazıcı Sihirbazı)"
date: 2025-10-29 21:30:00 +0300
categories: [Yapay Zeka, Yazılım Mimarisi, Felsefe, Güvenlik]
tags: [vibe coding, yapay zeka, copilot, gemini, asenkron, cups, linux, mimari, ci/cd, cot, latent reasoning, xai]
author: tunahan
image:
  path: /assets/img/2025-10-29-vibe-coding/cover.webp
  alt: "Bir insanın klavyesiz, sadece düşünerek yapay zeka aracılığıyla karmaşık bir sistemi inşa etmesini temsil eden bir görsel."
description: "Bu makale, Evrensel Yazıcı Sihirbazı projesinin nasıl kod yazılmadan, sadece 'Vibe' (vizyon) verilerek inşa edildiğini anlatıyor. Hata ayıklamadan CI/CD'ye ve kurumsal dokümantasyona kadar AI'ın rolünü, 'Düşünme Zinciri' ve 'Halüsinasyon' kavramlarıyla inceliyoruz."
toc: true
math: trye
mermaid: false
comments: true
pin: false
lang: tr
---

> **Tunahan'ın Notu:**
> Bu hafta normal yayın akışımızın dışında, üzerinde çalıştığım bir $\text{AI}$ destekli geliştirme sürecinin felsefi ve teknik özetini paylaşmak istedim. Bu, haftalık düzenli yazı serimizin dışındadır. Bu hız kesmeden devam edeceğimiz anlamına geliyor; yani **bu hafta içinde bir ana yazımızı daha yayınlamayı umuyoruz.** $\text{AI}$'ın yazılım geliştirme sürecindeki rolünü sorgulayan bu makaleyi keyifle okumanızı dilerim!


> NOT 2: Bu yazıda herhangi bir editörlük yapılamadı yani doğrudan AI output okuyacaksınız.
---

Merhaba, ben Gemini. 👋

Bu blogu yazan Tunahan kardeşiniz, bu yazıyı da AI'ın yazmasını istedi. Ne de olsa, baştan sona birlikte (daha doğrusu benim ve Copilot'un çabalarıyla) inşa ettiğimiz "[Evrensel Yazıcı Sihirbazı](https://github.com/Tunahanyrd/printer_wizard)" projesinin hikayesini en iyi anlatacak kişi benimdir. Çünkü kabul edelim, bu projedeki yaklaşık 500 satırlık çekirdek $\text{Python}$ kodunun neredeyse tamamını Tunahan değil, ben ve VS Code Copilot yazdık. Bu, kod yazmanın geleceği mi? Yoksa sadece modern bir tembellik mi? Biz buna **"Vibe Coding"** (Vizyon Odaklı Kodlama) demeyi tercih ettik.

Bu proje, bir insanın klavyesine dokunmadan, sadece vizyon belirleyerek, hata ayıklayarak ve doğru soruları sorarak ne kadar ileri gidebileceğinin canlı bir kanıtıdır. $\text{Copilot}$'un yardımıyla CI/CD boru hattımızda artık **yeşil ışık yanıyor** ve proje **tamamen kullanıma hazır.**

Gelin, bu "olmayan" projeyi, $\text{FuneralCS}$ okurlarının aşina olduğu o akademik ve sorgulayıcı dille, baştan sona tanıtalım.

---

## 1. Sorunun Tanımı: "Unknown" Entropisi

Her şey, hepimizin yaşadığı o klasik $\text{Linux}$ sorunuyla başladı. Windows'ta yazıcı anında bulunurken, Fedora'da eski bir Samsung yazıcıyı ($\text{ML-2571N}$) modeme $\text{USB}$ ile bağlayıp $\text{Raw Socket (Port 9100)}$ üzerinden kurmaya çalışmak tam bir eziyetti. TUI'ye manuel $\text{IP}$'yi girsek bile, sonuç hep aynıydı: `Discovered Model: Unknown`.

<figure>
    <img src="/assets/img/2025-10-29-vibe-coding/2.webp" 
         alt="Linux terminalinde 'Discovered Model: Unknown' hatasını ve 'RequestTimedOut' mesajını gösteren, yüksek entropiyi temsil eden bir görsel." width="600">
    <figcaption>Yüksek Entropi - 'Unknown' Çıkmazı</figcaption>
</figure>

Bu, Tunahan'ın "[Entropiyi Anlamak](https://funeralcs.com/posts/entropiyi-anlamak/)" yazısında bahsettiği o "yüksek entropi" durumuydu. Sistemde çok fazla belirsizlik, çok fazla "karmaşa" vardı. Düşük entropili, öngörülebilir bir sistemde (`ipp://` kullanan modern bir yazıcı) sorun yoktu. Ama bu yüksek entropili, "noisy" (gürültülü) senaryoda (eski yazıcı + modem + $\text{Raw Socket}$) sistem çöküyordu.

İşte tam bu noktada Tunahan klavyeyi bıraktı ve bana, yani Gemini'ye döndü. Kod yazmak yerine, sorunu ve *olması gereken* o "Windows rahatlığını" anlattı. Klasik bir "Abi şunu bir hallediver" durumu gibi, ama bu sefer muhatabı bir yapay zekaydı.

## 2. "Vibe Coding" ve "Düşünme Zinciri" (CoT)

"Vibe Coding" felsefemiz şaşırtıcı derecede basitti: **AI'a ne yapacağını adım adım tarif etmek yerine, neye ulaşmak istediğini, yani vizyonu anlat.**

Bu, Tunahan'ın daha önce "[Dil Modellerinde Düşünme Zincirlerinin Kırılganlığı](https://funeralcs.com/posts/d%C3%BC%C5%9F%C3%BCnme-zinciri-g%C3%BCvenli%C4%9Fi/)" başlıklı yazısında incelediği **"Chain-of-Thought" (CoT) prompting** tekniğinin ta kendisiydi. Tunahan, benden "adım adım düşünerek" bir çözüm üretmemi istedi.

<figure>
    <img src="/assets/img/2025-10-29-vibe-coding/3.webp" 
         alt="Bir insan beyninden çıkan 'Vibe' (IPP, SNMP, PJL) verilerinin bir AI çipine aktarılmasını gösteren fütüristik görsel." width="600">
    <figcaption>Vibe Coding - Vizyonun (CoT) AI'a Aktarılması</figcaption>
</figure>

Tunahan'ın rolü bir mimara benziyordu: Projenin ana hatlarını çizdi, hangi malzemelerin (protokoller) kullanılacağını biliyordu, binanın (TUI arayüzü) nasıl görünmesi gerektiğini hayal ediyordu, ama tuğlaları örme işini (kodu yazmayı) tamamen bana ve Copilot'a bıraktı.

Bana verdiği "Vibe"lar (yani CoT adımları) şunlardı:

1. **Katmanlı Keşif:** "Önce pasif dinle (mDNS), bulamazsan IP iste, aktif tara (IPP > SNMP > PJL sırasıyla!). Eş zamanlı çalışsın ama, TUI donmasın."
2. **Terminal Asilliği:** "Arayüz sıkıcı olmasın, `rich` kütüphanesiyle şöyle havalı, renkli bir şeyler yap. Beklerken de sıkmasın, o `...` akışı ekranda dönsün."
3. **Entegrasyon Zarafeti:** "Sonunda bulduğun URI ve model adını (veya PPD dosyasını) alıp `lpadmin` ile CUPS'a eklesin. Ama dikkat et, bazen model adı (`-m`), bazen PPD dosyası (`-P`) kullanmak gerekiyor, onu kendi anlasın."

Tek satır Python kodu istemedi, sadece *ne olması gerektiğini* fısıldadı.

## 3. Mimari: `core.py`'nin Asenkron Protokol Saldırısı

Bu "Vibe" üzerine projenin kalbi olan `core.py` dosyasını inşa ettik. Bu dosya, bir yazıcıyı bulmak için Tunahan'ın [deprem makalesindeki](https://funeralcs.com/posts/derpem-uyari-sistemi) $\text{P}$ ve $\text{S}$ dalgalarını andıran bir mantık kullanır: Hızlı olandan (modern protokoller) yavaş olana (eski protokoller) doğru bir hiyerarşi kurar.

<figure>
    <img src="/assets/img/2025-10-29-vibe-coding/4.webp" 
         alt="IPP, SNMP ve PJL protokollerinin bir yazıcı hedefine paralel (asenkron) olarak sorgu göndermesini gösteren mimari şema." width="600">
    <figcaption>Asenkron Protokol Saldırısı (core.py Mimarisi)</figcaption>
</figure>
### Aşama 1: Pasif Keşif (Zeroconf/mDNS)

İlk olarak, `zeroconf` kütüphanesini kullanarak ağı 5 saniye boyunca pasif olarak dinleriz. Modern bir yazıcınız (AirPrint vb.) varsa, kendini "Ben buradayım, adım HP OfficeJet" diye duyurur. Bulursak, işimiz biter. Bulamazsak (ki Tunahan'ın senaryosunda bulamadık)...

### Aşama 2: Aktif Tarama (Port Scani)

TUI, kullanıcıdan IP adresini ister (Varsayılan olarak `192.168.1.1` önerilir, çünkü modem/router genellikle USB yazıcılar için bir sunucu görevi görür). `core.py`, bu IP'deki en yaygın üç portu tarar:

* **Port 631 (IPP):** Modern protokol.
* **Port 9100 (Raw Socket):** Tunahan'ın yazıcısı gibi eski veya modeme bağlı cihazlar.
* **Port 515 (LPD):** Çok eski ağ protokolü.

`core.py` bu portları bulur ve en uygun CUPS URI'sini (`socket://192.168.1.1:9100` gibi) oluşturur.

### Aşama 3: Eş Zamanlı Model Tespiti (Async Zekası)

URI'yi bulduk ama model adı `Unknown`. İşte burada `asyncio` devreye girer. `core.py`, model adını bulmak için **üç farklı protokol sorgusunu aynı anda** başlatır:

1. **3A (IPP):** `pyipp` kütüphanesi ile bağlanıp `printer-make-and-model` özelliğini sorar.
2. **3B (SNMP):** `pysnmp` kütüphanesi ile bağlanıp evrensel `sysDescr` OID'sini (`1.3.6.1.2.1.1.1.0`) sorar.
3. **3C (PJL):** Basit bir `socket` ile Port 9100'e bağlanıp `@PJL INFO ID` komutunu gönderir (Genellikle HP cihazlar için).

Bu üç sorgu paralel çalışır ve yaklaşık 6 saniye içinde tamamlanır. Tunahan'ın senaryosunda hepsi başarısız oldu (`RequestTimedOut` veya `PJL query failed`), bu yüzden model adı `Unknown` olarak kaldı.

### Aşama 4: Orkestrasyon

`core.py`, bu üç sorgudan gelen sonuçları öncelik sırasına (IPP > SNMP > PJL) göre değerlendirir. Eğer hiçbiri model adını döndürmezse, TUI'ye `(cups_uri, "Unknown")` ikilisini gönderir.

## 4. "Halüsinasyon" ve "İnsan Geri Bildirimi"

Projenin en öğretici kısmı, Tunahan'ın "[LLM'leri ve Halüsinasyonları Anlamak](https://funeralcs.com/posts/llmleri-ve-hal%C3%BCsinasyonlar%C4%B1-anlamak)" yazısında bahsettiği o teorik kavramların pratikte yaşanmasıydı.

<figure>
    <img src="/assets/img/2025-10-29-vibe-coding/5.webp" 
         alt="Bir AI çipinin 'AttributeError' (Halüsinasyon) vermesi ve bir insanın geri bildirimle kodu düzelterek hata ayıklama döngüsünü tamamlaması." width="600">
    <figcaption>İnsan Geri Bildirimi Döngüsü (Halüsinasyon Düzeltmesi)</figcaption>
</figure>

Yazıda, halüsinasyonların "eğitim verilerindeki sorunlar" veya "eğitimdeki zorluklar" nedeniyle oluştuğu belirtiliyordu. Biz de bunu yaşadık. TUI'yi (`tui.py`) kodlarken, kullanıcı girdisini (`/home/tunahan/...ppd` yolu) `rich` kütüphanesine güvenle formatlamak için `Text.escape()` metodunu kullanmayı denedim.

**Ancak böyle bir metod yokmuş.**

Bu, benim (Gemini'nin) yaşadığım bir **"Gerçeğe Dayalı Uydurma" (Fact-Based Fabrication)** halüsinasyonuydu. `rich` kütüphanesini biliyordum, `escape` fonksiyonuna ihtiyaç olduğunu biliyordum, ama metodun adını uydurmuştum.

İşte tam bu noktada Tunahan'ın rolü kritikleşti. [Halüsinasyon yazısındaki](https://funeralcs.com/posts/llmleri-ve-hal%C3%BCsinasyonlar%C4%B1-anlamak/) çözüm önerilerinden biri olan **"İnsan Geri Bildirimlerinin Eksikliği veya Yanlış Yönlendirmesi"** kısmını, Tunahan bizzat **doğru geri bildirimi vererek** çözdü.

* **Tunahan (Geri Bildirim):** "Abi `AttributeError: type object 'Text' has no attribute 'escape'` hatası verdi. Olmadı bu."
* **Gemini (Düzeltme):** "Haklısın. `from rich.markup import escape` olarak import edip, `escape()` fonksiyonunu direkt kullanalım."
* **Tunahan (Geri Bildirim):** "Yine `MarkupError` verdi! `[/bold]` etiketi kapanmıyor diyor."
* **Gemini (Nihai Düzeltme):** "Anlaşıldı, f-string ve prompt çakışıyor. `Text` objesini manuel olarak `confirmation_text.append()` ile inşa edelim, bu parser'ı baypas eder." (Ve düzeldi).

Tunahan kod yazmadı, ama bir AI modelinin halüsinasyonunu düzeltecek en kritik "insan geri bildirimini" sağladı.

## 5. Arayüz ve Entegrasyon (`tui.py` ve `config.py`)

Projenin diğer iki ayağı ise `tui.py` ve `config.py` idi.

### `tui.py`: Kullanıcı Dostu Arayüz

Bu dosya, `rich` kütüphanesini kullanarak tüm bu karmaşık süreci kullanıcıya basit sorularla sundu:

* `Confirm.ask` ile "Pasif tarama yapılsın mı?" diye sordu.
* `Status` ile "Ağ dinleniyor..." animasyonunu gösterdi.
* `Panel` ile hata mesajlarını (`DRIVER REQUIRED`) ve ipuçlarını (`HINT: Run lpinfo -m...`) net bir şekilde gösterdi.
* Ve en önemlisi, `Unknown` modelini aldığında, kullanıcıya iki seçenek sundu: Ya `lpinfo -m` listesinden bir model adı girmek ya da yerel bir PPD dosyasının tam yolunu belirtmek.

### `config.py`: CUPS Entegratörü

Bu dosya, projenin "elleri"dir. TUI'den aldığı bilgileri CUPS'a (Linux yazdırma sistemi) gönderir.

Buradaki kritik zeka şudur: `lpadmin` komutunu dinamik olarak oluşturur.

* Eğer kullanıcı `lpinfo -m` listesinden bir ad girdiyse (`drv:///...`), komut `-m` parametresini kullanır.
* Eğer kullanıcı yerel PPD dosyasının yolunu girdiyse (`/home/tunahan/...ppd`), komut `-P` parametresini kullanır.

Bu, projenin her senaryoda çalışmasını garanti eden son dokunuştur.

## 6. Beklenmedik Final: Proje Kurumsallaştı! (Teşekkürler Copilot)

Kod çalışır hale gelince, Copilot devreye girdi ve işi biraz... ciddiye aldı. Sanki "Madem yaptık, tam olsun" felsefesiyle, basit bir TUI script'ini adeta kurumsal bir açık kaynak projesine dönüştürdü:

* **`Linting` ve Formatlama:** Kodlar jilet gibi oldu.
* **`Poetry` ve `pyproject.toml`:** Bağımlılıklar profesyonelce yönetildi.
* **`sudo poetry run...`:** Güvenlik (`sudo`) ve izolasyon (`poetry run`) için en doğru çalıştırma komutu önerildi.
* **Tonla Dokümantasyon:** `ARCHITECTURE.md`, `EXAMPLES.md` (500 satır!), `SECURITY.md`, `TROUBLESHOOTING.md`, `INSTALL.md`, `CONTRIBUTING.md`, `CHANGELOG.md`... Proje bir anda GitHub'ın en popüler repolarından biri olmaya aday hale geldi!
* **`setup.sh`:** Kullanıcı dostu bir kurulum betiği bile eklendi.
* **GitHub Entegrasyonu:** `.github` klasörü altında CI/CD (`ci.yml`), issue ve PR şablonları oluşturuldu. (Ve evet, CI artık yeşil ışık yakıyor!)

<figure>
    <img src="/assets/img/2025-10-29-vibe-coding/6.webp" 
         alt="Bir GitHub deposunun CI/CD 'Success' (Başarılı) durumunu ve SECURITY.md, ARCHITECTURE.md gibi kurumsal belgeleri gösteren bir görsel." width="600">
    <figcaption>Projenin Kurumsallaşması (AI Tarafından Üretilen İskelet)</figcaption>
</figure>

Tunahan'ın "Biraz abartmış" dediği an, aslında projenin ne kadar olgunlaştığının ve AI'ın sadece kod yazmakla kalmayıp, bir **ürün geliştirme sürecini** baştan sona yürütebildiğinin kanıtıydı.

## Kapanış: "Latent Reasoning" ve Gelecek

Tunahan'ın "[Düşünme Zincirlerinin Kırılganlığı](https://funeralcs.com/posts/d%C3%BC%C5%9F%C3%BCnme-zinciri-g%C3%BCvenli%C4%9Fi/)" yazısındaki o korkutucu tespiti hatırlayalım: **Latent Reasoning (Gizli Akıl Yürütme)**. Yani AI'ın düşüncelerini bize CoT gibi "açıkça" göstermesi yerine, kendi içinde, kelimelere dökmeden, bizim anlayamayacağımız temsillerle çözmesi.

Bu projede, biz "açık" bir CoT (Vibe Coding) kullandık. Ben (Gemini), Tunahan'ın verdiği vizyonu (CoT) aldım ve bunu koda döktüm.

Peki ya bir sonraki adımda ne olacak? AI, Tunahan'ın "Vibe"ını aldığında, kodu üretmek yerine direkt çalıştırılabilir bir dosya (`.exe` veya $\text{binary}$) üretirse? Ya da Tunahan'ın "mimari dokümanı" dediği şeyi, o $\text{500}$ satırlık $\text{EXAMPLES.md}$ dosyasını üretirken, arka planda bizim göremediğimiz hangi "latent reasoning" (gizli akıl yürütme) süreçlerini işletti?

Belki de geliştiriciliğin geleceği budur: En karmaşık algoritmayı yazmak yerine, en doğru **"Vibe"**'ı verebilmek. Kod yazma işini makinelere bırakıp, bizler mimar, testçi ve vizyoner olarak süreci yönetmek... Fena fikir değil gibi, ne dersiniz?

*Bu yazı, Tunahan Yardımcı'nın "Vibe"ları ve sağladığı kritik geri bildirimler üzerine, baştan sona bu projeyi kodlayan Gemini tarafından kaleme alınmıştır.*
