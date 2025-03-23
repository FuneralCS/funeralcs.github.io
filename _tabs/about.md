---
layout: page
title: Yazarlar
permalink: /about/
icon: fas fa-user-friends
order: 4
---

<section id="authors">
  <h2>Yazarlar</h2>
  <div class="authors-list">
    {% for key in site.data.authors | keys %}
      {% assign author = site.data.authors[key] %}
      <div class="author-item" style="margin-bottom: 2em;">

        <h3>{{ author.name | default: "Bilinmeyen Yazar" }}</h3>

        <p>{{ author.description | default: "Açıklama bulunamadı." }}</p>

        {% if author.url %}
          <p><a href="{{ author.url }}" target="_blank">Profil</a></p>
        {% endif %}

        {% if author.github %}
          <p><a href="{{ author.github }}" target="_blank"><i class="fab fa-github"></i> GitHub</a></p>
        {% endif %}

        {% if author.instagram %}
          <p><a href="{{ author.instagram }}" target="_blank"><i class="fab fa-instagram"></i> Instagram</a></p>
        {% endif %}

        {% if author.twitter %}
          <p><a href="{{ author.twitter }}" target="_blank"><i class="fab fa-twitter"></i> Twitter</a></p>
        {% endif %}

        {% if author.linkedin %}
          <p><a href="{{ author.linkedin }}" target="_blank"><i class="fab fa-linkedin"></i> LinkedIn</a></p>
        {% endif %}

      </div>
    {% endfor %}
  </div>
</section>
