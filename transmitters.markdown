---
layout: page
title: Transmitters
permalink: /transmitters/
---
<!--
Confirmed stations map:

<script type="text/javascript" charset="utf-8" async src="https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3Aa664fe2bf48cab289503df614ecbbf1af25ebbf3aa075c9f9fd48708148e5e77&amp;width=100%25&amp;height=311&amp;lang=ru_RU&amp;scroll=true"></script>

<br/>
-->

{% assign continents = site.countries | map: 'continent' | uniq | sort %}

{% for continent in continents %}

<br/>
<h3>{{ continent }}</h3>

{% assign countries = site.countries | where: 'continent', continent | sort  %}

{% for country in countries %}


    {% assign transmitters = site.transmitters | where: 'country', country.code | sort: 'title' %}
    {% for t in transmitters %}

<p><img src="{{ country.flag }}" class="flag"/> <a href="{{ t.url }}">{{ t.title }}</a></p>
    {% endfor %}
{% endfor %}
{% endfor %}
