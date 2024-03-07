from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from Student.student1 import Login1Screen, Register1Screen
from Teacher.teacher1 import Login2Screen, Register2Screen


Window.clearcolor = 1, 1, 1, 1


def switch_to_teacher1(instance):
    app = App.get_running_app()
    app.root.current = 'login2'


def switch_to_student1(instance):
    app = App.get_running_app()
    app.root.current = 'login1'


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.button1 = Button(
            size_hint=(1, 1),
            background_normal='student1.png',
            background_down='student2.png'
        )
        self.button1.bind(on_release=switch_to_student1)

        layout.add_widget(self.button1)

        self.button2 = Button(
            size_hint=(1, 1),
            background_normal='teacher1.png',
            background_down='teacher2.png'
        )
        self.button2.bind(on_release=switch_to_teacher1)

        layout.add_widget(self.button2)

        self.add_widget(layout)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(Login1Screen(name='login1'))
        sm.add_widget(Register1Screen(name='register1'))
        sm.add_widget(Login2Screen(name='login2'))
        sm.add_widget(Register2Screen(name='register2'))
        return sm


if __name__ == '__main__':
    MyApp().run()
