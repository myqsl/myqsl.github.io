---
layout: page
title: Stations
permalink: /stations/
---
<!-- 
National services map:

<script type="text/javascript" charset="utf-8" async src="https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3Ae1de8c605bbbe43e34663f48ed386aacdca0139a4a7612a958a115550d4258f0&amp;width=100%25&amp;height=400&amp;lang=ru_RU&amp;scroll=true"></script>
-->

{% assign kinds = "national:National services,show:Regular shows,pirate:Pirates,religious:Religious,dxcommunity:DX Programmes,transmitters:Transmitters,time:Time services,volmet:Meteo services" | split: ',' %}

{% assign continents = site.countries | map: 'continent' | uniq | sort %}
{% for continent in continents %}
    {% assign first_station = 1 %}

    {% assign countries = site.countries | where: 'continent', continent %}

    {% for country in countries %}
        {% assign its_stations = site.stations | where: 'country', country.code | sort: 'title' %}
        {% for station in its_stations %}

            {% if first_station == 1 %}
<br/>
<h3>{{ continent }}</h3>
                {% assign first_station = 0 %}
            {% endif %}
<p><img src="{{ country.flag }}" class="flag"/> <a href="{{ station.url }}">{{ station.title }}</a></p>
        {% endfor %}
    {% endfor %}
{% endfor %}



{% for kind in kinds %}

    {% assign kind_obj = kind | split: ':' %}
    {% assign kind_id = kind_obj[0] %}
    {% assign kind_title = kind_obj[1] %}

    {% assign stations = site.stations | where: 'kind', kind_id | where: 'country', nil | sort: 'title' %}

    {% assign first_station = 1 %}

    {% for station in stations %}

        {% if first_station == 1 %}
            {% assign first_station = 0 %}
<br/>
<h3>{{ kind_title }} (unid country)</h3>
        {% endif %}

<p>&nbsp;&mdash;&nbsp;<a href="{{ station.url }}">{{ station.title }}</a></p>
    {% endfor %}

{% endfor %}
