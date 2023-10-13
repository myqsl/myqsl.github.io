---
layout: page
title: By stations
permalink: /qsls/
---

<p style="text-align:center"><a href="/pirates/">Pirates stations</a> | <a href="/private/">Private stations</a> | <a href="/utility">Utility stations</a></p>

{% assign itulist = site.stations | map: 'itu' | uniq | sort %}

{% assign continents = site.countries | map: 'continent' | uniq | sort %}

{% for continent in continents %}

<div class="rounded-box">

<div class="header"><h2>{{ continent }}</h2></div>

{% assign countries = site.countries | where: 'continent', continent %}

<table>
<tr>
    <th>Station</th>
    <th>Program &bullet; Frequency &bullet; Date</th>
</tr>

{% for itu in itulist %}

{% for country in countries %}

{% assign stations = site.stations | where: 'itu', itu | where: 'country', country.code %}

{% for station in stations %}

    {% assign qsls = site.posts | where: 'station', station.code %}
    {% if station.short %}
        {% assign station_title = station.short %}
    {% else %}
        {% assign station_title = station.title %}
    {% endif %}

<tr>
    <td>
        <img class="flag" src="{{ country.flag }}"/>
        {{ itu }}
        <a href="{{ station.url }}">{{ station_title }}</a>
    </td>

    <td>
{% for qsl in qsls %}
    &bullet; <a href="{{ qsl.url }}">{{ qsl.title }}</a>
    &bullet; <a href="{{ qsl.url }}">{{ qsl.frequency }}</a>
    &bullet; {{ qsl.reception_date }}<br/>
{% endfor %}
    </td>

</tr>
{% endfor %}
{% endfor %}
{% endfor %}

</table>

</div>
{% endfor %}
