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

<p><a href="{{ serie.url }}">{{ country.title | upcase }} &mdash; {{ serie.title }}</a>:</p>
<ul>
{% for qsl in qsls %}
	{% for reception in qsl.receptions %}
		<li><a href="{{ serie.url }}#{{ qsl.date | date: "%Y-%m-%d" }}">
		{{ reception.frequency }}
		{% if reception.date %}
		on {{ reception.date }}
		{% endif %}
		{% if reception.station %}
		{% if serie.station == nil or serie.station != reception.station %}
		{% assign station = site.stations | where: 'code', reception.station | first %}
		via {{ station.title }}
			{% if station.country != country.code %}
			{% assign station_country = site.countries | where: 'code', station.country | first %}
			({{ station_country.title }})
			{% endif %}
		{% endif %}
		{% endif %}
		</a></li>
		
	{% endfor %}
{% endfor %}
</ul>

{% endfor %}
{% endfor %}

</div>

{% endfor %}
