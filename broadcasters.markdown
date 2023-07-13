---
layout: page
title: Broadcasters
permalink: /broadcasters/
---

{% assign continents = site.countries | map: 'continent' | uniq | sort %}

{% for continent in continents %}

<div class="rounded-box">

<div class="header"><h2>{{ continent }}</h2></div>

{% assign countries = site.countries | where: 'continent', continent %}

<table>
<tr>
    <th>Country &bullet; Name</th>
    <th>Station &bullet; Frequency &bullet; Date</th>
</tr>

{% for country in countries %} 

{% assign itulist = site.broadcasters | where: 'country', country.code | map: 'itu' | uniq | sort %}

{% for itu in itulist %}
    {% assign broadcasters = site.broadcasters | where: 'itu', itu %}
    {% assign country_code = broadcasters | map: 'country' | first %}
    {% assign country = site.countries | where: 'code', country_code | first %}
{% for broadcaster in broadcasters %}
    {% assign qsls = site.posts | where: 'broadcaster', broadcaster.code %}
{% if qsls != empty %}
<tr>
    <td>
    <img class="flag" src="{{ country.flag }}"/>
    {{ itu }}
    &bullet; <a href="{{ broadcaster.url }}">{{ broadcaster.title }}</a>
    </td>

    <td>
{% for qsl in qsls %}
    {% assign station = site.stations | where: 'code', qsl.station | first %}
    {% if qsl.station %}
    {% if qsl.station!= broadcaster.code %}&bullet; via <a href="{{ station.url }}">{{ station.title }}</a>{% endif %}{% endif %}
    {% if qsl.frequency %}
    &bullet; <a href="{{ qsl.url }}">{{ qsl.frequency }}</a>{% endif %}
    {% if qsl.reception_date %}
    &bullet; {{ qsl.reception_date }}{% endif %}<br/>
{% endfor %}
    </td>

</tr>
{% endif %}
{% endfor %}
{% endfor %}
{% endfor %}

</table>
</div>

{% endfor %}

{% assign no_itu_broadcasters = site.broadcasters | where: 'itu', none %}
{% if no_itu_broadcasters %}
<div class="rounded-box">
<div class="header"><h2>Unidentified</h2></div>
<table>
<tr>
    <th>Name</th>
    <th>Frequency</th>
    <th>Date</th>
</tr>

{% for broadcaster in no_itu_broadcasters %}
{% assign qsls = site.posts | where: 'broadcaster', broadcaster.code %}
{% for qsl in qsls %}
<tr>
    <td><a href="{{ broadcaster.url }}">{{ broadcaster.title }}</a></td>
    <td>{{ qsl.frequency }}</td>
    <td>{{ qsl.reception_date }}</td>
</tr>
{% endfor %}
{% endfor %}
</table>

</div>

{% endif %}
