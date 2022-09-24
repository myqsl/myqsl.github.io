---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

<h1>Подтверждения на сайте</h1>

<ul>
  {% for qsl in site.qsls %}
    <li>
      <h2><a href="{{ qsl.url }}">{{ qsl.title }}</a></h2>
      <!-- <p>{{ qsl.content | markdownify }}</p> -->
    </li>
  {% endfor %}
</ul>
