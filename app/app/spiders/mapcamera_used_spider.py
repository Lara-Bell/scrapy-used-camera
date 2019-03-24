# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy_splash import SplashRequest
from ..items import MapcameraUsedItem

class MapcameraUsedSpider(scrapy.Spider):
    name = 'mapcamera_used_spider'
    allowed_domains = ['www.mapcamera.com']
    page_number = 25
    start_urls = ['https://www.mapcamera.com/search?sell=used&limit=200&category=3&page={}#result'.format(i) for i in range(1, page_number+1)]

    custom_settings = {
        'CONCURRENT_REQUESTS': '1',
    }

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 1})

    def parse(self, response):
        items = MapcameraUsedItem()
        item_element = response.css('div#searchResult > ul.srcitemlist > li.item_wrap')

        for ele in item_element:
            jan_code_string = ele.css('div > a::attr(onclick)').extract_first()
            all_code = re.search(r'[0-9]{8,13}_[0-9]{2,15}', jan_code_string).group()
            map_code = ele.css('li::attr(data-mapcode)').extract_first()

            items['mapcode'] = map_code
            items['jancode'] = all_code.replace("_" + map_code, "")

            product_name = ele.css('li::attr(data-itemname)').extract_first()
            items['name'] = product_name

            all_name = ele.css('div > p.txt > a::text').extract_first()
            space_name = all_name.replace(product_name, "")

            items['maker'] = space_name.replace(u"\xa0", u"")

            if ele.css('div > p.txt > span.price > span > span > b::text').extract_first() is not None:
                price_data = ele.css('div > p.txt > span.price > span > span > b::text').extract_first()
                items['price'] = price_data.replace("(税込)", u"")
            else:
                price_data = ele.css('div > p.txt > span.price::text').extract_first()
                items['price'] = price_data.replace("(税込)", u"")

            items['state'] = ele.css('div > a > p.icon.clearfix > span::text').extract()[1]

            point_name = ele.css('div > p.txt > span.txtred::text').extract_first()
            items['point'] = point_name.replace("ポイント", "")

            yield items