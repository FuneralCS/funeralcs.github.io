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
      <div class="author-item">
        <!-- 'name' yoksa varsayılan "Bilinmeyen Yazar" gösterilir -->
        <h3>{{ author.name | default: "Bilinmeyen Yazar" }}</h3>
        
        <!-- 'description' yoksa varsayılan açıklama gösterilir -->
        <p>{{ author.description | default: "Açıklama bulunamadı." }}</p>
        
        <!-- 'url' bilgisi varsa profil bağlantısı oluşturulur -->
        {% if author.url %}
          <p><a href="{{ author.url }}" target="_blank">Profil</a></p>
        {% endif %}
        
        <!-- GitHub hesabı -->
        {% if author.github %}
          <p><a href="{{ author.github }}" target="_blank"><i class="fab fa-github"></i> GitHub</a></p>
        {% endif %}
        
        <!-- Sosyal medya hesapları -->
        <div class="social-links">
          {% if author.twitter %}
            <a href="{{ author.twitter }}" target="_blank"><i class="fab fa-twitter"></i> Twitter</a>
          {% endif %}
          {% if author.facebook %}
            <a href="{{ author.facebook }}" target="_blank"><i class="fab fa-facebook"></i> Facebook</a>
          {% endif %}
          {% if author.linkedin %}
            <a href="{{ author.linkedin }}" target="_blank"><i class="fab fa-linkedin"></i> LinkedIn</a>
          {% endif %}
          {% if author.instagram %}
            <a href="{{ author.instagram }}" target="_blank"><i class="fab fa-instagram"></i> Instagram</a>
          {% endif %}
        </div>
      </div>
    {% endfor %}
  </div>
</section>
