from scrapy.item import Item, Field

class RecipeItem(Item):
	name = Field()
	servings = Field()
	ingredients = Field()
	directions = Field()