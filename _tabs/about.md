---
layout: page
title: Yazarlar
permalink: /about/
icon: fas fa-user-friends
order: 4
---

<section id="authors">
  <h2>Ekibimiz</h2>
  <div class="authors-list">
    {% for author in site.data.authors %}
      <div class="author-item" style="margin-bottom: 2em;">
        <h3>{{ author[1].name | default: "Bilinmeyen Yazar" }}</h3>
        <p>{{ author[1].description | default: "Açıklama bulunamadı." }}</p>

        {% if author[1].github %}
          <p><a href="{{ author[1].github }}" target="_blank"><i class="fab fa-github"></i> GitHub</a></p>
        {% endif %}

        {% if author[1].instagram %}
          <p><a href="{{ author[1].instagram }}" target="_blank"><i class="fab fa-instagram"></i> Instagram</a></p>
        {% endif %}

        {% if author[1].twitter %}
          <p><a href="{{ author[1].twitter }}" target="_blank"><i class="fab fa-twitter"></i> Twitter</a></p>
        {% endif %}

        {% if author[1].linkedin %}
          <p><a href="{{ author[1].linkedin }}" target="_blank"><i class="fab fa-linkedin"></i> LinkedIn</a></p>
        {% endif %}
      </div>
    {% endfor %}
  </div>
</section>
