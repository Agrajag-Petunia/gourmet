# Scrapy settings for dirbot project

SPIDER_MODULES = ['recipespiders.spiders']
NEWSPIDER_MODULE = 'recipespiders.spiders'
DEFAULT_ITEM_CLASS = 'recipespiders.items.AllRecipeItems'

ITEM_PIPELINES = ['recipespiders.pipelines.CachingPipeline']
