---
layout: page
title: PoE
permalink: /poe/  
order: 4         
noindex: true
lang: tr
---

Proof of Egg (PoE) Konsensüs Mekanizması ve Biyolojik Veri Kümelerinin Finansal Entegrasyonu

Özet (Abstract)

Proof of Egg (PoE), dağıtık konsensüsü soyut dijital kaynaklardan (iş/kapital) alıp doğada gerçekleşen, zamanla bağlı, kopyalanması zor biyolojik olaylara (yumurtlama) bağlayan melez bir protokoldür. Her yumurtlama olayı; çoklu duyumsal veriden elde edilen bir Biyometrik Hash (BioHash) ile blok başlığına bağlanır ve Distributed Ovum Ledger (DOL) adlı Merkle-benzeri bir veri yapısında saklanır. Liveness ve adil ödül dağıtımı, Proof of Care (PoC) adlı ikinci katmanda; bakım, stres, beslenme ve çevre metriklerinden türetilmiş bir “bakım skoru”yla desteklenir. Ağın yerel parası Yusufacoin (YSC), biyolojik üretim kıtlığını modellleyen bir yarılanma programına (10^5 yumurta blok/epoch) sahiptir. Doküman; sistem ontolojisi, matematiksel formülasyon, tehdit/gizlilik modeli, tokenomik, yönetişim ve yol haritasını detaylandırır.


---

0. Terimler, Kısaltmalar ve Semboller

Node: Ağa bağlı “tavuk” veya onu temsil eden gözetimli donanım modülü (bkz. EggScanner).

Egg Event (EE): Zaman damgalı, sensörce teyit edilmiş yumurtlama olayı.

BioHash: Çoklu biyometrik ölçümden türetilmiş, hata toleranslı, çarpışması zor öz-hash.

DOL: Distributed Ovum Ledger, Merkle/Verkle hibrit veri yapısı.

PoC: Proof of Care, çevresel-biyolojik bakım skoruna dayalı teşvik katmanı.

EQP / OFI: Egg Quality Score / Ovum Frequency Index.

FEV: Farmer Extractable Value (MEV’in çiftlikteki kuzeni).

EDA: Egg Difficulty Adjustment — biyolojik hız/temposu için hedef blok aralığı ayarı.

BAT: Biologically Anchored Time — biyolojik olaylara göre re-senkronize edilmiş zaman.


Semboller:

: . yumurta olayı

: zaman damgası (BAT referanslı)

: sensör çoklusu (spektral, topolojik, vb.)

:  için BioHash

:  sonrası YSC ödülü

: PoC bakım skoru

: hedef blok oranı (yumurta/saniye)

: kriptografik hash ailesi

: fuzzy extractor (hata toleranslı öznitelik standardizasyonu)



---

1. Giriş ve Motivasyon (Derinleştirilmiş)

Klasik DLT konsensüsleri yapay kaynaklara (iş, stake) yaslanır. PoE, doğal entropiyi (yumurtlama olayları) ekonomik bir oyuna dönüştürür: tavuğun fizyolojisi ve çevre bakımı hem kopyalanması zor hem de ölçeklenmesi sınırlı bir üretkenlik belirler. Amaç:

1. Enerji/karbon maliyetini düşürmek,


2. Çoklu-sensör ile tekilliği artan “olay blokları” üretmek,


3. Gerçek dünya verisi ile zincir güvenliğini konumlamak (oracle-tam entegrasyon).




---

2. Sistem Modeli ve Varsayımlar

2.1 Aktörler

Layer-0 Biyolojik Aktör: Tavuk (node).

Edge Donanımı: EggScanner (sensör füzyonu, imza modülü).

Doğrulayıcılar: DOL üzerinde blok doğrulayan düğümler (insan/gözetimli cihazlar).

Yönetişim Katılımcıları: YSC sahipleri + Tavuk Otoritesi (DAO) üyeleri.

Köprü/Ortaklar: DeFi, DEX, L2 rollup zincirleri.


2.2 Güven Varsayımları

Sensör zinciri çoklu imzalı ve donanım kök anahtarları güvenli.

Tek bir aktörün yüksek hacimde yumurta taklidi üretmesi ekonomik olarak pahalı ve kolay keşfedilebilir.

Ağ gecikmeleri sınırlı; biyolojik olaylar yaklaşık Poisson süreçleri gibi davranır (sadelik varsayımı).



