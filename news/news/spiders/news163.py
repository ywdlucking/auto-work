import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from news.items import NewsItem

# https://www.163.com/news/article/HNRA3BL3000189FH.html
# https://www.163.com/news/article/.*?html
class News163Spider(CrawlSpider):
    name = 'news163'
    #包含了爬虫允许爬取的域名列表，当OffsiteMiddleware启动时，域名不在列表中的URL不会被爬取。
    allowed_domains = ['163.com']
    #URL的初始列表，如果没有指定特定的URL，爬虫将从该列表中进行爬取。
    start_urls = ['http://news.163.com/']

    # 链接处理规则
    rules = (
        
        # follow 决定是否继续在链接提取器提取的链接对应的响应中继续应用链接提取器，一般持续翻页的链接提取规则需要设置为true
        Rule(LinkExtractor(allow=r'/news/article/.*?html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # print("****************************message")
        item = NewsItem()
        item['news_thread'] = response.url.strip().split('/')[-1][:-5]
        item['news_title'] = response.xpath('//h1[@class="post_title"]/text()').get().strip()
        item['news_url'] = response.url
        self.get_news_time(response, item)
        item['news_source'] = response.xpath('//div[@class="post_info"]/a/text()').get()
        item['source_url'] = response.xpath('//div[@class="post_info"]/a/@href').get()
        self.get_body(response, item)
        # self.logger.info(" %s ", item)
        return item

    def get_news_time(self, response, item):
        src = response.xpath('//div[@class="post_info"]/text()').get().strip()
        # self.logger.info("get_news_time: %s", src)
        item['news_time'] = src[:-4]

    def get_body(self, response, item):
        # body = response.css('.post_text p::text').get()
        body = response.xpath('//div[@id="content"]//p/text()').getall()
        item['news_body'] = body