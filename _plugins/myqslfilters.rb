module MyqslFilters

  def keys(input)
    input.keys
  end

  def values(input)
    input.values
  end

  def continents_structure(site)

    continents = Hash.new do |hash, continent|
      hash[continent] = Hash.new do |hash, country_code|

        country = site.data.fetch('countries').fetch(country_code)

        hash[country_code] = {
          "title"=>country.fetch('title'),
          "url"=>"/countries/#{country_code}.html",
          "qsls_count"=>0,
        }
      end
    end

    site.posts.each do |qsl|

      if qsl['receptions']

        countries = []
        qsl['receptions'].each do |reception|
          if reception['station']
            station_code = reception.fetch('station')
            station = site.data.fetch('stations').fetch(station_code)
            countries << station.fetch('country')
          end
        end

        countries.uniq.each do |country_code|

          country = site.data['countries'].fetch(country_code)
          continent = country.fetch('continent')
  
          continents[continent][country_code]["qsls_count"] += 1
        end
      end
    end

    continents

  end

  def groups_to_hash(groups)
    h = {}
    groups.each do |item|
      name = item.fetch('name')
      items = item.fetch('items')
      h[name] = items
    end
    h
  end

  def qsls_stations_by_itu(site)
    itus = Hash.new do |hash, itu|
      hash[itu] = Hash.new do |hash, issuer|
        hash[issuer] = {
          'qsls' => [],
          'stations' => [],
        }
      end
    end

    site.posts.each do |qsl|
      qsl['receptions']&.each do |reception|        
        if reception['station']
          station = site.data['stations'].fetch(reception['station'])
          itu = station.fetch('itu')
          issuer_code = qsl['serie']

          if ! itus[itu][issuer_code]['qsls'].include?(qsl)
            itus[itu][issuer_code]['qsls'] << qsl
            itus[itu][issuer_code]['stations'] << station
          end
        end
      end
    end

    itus
  end

  # hash from station code to array<qsl>
  @@qsls_of_stations = Hash.new { |hash, station_code| hash[station_code] = [] }

  def qsls_for_station(site, station_code)

    if @@qsls_of_stations.size == 0
      # initialise the full structure
      site.posts.each do |qsl|
        qsl['receptions']&.each do |reception|
            if ! @@qsls_of_stations[reception['station']].include?(qsl)
                @@qsls_of_stations[reception['station']] << qsl
            end
        end
      end
    end

    @@qsls_of_stations[station_code]
  end

  # hash from serie code to array<qsl>
  @@qsls_of_series = Hash.new { |hash, serie_code| hash[serie_code] = [] }

  def qsls_for_serie(site, serie_code)

    if @@qsls_of_series.size == 0
      # initialise the full structure
      site.posts.each do |qsl|
        @@qsls_of_series[qsl['serie']] << qsl
      end
    end

    @@qsls_of_series[serie_code]
  end
  
  
end
  
Liquid::Template.register_filter(MyqslFilters)