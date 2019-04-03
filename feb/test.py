from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.listview import ListItemButton
from kivy.uix.listview import ListItemLabel
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from kivy.config import Config
from kivy.graphics import Color
from kivy.core.window import Window
from socket import *
import kivy
import sys
import os
import paint
import pong
import image

class testApp(App):
	def build(self):
		Config.set('input', 'fid1', 'tuio,0.0.0.0:3333')
       	 	# You can also add a second TUIO listener
        	# Config.set('input', 'source2', 'tuio,0.0.0.0:3334')
        	# Then do the usual things
       	 	# ...
		return testWidget()
class testWidget(Widget):	
	def on_touch_down(self,touch):
		if 'markerid' in touch.profile:
			if touch.fid==2:
				os.system("python image.py")
				testApp()
			if touch.fid==4:
				os.system("python pong.py")	
			
			if touch.fid==1:
				os.system("python paint.py")
				#paint.MyPaintApp.run()
				
if __name__ == '__main__':
	testApp().run()
