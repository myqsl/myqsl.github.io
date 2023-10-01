---
layout: page
title: By correspondents
permalink: /correspondents/
---

{% for broadcaster in site.broadcasters %}

{% assign qsls = site.posts | where: 'broadcaster', broadcaster.code %}

<div class="rounded-box">
<div class="header">
<h2><a href="{{ broadcaster.url }}">{{ broadcaster.title }}</a></h2>
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