---

3. BioHash Tasarımı

3.1 Duyumsal Modaliteler (yüksek seviyede)

Kabuk mikrotopolojisi: yüzey kabarıklık/çukurluk örüntüsü (temassız tarama).

Sarı/saydam spektral imza: geniş bant spektral reflektans/absorpsiyon ölçümü.

Protein katmanları için Raman imzası: karakteristik tepe noktaları.

Ağırlık/ölçü + akustik rezonans: kaba sınıf ayrımı destekleri.


> Not: Bu bölüm algoritmik/kriptografik olarak anlatılmakta; laboratuvar pratiği için herhangi bir adım, oran, kimyasal prosedür veya deney protokolü verilmiyor.



3.2 Fuzzy Extractor & Özellik Vektörü

Ham duyum  → öznitelik vektörü .
Hata-tolerans için fuzzy extractor:

(\mathsf{BH}_i, \mathsf{help}_i) = \mathsf{FEx}(\mathbf{x}_i)

 sadece yeniden-üretilmeye yardım eden, gizlilik sızdırmayan yardımcı veri.


3.3 BioHash Kararlılığı ve Entropi

Minimum min-entropi: .

Çarpışma olasılığı  (sensör bağımlı ).

Rekonstrüksiyon: aynı yumurta üzerinde tekrar ölçüm →  tekrarlanabilirliği; farklı yumurtalarda rastgelelik.


3.4 Donanım Onayı ve İmza

EggScanner, TEE-benzeri bir güvenli unsur içinde:

\sigma_i = \mathsf{Sign}_{sk_{\text{scanner}}}(\mathsf{BH}_i \parallel t(e_i) \parallel \text{meta})


---

4. Main-Coop Zinciri (DOL) ve Blok Mantığı

4.1 Blok Başlığı

struct EggBlockHeader {
  prev_hash;
  biohash;         // BH_i
  time_bat;        // t(e_i)
  scanner_sig;     // σ_i
  care_commit;     // Pedersen/Keccak tabanlı PoC taahhüdü
  egg_quality;     // EQP özet metriği
  difficulty;      // EDA hedefi
  tx_root;         // yumurta->YSC işlemlerinin Merkle kökü
}

4.2 Fork-Choice: “Heaviest-Yolk First”

Ağırlık = EDA uyumluluğu + toplam PoC katkısı + EQP ağırlıklandırması.

Zincir seçimi: toplam ağırlığı maksimize eden patika.


4.3 EDA — Hedef Blok Aralığı

Amaç belirli bir ortalama blok aralığı :

\text{difficulty}_{k+1} = \text{difficulty}_k \cdot \left( \frac{\Delta t_k}{\frac{1}{\lambda}} \right)^{\alpha}

: yumuşatma parametresi.


4.4 Finalite “PECK” Gadjeti

Niyet: BFT-benzeri yumuşak finalite.

Bir blok, 3 ardışık süper-çoğunluk oyu (PoC ağırlıklı) alınca PECK-final olur.

Cezalar: yanlış çift imza/çatal tercihinde PoC indirimi ve ödül yakımı.


4.5 Ağ Katmanı

Gossip: EE bildirimleri, blok başlıkları, PoC taahhütleri.

Anti-DoS: imza doğrulamadan önce hafif filtre (Bloom/PRF).

Rate-limit: node başına EE frekansı için biyolojik üst sınır denetimi.



---

5. Proof of Care (PoC) — Bakım Skoru

5.1 Metrikler (yüksek seviye, sansız/zararsız)

Ortam konforu (sıcaklık-nem bandında kalma süresi)

Işık döngüsü uyumu (sirkadiyen ritim korelasyonu)

Beslenme düzenliliği (zaman-varians özeti)

Stres göstergeleri (gürültü/ani değişim sinyalleri)

Hijyen ve kalabalıklık (prox. yoğunluk ölçütleri)


5.2 Skor Fonksiyonu

C_i = w_1 f_1 + w_2 f_2 + \dots + w_m f_m \quad ; \quad \sum w_j = 1

Zaman çürümesi: .


5.3 Ödül Bağlantısı

YSC ödülü:

R_i = \underbrace{\frac{R_0}{2^{\lfloor B/10^5 \rfloor}}}_{\text{halving}} \cdot \left( \eta_1 \cdot \frac{EQP_i}{\overline{EQP}} + \eta_2 \cdot \frac{C_i}{\overline{C}} \right)

