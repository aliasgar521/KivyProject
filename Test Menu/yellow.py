from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
class MyApp(App):
	def build(self):
		Window.clearcolor = (1, 1, 0, 1)
		return Label(text='Hello world')
if __name__ == '__main__':
	MyApp().run()

