---
layout: page
title: Stations
permalink: /stations/
---

{% assign countries = site.stations | map: 'country' | uniq | sort %}
<table>
<tr>
    <th>Country</th>
    <th>Station</th>
</tr>
{% for c in countries %}
    <tr>
    <td><p>{{ c }}</p></td>
    <td>
    {% assign its_stations = site.stations | where: 'country', c | sort: 'title' %}
    {% for s in its_stations %}
    <p><a href="{{ s.url }}">{{ s.title }}</a></p>
    {% endfor %}
    </td>
    </tr>
{% endfor %}
</table>
