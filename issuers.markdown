---
layout: page
title: Issuers (abc)
permalink: /issuers/
---

<div class="rounded-box">
<p style="padding: 10px 10px 10px 10px;">Here is the list of organizations
that have issued a confirmation of the listening to their programs.
Organizations are ordered by name.
Have a nice reading!
</p>
</div>

{% assign issuers = site.series | sort: 'title' %}

{% assign titles = issuers | map: 'title' %}
{% assign letters = empty %}
{% for title in titles %}
    {% assign letter = title | truncate: 1, "" | split: "," %}
    {% assign letters = letters | concat: letter %}
{% endfor %}
{% assign letters = letters | sort | uniq %}

{% for letter in letters %}

<div class="rounded-box">
<header><h2>{{ letter }}</h2></header>

{% for issuer in issuers %}

{% assign theletter = issuer.title | truncate: 1, "" %}
{% if letter == theletter %}

{% assign qsls = site.posts | where: 'serie', issuer.code %}

<details>
<summary>{{ issuer.title }}<sup>{{ qsls.size }}</sup><a href="{{ issuer.url }}"><em>pictures</em></a></summary>

<ul>

{% for qsl in qsls %}
    <li><a href="{{ qsl.url }}">{{ qsl.title }}</a> &bullet; {{ qsl.frequency }} &bullet; {{ qsl.reception_date }} {{ qsl.reception_time }}</li>    
{% endfor %}
</ul>

</details>
{% endif %}
{% endfor %} <!-- issuer -->
</div>
{% endfor %} <!-- letter -->
