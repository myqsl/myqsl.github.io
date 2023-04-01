---
layout: page
title: Gallery
permalink: /gallery/
---

{% for country in site.countries %}
<h2>{{ country.title }}</h2>
    {% assign stations = site.stations | where: 'country', country.code %}
    {% for station in stations %}
        {% assign qsls = site.qsls | where: 'station', station.code %}
        {% for qsl in qsls %}
<div style="margin-bottom: 5px">
  <a href="{{ qsl.url }}">
  <img src="{{ qsl.front_small }}"/>
  </a>
</div>
        {% endfor %}
    {% endfor %}
<br/>
{% endfor %}
