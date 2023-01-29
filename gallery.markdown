---
layout: page
title: Gallery
permalink: /gallery/
---

{% assign countries = site.stations | map: 'country' | uniq | sort %}

{% for country in countries %}
<h2>{{ country }}</h2>
{% assign stations = site.stations | where: 'country', country %}
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
