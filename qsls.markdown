---
layout: page
title: QSL list
permalink: /qsls/
---

<div class="rounded-box">
<p style="padding: 10px 10px 10px 10px; margin-bottom: 0px;">Here is
the list of my qsls.
It is ordered by ITU (country).
Click on date of the reception to get more information about QSL.
Have a nice reading!
</p>
</div>

{% assign qsls_group_by_itu = site | qsls_stations_by_itu %}
{% assign itu_codes_ordered = qsls_group_by_itu | keys | sort %}

<div class="large-itu-list">

<div class="itu-list">
{% for itu_code in itu_codes_ordered %}

{% assign qsls_stations_by_issuer = qsls_group_by_itu[itu_code] %}

<p class="qsls-itu-list">

{% assign itu_index = forloop.index %}

{% assign previous_index = nil %}
{% assign previous_itu_code = nil %}
{% assign previous_issuer_title = nil %}
{% assign previous_station_short = nil %}

{% assign series_ordered = qsls_stations_by_issuer | keys | sort %}
{% for issuer_code in series_ordered %}

{% assign qsls_this_issuer = qsls_stations_by_issuer[issuer_code]['qsls'] %}

{% if qsls_this_issuer.size == 0 %}
    {% continue %}
{% endif %}

{% assign stations_this_issuer = qsls_stations_by_issuer[issuer_code]['stations'] %}
{% assign max_station_short_len = nil %}
                        {% for s in stations_this_issuer %}
                            {% if s.short %}
                                {% assign max_station_short_len = max_station_short_len | default: 0 | at_least: s.short.size %}
                            {% endif %}
                        {% endfor %}

{% for qsl in qsls_this_issuer %}
{% for reception in qsl.receptions %}
{% assign frequency = reception.frequency | split: ' kHz' | first %}

{% if itu_index < 10 %}
    {% assign index = itu_index | prepend: "0" %}
{% else %}
    {% assign index = itu_index %}
{% endif %}


{% assign itu_upcased = itu_code | upcase %}
{% if itu_upcased.size == 1 %}
    {% assign itu_upcased = itu_upcased | append: "&nbsp;&nbsp;" %}
{% endif %}


{% assign itu_title = site.data['itus'][itu_code]['title'] | truncate: 9, "" %}
{% for i in (itu_title.size .. 8) %}
    {% assign itu_title = itu_title | append: "&nbsp;" %}
{% endfor %}


{% if max_station_short_len %}
    {% assign it = 30 | minus: max_station_short_len | minus: 2 %} <!-- 2 for ", " -->
{% else %}
    {% assign it = 30 %}
{% endif %}
{% assign issuer_title = site.data['series'][issuer_code]['title'] | truncate: it, "" %}
{% assign station_short = site.data['stations'][reception['station']].short %}


{% if previous_index == nil %}
    {% assign index_to_show = index %}
{% elsif previous_index == index %}
    {% assign index_to_show = "&nbsp;&nbsp;" %}
{% else %}
    {% assign index_to_show = index %}
{% endif %}


{% if previous_itu_code == nil %}
    {% assign itu_code_to_show = itu_upcased %}
{% elsif previous_itu_code == itu_upcased %}
    {% assign itu_code_to_show = "&nbsp;&nbsp;&nbsp;" %}
{% else %}
    {% assign itu_code_to_show = itu_upcased %}
{% endif %}


{% if previous_itu_title == nil %}
    {% assign itu_title_to_show = itu_title %}
{% elsif previous_itu_title == itu_title %}
    {% assign itu_title_to_show = "" %}
    {% for i in (1 .. 9) %}
        {% assign itu_title_to_show = itu_title_to_show | append: "&nbsp;" %}
    {% endfor %}
{% else %}
    {% assign itu_title_to_show = itu_title %}
{% endif %}


