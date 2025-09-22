---
layout: authors
title: Yazarlar
permalink: /authors/
icon: fas fa-user-friends
order: 4
lang: tr-TR
---

<style>
  /* ------------------------------
     1) GENEL / GRID YAPISI
  ------------------------------ */
  #authors {
    margin-top: 1rem;
  }
  #authors .authors-list {
    display: grid;
    /* Ekran boyutuna göre otomatik sütunlar: */
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-top: 1.5rem;
  }

  /* ------------------------------
     2) KART (LIGHT ve DARK MOD)
  ------------------------------ */

  /* Light tema (html[data-mode="light"]) */
  html[data-mode="light"] #authors .author-item {
    background-color: #f4f4f4;
    color: #333;
  }

  /* Dark tema (html'de data-mode="light" YOKSA) */
  html:not([data-mode="light"]) #authors .author-item {
    background-color: #2b2b2b;
    color: #ddd;
  }

  /* Kartın ortak stilleri */
  #authors .author-item {
    border-radius: 1rem;
    padding: 1.5rem 1rem;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    transition: background-color 0.3s, color 0.3s;
  }

  /* ------------------------------
     3) AVATAR DESTEĞİ
  ------------------------------ */
  #authors .author-avatar {
    width: 100px;
    height: 100px;
    margin: 0 auto 1rem;
    border-radius: 50%;
    background-color: #ccc; /* Avatar yoksa gri daire */
    background-size: cover;
    background-position: center;
  }

  /* Karanlık tema için default gri biraz daha koyu */
  html:not([data-mode="light"]) #authors .author-avatar {
    background-color: #444;
  }

  /* ------------------------------
     4) YAZI VE METİN
  ------------------------------ */
  #authors h3 {
    margin-bottom: 0.5rem;
    font-size: 1.25rem;
  }
  #authors p {
    margin-bottom: 0.5rem;
    font-size: 0.95rem;
    line-height: 1.4;
  }

  /* ------------------------------
     5) SOSYAL MEDYA LİNKLERİ
  ------------------------------ */
  #authors .social-links {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 0.75rem;
  }

  /* Light tema link rengi */
  html[data-mode="light"] #authors .social-links a {
    background-color: #e9ecef;
    color: #333;
  }
  html[data-mode="light"] #authors .social-links a:hover {
    background-color: #ced4da;
  }

  /* Dark tema link rengi */
  html:not([data-mode="light"]) #authors .social-links a {
    background-color: #3a3a3a;
    color: #ddd;
  }
  html:not([data-mode="light"]) #authors .social-links a:hover {
    background-color: #555;
  }

  /* Ortak link stili */
  #authors .social-links a {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    text-decoration: none;
    font-size: 18px;
    transition: background-color 0.3s ease;
  }
</style>

<section id="authors">
  <div class="authors-list">
    {% for author in site.data.authors %}
      <div class="author-item">
        <!-- Avatar resmi varsa background-image ile ekle -->
        {% if author[1].avatar %}
          <div class="author-avatar"
               style="background-image: url('{{ author[1].avatar }}');">
          </div>
        {% else %}
          <div class="author-avatar"></div>
        {% endif %}

        <h3>{{ author[1].name | default: "Bilinmeyen Yazar" }}</h3>
        <p>{{ author[1].description | default: "Açıklama bulunamadı." }}</p>

        {% if author[1].url %}
          <p><a href="{{ author[1].url }}" target="_blank">Profil</a></p>
        {% endif %}

        <div class="social-links">
          {% if author[1].github %}
            <a href="{{ author[1].github }}" target="_blank" title="GitHub">
              <i class="fab fa-github"></i>
            </a>
          {% endif %}
          {% if author[1].instagram %}
            <a href="{{ author[1].instagram }}" target="_blank" title="Instagram">
              <i class="fab fa-instagram"></i>
            </a>
          {% endif %}
          {% if author[1].twitter %}
            <a href="{{ author[1].twitter }}" target="_blank" title="Twitter">
              <i class="fab fa-twitter"></i>
            </a>
          {% endif %}
          {% if author[1].linkedin %}
            <a href="{{ author[1].linkedin }}" target="_blank" title="LinkedIn">
              <i class="fab fa-linkedin"></i>
            </a>
          {% endif %}
          {% if author[1].slug %}
            <a href="/authors/{{ author[1].slug }}/" title="Detaylı Bilgi">
              <i class="fas fa-info-circle"></i>
            </a>
          {% endif %}


        </div>
      </div>
    {% endfor %}
  </div>
</section>
