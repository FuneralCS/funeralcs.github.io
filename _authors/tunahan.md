---
layout: page
title: Tunahan Yardımcı
permalink: /authors/tunahan/
---

{% assign author = site.data.authors.tunahan %}

<section class="author-profile">
  {% if author.avatar %}
    <img src="{{ author.avatar }}" alt="{{ author.name }}" style="width:150px;border-radius:50%;margin-bottom:1rem;">
  {% endif %}

  <!-- BURASI CV / TANITIM ALANI -->
  <p>
  Merhaba, ben Tunahan. İstanbul Üniversitesi Bilgisayar Bilimleri 1. sınıf öğrencisiyim.  
  Aktif olarak makine öğrenmesi çalışıyorum aynı zamanda ekibimiz ile birlikte çeşitli çalışmalar yapmaktayım.
  </p>
  
  {% if author.url %}
    <p><a href="{{ author.url }}" target="_blank">Profil</a></p>
  {% endif %}

  <h3>Yazıları</h3>
  <ul>
    {% for post in site.posts %}
      {% if post.author == "tunahan" %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
      {% endif %}
    {% endfor %}
  </ul>
</section>
