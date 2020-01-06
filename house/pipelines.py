# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo


logger = logging.getLogger(__name__)


class HousePipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        host = crawler.settings['MONGODB_HOST']
        port = crawler.settings['MONGODB_PORT']
        dbname = crawler.settings['MONGODB_DBNAME']
        pyclient = pymongo.MongoClient(host=host, port=port)
        mdb = pyclient[dbname]
        s.post = mdb[crawler.settings['MONGODB_DOCNAME']]
        return s

    def process_item(self, item, spider):
        logger.info(item)
        house_item = dict(item)
        self.post.insert_one(house_item)
        return item
