from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from recipespiders.items import AllRecipesItem

class RecipesSpider(BaseSpider):
	DOWNLOAD_DELAY = 2
	name = "recipes"
	allowed_domains = ["allrecipes.com"]
	start_urls = ["http://allrecipes.com/recipes/ViewAll.aspx"]
	count = 0
	threshold = 20
	
	def __init__(self, key=None, num_recipes=None):
		if key is not None:
			self.start_urls = ['http://allrecipes.com/recipes/Search.aspx?WithTerm=%s' % key]

		if num_recipes is not None:
			self.threshold = num_recipes


	def parse(self, response):
		hxs = HtmlXPathSelector(response)

		#select recipe links in web page
		recipes = hxs.select("//div[@class='rectitlediv']/h3/a/@href").extract()
		for recipe in recipes:
			self.count = self.count + 1
			yield Request(recipe, self.parse_recipe)

		if (self.count < self.threshold):
			#select the next page to crawl
			next_page = hxs.select("//a[contains(text(),'NEXT')]/@href").extract()
			if not not next_page:
				yield Request(next_page[0], self.parse)


	def parse_recipe(self, response):
		hxs = HtmlXPathSelector(response)
		recipe = AllRecipesItem()
		
		name = hxs.select("//div[@class='detail-right fl-right']/h1/text()").extract()
		srvs = hxs.select("//span[@id='lblYield']/text()").extract()
		
		ingredients = []
		directions = []
		
		ingreds = hxs.select("//p[@class='fl-ing']")
		directs = hxs.select("//span[@class='plaincharacterwrap break']/text()").extract()
		
		#print 'Recipe: %s' % name
		#print 'Serves: %s' % srvs
		for ingred in ingreds:
			args = (ingred.select(".//span[@class='ingredient-amount']/text()").extract(), ingred.select(".//span[@class='ingredient-name']/text()").extract())
			ingredient = '%s - %s' % args
			ingredients.append(ingredient)
			#print '%s' % ingredient
			
		for index, direct in enumerate(directs):
			args = (index + 1, direct)
			direction = '%d) %s' % args
			directions.append(direction)
			#print '%s' % direction
			
		recipe['name'] = name
		recipe['servings'] = srvs
		recipe['ingredients'] = ingredients
		recipe['directions'] = directions
		
		yield recipe
			
		
