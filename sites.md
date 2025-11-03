---
layout: page
title: Transmission sites
---

{% assign continents = site.countries | map: 'continent' | sort | uniq %}

{% for continent in continents %}

{% assign countries = site.countries | where: 'continent', continent %}

{% if countries.size == 0 %}
	{% continue %}
{% endif %}

<div class="qsl-titles-structure">

<p><strong>{{ continent | upcase }}</strong></p>
<ul>

{% for country in countries %}

{% assign stations = site.stations | where: 'country', country.code %}

{% if stations.size == 0 %}
	{% continue %}
{% endif %}

{% for station in stations %}

{% assign qsls = site.posts %}

<li><details class="tiny-link"><summary>{{ country.title | upcase }} &mdash; {{ station.title }}</summary>
	<ul>
		{% for qsl in qsls %}
			{% assign serie = site.series | where: 'code', qsl.serie | first %}
			{% for reception in qsl.receptions %}
				{% if reception.station == station.code %}
					<li><a href="{{ serie.url }}#{{ qsl.date | date: "%Y-%m-%d" }}">
					{{ serie.title }} ({{ reception.language }})
					on {{ reception.frequency }}
					{% if reception.date %}
					on {{ reception.date }}
					{% endif %}
					</a></li>
				{% endif %}
			{% endfor %}
		{% endfor %}
	</ul>
</details></li>

{% endfor %}

{% endfor %}

</ul>
</div>

{% endfor %}
