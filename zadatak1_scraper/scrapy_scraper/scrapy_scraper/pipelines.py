# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
from scrapy_scraper import settings

class ScrapyScraperPipeline:
    def process_item(self, item, spider):
        self.write_to_csv(item)
        return item
    
    def write_to_csv(self, item):
       writer = csv.writer(open(settings.csv_file_path, 'a'), lineterminator='\n')
       writer.writerow([item[key] for key in item.keys()])
