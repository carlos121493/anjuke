import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule, Spider
from house.items import HouseItem
from scrapy.shell import inspect_response
import logging

logger = logging.getLogger(__name__)

class HouseSpider(CrawlSpider):
    name = 'house'
    start_urls = ['https://hangzhou.anjuke.com/sale/?pi=baidu-cpc-hz-cty1&kwid=12562615123&bd_vid=8269213342921491410']
    allowed_domains = ['anjuke.com']
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="multi-page"]/a[@class="aNxt"]', unique=True), callback="parse_item", follow=True),
    )

    def getFistItem(self, items):
        if not items:
            return ''
        return items.pop()

    def parse_item(self, response):
        items = response.xpath('//ul[@class="houselist-mod houselist-mod-new"]/li')
        logger.info(response.url)
        
        for item in items:
            room_type, capacity, house_type, house_time, detail = item.xpath('.//div[@class="details-item"]/span/text()').extract()
            name, infos = [d.strip() for d in detail.split('\xa0\xa0')]
            info_items = infos.split('-')
            info_items.reverse()
            # inspect_response(response, self)
            area = self.getFistItem(info_items)
            region = self.getFistItem(info_items)
            street = self.getFistItem(info_items)
            yield HouseItem({
                'title': item.xpath('.//div[@class="house-title"]/a/@title').get(),
                'labels': item.xpath('.//div[@class="tags-bottom"]/span/text()').extract(),
                'price': item.xpath('.//span[@class="price-det"]/strong/text()').get(),
                'mean_price': item.xpath('.//span[@class="unit-price"]/text()').get(),
                'time': house_time,
                'area': area,
                'region': region,
                'street': street,
                'name': name,
                'room_type': room_type,
                'house_type': house_type,
                'capacity': capacity,
            })