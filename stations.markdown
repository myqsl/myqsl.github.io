---
layout: page
title: Stations
permalink: /stations/
---

{% assign continents = site.countries | map: 'continent' | uniq | sort %}

{% for continent in continents %}

<h4>{{ continent }}</h4>

{% assign countries = site.countries | where: 'continent', continent %}

<table>
<tr>
    <th>ITU</th>
    <th>Country</th>
    <th>Station</th>
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
    <a href="{{ station.url }}">{{ station.title }}</a><br/>
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

{% assign no_itu_stations = site.stations | where: 'itu', none %}
{% if no_itu_stations %}
<h4>Unidentified</h4>
<table>
<tr>
    <th>Station</th>
    <th>Frequency</th>
    <th>Date</th>
</tr>

{% for station in no_itu_stations %}
{% assign qsls = site.qsls | where: 'station', station.code %}
{% for qsl in qsls %}
<tr>
    <td><a href="{{ station.url }}">{{ station.title }}</a></td>
    <td>{{ qsl.frequency }}</td>
    <td>{{ qsl.reception_date }}</td>
</tr>
{% endfor %}
{% endfor %}
</table>
{% endif %}
