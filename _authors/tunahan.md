---
layout: page
title: Tunahan Yardımcı
permalink: /authors/tunahan/
---

{% assign author = site.data.authors.tunahan %}

<section class="author-profile">
  <h2>{{ author.name }}</h2>
  {% if author.avatar %}
    <img src="{{ author.avatar }}" alt="{{ author.name }}" style="width:150px;border-radius:50%;margin-bottom:1rem;">
  {% endif %}

  <p>{{ author.description }}</p>

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
