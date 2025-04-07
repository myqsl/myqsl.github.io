---
layout: page
title: Stations (countries)
permalink: /stationsc/
---

<div class="rounded-box">
<p style="padding: 10px 10px 10px 10px;">Here is
the list of transmitting stations.
It is ordered by countries.
There are information about QSLs for each station.
Have a nice reading!
</p>
</div>

<p style="text-align:center"><a href="/pirates/">Pirates stations</a> | <a href="/private/">Private stations</a> | <a href="/utility">Utility stations</a></p>

{% assign countries = site.countries | sort: "title" %}

{% for country in countries %}

<div class="rounded-box">
<header><h2><img class="flag" src="{{ country.flag }}"/>
{{ country.title }}</h2></header>

{% assign stations = site.stations | where: 'country', country.code | sort: 'title' %}
{% for station in stations %}

{% assign receptions = 0 %}
{% for qsl in site.posts %}
    {% for reception in qsl.receptions %}
        {% if reception.station == station.code %}
            {% assign receptions = receptions | plus: 1 %}
        {% endif %}
    {% endfor %}
{% endfor %}

<p>&mdash; <a href="{{ station.url }}">{{ station.title }}</a> | receptions: {{ receptions }}</p>

{% endfor %} <!-- station -->
</div>


{% endfor %} <!-- country -->
