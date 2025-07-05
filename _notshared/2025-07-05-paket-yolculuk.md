---
title: "Paketlerin kısa yolculukları"
date: 2025-07-05 14:26:00 +0300
categories: [internet, bilgisayar]
tags: [internet, bilgisayar]
author: vladimirdelvis
image:
  path: /assets/img/2025-07-05-paket-yolculuk/2025-07-05-paket-yolculuk-kapak.webp
description: "Paketlerin kısa yolculukları"
toc: true
math: false
mermaid: false
comments: true
pin: false
---
# Ön söz

>Bir siteye girdiğinizde veya internetle çalışan bir uygulama çalıştırdığınızda nasıl oluyor da o görüntüler ve yazılar birden bire ekranınızda beliriveriyor?
>İşte bu yazıda bunu anlayacaksınız.

### Tanımlar ve Temel Kavramlar

- IP Adresi: Bu adres internet ortamındaki bir cihazın kimliğidir. 5 tane sınıfı vardır (A,B,C,D,E). İnternet Protokol adresi olarak anılır. İnternet protokolünün IPv4 ve IPv6 olacak şekilde iki tane sürümü vardır. [1]
	- Örnek: 192.168.1.56 (C), 84.785.642.125 (A)

- MAC Adresi: Fiziksel adres olarak anılır. [2] Aynı ağda bulunan iki cihaz için büyük önem arz eden bir adrestir.
	- Örnek: 9E:10:DC:AE:52:6D

>Antrparantez: Çoğu insan sadece IP adresini bilir ancak MAC adresinden bihaberdir. Aslında MAC adresi iletişimin temelinde yatan adrestir. Yazının ilerleyen kısımlarında bunu daha iyi anlayacaksınız.

- DNS: Alan adlarını IP adreslerine çevirmeye yarayan sistemdir. [3]

>Şimdi temel kavramları öğrendiğimize göre artık yolculuk başlasın!

---

### OSI Modeli
|Katman numarası|Adı|Protokolleri|
|:---:|:---:|:---:|
|7|UYGULAMA|HTTP,HTTPS,FTP,SFTP,SSH,DNS|
|6|SUNUM| 
|5|OTURUM|
|4|ULAŞIM|TCP,UDP|
|3|AĞ|IP,ICMP|
|2|VERİ|Ethernet|
|1|DONANIM|

Tabloda görüldüğü üzere OSI modeli 7 adet katmandan oluşmaktadır. [4] Bir siteye girdiğimiz vakit paket (paketler sunuculara gönderdiğimiz veriler topluluğudur), ilgili katmandan başlayarak 1. katmana doğru akmaya başlar ve bu sırada inşa olur.

---

### Örnek Senaryo

