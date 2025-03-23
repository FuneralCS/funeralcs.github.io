---
layout: page
title: Yazarlar
permalink: /about/
icon: fas fa-user-friends
order: 4
---

## ✍️ FuneralCS Ekibi

{% for id in site.data.authors %}
  {% assign author = site.data.authors[id[0]] %}
  {% if author.url %}
### 👤 [{{ author.name }}]({{ author.url }})
  {% else %}
### 👤 {{ author.name }}
  {% endif %}

{{ author.description }}

---
{% endfor %}

{: .prompt-tip }
