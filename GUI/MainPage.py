from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Window.clearcolor = 1,1,1,1

class MainBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ThirdScreen(Screen):
    pass
class MyScreenManager(ScreenManager):
    pass
class MainWidget(Widget):
    pass

class MainPage(App):
    def build(self):
        return Builder.load_file('mainpage.kv')

MainPage().run()