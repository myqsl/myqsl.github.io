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

{% for qsl in site.posts %}
{% for reception in qsl.receptions %}
{% assign station = site.data['stations'][reception['station']] %}
{% if station['kind'] == 'utility' %}
{% assign station_code = station['code'] %}
{% assign station_title = station['title'] %}
{% assign country_code = station['country'] %}
{% assign country = site.data['countries'][country_code] %}

<tr>
    <td>{% if station['country'] %}<img class="flag" src="{{ country['flag'] }}"/>{% endif %} <a href="/stations/{{ station_code }}.html">{{ station_title }}</a></td>
    <td><a href="{{ qsl.url }}">{{ reception.frequency }}</a></td>
    <td><a href="{{ qsl.url }}">{{ reception.date }}</a></td>
</tr>
{% endif %}
{% endfor %}
{% endfor %}

</table>
