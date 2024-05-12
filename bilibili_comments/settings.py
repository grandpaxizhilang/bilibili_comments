# Scrapy settings for bilibili_comments project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bilibili_comments'

SPIDER_MODULES = ['bilibili_comments.spiders']
NEWSPIDER_MODULE = 'bilibili_comments.spiders'
LOG_LEVEL = 'WARNING'


# 有关请求参数的设置:
# 设置bv号
BV = ['BV1pZ421E7Er']
# 爬取父评论的睡眠时间
father_time = 1
# 设置cookie
COOKIES = {
    "buvid3": "D1EB1C3E-15B1-EF1E-04B3-18CDD3AF80F650899infoc",
    "b_nut": "1709195250",
    "buvid4": "AF6DC7F7-0576-8584-C3A3-A11C1E3D563850899-024022908-NJZlfXRzL2DLcte75U0ArQ%3D%3D",
    "_uuid": "F3D96B4A-F9C8-11C5-B1068-581022437E5D155189infoc",
    "DedeUserID": "86853068",
    "DedeUserID__ckMd5": "89cba52406e553bd",
    "rpdid": "|(JlRYJlukku0J'u~|muml~JJ",
    "enable_web_push": "DISABLE",
    "header_theme_version": "CLOSE",
    "LIVE_BUVID": "AUTO7517092084513301",
    "buvid_fp_plain": "undefined",
    "hit-dyn-v2": "1",
    "share_source_origin": "WEIXIN",
    "CURRENT_QUALITY": "80",
    "go-back-dyn": "0",
    "fingerprint": "6663bd3cc6ffac7d84be2b0a2f5fbd81",
    "buvid_fp": "6663bd3cc6ffac7d84be2b0a2f5fbd81",
    "bsource": "search_bing",
    "FEED_LIVE_VERSION": "V_WATCHLATER_PIP_WINDOW3",
    "bp_video_offset_86853068": "920102155129454611",
    "home_feed_column": "5",
    "CURRENT_FNVAL": "4048",
    "bili_ticket": "eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTU1OTE4NjIsImlhdCI6MTcxNTMzMjYwMiwicGx0IjotMX0.JSzxvh44wfF5lIZIqPXm965qIBWEffxvTLIHKU7lWek",
    "bili_ticket_expires": "1715591802",
    "bp_t_offset_86853068": "930132136446394390",
    "SESSDATA": "d442f74e%2C1731051416%2Cc43e5%2A52CjC-oEn-aET88nL2CuVQFTELd9R0E5pWqs6RxUTEATENplxI5dJcEN6Yq5KAsA6ZiU4SVmRJdk1qbVlERUJOVW9HNkdXdzJkQTdjSEdveWhnTmtXY1VUSzF3b3lQQkNmbi03dGh4ZTdWLXNLUGJEZWN2ak8xWmM3Vkxva1lBNjR3eHVndUI5SFNBIIEC",
    "bili_jct": "600c5fc9c90ed83bd68870d5aff287f1",
    "browser_resolution": "1482-726",
    "sid": "6ffksbq3",
    "b_lsid": "C256210B8_18F6C6A39C8"
}
# 请求头
HEADERS = {
    'Origin':'https://space.bilibili.com',
    'Referer':'https://space.bilibili.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
}






# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.1
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'Origin':'https://space.bilibili.com',
#     'Referer':'https://space.bilibili.com',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'bilibili_comments.middlewares.BilibiliCommentsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'bilibili_comments.middlewares.BilibiliCommentsDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'bilibili_comments.pipelines.BilibiliCommentsPipeline': 300,
#}

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
