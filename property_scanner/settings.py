import numpy as np
# Scrapy settings for property_scanner project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'BingBongTime'


SPIDER_MODULES = ["property_scanner.spiders"]
NEWSPIDER_MODULE = "property_scanner.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = np.random.choice([
   "Aisha Chen",
   "Juan Singh",
   "Santiago Tanaka",
   "Chen Rossi",
   "Santiago Kovács",
   "Liam Zhang",
   "Juan Murphy",
   "Dmitri Müller",
   "Carlos Silveira",
   "Carlos Yoshida",
   "Lucas Rossi",
   "Mia Kumar",
   "Igor Gonzalez",
   "Lina Yoshida",
   "Pedro Singh",
   "Alejandro Ahmed",
   "Emma Zhang",
   "Gabriel Martinez",
   "Santiago Suzuki",
   "Gabriel Johnson",
   "Alejandro Silva",
   "Ethan Smith",
   "Ethan Martinez",
   "Felix Tanaka",
   "Zara Gonzalez",
   "Santiago Novak",
   "Hiro Sanchez",
   "Hiro Smith",
   "Alejandro Rossi",
   "Lucas Ivanov",
   "Omar Johansson",
   "Gabriel Smirnov",
   "Felix Dupont",
   "Lei Martinez",
   "Anya Yoshida",
   "Anya Garcia",
   "Mina Kumar",
   "Lina Johansson",
   "Lucas Silva",
   "Mia Kim",
   "Pedro Silveira",
   "Nia Nguyen",
   "Emma Schmidt",
   "Liam Williams",
   "Zara Khan",
   "Carlos Gruber",
   "Aarav Ivanov",
   "Alejandro Brown",
   "Lina Ivanov",
   "Mila Dupont",
   "Ivan Murphy",
   "Lina Schmidt",
   "Lei Ali",
   "Chen Smith",
   "Chen Garcia",
   "Mohammed Khan",
   "Carlos Singh",
   "Sara Chen",
   "Pedro Garcia",
   "Omar Khan",
   "Diego Gruber",
   "Omar Suzuki",
   "Nia Novak",
   "Ivan Gruber",
   "Carlos Martinez",
   "Mohammed Nguyen",
   "Sara Schmidt",
   "Chen Suzuki",
   "Chen Schmidt",
   "Fatima Chen",
   "Diego Kovács",
   "Sofia Tanaka",
   "Hiro Williams",
   "Lei Sanchez",
   "Lina Rossi",
   "Sergei Novak",
   "Emma Novak",
   "Diego Silva",
   "Ava Gonzalez",
   "Emma Williams",
   "Yuna Ahmed",
   "Sofia Díaz",
   "Omar Perez",
   "Mohammed Smirnov",
   "Sofia Smirnov",
   "Anya Schmidt",
   "Carlos Tanaka",
   "Hiro Hernandez",
   "Aisha Kumar",
   "Lina Silva",
   "Liam Khan",
   "Lei Kumar",
   "Chen Williams",
   "Yuna Müller",
   "Juan Martinez",
   "Isabella Dupont",
   "Anya Johnson",
   "Santiago Ahmed",
   "Chen O'Connor",
   "Olivia Rossi"
])

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "property_scanner.middlewares.PropertyScannerSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "property_scanner.middlewares.PropertyScannerDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "property_scanner.pipelines.PropertyScannerPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 3
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 10
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
