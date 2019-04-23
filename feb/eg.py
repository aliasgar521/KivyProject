import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.config import Config 
from socket import *
from kivy.uix.videoplayer import VideoPlayer
from kivy.graphics import Rectangle
class testWidget(Widget):
	def on_touch_down(self,touch):
		if 'markerid' in touch.profile:
			if touch.fid==5:
				with self.canvas.before:
					filename= 'sher.mp4'
					VideoPlayer(source=filename,state='play')	
					
			#		Rectangle(source="sher.mp4",pos=self.pos,size=self.size)
					#self.add_widget(Rectangle(source="download.jpeg"))
			elif touch.fid==6:
				with self.canvas.before:
					Rectangle(source="perspective1.png",pos=self.pos,size=self.size)
		

class EgApp(App):
	def build(self):
		Config.set('input','fid1','tuio,0.0.0.0:3333')
		return testWidget()

	
if __name__ == '__main__':
	EgApp().run()
