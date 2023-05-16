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
    <th>ITU</th>
    <th>Country</th>
    <th>Station, Broadcaster</th>
    <th>Frequency</th>
    <th>Date</th>
</tr>

{% for country in countries %} 

{% assign itulist = site.stations | where: 'country', country.code | map: 'itu' | uniq | sort %}

{% for itu in itulist %}
    {% assign stations = site.stations | where: 'itu', itu %}
    {% assign country_code = stations | map: 'country' | first %}
    {% assign country = site.countries | where: 'code', country_code | first %}
<tr>
    <td>{{ itu }}</td>
    <td>{{ country.title }}</td> 

    <td>
{% for station in stations %}
    {% assign qsls = site.qsls | where: 'station', station.code %}
{% for qsl in qsls %}
    {% assign broadcaster = site.broadcasters | where: 'code', qsl.broadcaster | first %}
    {% if station.short %}<a href="{{ station.url }}">{{ station.short }}</a>, {% endif %}{% if qsl.broadcaster %}<a href="{{ broadcaster.url }}">{{ broadcaster.title}}</a>{% endif %}<br/>
{% endfor %}
{% endfor %}
    </td>

    <td>
{% for station in stations %}
    {% assign qsls = site.qsls | where: 'station', station.code %}
{% for qsl in qsls %}
    <a href="{{ qsl.url }}">{{ qsl.frequency }}</a><br/>
{% endfor %}
{% endfor %}
    </td>

    <td>
{% for station in stations %}
    {% assign qsls = site.qsls | where: 'station', station.code %}
{% for qsl in qsls %}
    {{ qsl.reception_date }}<br/>
{% endfor %}
{% endfor %}
    </td>

</tr>
{% endfor %}
{% endfor %}

</table>

{% endfor %}
