---
layout: page
title: Tunahan Yardımcı
permalink: /authors/tunahan/
parent: /authors/
---

{% assign author = site.data.authors.tunahan %}

<h2>Yazar</h2>

{% if author.avatar %}
  <img alt="{{ author.name }}" src="{{ author.avatar }}"  style="width:150px;border-radius:50%;margin-bottom:1rem;">
{% endif %}

<!-- BURASI CV / TANITIM ALANI -->
<p>
  Merhaba, ben Tunahan. İstanbul Üniversitesi Bilgisayar Bilimleri 1. sınıf öğrencisiyim.  
  Aktif olarak makine öğrenmesi çalışıyorum aynı zamanda ekibimiz ile birlikte çeşitli çalışmalar yapmaktayım.
</p>

<!-- Sosyal ikonlar -->
<div class="social-links" style="margin-top:1rem;">
  {% if author.github %}
    <a href="{{ author.github }}" target="_blank" title="GitHub">
      <i class="fab fa-github"></i>
    </a>
  {% endif %}
  {% if author.instagram %}
    <a href="{{ author.instagram }}" target="_blank" title="Instagram">
      <i class="fab fa-instagram"></i>
    </a>
  {% endif %}
</div>

<!-- Yazıları -->
<h3 style="margin-top: 2rem;">Yazıları</h3>
<ul>
  {% for post in site.posts %}
    {% if post.author == "tunahan" %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>
