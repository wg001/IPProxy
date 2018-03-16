# -*- coding: utf-8 -*-
import scrapy
from scrapy.conf import settings


class IpproxySpider(scrapy.Spider):
    name = 'ipproxy'
    url = "http://www.xicidaili.com/nn"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.xicidaili.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    cookie = settings['COOKIE']

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse_ip, errback=self.error_handle, cookies=self.cookie,
                             headers=self.headers)

    def parse(self, response):
        pass

    def parse_ip(self, response):
        get_res = response.xpath('//table[@id="ip_list"]/tr')
        for child in get_res:
            c_res = child.xpath('./td/text()').extract()
            # for i in range(len(c_res)):
            #     print(i, ">>>", c_res[i])
            if len(c_res) > 0:
                ip_arr = c_res[5] + "://" + c_res[0] + ":" + c_res[1]
                print(ip_arr)
            print("-----------------")

    def error_handle(self, failure):
        print(failure)
