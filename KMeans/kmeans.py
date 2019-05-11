import kivy
from functools import wraps
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.config import Config
from socket import *
from kivy.graphics import Rectangle
from kivy.clock import Clock
import time


class testWidget(Widget):
	def my_callback(self,dt):
		print("Hello")
		time.sleep(5)
		pass
		
	def on_touch_down(self,touch):
		if 'markerid' in touch.profile:
			if touch.fid==2:
				with self.canvas.before:
					
					Rectangle(source="KM_k2_1.jpg",pos=self.pos,size=self.size)
					print("yes")
					Clock.schedule_once(root.ping,5)
					#time.sleep(1)
					print("After 5 seconds")
					Rectangle(source="KM_k2_2.jpg",pos=self.pos,size=self.size)
					print("Second image")
					Clock.schedule_once(self.my_callback,5)
					#time.sleep(1)
					Rectangle(source="KM_k2_3.jpg",pos=self.pos,size=self.size)
					print("Third image")
					#self.add_widget(Rectangle(source="download.jpeg"))
			elif touch.fid==6:
				with self.canvas.before:
					Rectangle(source="3.jpg",pos=self.pos,size=self.size)
			elif touch.fid==7:
				with self.canvas.before:
					Rectangle(source="1.jpg",pos=self.pos,size=self.size)
					
	
		

class KmeansApp(App):
	def build(self):
		Config.set('input','fid1','tuio,0.0.0.0:3333')
		return testWidget()

	
if __name__ == '__main__':
	my_callback=testWidget()
	KmeansApp().run()
