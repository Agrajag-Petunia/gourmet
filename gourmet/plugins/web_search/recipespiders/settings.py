# Scrapy settings for dirbot project

SPIDER_MODULES = ['recipespiders.spiders']
NEWSPIDER_MODULE = 'recipespiders.spiders'
DEFAULT_ITEM_CLASS = 'recipespiders.items.Website'

ITEM_PIPELINES = ['recipespiders.pipelines.FilterWordsPipeline']
