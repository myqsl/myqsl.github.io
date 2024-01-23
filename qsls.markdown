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

    {% if itu == 'EGY' %}{% assign itu_title = 'EGYPT' %}
    {% elsif itu == 'MDG' %}{% assign itu_title = 'MADAGASCAR' %}
    {% elsif itu == 'SWZ' %}{% assign itu_title = 'eSWATINI' %}
    {% elsif itu == 'ALS' %}{% assign itu_title = 'ALASKA' %}
    {% elsif itu == 'B' %}{% assign itu_title = 'BRAZIL' %}
    {% elsif itu == 'CAN' %}{% assign itu_title = 'CANADA' %}
    {% elsif itu == 'CLM' %}{% assign itu_title = 'COLOMBIA' %}
    {% elsif itu == 'CUB' %}{% assign itu_title = 'CUBA' %}
    {% elsif itu == 'EQA' %}{% assign itu_title = 'EQUADOR' %}
    {% elsif itu == 'USA' %}{% assign itu_title = 'UNITED STATES OF AMERICA' %}
    {% elsif itu == 'ATA' %}{% assign itu_title = 'ANTARCTIDA' %}
    {% elsif itu == 'ARM' %}{% assign itu_title = 'ARMENIA' %}
    {% elsif itu == 'CHN' %}{% assign itu_title = 'CHINA' %}
    {% elsif itu == 'CLN' %}{% assign itu_title = 'SRI LANKA' %}
    {% elsif itu == 'IND' %}{% assign itu_title = 'INDIA' %}
    {% elsif itu == 'KOR' %}{% assign itu_title = 'REPUBLIC OF KOREA' %}
    {% elsif itu == 'MNG' %}{% assign itu_title = 'MONGOLIA' %}
    {% elsif itu == 'PHL' %}{% assign itu_title = 'PHILIPPINES' %}
    {% elsif itu == 'THA' %}{% assign itu_title = 'THAILAND' %}
    {% elsif itu == 'TJK' %}{% assign itu_title = 'TAJIKISTAN' %}
    {% elsif itu == 'TUR' %}{% assign itu_title = 'TURKIYE' %}
    {% elsif itu == 'UAE' %}{% assign itu_title = 'UNITED ARABIC EMIRATES' %}
    {% elsif itu == 'VTN' %}{% assign itu_title = 'VIETNAM' %}
    {% elsif itu == 'ASC' %}{% assign itu_title = 'ASCENSION ISLANDS' %}
    {% elsif itu == 'AUT' %}{% assign itu_title = 'AUSTRIA' %}
    {% elsif itu == 'BUL' %}{% assign itu_title = 'BULGARIA' %}
    {% elsif itu == 'CVA' %}{% assign itu_title = 'VATICAN CITY' %}
    {% elsif itu == 'CZE' %}{% assign itu_title = 'CZECHIA' %}
    {% elsif itu == 'D' %}{% assign itu_title = 'GERMANY' %}
    {% elsif itu == 'DNK' %}{% assign itu_title = 'DENMARK' %}
    {% elsif itu == 'E' %}{% assign itu_title = 'SPAIN' %}
    {% elsif itu == 'F' %}{% assign itu_title = 'FRANCE' %}
    {% elsif itu == 'FIN' %}{% assign itu_title = 'FINLAND' %}
    {% elsif itu == 'G' %}{% assign itu_title = 'GREAT BRITAIN' %}
    {% elsif itu == 'GRC' %}{% assign itu_title = 'GREECE' %}
    {% elsif itu == 'HOL' %}{% assign itu_title = 'THE NETHERLANDS' %}
    {% elsif itu == 'I' %}{% assign itu_title = 'ITALIA' %}
    {% elsif itu == 'LTU' %}{% assign itu_title = 'LITHUANIA' %}
    {% elsif itu == 'LVA' %}{% assign itu_title = 'LATVIA' %}
    {% elsif itu == 'MDA' %}{% assign itu_title = 'MOLDAVIA/PRIDNESTROVIE' %}
    {% elsif itu == 'ROU' %}{% assign itu_title = 'ROMANIA' %}
    {% elsif itu == 'RUS' %}{% assign itu_title = 'RUSSIA' %}
    {% elsif itu == 'AUS' %}{% assign itu_title = 'AUSTRALIA' %}
    {% elsif itu == 'GUM' %}{% assign itu_title = 'GUAM' %}
    {% elsif itu == 'MRA' %}{% assign itu_title = 'MARIANA ISLANDS' %}
    {% elsif itu == 'PLW' %}{% assign itu_title = 'PALAU' %}
    {% elsif itu == 'VUT' %}{% assign itu_title = 'VANUATU' %}
    {% else %}{% assign itu_title = itu %}
    {% endif %}

    {% assign qsls = site.posts | where: 'station', station.code %}

    {% if qsls.size > 0 %}

<br/><strong>&bullet; {{ itu_title  }} <a href="{{ station.url }}">{{ station_title }}</a></strong>
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
