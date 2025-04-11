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

<p style="text-align:center"><a href="/pirates/">Pirates stations</a> | <a href="/private/">Private stations</a> | <a href="/utility/">Utility stations</a></p>


{% assign stations_group_by_country = site.data['stations'] | values | group_by: 'country' | groups_to_hash %}
{% assign countries_ordered = stations_group_by_country | keys | sort %}

{% for country_code in countries_ordered %}

{% assign stations = stations_group_by_country[country_code] %}
{% assign country = site.data['countries'][country_code] %}
{% assign country_flag = country['flag'] %}
{% assign country_title = country['title'] %}

<div class="rounded-box">
<header><h2>{% if country_code != "unid" %}<img class="flag" src="{{ country_flag }}"/>{% endif %}
{{ country_title }}</h2></header>

{% for station in stations %}
{% assign station_code = station['code'] %}
{% assign station_title = station['title'] %}
{% assign qsls = site | qsls_for_station: station_code %}
<p>&mdash; <a href="/stations/{{ station_code }}.html">{{ station_title }}</a> | qsls: {{ qsls.size }}</p>
{% endfor %}

</div>

{% endfor %}


