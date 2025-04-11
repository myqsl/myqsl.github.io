module DataPages

    class DataPageGenerator < Jekyll::Generator
        safe true

        def generate(site)
            ['countries', 'series', 'stations'].each do |category|
                site.data[category].each do |name, item|
                    site.pages << DataPage.new(site, name, item, category)
                end
            end
        end
    end

    class DataPage < Jekyll::Page
        def initialize(site, name, item, dir)
            @site = site
            @base = site.source
            @dir = dir

            @basename = name
            @ext = '.html'
            @name = name + '.html'

            @data = item.clone
            data.default_proc = proc do |_, key|
                site.frontmatter_defaults.find(relative_path, dir, key)
            end
        end

        def url_placeholders
            {
                :path => @dir,
                :basename => basename,
                :output_ext => output_ext,
                :name => @name,
            }
        end
    end

end