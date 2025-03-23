---
layout: page
title: Yazarlar
permalink: /about/
icon: fas fa-user-friends
order: 4
---

<style>
  #authors .authors-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1rem;
    margin-top: 1.5rem;
  }

  #authors .author-item {
    background-color: #f5f5f5;
    border-radius: 1rem;
    padding: 1rem;
    text-align: center;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  }

  .dark #authors .author-item {
    background-color: #2b2b2b;
    color: #ddd;
  }

  #authors .author-avatar {
    width: 100px;
    height: 100px;
    margin: 0 auto 1rem;
    border-radius: 50%;
    background-color: #ccc;
  }

  #authors .social-links {
    display: flex;
    justify-content: center;
    gap: 0.5rem;
    margin-top: 0.5rem;
  }

  #authors .social-links a {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    text-decoration: none;
    color: inherit;
    background-color: #e9ecef;
    transition: background-color 0.3s;
  }

  #authors .social-links a:hover {
    background-color: #ced4da;
  }
</style>

<section id="authors">
  <h2>Yazarlar</h2>
  <div class="authors-list">
    {% for author in site.data.authors %}
      <div class="author-item">
        <div class="author-avatar"></div>

        <h3>{{ author[1].name | default: "Bilinmeyen Yazar" }}</h3>
        <p>{{ author[1].description | default: "Açıklama bulunamadı." }}</p>

        {% if author[1].url %}
          <p><a href="{{ author[1].url }}" target="_blank">Profil</a></p>
        {% endif %}

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
