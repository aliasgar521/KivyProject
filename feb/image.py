import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.config import Config 
from socket import *
from kivy.graphics import Rectangle
class testWidget(Widget):
	def on_touch_down(self,touch):
		if 'markerid' in touch.profile:
			if touch.fid==5:
				with self.canvas.before:
					Rectangle(source="Sun.png",pos=self.pos,size=self.size)
					#self.add_widget(Rectangle(source="download.jpeg"))
			elif touch.fid==6:
				with self.canvas.before:
					Rectangle(source="Planet1.jpg",pos=self.pos,size=self.size)
			elif touch.fid==7:
				with self.canvas.before:
					Rectangle(source="planet2.jpg",pos=self.pos,size=self.size)
			elif touch.fid==8:
				with self.canvas.before:
					Rectangle(source="planet3.jpg",pos=self.pos,size=self.size)
			elif touch.fid==9:
				with self.canvas.before:
					Rectangle(source="planet4.jpg",pos=self.pos,size=self.size)
			elif touch.fid==10:
				with self.canvas.before:
					Rectangle(source="planet5.jpg",pos=self.pos,size=self.size)
			elif touch.fid==11:
				with self.canvas.before:
					Rectangle(source="planet6.jpg",pos=self.pos,size=self.size)
			elif touch.fid==12:
				with self.canvas.before:
					Rectangle(source="planet8.jpg",pos=self.pos,size=self.size)
			elif touch.fid==13:
				with self.canvas.before:
					Rectangle(source="planet7.jpg",pos=self.pos,size=self.size)
		

class ImageApp(App):
	def build(self):
		Config.set('input','fid1','tuio,0.0.0.0:3333')
		return testWidget()

	
if __name__ == '__main__':
	ImageApp().run()
