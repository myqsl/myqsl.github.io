---
layout: page
title: Data
permalink: /qsls/
---

<div class="rounded-box">
<p style="padding: 10px 10px 10px 10px;">Here is the list of continents and transmitter stations.
Stations are ordered by countries.
There are information about QSLs for each station.
Have a nice reading!
</p>
</div>

<p style="text-align:center"><a href="/pirates/">Pirates stations</a> | <a href="/private/">Private stations</a> | <a href="/utility">Utility stations</a></p>

{% assign itulist = site.stations | map: 'itu' | uniq | sort %}

{% assign continents = site.countries | map: 'continent' | uniq | sort %}

{% for continent in continents %}

<div class="small-title">

<br/>
<strong>== {{ continent | upcase }} ==</strong>

{% assign countries = site.countries | where: 'continent', continent %}

{% for itu in itulist %}

{% for country in countries %}

{% assign stations = site.stations | where: 'itu', itu | where: 'country', country.code %}

{% for station in stations %}

    {% if station.short %}
        {% assign station_title = station.short %}
    {% else %}
        {% assign station_title = station.title %}
    {% endif %}

    {% assign qsls = site.posts | where: 'station', station.code %}

    {% if qsls.size > 0 %}

<br/><strong>&bullet; {{ itu  }} <a href="{{ station.url }}">{{ station_title }}</a></strong>
{% for serie in site.series %}

    {% assign serie_qsls = qsls | where: 'serie', serie.code %}

    {% if serie_qsls.size > 0 %}
&bullet; <a href="{{ serie.url }}">{{ serie.title }}</a> ({{ serie_qsls.size }})
    {% endif %} 
{% endfor %}

    {% endif %}

{% endfor %}
{% endfor %}
{% endfor %}

</div>

<!-- ---------------------------- -->

<div class="large-title">

<div class="rounded-box">

<div class="header"><h2>{{ continent }}</h2></div>

{% assign countries = site.countries | where: 'continent', continent %}

<table>
<tr>
    <th>Station</th>
    <th>Program &bullet; Frequency &bullet; Date</th>
</tr>

{% for itu in itulist %}

{% for country in countries %}

{% assign stations = site.stations | where: 'itu', itu | where: 'country', country.code %}

{% for station in stations %}

    {% assign qsls = site.posts | where: 'station', station.code %}
    {% if station.short %}
        {% assign station_title = station.short %}
    {% else %}
        {% assign station_title = station.title %}
    {% endif %}

<tr>
    <td>
        <img class="flag" src="{{ country.flag }}"/>
        {{ itu }}
        <a href="{{ station.url }}">{{ station_title }}</a>
    </td>

    <td>
{% for qsl in qsls %}
    &bullet; <a href="{{ qsl.url }}">{{ qsl.title }}</a>
    &bullet; <a href="{{ qsl.url }}">{{ qsl.frequency }}</a>
    &bullet; {{ qsl.reception_date }}<br/>
{% endfor %}
    </td>

</tr>
{% endfor %}
{% endfor %}
{% endfor %}

</table>

</div>

</div>
{% endfor %}
