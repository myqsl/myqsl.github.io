---
layout: page
title: Stations
permalink: /stations/
---

{% assign continents = site.countries | map: 'continent' | uniq | sort %}

{% for continent in continents %}

<br/>
<h3>{{ continent }}</h3>

{% assign countries = site.countries | where: 'continent', continent | sort  %}

{% for country in countries %}

    {% assign stations = site.stations | where: 'country', country.code | sort: 'title' %}
    {% for t in stations %}

<p><img src="{{ country.flag }}" class="flag"/> <a href="{{ t.url }}">{{ t.title }}</a></p>
    {% endfor %}

{% endfor %}
{% endfor %}
