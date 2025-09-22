---
layout: authors
title: Tunahan Yardımcı
permalink: /authors/tunahan/
lang: en
---

{% assign author = site.data.authors.tunahan %}
{% if author.avatar %}
  <img alt="{{ author.name }}" src="{{ author.avatar }}"  style="width:150px;border-radius:50%;margin-bottom:1rem;">
{% endif %}

<!-- BURASI CV / TANITIM ALANI -->
<p>
  Hello, my name is Tunahan. I am a second-year student in Computer Science at Istanbul University.
  I am actively working on machine learning and also conducting various studies with my team.
</p>

<!-- Sosyal ikonlar -->
<div class="author-links">
  {% if author.github %}
    <a href="{{ author.github }}" target="_blank" class="social-link">
      <i class="fab fa-github"></i> GitHub
    </a>
  {% endif %}
  {% if author.instagram %}
    <a href="{{ author.instagram }}" target="_blank" class="social-link">
      <i class="fab fa-instagram"></i> Instagram
    </a>
  {% endif %}
  {% if author.linkedin %}
    <a href="{{ author.linkedin }}" target="_blank" class="social-link">
      <i class="fab fa-linkedin"></i> LinkedIn
    </a>
  {% endif %}
</div>
<style>
  .author-links {
    display: flex;
    gap: 1rem;
    margin-top: 1rem;
    flex-wrap: wrap;
  }

  .author-links .social-link {
    display: inline-flex;
    align-items: center;
    font-size: 1rem;
    text-decoration: none;
    gap: 0.5rem;
    color: inherit;
    transition: color 0.2s;
  }

  .author-links .social-link:hover {
    color: #0d6efd; /* hover rengi */
  }
</style>
<!-- Yazıları -->
<h3 style="margin-top: 2rem;">Yazıları</h3>
<ul>
  {% for post in site.posts %}
  {% if post.authors contains "tunahan" or post.author == "tunahan" %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
  {% endfor %}
</ul>
