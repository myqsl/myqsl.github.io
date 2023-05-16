---
layout: page
title: Broadcasters
permalink: /broadcasters/
---

{% assign continents = site.countries | map: 'continent' | uniq | sort %}

{% for continent in continents %}

<h4>{{ continent }}</h4>

{% assign countries = site.countries | where: 'continent', continent %}

<table>
<tr>
    <th>ITU</th>
    <th>Country</th>
    <th>Name, Station</th>
    <th>Frequency</th>
    <th>Date</th>
</tr>

{% for country in countries %} 

{% assign itulist = site.broadcasters | where: 'country', country.code | map: 'itu' | uniq | sort %}

{% for itu in itulist %}
    {% assign broadcasters = site.broadcasters | where: 'itu', itu %}
    {% assign country_code = broadcasters | map: 'country' | first %}
    {% assign country = site.countries | where: 'code', country_code | first %}
<tr>
    <td>{{ itu }}</td>
    <td>{{ country.title }}</td>

    <td>
{% for broadcaster in broadcasters %}
    {% assign qsls = site.qsls | where: 'broadcaster', broadcaster.code %}
{% for qsl in qsls %}
    {% assign station = site.stations | where: 'code', qsl.station | first %}
    <a href="{{ broadcaster.url }}">{{ broadcaster.title }}</a>{% if qsl.station %}, {{ station.title }}{% endif %}
    <br/>
{% endfor %}
{% endfor %}
    </td>

    <td>
{% for broadcaster in broadcasters %}
    {% assign qsls = site.qsls | where: 'broadcaster', broadcaster.code %}
{% for qsl in qsls %}
    <a href="{{ qsl.url }}">{{ qsl.frequency }}</a><br/>
{% endfor %}
{% endfor %}
    </td>

    <td>
{% for broadcaster in broadcasters %}
    {% assign qsls = site.qsls | where: 'broadcaster', broadcaster.code %}
{% for qsl in qsls %}
    {{ qsl.reception_date }}<br/>
{% endfor %}
{% endfor %}
    </td>

</tr>
{% endfor %}
{% endfor %}

</table>

{% endfor %}

{% assign no_itu_broadcasters = site.broadcasters | where: 'itu', none %}
{% if no_itu_broadcasters %}
<h4>Unidentified</h4>
<table>
<tr>
    <th>Name</th>
    <th>Frequency</th>
    <th>Date</th>
</tr>

{% for broadcaster in no_itu_broadcasters %}
{% assign qsls = site.qsls | where: 'broadcaster', broadcaster.code %}
{% for qsl in qsls %}
<tr>
    <td><a href="{{ broadcaster.url }}">{{ broadcaster.title }}</a></td>
    <td>{{ qsl.frequency }}</td>
    <td>{{ qsl.reception_date }}</td>
</tr>
{% endfor %}
{% endfor %}
</table>
{% endif %}
