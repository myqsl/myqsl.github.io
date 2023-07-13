---
layout: page
title: QSLs
permalink: /qsls/
---

<p style="text-align:center"><a href="/pirates/">Pirates stations</a> | <a href="/private/">Private stations</a> | <a href="/utility">Utility stations</a></p>

{% assign continents = site.countries | map: 'continent' | uniq | sort %}

{% for continent in continents %}

<div class="rounded-box">

<div class="header"><h2>{{ continent }}</h2></div>

{% assign countries = site.countries | where: 'continent', continent %}

<table>
<tr>
    <th>Station</th>
    <th>Broadcaster &bullet; Frequency &bullet; Date</th>
</tr>

{% for country in countries %} 

{% assign itulist = site.stations | where: 'country', country.code | map: 'itu' | uniq | sort %}

{% for itu in itulist %}
    {% assign stations = site.stations | where: 'itu', itu %}
    {% assign country_code = stations | map: 'country' | first %}
    {% assign country = site.countries | where: 'code', country_code | first %}
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
    {% assign broadcaster = site.broadcasters | where: 'code', qsl.broadcaster | first %}
    {% if qsl.broadcaster %}{% if broadcaster.code != station.code %}&bullet; <a href="{{ broadcaster.url }}">{{ broadcaster.title}}</a>{% endif %}{% endif %}
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
