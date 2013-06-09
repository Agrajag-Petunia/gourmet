from scrapy.exceptions import DropItem
from . import storage
from cache import Storage, Recipe

class CachingPipeline(object):
    """Stores recipes in the temporary database as a form of caching to reduce
    duplicate requests"""
    
    def process_item(self, item, spider):
	session = storage.get_session()
	
	name = item['name']
	ingredients = ' '.join(item['ingredients'])
	directions = ' '.join(item['directions'])
	
	recipe = Recipe(name, ingredients, directions)
	
	#try:
	session.add(recipe)
	session.commit()
	#except:
	#print "Failed to add recipe to db"
	#session.rollback()
	
	return item
