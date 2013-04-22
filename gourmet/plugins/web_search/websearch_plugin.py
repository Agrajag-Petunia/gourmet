from gourmet.plugin import MainPlugin
import gtk
import websearch_index

class WebSearchPlugin (MainPlugin):

	def activate(self, pluggable):
		MainPlugin.activate(self, pluggable)
		self.browser = browser.WebSearchIndex(pluggable.rd)
        self.add_tab(self.browser,'Web Recipe Search')
