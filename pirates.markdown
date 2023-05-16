---
layout: page
title: Pirates
permalink: /pirates/
---

<table>
<tr>
    <th>Country</th>
    <th>Station</th>
    <th>Frequency</th>
    <th>Date</th>
</tr>

{% assign stations = site.stations | where: 'kind', 'pirate' %}

{% for station in stations %}

{% assign country = site.countries | where: 'code', station.country | first %}
{% assign qsls = site.qsls | where: 'station', station.code %}
{% for qsl in qsls %}

{% assign broadcaster = site.broadcasters | where: 'code', qsl.broadcaster | first %}

<tr>
    <td>{% if station.country %}{{ country.title }}{% endif %}</td>
    <td><a href="{{ station.url }}">{{ station.title }}</a>{% if station.code != broadcaster.code %} relays <a href="{{ broadcaster.url }}">{{ broadcaster.title }}</a>{% endif %}</td>
    <td><a href="{{ qsl.url }}">{{ qsl.frequency }}</a></td>
    <td><a href="{{ qsl.url }}">{{ qsl.reception_date }}</a></td>
</tr>
{% endfor %}
{% endfor %}

</table>
