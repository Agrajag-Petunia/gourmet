from gourmet.plugin import MainPlugin
from websearch_tab import WebSearchTab
import gtk

class WebSearchPlugin (MainPlugin):

	def activate(self, pluggable):
		MainPlugin.activate(self, pluggable)
		self.browser = WebSearchTab(pluggable.rd)
		self.add_tab(self.browser,'Web Recipe Search')
