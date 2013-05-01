from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

class Recipe(Base):
    __tablename__ = "recipes"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ingredients = Column(String)
    directions = Column(String)
    
    def __init__(self, name, ingredients, directions):
	self.name = name
	self.ingredients = ingredients
	self.directions = directions

    def __repr__(self):
	return "Recipe(%r, %r, %r)" % (self.name, self.ingredients, self.directions)

class Storage:
    def __init__(self):
	self.engine = None
	self.Session = None

    def get_session(self):
	if self.engine is None:
	    self.engine = create_engine('sqlite:///recipespider.db')
	    Base.metadata.create_all(self.engine)
	    self.Session = sessionmaker(bind=self.engine)
	
	return self.Session()

    def destroy(self)
	Base.metadata.drop_all(bind=self.engine)
	os.remove('recipespider.db')


def try_out ():
    r1 = Recipe("Vegan Soup", "Veggie Broth, Peppers, Tomatoes, Black Beans, ...", "Stick all in a pot and cook till ready")
    cache = Storage()
    session = cache.get_session()
    
    try:
	session.add(r1)
	session.commit()
    except:
	session.rollback()
    
if __name__ == '__main__':
    try_out()
