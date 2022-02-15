# Scrapy settings for real_estate project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html


BOT_NAME = 'scrapy_scraper'

SPIDER_MODULES = ['scrapy_scraper.spiders']
NEWSPIDER_MODULE = 'scrapy_scraper.spiders'


ROBOTSTXT_OBEY = False


ITEM_PIPELINES = {
    'scrapy_scraper.pipelines.ScrapyScraperPipeline': 1
}

csv_file_path = 'scrapy_scraper/output/scraped_nekretnine_odbrana.csv'


LOG_STDOUT = True
LOG_FILE = 'scrapy_scraper/output/odbrana_log'

DOWNLOAD_TIMEOUT=5

DOWNLOADER_MIDDLEWARES = {
'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
}

USER_AGENTS = [
('Mozilla/5.0 (X11; Linux x86_64) '
'AppleWebKit/537.36 (KHTML, like Gecko) '
'Chrome/57.0.2987.110 '
'Safari/537.36'),  # chrome
('Mozilla/5.0 (X11; Linux x86_64) '
'AppleWebKit/537.36 (KHTML, like Gecko) '
'Chrome/61.0.3163.79 '
'Safari/537.36'),  # chrome
('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
'Gecko/20100101 '
'Firefox/55.0'),  # firefox
('Mozilla/5.0 (X11; Linux x86_64) '
'AppleWebKit/537.36 (KHTML, like Gecko) '
'Chrome/61.0.3163.91 '
'Safari/537.36'),  # chrome
('Mozilla/5.0 (X11; Linux x86_64) '
'AppleWebKit/537.36 (KHTML, like Gecko) '
'Chrome/62.0.3202.89 '
'Safari/537.36'),  # chrome
('Mozilla/5.0 (X11; Linux x86_64) '
'AppleWebKit/537.36 (KHTML, like Gecko) '
'Chrome/63.0.3239.108 '
'Safari/537.36'),  # chrome
]
