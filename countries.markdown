---
layout: page
title: Countries
permalink: /countries/
---

<div class="rounded-box">
<p style="padding: 10px 10px 10px 10px;">
Here is the list of countries of transmitting
stations (sites) with count of qsls for transmissions
from that station.
Have a nice reading!
</p>
</div>

{% assign continents = site | continents_structure %}

{% for continent_pair in continents %}
{% assign continent = continent_pair[0] %}
{% assign countries = continent_pair[1] %}
{% assign countries_ordered = countries | keys | sort %}

<div class="rounded-box">
<div class="header">
<h2>{{ continent }}</h2>
</div>

<div style="padding: 15px 5px 5px 15px;">

<p>
{% for country_code in countries_ordered %}
{% assign country_structure = countries[country_code] %}
{% assign country_url = country_structure['url'] %}
{% assign country_title = country_structure['title'] %}
{% assign qsls_count = country_structure['qsls_count'] %}

{%- if forloop.index > 1 -%}&bullet;&nbsp;{%- endif -%}

{% if qsls_count == 0 %}
{{ country_title }}
{% else %}
<a href="{{ country_url }}">{{ country_title }}</a><sup>{{ qsls_count }}</sup>
{% endif %}

{% endfor %} <!-- for country -->
</p>

</div>
</div>
{% endfor %} <!-- for continent --> 
