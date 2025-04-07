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
{% for qsl in site.posts %}
{% for reception in qsl.receptions %}
{% if reception.station == station.code %}

<tr>
    <td>{% if station.country %}<img class="flag" src="{{ country.flag }}"/>{% endif %} <a href="{{ station.url }}">{{ station.title }}</a></td>
    <td><a href="{{ qsl.url }}">{{ reception.frequency }}</a></td>
    <td><a href="{{ qsl.url }}">{{ reception.date }}</a></td>
</tr>
{% endif %}
{% endfor %}
{% endfor %}
{% endfor %}

</table>
