---
layout: page
title: QSL list
---

{% assign continents = site.countries | map: 'continent' | sort | uniq %}

{% for continent in continents %}

{% assign countries = site.countries | where: 'continent', continent %}

{% if countries.size == 0 %}
	{% continue %}
{% endif %}

<div class="qsl-titles-structure">

<p><strong>{{ continent | upcase }}</strong></p>


{% for country in countries %}

{% assign series = site.series | where: 'country', country.code %}

{% if series.size == 0 %}
	{% continue %}
{% endif %}


{% for serie in series %}

{% assign qsls = site.posts | where: 'serie', serie.code %}

{% if qsls.size == 0 %}
	{% continue %}
{% endif %}

<p>{{ country.title | upcase }} &mdash; <a href="{{ serie.url }}">{{ serie.title }}</a>:</p>
<ul>
{% for qsl in qsls %}
	{% for reception in qsl.receptions %}
		<li><a href="{{ serie.url }}#{{ qsl.date | date: "%Y-%m-%d" }}">
		{{ reception.frequency }}</a>
		{% if reception.station %}
		{% assign station = site.stations | where: 'code', reception.station | first %}
		<a href="/sites#{{ station.code }}">{{ station.short }}</a>
		{% endif %}
        {% if reception.language %}
        in {{ reception.language }}
        {% endif %}
		{% if reception.date %}
		on {{ reception.date }}
		{% endif %}
		</li>
		
	{% endfor %}
{% endfor %}
</ul>

{% endfor %}
{% endfor %}

</div>

{% endfor %}
