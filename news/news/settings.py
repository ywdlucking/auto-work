# Scrapy settings for news project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'news'

SPIDER_MODULES = ['news.spiders']
NEWSPIDER_MODULE = 'news.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'news (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'Referer': 'https://news.163.com/',
  'Host': 'www.163.com',
  'Cookie': '_ntes_nnid=902903f6f66c4e74d1e5b95331034df4,1636632537630; _ntes_nuid=902903f6f66c4e74d1e5b95331034df4; WM_TID=K71y172jBPlBFQAABQN%2F3MfNHf0FBXg%2B; _antanalysis_s_id=1669017780633; pver_n_f_l_n3=a; WM_NI=Fobsn6xEYx%2BYYTRipNQrKaGlYOsP8uuKRhlqglwF%2B8mGZIsmYEZGKuimzPaNm%2FBkoWXbvVwvdwhID%2FFuZPWQrV7vB6q1EldfgS35kl8TW57D620Wz0uumZvJvJWlzalTUzk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee85d267f5eb0093d53aa2928ab6d55a979e9aadc152a3a9b69be672b88af9a6f12af0fea7c3b92a86b1ae94ed3ebc9b9799aa539b8c9e8af34693ae8582c6689b91bdb1bb7fb7959e89ef7ba5b4b9a7aa34af9996aaf2679b9b96a8ca7fabb3b6b1e446aff18e8cee5d9cbebab7f67ea8a9a8aac72586ab96b1d65bb28af997c13eb3ef8b8de76ea58dfdd6ea68fc8c99d6b650f6ee00b8f93cb7aba3bbf542b696998df96bb08c9b9bea37e2a3; s_n_f_l_n3=78e4e0be1b14c8491670306160631; W_HPTEXTLINK=old; ne_analysis_trace_id=1670306303683; vinfo_n_f_l_n3=78e4e0be1b14c849.1.4.1670229095726.1670294910496.1670306790725',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'news.middlewares.NewsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'news.middlewares.NewsDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'news.pipelines.NewsPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
