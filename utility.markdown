---
layout: page
title: Utility stations
permalink: /utility/
---

<table>
<tr>
    <th>Station</th>
    <th>Frequency</th>
    <th>Date</th>
</tr>

{% assign stations = site.stations | where: 'kind', 'utility' %}

{% for station in stations %}

{% assign country = site.countries | where: 'code', station.country | first %}
{% assign qsls = site.posts | where: 'station', station.code %}
{% for qsl in qsls %}

<tr>
    <td>{% if station.country %}<img class="flag" src="{{ country.flag }}"/>{% endif %} <a href="{{ station.url }}">{{ station.title }}</a></td>
    <td><a href="{{ qsl.url }}">{{ qsl.frequency }}</a></td>
    <td><a href="{{ qsl.url }}">{{ qsl.reception_date }}</a></td>
</tr>
{% endfor %}
{% endfor %}

</table>
