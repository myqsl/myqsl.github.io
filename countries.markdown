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

{% assign qsls_count = 0 %}
{% for station in site.stations %}
    {% if station.country == country.code %}
        {% for qsl in site.posts %}
            {% for reception in qsl.receptions %}
                {% if reception.station == station.code %}
                    {% assign qsls_count = qsls_count | plus: 1 %}
                    {% break %}
                {% endif %}
            {% endfor %}
        {% endfor %}
    {% endif %}
{% endfor %}

{% if qsls_count == 0 %}
{{ country.title }}
{% else %}
<a href="{{ country.url }}">{{ country.title }}</a><sup>{{ qsls_count }}</sup>
{% endif %}

{% endfor %} <!-- for country -->
</p>

</div>
</div>
{% endfor %} <!-- for continent --> 
