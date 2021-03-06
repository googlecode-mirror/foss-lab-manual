#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld:
	def on_button_clicked(self, widget, data=None):
		print "Hello World"
		
	def on_window_destroy(self, widget, data=None):
		gtk.main_quit()
		
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("destroy", self.on_window_destroy)
		self.window.set_border_width(5)
		
		self.button = gtk.Button("Hello World")
		self.button.connect("clicked", self.on_button_clicked)
		self.window.add(self.button)

		self.window.show_all()
		
	def main(self):
		gtk.main()
		
if __name__ == "__main__":
	hello = HelloWorld()
	hello.main()

