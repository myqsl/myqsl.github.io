---
layout: page
title: Transmitters
permalink: /transmitters/
---

Confirmed stations map:

<script type="text/javascript" charset="utf-8" async src="https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3Aa664fe2bf48cab289503df614ecbbf1af25ebbf3aa075c9f9fd48708148e5e77&amp;width=100%25&amp;height=311&amp;lang=ru_RU&amp;scroll=true"></script>

<br/>

{% assign countries = site.transmitters | map: 'country' | uniq | sort %}
<table>
<tr>
    <th>Country</th>
    <th>Transmitter</th>
    <th>Stations</th>
</tr>
{% for c in countries %}
    {% assign transmitters = site.transmitters | where: 'country', c | sort: 'title' %}
    {% for t in transmitters %}
    <tr>
    <td><p>{{ c }}</p></td>
    <td><p><a href="{{ t.url }}">{{ t.title }}</a></p></td>
    <td>
        {% assign stations_codes = site.qsls | where: 'transmitter', t.code | map: 'station' | uniq %}
        {% for sc in stations_codes %}
            {% assign s = site.stations | where: 'code', sc | first %}
            <p><a href="{{ s.url }}">{{ s.title }}</a></p>
        {% endfor %}
    </td>
    </tr>
{% endfor %}
{% endfor %}
</table>
