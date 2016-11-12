import scrapy


class GloboSpider(scrapy.Spider):
    name = "globo"

    def start_requests(self):
        urls = [
            'http://g1.globo.com/economia/noticia/2016/11/pib-da-regiao-norte-deve-ter-o-maior-crescimento-em-2017-diz-estudo.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def scraping_daily(self, response):
        for d in response.css("glb-conteudo"):
            yield {
            'title': response.css('h1.entry-title::text').extract(),
            'date':response.css('published::text').extract(),
            'update':response.css('updated::text').extract(),
            'author':response.css('vcard::text').extract(),
            #'content':response.css('materia-letra::text').extract()
            }

    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'globo-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

'''


'''