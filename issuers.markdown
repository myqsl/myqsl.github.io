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

{% assign issuers = site.data['series'] | values | sort: 'title' %}

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

{% assign theletter = issuer['title'] | truncate: 1, "" %}
{% if letter == theletter %}

{% assign issuer_code = issuer['code'] %}
{% assign issuer_title = issuer['title'] %}
{% assign qsls = site | qsls_for_serie: issuer['code']  %}

<p>&mdash; <a href="/series/{{ issuer_code }}.html">{{ issuer_title }}</a> | qsls: {{ qsls.size }}</p>

{% endif %}
{% endfor %} <!-- issuer -->
</div>
{% endfor %} <!-- letter -->
