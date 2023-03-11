---
layout: page
title: Stations
permalink: /stations/
---
<!-- 
National services map:

<script type="text/javascript" charset="utf-8" async src="https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3Ae1de8c605bbbe43e34663f48ed386aacdca0139a4a7612a958a115550d4258f0&amp;width=100%25&amp;height=400&amp;lang=ru_RU&amp;scroll=true"></script>
-->

{% assign kinds = "national:National services,show:Regular shows,pirate:Pirates,religious:Religious,dxcommunity:DX Programmes,transmitters:Transmitters,time:Time services" | split: ',' %}

{% for kind in kinds %}

{% assign kind_obj = kind | split: ':' %}
{% assign kind_id = kind_obj[0] %}
{% assign kind_title = kind_obj[1] %}

<br/>
<h3>{{ kind_title }}</h3>

{% assign stations = site.stations | where: 'kind', kind_id | sort: 'title' %}

{% if kind_id == "national" or kind_id == "transmitters" or kind_id == "time" %}

    {% assign continents = site.countries | map: 'continent' | uniq | sort %}
    {% for continent in continents %}
        {% assign countries = site.countries | where: 'continent', continent %}
        {% for country in countries %}
            {% assign its_stations = stations | where: 'country', country.code %}
            {% for station in its_stations %}
<p><img src="{{ country.flag }}" class="flag"/> <a href="{{ station.url }}">{{ station.title }}</a></p>
            {% endfor %}
        {% endfor %}
    {% endfor %}

{% else %}

{% for station in stations %}
<p>&nbsp;&mdash;&nbsp;<a href="{{ station.url }}">{{ station.title }}</a></p>
{% endfor %}

{% endif %}

{% endfor %}
