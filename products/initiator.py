import os
from products.domain import *
from lxml import html
import requests
import datetime
import ast
import time
from products.get_all_major_category_links import HomeCrawler


def count_words_at_url(url):
	crawler = HomeCrawler(url, "//ul[@id='site-navigation']/li/a/@href", "")
	crawler.crawl()

