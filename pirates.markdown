---
layout: page
title: Pirates
permalink: /pirates/
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
{% if station['kind'] == 'pirate' %}
{% assign serie = site.data['series'][qsl.serie] %}
{% assign serie_title = serie['title'] %}
{% assign country = site.data['countries'][station['country']] %}
{% assign country_flag = country['flag'] %}
{% assign station_title = station['title'] %}

<tr>
    <td>{% if country_flag %}<img class="flag" src="{{ country_flag }}"/>{% endif %} <a href="/stations/{{ reception['station'] }}.html">{{ station_title }}</a>{% if reception['station'] != qsl.serie %} relays <a href="/series/{{ qsl.serie }}.html">{{ serie_title }}</a>{% endif %}</td>
    <td><a href="{{ qsl.url }}">{{ reception.frequency }}</a></td>
    <td><a href="{{ qsl.url }}">{{ reception.date }}</a></td>
</tr>

{% endif %}
{% endfor %}
{% endfor %}

</table>
