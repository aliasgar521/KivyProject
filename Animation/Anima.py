from kivy.uix.widget import Widget
from kivy.app import App
from kivy.animation import Animation
from kivy.properties import StringProperty

class Ball(Widget):
	#anim_choice = StringProperty('touch_down to animate ball')
	#counter=0
	def on_touch_down(self, touch):
		print(touch)
		#Animation.cancel_all(self)
		#anim_choices = ['in_back','in_bounce','in_circ','in_cubic','in_elastic','in_expo','in_out_back','in_out_bounce','in_out_circ','out_sine']
		#self.anim_choice = anim_choices [self.counter]
		#anim = Animation(center_x = touch.x, center_y=touch.y, t=self.anim_choice)
		#anim.start(self)
		#print(touch.x,touch.y)
		#self.counter = (self.counter + 1) % len(anim_choices)

class Anima(Widget):
	pass

class AnimaApp(App):
	def build(self):
		return Anima()

if __name__=='__main__':
	AnimaApp().run()
