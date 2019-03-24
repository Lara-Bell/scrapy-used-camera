# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy_splash import SplashRequest
from ..items import KitamuraUsedItem

class KitamuraUsedSpider(scrapy.Spider):
    name = 'kitamura_used_spider'
    allowed_domains = ['www.net-chuko.com']
    page_number = 25
    start_urls = ['http://www.net-chuko.com/buy/list.do?kindName=%E4%BA%A4%E6%8F%9B%E3%83%AC%E3%83%B3%E3%82%BA&detailsName=&makerName=&keyword=&price=&condition=&shop=0&photo=false&selling=false&ob=ud-&lc=100&pg={}&is=1&ecmount=&eccolor=&ectype=&eclan=&ecundai=&eccase=&eczoom=&ecwater=&ecdust=&ecfilter=&echeight=&ecpixel='.format(i) for i in range(1, page_number+1)]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 1})

    def parse(self, response):
        items = KitamuraUsedItem()
        item_element = response.css('li.item-element')

        for ele in item_element:
            ac_number_string = ele.css('dl > dt > a::attr(href)').extract_first()
            ac_string = re.search(r'[0-9]*\&', ac_number_string).group()

            items['ac'] = ac_string.replace("&", "")
            items['maker'] = ele.css('dl > dt > span::text').extract_first()
            items['name'] = ele.css('dl > dt > a::text').extract_first()
            items['price'] = ele.css('dl > dd.plice > a > span::text').extract_first()
            items['shop'] = ele.css('dl > dd.shop::text').extract_first()

            item_state = ele.css('dl > dd.state::text').extract_first()
            items['state'] = item_state.replace("状態：", "")

            item_date = ele.css('dl > dd.date::text').extract_first()
            items['date'] = item_date.replace("更新日：", "")

            yield items
