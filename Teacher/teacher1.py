from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class Teacher1Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text="Go Back teacher",
                           color=(1,0,0,1)

                              )


        self.add_widget(self.label)