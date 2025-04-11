---
layout: page
title: Gallery
permalink: /gallery/
---

<div class="rounded-box">
<p style="padding: 10px 10px 10px 10px;">
Here is the list of QSL series.
There are different sources for the series.
Mostly there are come from serie or
program owner. But transmitter station team
may issue QSL cards also.
Have a nice reading!
</p>
</div>

{% assign qsls_group_by_serie = site.posts | group_by: 'serie' %}

{% for qsl_group in qsls_group_by_serie %}

{% assign serie_code = qsl_group['name'] %}
{% assign qsls = qsl_group['items'] %}
{% assign serie = site.data['series'][serie_code] %}
{% assign serie_title = serie['title'] %}

<div class="rounded-box">
<div class="header">
<h2><a href="/series/{{ serie_code }}.html">{{ serie_title }}</a></h2>
</div><!-- header -->

<div style="padding-bottom: 10px">
{% for qsl in qsls %}
{% for image in qsl.gallery %}
{% assign full_small = image | split: ":" %}
<a href="{{ qsl.url }}">
<img class="gallery" src="{% if full_small[1] %}{{ full_small[1] }}{% else %}{{ full_small[0] }}{% endif %}" />
</a>
{% endfor %}
{% endfor %}
</div> <!-- gallery -->
</div> <!-- rounded-box -->
{% endfor %}
