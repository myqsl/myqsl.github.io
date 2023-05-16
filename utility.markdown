---
layout: page
title: Utility stations
permalink: /utility/
---

<table>
<tr>
    <th>Country</th>
    <th>Station</th>
    <th>Frequency</th>
    <th>Date</th>
</tr>

{% assign stations = site.stations | where: 'kind', 'utility' %}

{% for station in stations %}

{% assign country = site.countries | where: 'code', station.country | first %}
{% assign qsls = site.qsls | where: 'station', station.code %}
{% for qsl in qsls %}

<tr>
    <td>{% if station.country %}{{ country.title }}{% endif %}</td>
    <td><a href="{{ station.url }}">{{ station.title }}</a></td>
    <td><a href="{{ qsl.url }}">{{ qsl.frequency }}</a></td>
    <td><a href="{{ qsl.url }}">{{ qsl.reception_date }}</a></td>
</tr>
{% endfor %}
{% endfor %}

</table>
