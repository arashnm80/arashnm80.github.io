require 'yaml'

module Jekyll
  class RedirectsGenerator < Generator
    safe true

    def generate(site)
      redirects = YAML.load_file('_redirects.yml')['redirects']
      redirects.each do |redirect|
        create_redirect_page(site, redirect['from'], redirect['to'])
      end
    end

    def create_redirect_page(site, from, to)
      site.pages << RedirectPage.new(site, site.source, from, to)
    end
  end

  class RedirectPage < Page
    def initialize(site, base, from, to)
      @site = site
      @base = base
      @dir  = from
      @name = 'index.html'

      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'redirect.html')
      self.data['redirect_to'] = to
    end
  end
end
