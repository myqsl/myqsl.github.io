---
layout: page
title: Stations
permalink: /stations/
---

Confirmed stations map:

<script type="text/javascript" charset="utf-8" async src="https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3Aa664fe2bf48cab289503df614ecbbf1af25ebbf3aa075c9f9fd48708148e5e77&amp;width=100%25&amp;height=311&amp;lang=ru_RU&amp;scroll=true"></script>

<br/>

National services map:

<script type="text/javascript" charset="utf-8" async src="https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3Ae1de8c605bbbe43e34663f48ed386aacdca0139a4a7612a958a115550d4258f0&amp;width=100%25&amp;height=400&amp;lang=ru_RU&amp;scroll=true"></script>

<br/>

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
