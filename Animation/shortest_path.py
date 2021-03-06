import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.config import Config 
from socket import *
from kivy.graphics import Rectangle
from kivy.animation import Animation
from kivy.core.window import Window

f1,f2,f3,f4 = False, False, False, False

class testWidget(Widget):
	def animate(self, instance):
        # create an animation object. This object could be stored
        # and reused each call or reused across different widgets.
        # += is a sequential step, while &= is in parallel
		instance.opacity = 100
		animation = Animation(pos=(640, 160)) + Animation(pos=(580,110))
		#animation += Animation(pos=(200, 100), t='out_back')
		animation.repeat = True
        #animation &= Animation(size=(500, 500))
        #animation += Animation(size=(100, 50))

        # apply the animation on the button, passed in the "instance" argument
        # Notice that default 'click' animation (changing the button
        # color while the mouse is down) is unchanged.
		animation.start(instance)
	def animate2(self, instance):
		instance.opacity = 100
		animation = Animation(pos=(880, 370)) + Animation(pos=(690,220))
		animation.repeat = True
		animation.start(instance)
	def animate3(self, instance):
		instance.opacity = 100
		animation = Animation(pos=(580, 500)) + Animation(pos=(880,400))
		animation.repeat = True
		animation.start(instance)
	def animate4(self, instance):
		instance.opacity = 100
		animation = Animation(pos=(535, 750)) + Animation(pos=(555,570))
		animation.repeat = True
		animation.start(instance)
	def on_touch_down(self,touch):
		global f1,f2,f3,f4
		
		if 'markerid' in touch.profile:
			
			if touch.fid==2:
				f1=True
				self.ids.image1=self.animate(self.ids.image1)
				print("yes1")
				
			if touch.fid==3:
				f2=True
				self.ids.image2=self.animate2(self.ids.image2)
				print("yes2")
				
			if touch.fid==4:
				f3=True
				self.ids.image3=self.animate3(self.ids.image3)
				print("yes3")
			if touch.fid==11:
				f4=True
				self.ids.image4=self.animate4(self.ids.image4)
				print("yes4")
				
			if f1 and f2 and f3 and f4:
				with self.canvas.before:
					Rectangle(source="Map2.jpg",pos=self.pos,size=self.size)
	
class Shortest_pathApp(App):    
	def build(self):
		Config.set('input','fid1','tuio,0.0.0.0:3333')
		return testWidget()

	
if __name__ == '__main__':
	#Window.fullscreen = True
	Shortest_pathApp().run()
