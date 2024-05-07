---
layout: page
title: Stations (countries)
permalink: /stationsc/
---

<div class="rounded-box">
<p style="padding: 10px 10px 10px 10px;">Here is
the list of transmitting stations.
It is ordered by countries.
There are information about QSLs for each station.
Have a nice reading!
</p>
</div>

<p style="text-align:center"><a href="/pirates/">Pirates stations</a> | <a href="/private/">Private stations</a> | <a href="/utility">Utility stations</a></p>

{% assign countries = site.countries | sort: "title" %}

{% for country in countries %}

<div class="rounded-box">
<header><h2><img class="flag" src="{{ country.flag }}"/>
{{ country.title }}</h2></header>

{% for station in site.stations %}

{% if station.country != country.code %}
    {% continue %}
{% endif %}

{% assign qsls = site.posts | where: 'station', station.code %}

<p><details>
<summary>{{ station.title }}<sup>{{ qsls.size }}</sup><a href="{{ station.url }}"><em>pictures</em></a></summary>

<ul>

{% for qsl in qsls %}
    <li><a href="{{ qsl.url }}">{{ qsl.title }}</a> &bullet; {{ qsl.frequency }} &bullet; {{ qsl.reception_date }} {{ qsl.reception_time }}</li>    
{% endfor %}
</ul>

</details></p>

{% endfor %} <!-- station -->
</div>


{% endfor %} <!-- country -->
