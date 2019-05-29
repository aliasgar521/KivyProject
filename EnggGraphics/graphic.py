import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.config import Config 
from socket import *
from kivy.core.window import Window
import os

from kivy.graphics import Rectangle
f1,f2,f3,f4 = False, False, False, False
class testWidget(Widget):
	def on_touch_down(self,touch):
		global f1,f2,f3,f4
		if 'markerid' in touch.profile:
			#print(touch.x,touch.y)
			#and touch.x < 200 and touch.y < 300
			if touch.fid==3:
				print(touch.x,touch.y)
				f1=True
				
			elif f1:
				if touch.fid==2:
					with self.canvas.before:
						Rectangle(source="2.jpg",pos=self.pos,size=self.size)
						#self.add_widget(Rectangle(source="download.jpeg"))
			elif touch.fid==6:
				with self.canvas.before:
					Rectangle(source="3.jpg",pos=self.pos,size=self.size)
					
			if touch.fid==9:
				os.system("python ../project_jan_update/test.py")
				quit()
			
	def on_touch_up(self,touch):
		if 'markerid' in touch.profile:
			if touch.fid==6:
				with self.canvas.before:
					Rectangle(source="1.jpg",pos=self.pos,size=self.size)

class GraphicApp(App):
	def build(self):
		Config.set('input','fid1','tuio,0.0.0.0:3333')
		return testWidget()

	
if __name__ == '__main__':
	#Window.fullscreen = True

	GraphicApp().run()
