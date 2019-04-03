import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.config import Config 
from socket import *
from kivy.graphics import Rectangle

f1,f2,f3 = False, False, False

class testWidget(Widget):
	def on_touch_down(self,touch):
		global f1,f2,f3
		if 'markerid' in touch.profile:
			if touch.fid==2:
				f1=True
				print("yes1")
				
			if touch.fid==4:
				f2=True
				print("yes2")
				
			if f1 and f2:
				with self.canvas.before:
					Rectangle(source="Map2.jpg",pos=self.pos,size=self.size)
class Shortest_pathApp(App):
	def build(self):
		Config.set('input','fid1','tuio,0.0.0.0:3333')
		return testWidget()

	
if __name__ == '__main__':
	Shortest_pathApp().run()
