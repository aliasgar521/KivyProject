from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image

from kivy.clock import Clock
from kivy.lang import Builder

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


CarouselApp().run()
