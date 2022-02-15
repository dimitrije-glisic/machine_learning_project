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

CONCURRENT_REQUESTS = 32

DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 32
CONCURRENT_REQUESTS_PER_IP = 32

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False


# Enable and configure the AutoThrottle extension (disabled by default)
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 6.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True



ITEM_PIPELINES = {
    'scrapy_scraper.pipelines.ScrapyScraperPipeline': 1
}

csv_file_path = 'scrapy_scraper/output/scraped_nekretnine_odbrana.csv'


LOG_STDOUT = True
LOG_FILE = 'scrapy_scraper/output/odbrana_log'

ROTATING_PROXY_LIST_PATH='../proxies/proxies'

DOWNLOAD_TIMEOUT=2

DOWNLOADER_MIDDLEWARES = {
'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,

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
