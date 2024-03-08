from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from Student.student_login import StudentLoginRegister
from Teacher.register_screen import RegisterScreen
from Student.student_register import StudentRegisterScreen
from Teacher.teacher_login_register import TeacherLoginRegister
from welcome_screen import WelcomeScreen
from kivy.core.window import Window
from kivy.core.text import LabelBase

#To get output that would appear on mobile
Window.size = (360, 640)

#For Custom Font Style
LabelBase.register(name="MPoppins", fn_regular="C:/Users/anura/PycharmProjects/MiniProject/fonts/Poppins/Poppins"
                                               "-Medium.ttf",
                   )

LabelBase.register(name="BPoppins", fn_regular="C:/Users/anura/PycharmProjects/MiniProject/fonts/Poppins/Poppins"
                                               "-SemiBold.ttf",
                   )


class MainApp(MDApp):
    def build(self):
        # Load the KV files
        Builder.load_file('welcome_screen.kv')
        Builder.load_file('Student/student_login.kv')
        Builder.load_file('Teacher/teacher_login_register.kv')
        Builder.load_file('Teacher/register_screen.kv')
        Builder.load_file('Student/student_register.kv')


        # Initialize the ScreenManager
        self.sm = ScreenManager()
        self.sm.add_widget(WelcomeScreen(name='welcome'))
        self.sm.add_widget(StudentLoginRegister(name='student_login_register'))
        self.sm.add_widget(TeacherLoginRegister(name='teacher_login_register'))
        self.sm.add_widget(RegisterScreen(name='register_screen'))
        self.sm.add_widget(StudentRegisterScreen(name='student_register_screen'))
        return self.sm


if __name__ == '__main__':
    MainApp().run()
