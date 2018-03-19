# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis


class IpproxyPipeline(object):
    key = "ipproxy"

    def __init__(self):
        print("rrrrrrrrrrrrrrr")
        # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
        pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
        self.r = redis.Redis(connection_pool=pool)
        # self.redis = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def process_item(self, item, spider):
        res = self.r.sadd(self.key, item['ip'])
        print(res)
        print("------------------------------")
        print(item)
        # return item