, politika parametreleri.


5.4 Oyun Teorisi / Anti-Gaming

Ani metrik sıçramaları → robust z-score ile kırpma.

Sensör tekilliği → çoklu üreticiden eşdeğer onay.

Bribe/koordinasyon → PECK finalitesi + PoC kesintileri.



---

6. YSC Tokenomik ve Piyasa Mekaniği

6.1 Arz Eğrisi

Toplam ihraç edilen arz :

S(B) = \sum_{k=0}^{\lfloor B/10^5 \rfloor} \left(R_0 \cdot \frac{10^5}{2^k}\right)
= 10^5 R_0 \cdot \left(2 - 2^{-\lfloor B/10^5 \rfloor}\right)

6.2 Ücret Pazarı ve Yakım

İşlem ücretleri  → kısmen yakım, kısmen Bakım Havuzu.

FEV (Farmer Extractable Value) azaltımı: PECK-final, gecikmeli açık artırma, order flow gizliliği.


6.3 Likidite ve Türevler

Yumurta Vadeli (cash-settled; zincir içi yumurta sayacı referanslı).

PoC Endeksi ETF: bakım puanı ağırlıklı YSC sepeti.

Opsiyonlar: halving öncesi implied vol oynaklığı; mizahi ama ölçülebilir piyasa.



---

7. Oracle ve Donanım Mimarisi (Yüksek Seviye)

7.1 EggScanner Bileşenleri

Çoklu sensör girişleri, güvenli element (anahtar saklama),

Zaman kaynağı (BAT),

Attestation: üretici kök sertifikasıyla imzalanmış yazılım ölçümleri.


7.2 Çoklu Tanık (Multi-Attester)

Aynı EE, en az iki bağımsız tanık tarafından gözlemlenirse ek ödül katsayısı.

7.3 NFC/RFID — “Kümestransfer”

Fiziksel yumurta transferinde tag-commit → zincirde release işlemi.

Çift harcama (iki farklı varış) denemesinde tag siyah liste + yakım.


> Güvenlik açısından yalnızca kavramsal akış veriyoruz; uygulamalı protokol adımlarına inmiyoruz.




---

8. Gizlilik ve Uyum (Privacy-by-Design)

8.1 ZK Kanıtları

ZK-SNARK devresi: “Bu BioHash, sertifikalı bir EggScanner’dan ve geçerli sensörden geldi” ama ham ölçümü ifşa etmiyor.

Taahhütler:  → zincire, açıklama opsiyonel.


8.2 Diferansiyel Gizlilik (Agregalar)

Bakım/kalite istatistikleri için -DP gürültüsü; tek tavuğun profili sızmasın.


8.3 Veri Saklama ve Unutulma

Ham sensör verisi yerelde ve kısa süre; zincirde sadece hash/taahhüt.

İsteğe bağlı veri minimizasyonu politikaları.



---

9. Tehdit Modeli ve Güvenlik Analizi

Saldırı	Vektör	Azaltım

Sahte yumurta	3D baskı/kabuk taklidi	Çoklu modalite + fuzzy extractor + çoklu tanık
Sensör spoofing	Işık/ısı manipülasyonu	Anomali tespiti, out-of-band denetimler
Anahtar sızıntısı	Donanım ele geçirilmesi	TEE, anti-tamper, hızlı anahtar iptali
Zincir bölünmesi	Ağ partisyonu	PECK final + yeniden ağırlıklandırma
Bribery/kolüsyon	PoC oyu satın alma	PoC şeffaflığı, kamu audit, ceza katsayıları
FEV/Ön-çıkış	Sıralama manipülasyonu	Gecikmeli açık artırma, gizli mempool



---

10. Zaman ve Senkronizasyon: BAT

BAT: NTP/UTC yerine biyolojik olayların istatistikleriyle drift düzeltme.

Outlier yumurta aralıkları → winsorize + EDA geri besleme.



---

11. Yönetişim — Tavuk Otoritesi (DAO)

11.1 Oy Ağırlığı

\text{vote\_weight}(u) = \theta_1 \cdot \text{YSC}_u + \theta_2 \cdot \overline{OFI}_u + \theta_3 \cdot \overline{EQP}_u

11.2 Öneri Yaşam Döngüsü

Tavsiye → Islak Oylama (snapshot) → PECK-onay → Yürütme.

