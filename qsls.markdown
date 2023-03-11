---
layout: page
title: QSLs
permalink: /qsls/
---
{% assign qsls = site.qsls | sort: 'title' %}
<!--
{% for q in qsls %}
<p><a href="{{ q.url }}">{{ q.title}}</a></p>
{% endfor %}
-->
{% for qsl in qsls %}
<!--  <div class="latest-qsl"> -->
<p>
    {% assign station = site.stations | where: 'code', qsl.station | first %}
    <code>{{ qsl.reception_date }} {{ qsl.reception_time }}</code> 
    <a href="{{ qsl.url }}">
    {{ qsl.kind }}
        from {{ station.title }}
        | {{ qsl.frequency }}
        {% assign tx = site.transmitters | where: 'code', qsl.transmitter | first %}
        {% assign country = site.countries | where: 'code', tx.country | first %}
        | {{ tx.title }}, {{ country.title }}
    </a>
<!--  </div>
  <div style="clear:both">&nbsp;</div> -->
</p>
{% endfor %}


