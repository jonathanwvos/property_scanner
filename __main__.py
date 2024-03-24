from os.path import dirname, join, realpath
from property_scanner.spiders.property24 import Property24Scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from statistical_evaluation import execute as ex_stat_eval
from recommendations import execute as ex_recommendations

process = CrawlerProcess(get_project_settings())
process.crawl(Property24Scrapy)
process.start()

filename = join(dirname(realpath(__file__)), 'data', 'property_24.csv')
insights = ex_stat_eval(filename)
ex_recommendations(insights)
# print(insights)