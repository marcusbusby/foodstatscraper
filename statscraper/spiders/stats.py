import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from statscraper.items import WebsiteItem

class StatSpider(Spider):
	name = "stats"
	allowed_domains = ["thelunchtray.com"]
	start_urls = [
		"http://www.thelunchtray.com/"
	]

	def parse(self, response):
		for href in response.css('h2 a::attr(href)'):
			url = href.extract()
			yield scrapy.Request(url, callback=self.parse_article)		

	def parse_article(self, response):
		for paragraph in response.css('li::text, p::text'):
			if 'percent' in paragraph.extract():
				item = WebsiteItem()
				item['paragraph'] = paragraph.extract()
				item['link'] = response.url
				yield item



