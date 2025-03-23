---
layout: page
title: Yazarlar
permalink: /about/
icon: fas fa-user-friends
order: 4
---

<style>
  /* --- GENEL AYARLAR --- */
  #authors {
    margin-top: 1rem;
  }

  #authors .authors-list {
    /* Responsive grid: geniş ekranda yan yana, dar ekranda alt alta */
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-top: 1.5rem;
  }

  #authors .author-item {
    background-color: #f4f4f4;
    border-radius: 1rem;
    padding: 1.5rem 1rem;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    transition: background-color 0.3s, color 0.3s;
  }

  /* --- DARK MODE DESTEĞİ --- */
  /* Chirpy teması koyu moda geçtiğinde <html data-mode="dark"> oluyor */
  html[data-mode="dark"] #authors .author-item {
    background-color: #2b2b2b;
    color: #ddd;
  }

  /* --- AVATAR ALANI --- */
  #authors .author-avatar {
    width: 100px;
    height: 100px;
    margin: 0 auto 1rem;
    border-radius: 50%;
    background-color: #ccc; /* Eğer avatar resmi yoksa gri daire */
    background-size: cover;
    background-position: center;
  }

  html[data-mode="dark"] #authors .author-avatar {
    background-color: #444; /* Koyu modda gri daire biraz daha koyu */
  }

  /* --- YAZI TARZI --- */
  #authors h3 {
    margin-bottom: 0.5rem;
    font-size: 1.25rem;
  }

  #authors p {
    margin-bottom: 0.5rem;
    font-size: 0.95rem;
    line-height: 1.4;
  }

  /* --- SOSYAL LİNKLER --- */
  #authors .social-links {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 0.75rem;
  }

  #authors .social-links a {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background-color: #e9ecef;
    text-decoration: none;
    color: inherit;
    font-size: 18px;
    transition: background-color 0.3s ease;
  }

  #authors .social-links a:hover {
    background-color: #bfc0c2;
  }

  html[data-mode="dark"] #authors .social-links a {
    background-color: #3a3a3a;
  }

  html[data-mode="dark"] #authors .social-links a:hover {
    background-color: #555;
  }
</style>

<section id="authors">
  <h2>Yazarlar</h2>
  <div class="authors-list">
    {% for author in site.data.authors %}
      <div class="author-item">
        <!-- Avatar resmi varsa background-image ile ekleyelim -->
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

        <!-- Sosyal medya linkleri -->
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
        </div>
      </div>
    {% endfor %}
  </div>
</section>
