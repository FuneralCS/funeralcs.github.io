---
title: "Şifreleme ve İmzalama"
date: 2025-09-28 13:00:00 +0300
categories: [teknoloji, kriptoloji]
tags: [şifreleme, şifre çözme, matematik, sayılar, hesap, bilgisayar, matematik, kriptoloji, veri, veri güvenliği, siber güvenlik, gizlilik, e-posta, PGP, OpenPGP, protonmail, uçtan uca şifreleme]
author: vladimirdelvis
image:
  path: /assets/img/2025-09-28-sifreleme-imzalama/banner.webp
description: "Asimetrik ve simetrik şifrelemeyi, imzalamayı ve bunların günlük hayattaki kullanımları hakkında."
toc: true
math: true
mermaid: false
comments: true
pin: false
lang: tr
---

## ŞİFRELEME

Verilerin okunabilir bir biçimden şifreli bir biçime dönüştürülmesidir. Bunu yapmanın birden çok yolu vardır. Şifreleme genel olarak ikiye ayrılır: simetrik ve asimetrik. Şifreleme veri güvenliğinin temel yapı taşıdır. 

<figure>
    <img src="/assets/img/2025-09-28-sifreleme-imzalama/sifreleme.webp" width="650" alt="Görsel: Şifreleme">
</figure>
<figure>
    <img src="/assets/img/2025-09-28-sifreleme-imzalama/diyagram.webp" width="650" alt="Görsel: Şifreleme Diyagramı">
</figure>

#### Simetrik Şifreleme

Bu özel anahtar şifrelemesi olarak da bilinir. Şifreleme için kullanılan anahtar ile şifreyi çözmek kullanılan anahtar bir tanedir. Bu anahtarın güvenliği çok büyük bir önem arz eder. Bu kategoriye ait olan en popüler şifreleme algoritmaları bunlardır: AES, DES (eskiden AES yoktu bu vardı ancak bu kırıldığı için AES bulundu), Twofish, Blowfish.

>Not: Ortada gizli bir anahtar olmasa da sezar şifrelemesi gibi şifremeler de bu kategoriye dahil edilebilir.

##### Simetrik Şifreleme Algoritmalarına Genel Bakış

