import scrapy
from project1.items import DmozItem
class FirstSpider(scrapy.Spider):
	name = "test"
	allowed_domains = ['dmoz.org']
	start_urls = ["http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"]
	
	def parse(self,response):
		sel = scrapy.selector.Selector(response)
		sites = sel.xpath('//div[@class="title-and-desc"]')
		items = []
		for site in sites:
			item = DmozItem()
			item['title'] = site.xpath('a/div/text()').extract()
			item['link'] = site.xpath('a/@href').extract()
			item['desc'] = [site.xpath('div/text()').extract()[0].lstrip().rstrip()]
			items.append(item)
		
		return items