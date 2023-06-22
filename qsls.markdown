---
layout: page
title: QSLs
permalink: /qsls/
---

<p><a href="/pirates/">Pirates stations</a> | <a href="/private/">Private stations</a> | <a href="/utility">Utility stations</a></p>

{% assign continents = site.countries | map: 'continent' | uniq | sort %}

{% for continent in continents %}

<h4>{{ continent }}</h4>

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
    <a href="{{ qsl.url }}">{% if qsl.kind == 'QSL' %}
    &#128231;
    {% elsif qsl.kind == 'e-QSL' %}
    &#128206;
    {% elsif qsl.kind == 'e-letter' %}
    &#128292;
    {% elsif qsl.kind == 'letter' %}
    &#128240;
    {% endif %}</a>
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

{% endfor %}
