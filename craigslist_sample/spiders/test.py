from scrapy.spiders import Spider
from scrapy.selector import Selector
from craigslist_sample.items import SimpleCraigslistItem

_url = "https://richmond.craigslist.org/search/fua?query=bunk+bed&hasPic=1&search_distance=25&max_price=198"
_url_prefix = "http://richmond.craigslist.org/"


class BunkBedSpider(Spider):
    name = "BunkBedSpider"
    allowed_domains = ["craigslist.org"]
    start_urls = [_url]

    def parse(self, response):
        hxs = Selector(response=response)
        rows = hxs.xpath("//p[@class='row']")
        items = list()
        for row in rows:
            newItem = SimpleCraigslistItem()
            title = row.xpath("span[@class='txt']/span[@class='pl']/a/text()").extract()
            if len(title) == 0:
                title = row.xpath("span[@class='txt']//span[@id='titletextonly']/text()").extract()
            newItem["title"] = self.makeNonUnicodeString(title[0])
            link = row.xpath("a/@href").extract()[0]
            newItem["link"] = self.makeNonUnicodeString(self.formatLink(link))
            newItem["price"] = self.makeNonUnicodeString(row.xpath("a/span[@class='price']/text()").extract()[0])
            items.append(newItem)
        return items

    def formatLink(self, link):
        if link == link.replace("//", ""):
            return _url_prefix + link[1:]
        else:
            return link.replace("//", "")

    def makeNonUnicodeString(self, unicodeString):
        plainString = unicodeString.encode('ascii', 'ignore')
        return plainString.replace('"', '')
