---
layout: page
title: QSLs
permalink: /qsls/
---

{% assign continents = site.countries | map: 'continent' | uniq | sort %}

{% for continent in continents %}

<h4>{{ continent }}</h4>

{% assign countries = site.countries | where: 'continent', continent %}

<table>
<tr>
    <th>ITU</th>
    <th>Country</th>
    <th>Station</th>
    <th>Frequency</th>
    <th>Date</th>
</tr>

{% for country in countries %} 

{% assign itulist = site.transmitters | where: 'country', country.code | map: 'itu' | uniq | sort %}

{% for itu in itulist %}
    {% assign transmitters = site.transmitters | where: 'itu', itu %}
    {% assign country_code = transmitters | map: 'country' | first %}
    {% assign country = site.countries | where: 'code', country_code | first %}
<tr>
    <td>{{ itu }}</td>
    <td>{{ country.title }}</td> 

    <td>
{% for transmitter in transmitters %}
    {% assign qsls = site.qsls | where: 'transmitter', transmitter.code %}
{% for qsl in qsls %}
    {% assign station = site.stations | where: 'code', qsl.station | first %}
    {% if transmitter.short %}<a href="{{ transmitter.url }}">{{ transmitter.short }}</a>, {% endif %}<a href="{{ station.url }}">{{ station.title}}</a><br/>
{% endfor %}
{% endfor %}
    </td>

    <td>
{% for transmitter in transmitters %}
    {% assign qsls = site.qsls | where: 'transmitter', transmitter.code %}
{% for qsl in qsls %}
    <a href="{{ qsl.url }}">{{ qsl.frequency }}</a><br/>
{% endfor %}
{% endfor %}
    </td>

    <td>
{% for transmitter in transmitters %}
    {% assign qsls = site.qsls | where: 'transmitter', transmitter.code %}
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
