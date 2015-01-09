import scrapy

class ScienceSpider(scrapy.Spider):
    name = "getScience"
    allowed_domains = ["newscientist.com"]
    start_urls = [
                    "http://www.newscientist.com/special/instant-expert-general-relativity"
                    "http://www.newscientist.com/special/carbon-capture-storage"
                 ]

    def parse(self, response):
        filename = response.url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)

