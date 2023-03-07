---
layout: page
title: Transmitters
permalink: /transmitters/
---
<!--
Confirmed stations map:

<script type="text/javascript" charset="utf-8" async src="https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3Aa664fe2bf48cab289503df614ecbbf1af25ebbf3aa075c9f9fd48708148e5e77&amp;width=100%25&amp;height=311&amp;lang=ru_RU&amp;scroll=true"></script>

<br/>
-->

{% assign continents = site.transmitters | map: 'continent' | uniq | sort %}

{% for continent in continents %}

<br/>
<h3>{{ continent }}</h3>

{% assign countries = site.transmitters | where: 'continent', continent | map: 'country' | uniq | sort %}

{% for c in countries %}
    {% assign transmitters = site.transmitters | where: 'country', c | sort: 'title' %}
    {% for t in transmitters %}

<h4><a href="{{ t.url }}">{{ c }} &mdash; {{ t.title }}</a></h4>

{% assign transmitter_qsls = site.qsls | where: 'transmitter', t.code | sort: 'reception_date' %}
{% for q in transmitter_qsls %}
<div class="latest-qsl">
{% assign station = site.stations | where: 'code', q.station | first %}
<code>{{ q.reception_date }} {{ q.reception_time }}</code>
<a href="{{ q.url }}">
{{ q.kind }}
    | {{ q.frequency }}
    | {{ station.title }}
    | {{ q.language }}
</a>
</div>
{% endfor %}
{% endfor %}
{% endfor %}
{% endfor %}
