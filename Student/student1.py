import email

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager


class Login1Screen(Screen):
    def __init__(self, **kwargs):
        super(Login1Screen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.label1 = Label(text='Email')
        self.email = TextInput(multiline=False)
        layout.add_widget(self.email)

        self.label1 = Label(text='Password')
        self.password = TextInput(password=True, multiline=False)
        layout.add_widget(self.password)

        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.validate_login)
        layout.add_widget(self.login_button)

        self.register_button = Button(text='Register')
        self.register_button.bind(on_press=self.go_to_register)
        layout.add_widget(self.register_button)

        self.add_widget(layout)

    def validate_login(self, instance):
        username = self.username.text
        password = self.password.text
        if username == 'admin' and password == 'password':
            print('Login successful')
            # Here you can navigate to another screen or perform other actions
        else:
            print('Login failed')

    def go_to_register(self, instance):
        self.manager.current = 'register1'


class Register1Screen(Screen):
    def __init__(self, **kwargs):
        super(Register1Screen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.label1 = Label(text='Email')
        self.email = TextInput(multiline=False)
        layout.add_widget(self.email)

        self.label2 = Label(text='Password')
        self.password = TextInput(password=True, multiline=False)
        layout.add_widget(self.password)

        self.register_button = Button(text='Register')
        self.register_button.bind(on_press=self.register_user)
        layout.add_widget(self.register_button)

        self.back_button = Button(text='Back to Login')
        self.back_button.bind(on_press=self.go_to_login)
        layout.add_widget(self.back_button)

        self.add_widget(layout)

    def register_user(self, instance):
        username = self.email.text
        password = self.password.text
        # Here you would typically add the user to a database or authentication service
        print(f'User {email} registered with password {password}')
        # Optionally, navigate back to the login screen after successful registration
        self.go_to_login(instance)

    def go_to_login(self, instance):
        self.manager.current = 'login1'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        return sm


if __name__ == '__main__':
    MyApp().run()
