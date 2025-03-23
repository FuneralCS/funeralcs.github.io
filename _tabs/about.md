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
    {% for author in site.data.authors %}
      <div class="author-item">
        <!-- Eğer avatar desteği de eklemek istersen: 
             Yaml'da "avatar: /assets/img/tunahan.jpg" gibi bir alan tanımlayıp
             arka planı bu resmi gösterecek şekilde yapabilirsin. 
             Şimdilik sabit bir arka plan rengi kullanacağız. -->
        <div class="author-avatar"></div>

        <h3>{{ author[1].name | default: "Bilinmeyen Yazar" }}</h3>
        <p>{{ author[1].description | default: "Açıklama bulunamadı." }}</p>

        {% if author[1].url %}
          <p><a href="{{ author[1].url }}" target="_blank">Profil</a></p>
        {% endif %}

        <!-- Sosyal medya linklerini yan yana dizmek için .social-links kullanıyoruz. -->
        <div class="social-links">
          {% if author[1].github %}
            <a href="{{ author[1].github }}" target="_blank"><i class="fab fa-github"></i></a>
          {% endif %}
          {% if author[1].instagram %}
            <a href="{{ author[1].instagram }}" target="_blank"><i class="fab fa-instagram"></i></a>
          {% endif %}
          {% if author[1].twitter %}
            <a href="{{ author[1].twitter }}" target="_blank"><i class="fab fa-twitter"></i></a>
          {% endif %}
          {% if author[1].linkedin %}
            <a href="{{ author[1].linkedin }}" target="_blank"><i class="fab fa-linkedin"></i></a>
          {% endif %}
        </div>
      </div>
    {% endfor %}
  </div>
</section>
