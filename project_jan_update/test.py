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
import kivy
import sys
import os
import paint
import pong
#import MyPaintApp			
#import green
#import main
import subprocess

f1,f2,f3,f4 = False, False, False, False

class testApp(App):
	def build(self):
		
		Config.set('input', 'fid1', 'tuio,0.0.0.0:3333')
       	 	# You can also add a second TUIO listener
        	# Config.set('input', 'source2', 'tuio,0.0.0.0:3334')
        	# Then do the usual things
       	 	# ...
		#Window.clearcolor = (0, 0, 1, 1)
		#Label(text='Hello world')
		def __init__(self, **kwargs):
			super(testApp,self).__init__(**kwargs)
		#self.add_widget(Label(text="Hello world"))
		return testWidget()
class testWidget(Widget):
	
	
	def on_touch_down(self,touch):
		global f1,f2,f3,f4

		if 'markerid' in touch.profile:
			if touch.fid==116:
				os.system("python ../Animation/shortest_path.py")				
				#pong.PongApp().run()
				return
			if touch.fid==9:
				f1=True
				p = subprocess.os.system("python ../EnggGraphics/graphic.py")
				p.terminate()
			#	os.system("python ../EnggGraphics/graphic.py")
				#paint.MyPaintApp.run()
			if f1:
				sys.exit()
				return
			if touch.fid==114:
				os.system("python ../feb/image.py")
				#paint.MyPaintApp.run()
				return
if __name__ == '__main__':
	testApp().run()