1. **DES** (Data Encryption Standard): Dünyada en çok kullanılan simetrik şifreleme algoritmalarından birisidir. [Feistel şifreleme](https://tr.wikipedia.org/wiki/Feistel_%C5%9Fifresi) metodunu kullanır. Blok şifreleme kullanan DES, işlem sırasında 64 bitlik veriyi 56 bitlik anahtar kullanarak şifreler. Anahtar uzunluğunun kısa olması nedeniyle kırılmıştır.
2.  **AES** (Advanced Encrption Standard): DES kırıldıktan sonra yeni bir arayışa girilmiş ve AES simetrik şifreleme algoritması oluşturulmuştur. DES’in zayıf yönleri kuvvetlendirilmiş halidir ve blok şifreleme algoritmasını kullanır. DES’e göre daha hızlı ve güvenlidir. Uzunluk olarak 128, 192 ve 256 bit anahtarları destekler.

<figure>
    <img src="/assets/img/2025-09-28-sifreleme-imzalama/simetrik.webp" width="650" alt="Görsel: Simetrik Şifreleme">
</figure>

#### Asimetrik Şifreleme

Klasik şifreleme (Simetrik Şifreleme) tek bir anahtar kullanırken asimetrik şifrelemede farklı iki türlü anahtar bulunur. Bunlar sırasıyla ortak anahtar ve gizli anahtardır. Bu iki anahtar birbirine matematiksel olarak bağlıdır bu nedenle asimetrik terimi kullanılır. Bu anahtarlardan bir tanesiyle (çoğunlukla ortak anahtar) şifreleme yapılırken diğeriyle de şifre çözme işlemi gerçekleştirilir (çoğunlukla özel anahtar). Özel anahtara sahip olan bunu kişi çok iyi saklamalı ve gizlemelidir. Ortak anahtar gönül rahatlığı ile herkesle paylaşabilir. Bu kategoriye ait olan en popüler şifreleme algoritmaları bunlardır: RSA, D-H, ECC.


<center><strong>ASİMETRİK ŞİFRELEME İLE SİMETRİK ŞİFRELEME FARKLARI</strong></center>

| Özellik | Simetrik Şifreleme | Asimetrik Şifreleme |
|:---:|:---:|:---:|
| **Kullanılan Anahtar** | Tek bir **gizli anahtar** kullanılır. Şifreleme ve deşifreleme işlemleri aynı anahtarla yapılır. | Birbiriyle matematiksel olarak ilişkili iki anahtar kullanılır: **Genel Anahtar (Public Key)** ve **Özel Anahtar (Private Key)**. |
| **Hız ve Performans** | Çok hızlıdır ve daha az işlem gücü gerektirir. Büyük boyutlu verilerin şifrelenmesi için idealdir. | Hesaplama açısından yoğun olduğu için çok yavaştır. Bu nedenle genellikle küçük veriler için kullanılır. |
| **Anahtar Yönetimi**| En büyük zorluğu, tek anahtarın gönderici ve alıcı arasında güvenli bir şekilde paylaşılmasıdır (Anahtar Dağıtım Problemi). | Genel anahtar herkesle güvenle paylaşılabilir. Sadece özel anahtarın gizli tutulması gerekir, bu da anahtar yönetimini kolaylaştırır. |
| **Temel Kullanım Amacı** | Verinin kendisini gizlemek (dosya, disk, veritabanı ve ağ trafiği şifrelenmesi gibi). | Kimlik doğrulama (dijital imzalar), anahtar değişimi (simetrik anahtarı güvenle iletmek) ve bütünlük sağlama. |
| **Güvenlik Dayanağı** | Güvenlik, tamamen tek gizli anahtarın gizliliğine bağlıdır. Anahtar ele geçirilirse tüm sistem çöker. | Güvenlik, özel anahtarın gizliliğine bağlıdır. Genel anahtarın bilinmesinin bir sakıncası yoktur. |
| **Popüler Algoritmalar** | AES, DES, 3DES, Blowfish, RC4 | RSA, ECC (Eliptik Eğri Kriptografisi), Diffie-Hellman, DSA |

>Not: Günümüzde en çok kullanılan simetrik şifreleme algoritması AES, asimetrik şifreleme algoritması ise RSA ve ECC idir.

>Windows'da Pretty Good Privacy ve Linux'te GnuPG kullanarak dosyalarınızı asimetrik veya simetrik olarak şifreleyebilir ve dosyalarınızı imzalayabilirsiniz. 
{: .prompt-info }

>Antrparantez: Gününümüzdeki whatsapp gibi uygulamalar signal protokolü kullanır. Bu signal protokolü ise hem asimetrik hem de simetrik şifrelemeyi bir arada kullanır. Asimetrik şifrelemeyi "güvenli bir el sıkışma ve gizli bir anahtar oluşturma" için, simetrik şifrelemeyi ise bu anahtarı kullanarak "asıl sohbeti hızlı ve verimli bir şekilde şifrelemek" için kullanır.

##### Asimetrik Şifreleme Algoritmalarına Genel Bakış

1. **(D-H)** (Diffie-Hellman key exchange): İlk asimetrik şifreleme algoritması olarak karşımıza çıkar. Asıl amacı simetrik şifrelemede kullanılacak olan gizli anahtarın taraflara gizli ve güvenli bir şekilde iletilmesini sağlamaktır. Bunun için bu gizli anahtarı karşı tarafa asimetrik şifreleme yaparak iletir.
2. **RSA** (Rivest-Shamir-Adleman): Üç bilim adamının baş harflerinden oluşan RSA, dijital imzalama içinde kullanılmaktadır. Güvenilirliği, çok büyük asal sayıların işlem yapma zorluğuna dayanan bir algoritmadır. Günümüzde bankacılık sistemleri ve ticari sistemlerde öncelikli tercih edilen şifreleme tekniğidir. Bu büyük sayılar nedeniyle oldukça güvenilirdir ama işlemler yavaştır.
3. **ECC** (Elliptic Curve Cryptography): Sonlu cisimler üzerindeki eliptik eğrilerin cebirsel topolojisine dayanan bir açık anahtar şifrelemesidir. Eliptik eğri kriptografisinin en büyük özelliği depolama ve iletme gereksinimlerini azaltarak daha küçük anahtar boyutuna sahip olmasıdır. Bir eliptik eğri grubu, büyük modülerli ve buna bağlı olarak büyük anahtar boyutlu RSA tabanlı sistem ile aynı güvenlik seviyesi sunabilir.

<figure>
    <img src="/assets/img/2025-09-28-sifreleme-imzalama/asimetrik.webp" width="650" alt="Görsel: Asimetrik Şifreleme">
</figure>

---

## İMZALAMA

Bir verinin şifrelenmesinden sonra en önemli diğer durağı imzalamadır. Bu aslında asimetrik şifrelemenin tersidir. Yukarıda anlattığım şifreleme işleminde ortak anahtar kullanılarak şifreleniyordu ancak burada özel anahtar kullanılarak verinin hash değeri şifreleniyor. İşlemler şu şekilde sıralanabilir:

1. Öncelikle verinin hashi hesaplanır.
2. Bu özet değeri imzalayan kişinin özel anahtarı ile şifrelenir.
3. Doğrulayıcı ise imzalayan kişinin ortak anahtarı ile imzanın şifresini çözerek verinin hashi ile karşılaştırır.

>Not: Hash değeri yani verinin özeti demek bu verinin SHA-256, SHA-512, MD5 gibi fonksiyonlar yardımı ile her zaman aynı olacak şekilde sabit uzunlukta (algoritmadan algoritmaya değişir) olan bir sayıya indirgenmesidir. Şifreleme şeklinde anmadım (ancak gerçek tabiri şifrelenme şeklinde) çünkü genellikle şifrelenmiş verilerin şifresi çözülebilir ancak bu forma indirgenmiş verilerin geri dönüşü yoktur. Bu değer veriye özgüdür. Veride olacak en ufak değişiklik bu özetin tamamını değiştirecektir.

> Asimetrik şifreleme ile imzalamanın bir arada kullanılması hem verinin güvenliğini hem de verinin sahipliğini ve tamlığını doğrularız.

---

<center><strong>GÜNÜMÜZDEKİ UYGULAMALARI</strong></center>

1. Örnek: [ProtonMail](https://proton.me/mail) veya [Tuta](https://tuta.com/) gibi e-posta hizmetleri asimetrik şifreleme ve simetrik şifrelemeyi bir arada kullanır. Birine posta yollayacakken alıcının genel anahtarı ile posta şifrelenir ve bizim özel anahtarımız ile imzalanır. Alıcı ise ilk önce özel anahtarı ile şifresini çözer sonra kaynağın ortak anahtarı ile imzayı doğrular.
2. Örnek: Whatsapp, signal gibi uçtan uca şifreleme kullanan uygulamalar.
3. Örnek: HTTPS için sitenin imzası ve aradaki güvenli haberleşme yine bu algoritmalar sayesinde gerçekleşir.
4. Örnek: VPN.
5. Örnek: Secure boot, code signing, yazılım güncellemeleri.
6. Örnek: Kripto paralar.
7. Örnek: E-imza.

---

## Ayrıca Bknz.

1. [HTTPS - WIKIPEDIA](https://tr.wikipedia.org/wiki/HTTPS)
2. [SECURE BOOT - WIKIPEDIA](https://en.wikipedia.org/wiki/UEFI#Secure_Boot)
3. [CODE SIGNING - MICROSOFT](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/deployment/use-code-signing-for-better-control-and-protection)

## Kaynakça & İleri Okuma

1. [SIMETRIK VE ASIMETRIK SIFRELEME - MEDIUM](https://medium.com/@hicranozkan/simetrik-ve-asimetrik-anahtarl%C4%B1-%C5%9Fifreleme-algoritmalar%C4%B1-a60a4e0eb079)
2. [SIFRELEME - WIKIPEDIA](https://tr.wikipedia.org/wiki/%C5%9Eifreleme)
3. [SIFRELEME - KASPERKSY](https://www.kaspersky.com.tr/resource-center/definitions/encryption)
4. [ADVANCED ENCRPYTION STANDARD - NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf)
5. [SIMETRIK VE ASIMETRIK SIFRELEME - KERTERIZ](https://kerteriz.net/modern-sifreleme-yontemleri-simetrik-asimetrik-sifreleme/)
6. [KRIPTOGRAFIK OZET FONKSIYONLARI - WIKIPEDIA](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
7. [UCTAN UCA SIFRELEME VE WHATSAPP - WHATSAPP](https://faq.whatsapp.com/820124435853543#business-messaging-whatsapp-security)
8. [SIGNAL PROTOKOLU - INTERNATIONAL ASSOCIATION FOR CRYPTOLOGIC RESEARCH](https://eprint.iacr.org/2016/1013.pdf)
9. [DCODE.FR](https://www.dcode.fr/en)
10. [SIFIR BILGI ISPATI - WIKIPEDIA](https://en.wikipedia.org/wiki/Zero-knowledge_proof)
11. [KDF FONKSIYONLARI - WIKIPEDIA](https://en.wikipedia.org/wiki/Key_derivation_function)

## Görsel Kaynakça

1. <https://miro.medium.com/v2/1*84FEHMpc0pH2mna06Wtjfw.png>
2. <https://miro.medium.com/v2/1*WxD7iuqGYuQT8mIQFSc1pg.png>
3. <https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Public_key_encryption_keys.svg/2880px-Public_key_encryption_keys.svg.png>
4. <https://miro.medium.com/v2/1*FzBtDSOIb6JUkys33e0JZg.png>