Örneğin [duckduckgo.com](https://duckduckgo.com) sitesini ziyaret etmek isteyen biri olalım. Siteye girmek için *enter* tuşuna bastığımız an öncelikle bilgisayarımızda bulunan dns resolver bu alan adını çözmek için belli başlı işlemler gerçekleştirir.

#### Örnek Senaryo - Basitçe DNS Çözümlemesi

1. **Kullanıcı Talebi (Recursive Query)**: Bilgisayarınızdaki DNS resolver, DNS önbelleğini kontrol eder. Eğer daha önce aynı alan adı sorgulandıysa bu kısımdan IP adresi döner. Burada bir şey bulunamazsa 2. aşamaya geçilir.
2. **DNS Çözücüsü (Resolver)**: Bilgisayarınızda DNS adresi ayarlanmış değilse ve DNS ayarları varsayılan olarak bırakıldıysa, DNS isteği modeme gönderilir. Modemde ISS'nin çözücüsüne gönderir.
3. **Cevap**: ISS'nin çözücüsü sorguyu çözer ve IP adresini kullanıcıya yollar.

Bu DNS Sorgusunun cevabı:

<figure>
    <img src="/assets/img/2025-07-05-paket-yolculuk/dns_cevabi.webp" alt="DIG komutu ile duckduckgo.com için DNS cevabı">
    <figcaption>Görsel: DIG komutu ile duckduckgo.com için DNS cevabı</figcaption>
</figure>

==Not: Burada DNS sorgusunun sadece mantığı gösterildi. DNS protokolü OSI modelinde bulunur ve o protokol de aynı şekilde 7. katmandan başlayarak 1. katmana doğru oluşturulur. Onu DNS kısmında yazmadım çünkü yazının ilerleyen kısımlarında yazacağım.==

---

#### Örnek Senaryo - Devam

IP adresini elde ettiğimize göre artık siteye bağlanmaya başlayabiliriz.

1. **7. katman (HTTPS)**: Bu katman uygulama katmanıdır ve yüksek düzeylidir. Hedef sunucu bir site olduğundan HTTPS protokolü ile haberleşme kurulacak. Paketin içeriğine site için gereken headerlar ve HTTP methodu gibi şeyler konulacak. HTTPS protokolü HTTP protokolünün şifrelenmiş halidir.

HTTP isteğinin yapısı:

<figure>
    <img src="/assets/img/2025-07-05-paket-yolculuk/http.webp" alt="HTTP istek yapısı">
    <figcaption>Görsel: HTTP istek yapısı</figcaption>
</figure>

2. **4. katman (TCP)**: Bu katman ulaşım katmanıdır. HTTP protokolü TCP üzerinde çalışıtığından TCP taşıma protokolü olarak görev yapacaktır. Burada kaynak ve hedef cihazın IP adresleri, port bilgileri (kaynak için rastgele, hedef için 443) ve payload yer alır. Bu payload aslında sırasıyla 7,6,5 katmanlarının sonucunda üretilmiş paketin ta kendisidir. Aşağıda 2 adet görsel var. Mavi kısımlar payloadı gösteriyor. Birisinde şifreleme olduğu için payloadın içeriğinin ne olduğu bilinmiyor ama diğerinde ne olduğu biliniyor.

<figure>
    <img src="/assets/img/2025-07-05-paket-yolculuk/http_tcp.webp" alt="TCP payload (HTTP)">
    <figcaption>Görsel: TCP yükü olarak HTTP</figcaption>
</figure>

<figure>
    <img src="/assets/img/2025-07-05-paket-yolculuk/https_tcp.webp" alt="TLS payload (HTTPS)">
    <figcaption>Görsel: TLS yükü olarak HTTP</figcaption>
</figure>

3. **3. katman (IP)**: Bu katman ağ katmanıdır. Hedef ve kaynak IP adresleri bu katmanda paketin içeriğine dahil edilir.

<figure>
    <img src="/assets/img/2025-07-05-paket-yolculuk/IP.webp" alt="IP protokolünün yapısı">
    <figcaption>Görsel: IP protokolünün yapısı</figcaption>
</figure>

4. **2. katman (Ethernet)**: Geldik en önemli katmana burada hedef IP adresine gitmek için aracı seçilecek. İşletim sistemi bu aracıyı seçerken ROUTE tablosu ve ARP tablosundan yararlanır. Hedef IP eğer LAN ağının içinde değilse modemin, LAN ağında ise hedef cihazın MAC adresi ethernet protokolü için bir hedef adres olacaktır. Kaynak adresi bizim paketi yolladığımız arayüzün MAC adresidir. MAC adresini elde etmek için ARP tablosunu kullanırız.

<figure>
    <img src="/assets/img/2025-07-05-paket-yolculuk/ethernet.webp" alt="Ethernet protokolünün yapısı" width="600">
    <figcaption>Görsel: Ethernet protokolünün yapısı</figcaption>
</figure>

5. **1. katman**: Son olarak bu oluşturulan paket donanım üzerinden aktarılır. Bilgisayarınıza kablo ile bağladığınız modem ya da routera iletilecektir.

---

#### Örnek Senaryo - Modem/Router

Ben burayı direkt kabloyu modeminize bağlamışsınız gibi anlatacağım.
Modeme ulaşan paket 3. katmana kadar açılır ve Hedef MAC adresi değerlendirmeye tabi tutulur. Hedef MAC adresi LAN ağından başka bir cihaza ait ise paket o cihaza yönlendirilir. Eğer hedef MAC adresi ile modemin MAC adresi ile aynı ise pakete ait TTL (Time-To-Live) değeri 1 azaltılır ve pakete NAT yapılır. (NAT artık başka bir yazının konusu) Basitçe paket 4. katmana kadar açılacak kaynak IP adresi ve kaynak portu değişecek. Kaynak IP adresi modemin IP adresi, kaynak portu ise modeme ait rastgele seçilmiş bir port olacak.
Müteakiben modem şunu kaydedecek: Eğer benim y adresimin z portuna bir paket gelirse bu paketi yine NAT uygulayarak x adresinin f portuna yolla. Burada y modemin IP adresi, z modemden seçilmiş olan KAYNAK portu, x bizim cihazımızın IP adresi ve f bizim cihazımızın rastgele olarak seçtiği KAYNAK portudur. Yani değişmeyen tek şey hedef IP adresi ve hedef portudur.

Modem bunu kaydettikten sonra paketi 3.katmana kadar geri paketler. Bu katman üzerinde hedef MAC adresini yine kendi ROUTE tablosu ve ARP tablosuna göre ayarlar. Kaynak MAC adresi modemin MAC adresi olur.

>Not 1: NAT ağından çıkmak için birden fazla yol vardır. Çoğumuzun modeminde ve ISS'sinde gerçekleşen yöntem PAT dır. (Port Address Translation). [5]

>Not 2: Burada NAT'ın amacı dış ağ ile iç ağı köprülemektir. Bunu adeta bir soğanın halkalarına benzetebiliriz. Paketin dış ağa geçmesi gerektiğinde (buna route tablosu üzerinden karar verilecek) NAT işlemine tabi tutulacaktır. Paket modemimizden dış ağa geçtikten sonra, bir kademe daha büyük bir dış ağa geçmesi gerekirse yine NAT (CGNAT) işlemi uygulanacaktır. Bu işlem gerektiği kadar tekrarlanacaktır.

>Antrparantez: CGNAT teknolojisi ile modemi de bir NAT ağına dahil ederiz. Hatırlarsanız NAT, kaynak IP adresini ve kaynak portunu değiştiriyordu. Bu en büyük NAT ağının sahibi ise ISS'nizin ta kendisidir. Bu yüzden genel IP adresimiz ile modem arayüzünde gördüğümüz IP adresi farklı olacaktır.

Aynen bu şekilde belirli NAT ve yönlendirme işlemleri sonucunda paket en sonunda hedefe ulaşacaktır. Hedef sunucu paket üzerinde gerekenleri yaptıktan sonra pakete bir cevap (cevap bir HTTP cevabı olacak) vermeye karar verirse, bizim ISS'mizin belirlediği genel IP adresi ve ISS'nin seçtiği rastgele olan porta, kendi IP adresi (duckduckgo.com) ve 443 portundan veri yollayacaktır. Burada ISS yine aynı modemimiz gibi NAT yapacaktır. Bunu modemimizin kaydettiği x,y,z ve f değerleri gibi kendisinin ve iç ağa ait başka bir cihazın değerlerini kaydettiği için yapabilecek. Paket ISS'den geçerken hedef IP adresi ve hedef portu değişmekle beraber kaynak ve hedef MAC adresi de değişecek (PAT işleminin tersi). Paket birden fazla kez dış ağdan iç ağa geçicektir. En sonunda paket modemimizin y:z (y adresinin z portu) soketine geldiğinde bu paketi 4.katmana kadar açarak hedef ip adresini x, hedef portunu f; hedef MAC adresini bizim cihazımızın MAC adresi, kaynak MAC adresini kendi MAC adresi yaparak paketi bilgisayarımızın arayüzüne yollayacaktır.

Arayüz bu paketi aldıktan sonra sırasıyla paket 1. katmandan 7. katmana doğru açılacak. Nihayet artık o metin ve görseller ekranımızda belirivermeye başlayacak.

Burada gördüğünüz işlemler sadece buzdağının görünen kısmıdır. Şifreleme, TCP'nin kontrol paketleri ve paketi alan cihazların işletim sisteminin yaptığı tüm işlemler anlatılmamıştır. Ancak bu işlemlere rağmen bu iletişim çok kısa bir süre içerisinde gerçekleşir.

İşte bir paketin kısa hayatının kısa yolcuğunu size anlatmaya çalıştım. 

---

# KAYNAKÇA

Görseller wireshark programı kullanılarak alınmıştır.

1. https://tr.wikipedia.org/wiki/IP_adresi
2. https://tr.wikipedia.org/wiki/MAC_adresi
3. https://tr.wikipedia.org/wiki/DNS
4. https://tr.wikipedia.org/wiki/OSI_modeli
5. https://www.networkacademy.io/ccna/network-services/nat-overload-pat

[1]: https://tr.wikipedia.org/wiki/IP_adresi
[2]: https://tr.wikipedia.org/wiki/MAC_adresi
[3]: https://tr.wikipedia.org/wiki/DNS
[4]: https://tr.wikipedia.org/wiki/OSI_modeli
[5]: https://www.networkacademy.io/ccna/network-services/nat-overload-pat