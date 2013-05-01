import gtk, gobject, os.path
from gourmet.gglobals import DEFAULT_ATTR_ORDER, REC_ATTR_DIC

class WebSearchTab (gtk.VBox):
	def __init__ (self, rd):
		gtk.VBox.__init__(self)
		
		#create the search bar
		self.search_bar = gtk.HBox()
		self.search_bar.set_spacing(6)
		self.pack_start(self.search_bar, expand=False)
		
		#create the list view
		self.search_results = gtk.ListStore(str, str)
		#append this list with new data
		self.search_tree = gtk.TreeView(model=self.search_results)
		
		sw = gtk.ScrolledWindow()
		sw.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
		sw.add(self.search_tree)
		self.pack_start(sw)
		
		#add the search entry and button to the search bar
		self.search_entry = gtk.Entry()
		self.search_entry.set_text("Empty Search")
		self.search_bar.pack_start(self.search_entry, expand=True, fill=True)
		
		self.search_button = gtk.Button("Search")
		self.search_button.set_size_request(150, -1)
		self.search_bar.pack_start(self.search_button, expand=False, fill=False)
		
		#create the columns for the index
		self.create_columns(self.search_tree)
		
		#create the progress bar
		self.status_bar = gtk.Statusbar()
		self.pack_start(self.status_bar, expand=False)

		self.show_all()
        
	def create_columns(self, treeView):
		rendererText = gtk.CellRendererText()
		column = gtk.TreeViewColumn("Title", rendererText, text=0)
		column.set_sort_column_id(0)    
		treeView.append_column(column)

		rendererText = gtk.CellRendererText()
		column = gtk.TreeViewColumn("Description", rendererText, text=1)
		column.set_sort_column_id(1)
		treeView.append_column(column)
        
	def on_activated(self, widget, row, col):
		model = widget.get_model()
		#text = model[row][0] + ", " + model[row][1] + ", " + model[row][2]
		self.statusbar.push(0, text)

def try_out ():
	import gourmet.recipeManager
	rb = WebSearchTab(gourmet.recipeManager.get_recipe_manager())
	#vb = gtk.VBox()
	#vb.pack_start(rb)
	#rb.show()
	w = gtk.Window()
	#w.add(vb)
	w.add(rb)
	w.set_default_size(800,500)
	w.connect('delete-event',gtk.main_quit)
	w.show_all()
	gtk.main()
    
if __name__ == '__main__':
	try_out()