{% if previous_issuer_title == nil %}
    {% assign issuer_title_to_show = issuer_title %}
{% elsif previous_issuer_title == issuer_title %}
    {% assign issuer_title_to_show = "" %}
    {% for i in (1 .. issuer_title.size) %}
        {% assign issuer_title_to_show = issuer_title_to_show | append: "&nbsp;" %}
    {% endfor %}
{% else %}
    {% assign issuer_title_to_show = issuer_title %}
{% endif %}

{% if station_short %}

    {% if previous_station_short == station_short %}
        {% if previous_issuer_title == issuer_title %}
            {% assign station_short_to_show = "" %}
            {% for i in (1 .. station_short.size) %}
                {% assign station_short_to_show = station_short_to_show | append: "&nbsp;" %}
            {% endfor %}
            {% assign station_short_to_show = station_short_to_show | prepend: "&nbsp;&nbsp;" %}
        {% else %}
            {% assign station_short_to_show = station_short %}
            {% assign station_short_to_show = station_short_to_show | prepend: ",&nbsp;" %}
        {% endif %}
    {% else %}
        {% assign station_short_to_show = station_short %}
        {% assign station_short_to_show = station_short_to_show | prepend: ",&nbsp;" %}
    {% endif %}

    {% assign m = issuer_title.size | plus: 2 | plus: station_short.size | plus: 1 %}
    {% for i in (m .. 30) %}
        {% assign station_short_to_show = station_short_to_show | append: "&nbsp;" %}
    {% endfor %}

{% else %}

    {% assign station_short_to_show = "" %}
    {% assign m = issuer_title.size | plus: 1 %}
    {% for i in (m .. 30) %}
        {% assign station_short_to_show = station_short_to_show | append: "&nbsp;" %}
    {% endfor %}

{% endif %}


{% assign frequency_to_show = frequency %}
{% for i in (frequency.size .. 6) %}
    {% assign frequency_to_show = frequency_to_show | prepend: "&nbsp;" %}
{% endfor %}


{{ index_to_show }}&nbsp;&nbsp;{{ itu_code_to_show }}&nbsp;&nbsp;{{ itu_title_to_show }}&nbsp;&nbsp;{{ issuer_title_to_show }}{{ station_short_to_show }}{{ frequency_to_show }}&nbsp;&nbsp;<a href="{{ qsl.url }}">{{ reception.date }}</a><br/>



{% assign previous_index = index %}
{% assign previous_itu_code = itu_upcased %}
{% assign previous_itu_title = itu_title %}
{% assign previous_issuer_title = issuer_title %}
{% assign previous_station_short = station_short %}


{% endfor %} <!-- reception -->
{% endfor %} <!-- qsl -->

{% endfor %} <!-- issuer -->
</p>
{% endfor %} <!-- itu -->
</div>

</div><!-- large-itu-list -->

<div class="small-itu-list">

<div class="itu-list">
{% for itu_code in itu_codes_ordered %}
{% assign qsls_stations_by_issuer = qsls_group_by_itu[itu_code] %}

<p class="qsls-itu-list">

{% assign itu_index = forloop.index %}

{% assign previous_index = nil %}
{% assign previous_itu_code = nil %}
{% assign previous_issuer_title = nil %}
{% assign previous_station_short = nil %}

{% assign series_ordered = qsls_stations_by_issuer | keys | sort %}
{% for issuer_code in series_ordered %}

{% assign qsls_this_issuer = qsls_stations_by_issuer[issuer_code]['qsls'] %}
{% if qsls_this_issuer.size == 0 %}
    {% continue %}
{% endif %}

{% assign stations_this_issuer = qsls_stations_by_issuer[issuer_code]['stations'] %}
{% assign max_station_short_len = nil %}
                        {% for s in stations_this_issuer %}
                            {% if s.short %}
                                {% assign max_station_short_len = max_station_short_len | default: 0 | at_least: s.short.size %}
                            {% endif %}
                        {% endfor %}

{% for qsl in qsls_this_issuer %}
{% for reception in qsl.receptions %}
{% assign frequency = reception.frequency | split: ' kHz' | first %}

