from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.config import Config


class MyPaintWidget(Widget):

    #def on_touch_down(self, touch):
        #with self.canvas:
          #  Color(1, 1, 0)
           # d = 30.0
           # Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))

	def on_touch_move(self, touch):
		if 'markerid' in touch.profile:
			if touch.fid%2==0:
				print(touch)
				with self.canvas:
					Color(1, 1, 0)
					d = 30.0
					Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
					touch.ud['line'] = Line(points=(touch.x, touch.y))
			if touch.fid%2==1:
				print(touch)
				with self.canvas:
					Color(0, 1, 0)
					d = 30.0
					Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
					touch.ud['line'] = Line(points=(touch.x, touch.y))


class MyPaintApp(App):

    def build(self):
		Config.set('input', 'fid1', 'tuio,0.0.0.0:3333')
		return MyPaintWidget()


if __name__ == '__main__':
    MyPaintApp().run()
