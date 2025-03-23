---
# the default layout is 'page'
icon: fas fa-info-circle
order: 4
---

---
layout: page
title: Yazarlar
permalink: /about/
---

## ✍️ FuneralCS Ekibi

{% for id in site.data.authors %}
  {% assign author = site.data.authors[id[0]] %}
### 👤 [{{ author.name }}]({{ author.url }})
{{ author.description }}

---
{% endfor %}
{: .prompt-tip }