{% if itu_index < 10 %}
    {% assign index = itu_index | prepend: "0" %}
{% else %}
    {% assign index = itu_index %}
{% endif %}


{% assign itu_upcased = itu_code | upcase %}
{% if itu_upcased.size == 1 %}
    {% assign itu_upcased = itu_upcased | append: "&nbsp;&nbsp;" %}
{% endif %}


{% if max_station_short_len %}
    {% assign it = 28 | minus: max_station_short_len | minus: 2 %} <!-- 2 for ", " -->
{% else %}
    {% assign it = 28 %}
{% endif %}
{% assign issuer_title = site.data['series'][issuer_code]['title'] | truncate: it, "" %}
{% assign station_short = site.data['stations'][reception['station']].short %}


{% if previous_index == nil %}
    {% assign index_to_show = index %}
{% elsif previous_index == index %}
    {% assign index_to_show = "&nbsp;&nbsp;" %}
{% else %}
    {% assign index_to_show = index %}
{% endif %}


{% if previous_itu_code == nil %}
    {% assign itu_code_to_show = itu_upcased %}
{% elsif previous_itu_code == itu_upcased %}
    {% assign itu_code_to_show = "&nbsp;&nbsp;&nbsp;" %}
{% else %}
    {% assign itu_code_to_show = itu_upcased %}
{% endif %}


{% if previous_issuer_title == nil %}
    {% assign issuer_title_to_show = issuer_title %}
{% elsif previous_issuer_title == issuer_title %}
    {% assign issuer_title_to_show = "" %}
    {% for i in (1 .. issuer_title.size) %}
        {% assign issuer_title_to_show = issuer_title_to_show | append: "&nbsp;" %}
    {% endfor %}
{% else %}
    {% assign issuer_title_to_show = issuer_title %}
{% endif %}

{% if station_short %}

    {% if previous_station_short == station_short %}
        {% if previous_issuer_title == issuer_title %}
            {% assign station_short_to_show = "" %}
            {% for i in (1 .. station_short.size) %}
                {% assign station_short_to_show = station_short_to_show | append: "&nbsp;" %}
            {% endfor %}
            {% assign station_short_to_show = station_short_to_show | prepend: "&nbsp;&nbsp;" %}
        {% else %}
            {% assign station_short_to_show = station_short %}
            {% assign station_short_to_show = station_short_to_show | prepend: ",&nbsp;" %}
        {% endif %}
    {% else %}
        {% assign station_short_to_show = station_short %}
        {% assign station_short_to_show = station_short_to_show | prepend: ",&nbsp;" %}
    {% endif %}

    {% assign m = issuer_title.size | plus: 2 | plus: station_short.size | plus: 1 %}
    {% for i in (m .. 28) %}
        {% assign station_short_to_show = station_short_to_show | append: "&nbsp;" %}
    {% endfor %}

{% else %}

    {% assign station_short_to_show = "" %}
    {% assign m = issuer_title.size | plus: 1 %}
    {% for i in (m .. 28) %}
        {% assign station_short_to_show = station_short_to_show | append: "&nbsp;" %}
    {% endfor %}

{% endif %}


{% assign frequency_to_show = frequency %}
{% for i in (frequency.size .. 6) %}
    {% assign frequency_to_show = frequency_to_show | prepend: "&nbsp;" %}
{% endfor %}


{{ index_to_show }}&nbsp;&nbsp;{{ itu_code_to_show }}&nbsp;&nbsp;{{ issuer_title_to_show }}{{ station_short_to_show }}<a href="{{ qsl.url }}">{{ frequency_to_show }}</a><br/>



{% assign previous_index = index %}
{% assign previous_itu_code = itu_upcased %}
{% assign previous_issuer_title = issuer_title %}
{% assign previous_station_short = station_short %}


{% endfor %} <!-- reception -->
{% endfor %} <!-- qsl -->

{% endfor %} <!-- issuer -->
</p>
{% endfor %} <!-- itu -->
</div>


</div><!-- small-itu-list --> 