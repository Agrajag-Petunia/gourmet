from scrapy.exceptions import DropItem
from . import storage
from cache import Storage, Recipe

class CachingPipeline(object):
    """Stores recipes in the temporary database as a form of caching to reduce
    duplicate requests"""
    
    def process_item(self, item, spider):
	session = storage.get_session()
	
	name = item['name']
	ingredients = ''
	directions = ''
	
	for ingredient in item['ingredients']:
	    ingredients += ingredient
	
	for direction in item['directions']:
	    directions += direction'
	
	recipe = Recipe(name, ingredients, directions)
	
	try:
	    session.add(recipe)
	    session.commit()
	except:
	    session.rollback()
	
	return item
