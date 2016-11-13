import scrapy


class GloboSpider(scrapy.Spider):
    name = "globo"

    def start_requests(self):
        urls = [
            'http://g1.globo.com/economia/noticia/2016/11/pib-da-regiao-norte-deve-ter-o-maior-crescimento-em-2017-diz-estudo.html',
            'http://g1.globo.com/politica/noticia/2016/11/stf-manda-uniao-depositar-em-juizo-cota-da-repatriacao-de-mais-16-estados.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.scraping_daily)

    #funcao para visitar paginas seguintesS

            
    def scraping_daily(self, response):
        xpath_clear = ".//*[not(self::script or self::style)]/text()[normalize-space(.)]" 
        #for d in response.css("glb-conteudo"):
        yield {
            'title': response.css('h1.entry-title').xpath("string(.)").extract_first(),
            'date':response.css('.materia-cabecalho .published::text').extract_first(),
            'update':response.css('.materia-cabecalho .updated::text').extract_first(),
            'author':response.css('.materia-assinatura .vcard').xpath("string(.)").extract_first(),
            'content': ' '.join(response.css('.materia-conteudo').xpath(xpath_clear).extract()) #retorna texto sem as tags html

            #response.css('.materia-conteudo::text').xpath(".").extract_first() 
            
            }



    
