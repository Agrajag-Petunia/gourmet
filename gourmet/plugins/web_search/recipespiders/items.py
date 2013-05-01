from scrapy.item import Item, Field

class AllRecipesItem(Item):
	name = Field()
	servings = Field()
	ingredients = Field()
	directions = Field()