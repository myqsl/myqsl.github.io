---
layout: page
title: Countries
permalink: /countries/
---

<div class="rounded-box">
<p style="padding: 10px 10px 10px 10px;">
Here is the list of countries of transmitting
stations (sites).
Have a nice reading!
</p>
</div>

{% assign continents = site.countries | map: 'continent' | uniq | sort %}

{% for continent in continents %}

<div class="rounded-box">
<div class="header">
<h2>{{ continent }}</h2>
</div>

<div style="padding: 15px 5px 5px 15px;">

{% assign countries = site.countries | where: 'continent', continent | sort: 'code' %}

<p>
{% for country in countries %}

{%- if forloop.index > 1 -%}&bullet;&nbsp;{%- endif -%}
<a href="{{ country.url }}">{{ country.title }}</a>

{% endfor %} <!-- for country -->
</p>

</div>
</div>
{% endfor %} <!-- for continent --> 
