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

{% for serie in site.series %}

{% assign qsls = site.posts | where: 'serie', serie.code %}

<div class="rounded-box">
<div class="header">
<h2><a href="{{ serie.url }}">{{ serie.title }}</a></h2>
</div>

<div style="padding-bottom: 10px">
{% for qsl in qsls %}
{% for image in qsl.gallery %}
{% assign full_small = image | split: ":" %}
<a href="{{ qsl.url }}">
<img class="gallery" src="{% if full_small[1] %}{{ full_small[1] }}{% else %}{{ full_small[0] }}{% endif %}" />
</a>
{% endfor %}
{% endfor %}
</div>
</div>
{% endfor %}
