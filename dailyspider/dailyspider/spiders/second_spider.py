import scrapy


class SecondSpider(scrapy.Spider):
    name = 'second'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def raspagem(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").extract_first(),
                'author': quote.css("span > small.author::text").extract_first(),
                'tags': quote.css("a.tag::text").extract()
}

    def parse(self, response):
            page = response.url.split("/")[-2]
            filename = 'second-%s.html' % page
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)