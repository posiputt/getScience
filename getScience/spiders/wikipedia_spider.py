import scrapy

class ScienceSpider(scrapy.Spider):
    name = "getScience"
    allowed_domains = ["newscientist.com"]
    start_urls = [
                    "http://en.wikipedia.org/wiki/Willis_Steell"
                 ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)

