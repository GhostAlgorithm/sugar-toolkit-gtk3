import random
import re

import gobject
import gtk
import goocanvas

from sugar.util import GObjectSingletonMeta

class IconColor:
	__colors_dict = {
	'white'   : 'black'  , \
	'#66A531' : '#3D6E1C', \
	'#C96FF4' : '#3D6E1C', \
	'#AD9329' : '#7A5E21', \
	'#3698FD' : '#7A5E21', \
	'#EC7414' : '#AD3E19', \
	'#3DA0C6' : '#AD3E19', \
	'#F96564' : '#C3191D', \
	'#48A39B' : '#C3191D', \
	'#F85DA3' : '#BA1876', \
	'#26AA65' : '#BA1876', \
	'#C96FF4' : '#A116C8', \
	'#66A531' : '#A116C8', \
	'#3698FD' : '#4B44FB', \
	'#AD9329' : '#4B44FB', \
	'#3DA0C6' : '#276986', \
	'#EC7414' : '#276986', \
	'#48A39B' : '#366B68', \
	'#F96564' : '#366B68', \
	'#26AA65' : '#236F52', \
	'#F85DA3' : '#236F52', \
	'#77C32B' : '#318D34', \
	'#C39EFD' : '#318D34', \
	'#C2B10D' : '#9A7617', \
	'#7DB2FB' : '#9A7617', \
	'#F19D24' : '#C45F18', \
	'#0FBEF1' : '#C45F18', \
	'#F89760' : '#F71717', \
	'#36C2C0' : '#F71717', \
	'#F393B5' : '#E42D8E', \
	'#2DC78E' : '#E42D8E', \
	'#C39EFD' : '#C820FB', \
	'#77C32B' : '#C820FB', \
	'#7DB2FB' : '#576EF8', \
	'#C2B10D' : '#576EF8', \
	'#0FBEF1' : '#1485AC', \
	'#F19D24' : '#1485AC', \
	'#36C2C0' : '#2F8882', \
	'#F89760' : '#2F8882', \
	'#2DC78E' : '#108C64', \
	'#F393B5' : '#108C64', \
	'#3AE93B' : '#66A531', \
	'#DFBCFA' : '#66A531', \
	'#D3CF34' : '#AD9329', \
	'#AECCF7' : '#AD9329', \
	'#F9C216' : '#EC7414', \
	'#52DCEE' : '#EC7414', \
	'#FDBB98' : '#F96564', \
	'#18E3C4' : '#F96564', \
	'#F8B9C6' : '#F85DA3', \
	'#41E586' : '#F85DA3', \
	'#DFBCFA' : '#C96FF4', \
	'#3AE93B' : '#C96FF4', \
	'#AECCF7' : '#3698FD', \
	'#D3CF34' : '#3698FD', \
	'#52DCEE' : '#3DA0C6', \
	'#F9C216' : '#3DA0C6', \
	'#18E3C4' : '#48A39B', \
	'#FDBB98' : '#48A39B', \
	'#41E586' : '#26AA65', \
	'#F8B9C6' : '#26AA65', \
	'#3AE93B' : '#3D6E1C', \
	'#DFBCFA' : '#3D6E1C', \
	'#D3CF34' : '#7A5E21', \
	'#AECCF7' : '#7A5E21', \
	'#F9C216' : '#AD3E19', \
	'#52DCEE' : '#AD3E19', \
	'#FDBB98' : '#C3191D', \
	'#18E3C4' : '#C3191D', \
	'#F8B9C6' : '#BA1876', \
	'#41E586' : '#BA1876', \
	'#DFBCFA' : '#A116C8', \
	'#3AE93B' : '#A116C8', \
	'#AECCF7' : '#4B44FB', \
	'#D3CF34' : '#4B44FB', \
	'#52DCEE' : '#276986', \
	'#F9C216' : '#276986', \
	'#18E3C4' : '#366B68', \
	'#FDBB98' : '#366B68', \
	'#41E586' : '#236F52', \
	'#F8B9C6' : '#236F52', \
	'#98FC88' : '#318D34', \
	'#EDDFFD' : '#318D34', \
	'#F0EB10' : '#9A7617', \
	'#E2E4EF' : '#9A7617', \
	'#F3E3C9' : '#C45F18', \
	'#D5E8EF' : '#C45F18', \
	'#F3E1DE' : '#F71717', \
	'#63FCE9' : '#F71717', \
	'#FEDBEB' : '#E42D8E', \
	'#92FBB0' : '#E42D8E', \
	'#EDDFFD' : '#C820FB', \
	'#98FC88' : '#C820FB', \
	'#E2E4EF' : '#576EF8', \
	'#F0EB10' : '#576EF8', \
	'#D5E8EF' : '#1485AC', \
	'#F3E3C9' : '#1485AC', \
	'#63FCE9' : '#2F8882', \
	'#F3E1DE' : '#2F8882', \
	'#92FBB0' : '#108C64', \
	'#FEDBEB' : '#108C64', \
	}

	def __init__(self, fill_color=None):
		if fill_color == None:
			n = int(random.random() * (len(self.__colors_dict) - 1))
			fill_color = self.__colors_dict.keys()[n]

		self._fill_color = fill_color

	def get_stroke_color(self):
		return self.__colors_dict[self._fill_color]

	def get_fill_color(self):
		return self._fill_color

class IconCache(gobject.GObject):
	__metaclass__ = GObjectSingletonMeta

	def __init__(self):
		gobject.GObject.__init__(self)
		self._icons = {}

	def _create_icon(self, name, color, size):
		theme = gtk.icon_theme_get_default()
		info = theme.lookup_icon(name, size, 0)
		icon_file = open(info.get_filename(), 'r')
		data = icon_file.read()
		icon_file.close()

		if color != None:
			fill = color.get_fill_color()
			stroke = color.get_stroke_color()

			style = '.fill {fill:%s;stroke:%s;}' % (fill, fill)
			data = re.sub('\.fill \{.*\}', style, data)

			style = '.shape {stroke:%s;fill:%s;}' % (stroke, stroke)
			data = re.sub('\.shape \{.*\}', style, data)

			style = '.shape-and-fill {fill:%s; stroke:%s;}' % (fill, stroke)
			data = re.sub('\.shape-and-fill \{.*\}', style, data)

		loader = gtk.gdk.pixbuf_loader_new_with_mime_type('image/svg-xml')
		loader.set_size(size, size)
		loader.write(data)
		loader.close()
		
		return loader.get_pixbuf()

	def get_icon(self, name, color, size):
		key = (name, color, size)
		if self._icons.has_key(key):
			return self._icons[key]
		else:
			icon = self._create_icon(name, color, size)
			self._icons[key] = icon
			return icon

class IconItem(goocanvas.Image):
	def __init__(self, icon_name, color, size, **kwargs):
		goocanvas.Image.__init__(self, **kwargs)

		icon_cache = IconCache()
		pixbuf = icon_cache.get_icon(icon_name, color, size)
		self.set_property('pixbuf', pixbuf)
