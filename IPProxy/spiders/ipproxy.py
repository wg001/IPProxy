# -*- coding: utf-8 -*-
import scrapy
from scrapy.conf import settings
from IPProxy.items import IpproxyItem


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
            if len(c_res) > 0:
                item = IpproxyItem()
                url_pre = ""
                if c_res[5] in ["HTTPS", "HTTP"]:
                    url_pre = c_res[5]
                elif c_res[4] in ["HTTPS", "HTTP"]:
                    url_pre = c_res[4]
                ip_str = url_pre + "://" + c_res[0] + ":" + c_res[1]
                item['ip'] = ip_str
                yield item
                # print(ip_str)
            print("-----------------")

    def error_handle(self, failure):
        print(failure)
