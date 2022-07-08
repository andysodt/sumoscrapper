import scrapy

class BrickSetSpider(scrapy.Spider):
    name = 'brick_spider'
    start_urls = ['https://sumodb.sumogames.de/Banzuke_text.aspx']

    def parse(self, response):
        

        yield {
            'title': response.xpath('//title/text()'),
        }