Zincir üstü parametreler: , EDA sınırları.


11.3 Uyum ve Etik

Hayvan refahı göstergeleri PoC’e içkin; kötü muamele cezaları otomatik.



---

12. Birlikte Çalışabilirlik ve Katmanlama

HenL2: PoE L1 güvenliğini kullanıp yüksek TPS işlemleri L2’ye alan rollup.

Köprü: IBC-benzeri hafif istemci; YSC ↔ diğer zincirler.

Ortak Uygulamalar: DeFi teşvikleri, sigorta, lojistik NFT’leri (yumurta partileri).



---

13. Referans Uygulama Taslağı

Modüller: eggchain-core, poc-engine, scanner-attestation, fee-market.

Dil: çekirdek Rust/Go; devreler için circom/halo2 eşleniği.

Testnet: IncubatorNet (geliştirici faucet’i, sahte EE jeneratörü).

Gözlem: Prometheus uyumlu metrikler; open dashboards.



---

14. Deneysel/Analitik Modellemler (oyuncak örnekler)

Hedef blok aralığı  dakika; günlük ≈ 144 blok.

Halving epoch  yumurta → ≈ 694 gün (~1.9 yıl) (varsayımsal).

 YSC ise  YSC üst sınır.


> Rakamlar örnek niteliğinde; gerçek parametreler yönetişimle belirlenecektir.




---

15. Gelecek Entegrasyon ve Yol Haritası (Genişletilmiş)

2026 Q1 — Akıllı Yemleme Sözleşmeleri (prototip; oracle-güvenli sipariş taahhüdü)

2026 Q2 — IncubatorNet v2: PECK finalite ve EDA tuning

2026 Q3 — Kümestransfer Beta (NFC/RFID tag-commit → chain-release)

2026 Q4 — ZK devreleri açık kaynak, üçüncü taraf audit

2027 Q1 — HenL2 deneme ağı; FEV azaltım mekanizmaları

2027 Q2 — Civciv Fonu (CVCF) ve Kuluçka Kredileri (teminat: PoC akışı)

2027 Q4 — Çoklu üretici attestation federasyonu



---

16. Blog (ve Sunum) için “Vurgu” Paketleri + Görsel Fikirler

Kısa Seri İçerik Önerisi (5 parça):

1. “PoE Nedir?” — olay temelli konsensüs, BAT/EDA kavramları.


2. “BioHash Nasıl Doğar?” — infografik: sensör → fuzzy extractor → taahhüt → blok başlığı.


3. “Proof of Care ile Teşvik” — grafik: PoC metrikleri ve ödüle etkisi.


4. “YSC Ekonomisi” — halving eğrisi ve  görseli.


5. “Tehditler ve Mizah” — FEV → Farmer Extractable Value kavram karikatürü.



İnfografik taslakları:

BioHash Boru Hattı: (Sensörler) → (Özellik Vektörü) → (Fuzzy Extractor) → (BH) → (ZK Kanıt) → (Blok).

Konsensüs Akışı: EE yayını → DOL güncelleme → PECK oylaması → finalite.

PoC Radar Grafiği: 5–7 metrik, öncesi/sonrası karşılaştırması.

Halving Merdiveni: 10^5 blok başına ödül yarılanması.



---

17. SSS (Mizah + Teknik)

S: Yumurtayı kim doğrular?
C: EggScanner + çoklu attestation + PECK-final oyları.

S: Aynı yumurtayı iki kez “blok” yapabilir miyim?
C: BioHash + tag bağlamı + NFC “release” ile çift harcama önlenir.

S: Hayvan refahı ne olacak?
C: PoC tasarım gereği refahı teşvik eder; ihlaller ekonomik olarak cezalandırılır.

S: PoE çevreci mi?
C: İş israfı yerine biyolojik olay bağlama; hedef düşük karbon ayak izi.



---

18. Açık Sorular ve Araştırma Gündemi

BioHash entropi alt sınırlarının deneysel ispatı (çoklu donanım üreticisi).

ZK devrelerinde devre boyutu/latency optimizasyonu.

FEV’yi azaltan sıralama oyunları ve klasik AMM etkileşimi.

BAT ile NTP/UTC harmanlamasında hatalı kalibrasyon dayanıklılığı.

PoC metriklerinde kültürel/iklimsel norm farklarının dengelenmesi.





