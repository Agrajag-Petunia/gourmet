import gtk, gobject, os.path
from gourmet.gglobals import DEFAULT_ATTR_ORDER, REC_ATTR_DIC

class WebSearchIndex (gtk.VBox):

    def __init__ (self, rd):
        gtk.VBox.__init__(self)
        
        self.search_view = gtk.Table(30, 30, True)
        self.add(self.search_view)
        
        self.search_entry = gtk.Entry()
        self.search_entry.set_text("Empty Search")
        self.search_button = gtk.Button("Search")
        
        self.search_results = gtk.ListStore(str, str)
        #append this list with new data
        
        self.search_tree = gtk.TreeView(model=self.search_results)
        
        self.search_view.attach(self.search_entry, 0, 20, 0, 1)
        self.search_view.attach(self.search_button, 20, 30, 0, 1)
        self.search_view.attach(self.search_tree, 0, 30, 1, 30)
        
        sw = gtk.ScrolledWindow()
        sw.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
        self.pack_start(sw)
        

def try_out ():
    import gourmet.recipeManager
    rb = WebSearchIndex(gourmet.recipeManager.get_recipe_manager())
    vb = gtk.VBox()
    vb.pack_start(rb)
    #rb.show()
    w = gtk.Window()
    w.add(vb)
    w.show(); vb.show()
    w.set_size_request(800,500)
    w.connect('delete-event',gtk.main_quit)
    w.show_all()
    gtk.main()
    
if __name__ == '__main__':
    try_out()