---
layout: page
title: Issuers (countries)
permalink: /issuersc/
---

<div class="rounded-box">
<p style="padding: 10px 10px 10px 10px;">Here is the list of organizations
that have issued a confirmation of the listening to their programs.
Organizations are ordered by country if identified.
Have a nice reading!
</p>
</div>

{% assign c = "" %}
{% for issuer in site.series %}

    {% if issuer.country == nil %}
        {% continue %}
    {% endif %}

    {% if c == empty  %}
        {% assign c = issuer.country %}
    {% else %}
        {% assign c = c | append: ":" | append: issuer.country %}
    {% endif %}

{% endfor %}

<!-- array of country.codes; ordered by country.code -->
{% assign countries1_codes = c | split: ":" | sort | uniq %}

<!-- resort by country.title + unid -->
{% assign countries_list = "" %}
{% assign countries_orderedby_title = site.countries | sort: "title" %}
{% for country in countries_orderedby_title %}
    {% for code in countries1_codes %}
        {% if country.code == code %}
            {% if countries_list == empty %}
                {% assign countries_list = code %}
            {% else %}
                {% assign countries_list = countries_list | append: ":" | append: code %}
            {% endif %}
            {% break %}
        {% endif %}
    {% endfor %}
{% endfor %}
{% assign countries = countries_list | append: ":unid" | split: ":" %}



{% for country_code in countries %}

{% if country_code == "unid" %}
    {% assign country_title = "Unidentified" %}
{% else %}
    {% assign country = site.countries | where: "code", country_code | first %}
    {% assign country_title = country.title %}
    {% assign country_flag = country.flag %}
{% endif %}

<div class="rounded-box">
<header><h2>{% if country_code != "unid" %}<img class="flag" src="{{ country_flag }}"/>{% endif %}
{{ country_title }}</h2></header>

{% for issuer in site.series %}

{% if issuer.country and issuer.country != country_code %}
    {% continue %}
{% elsif issuer.country == nil and country_code != "unid" %}
    {% continue %}
{% endif %}

{% assign qsls = site.posts | where: 'serie', issuer.code %}

<p>&mdash; <a href="{{ issuer.url }}">{{ issuer.title }}</a> | qsls: {{ qsls.size }}</p>

{% endfor %} <!-- issuer -->
</div>
{% endfor %} <!-- country_code -->
