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
from kivy.uix.carousel import Carousel


class testWidget(Widget):
	def my_callback(self,dt):
		print("Hello")
		
		pass
		
	def on_touch_down(self,touch):
		if 'markerid' in touch.profile:
			if touch.fid==2:
				with self.canvas.before:
					
					Rectangle(source="KM_k2_1.jpg",pos=self.pos,size=self.size)
					print("yes")
					Clock.schedule_once(self.my_callback,5)
					#time.sleep(3)
					print("After 5 seconds")
					Rectangle(source="KM_k2_2.jpg",pos=self.pos,size=self.size)
					print("Second image")
					Clock.schedule_once(self.my_callback,5)
					#time.sleep(3)
					Rectangle(source="KM_k2_3.jpg",pos=self.pos,size=self.size)
					print("Third image")
					#self.add_widget(Rectangle(source="download.jpeg"))
			elif touch.fid==6:
				with self.canvas.before:
					Rectangle(source="3.jpg",pos=self.pos,size=self.size)
			elif touch.fid==7:
				with self.canvas.before:
					Rectangle(source="1.jpg",pos=self.pos,size=self.size)
					
	
class MyCarousel(Carousel):

    def __init__(self, **kwargs):
        super(MyCarousel, self).__init__(**kwargs)
        self.direction = "right"
        for i in range(0,4):
            src = "KM_k2_%d.jpg" % i
            image = Image(source=src, allow_stretch=True)
            self.add_widget(image)

        self.loop = False
        Clock.schedule_interval(self.load_next,3)
        
        

KV = """

ScreenManager:
    Screen:
        name: "scr1"
        BoxLayout:
            Button:
                text: "Carousel"
                on_release: root.current = "scr2"
    Screen:
        name: "scr2"
        BoxLayout:
			orientation: "vertical"
            MyCarousel:
            Button:
                text: "Back"
                on_release: root.current = "scr1"
				size_hint: None, None

"""


class CarouselApp(App):
    def build(self):
        return Builder.load_string(KV)
        
class KmeansApp(App):
	def build(self):
		Config.set('input','fid1','tuio,0.0.0.0:3333')
		return testWidget()

	
if __name__ == '__main__':
	KmeansApp().run()
