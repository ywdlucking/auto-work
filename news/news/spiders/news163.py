import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from news.items import NewsItem

# https://www.163.com/news/article/HNRA3BL3000189FH.html
# https://www.163.com/news/article/.*?html
class News163Spider(CrawlSpider):
    name = 'news163'
    allowed_domains = ['news.163.com']
    start_urls = ['http://news.163.com/']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.163.com/news/article/.*?html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # item = NewsItem()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # item[''] = response.url.strip().split('/')
        item={}
        return item
