import scrapy

'''
命令行执行: 
scrapy runspider julyedu_spider.py -o julyedu_class.json
'''

class CnblogSpider(scrapy.Spider):
    name = 'cnblog'
    start_urls = ['https://www.cnblogs.com/pick/#p%s' %p for p in range(1, 21) ]

    def parse(self, response):
        for julyedu_class in response.xpath('//div[@class="post_item"]'):
            print('-----------------------------------------')
            print(julyedu_class.xpath(' a / h4/text()').extract_first())
            print(julyedu_class.xpath('a/ p[@class="course-info-tip"][1]/text()').extract_first())
            print(julyedu_class.xpath('a/ p[@class="course-info-tip"][2]/text()').extract_first())


            yield{'title' : julyedu_class.xpath(' a / h4/text()').extract_first(),
                  'desc' :  julyedu_class.xpath('a/ p[@class="course-info-tip"][1]/text()').extract_first(),
                  'time' :  julyedu_class.xpath('a/ p[@class="course-info-tip"][2]/text()').extract_first()
                  }


