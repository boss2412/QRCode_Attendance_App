import qrcode
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.list import TwoLineListItem
from qrcode.main import QRCode
from Student.student_dashboard import StudentDashboard
from Student.student_login import StudentLogin, login
from Teacher.teacher_create import TeacherCreate
from Teacher.teacher_register import TeacherRegister
from Student.student_register import StudentRegister, insert_student_data, generate_qr_code
from Teacher.teacher_login import TeacherLogin, login1
from Teacher.teacher_scanner import TeacherScanner
from welcome_screen import WelcomeScreen
from kivy.core.window import Window
from kivy.core.text import LabelBase
import mysql.connector
import os
from kivy.uix.image import Image
from datetime import datetime

# To get output that would appear on mobile
Window.size = (360, 640)

# For Custom Font Style
LabelBase.register(name="MPoppins", fn_regular="C:/Users/anura/PycharmProjects/MiniProject/fonts/Poppins/Poppins"
                                               "-Medium.ttf",
                   )

LabelBase.register(name="BPoppins", fn_regular="C:/Users/anura/PycharmProjects/MiniProject/fonts/Poppins/Poppins"
                                               "-SemiBold.ttf",
                   )


class MainApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = None

    def build(self):
        # Load the KV files
        Builder.load_file('welcome_screen.kv')
        Builder.load_file('Student/student_register.kv')
        Builder.load_file('Student/student_login.kv')
        Builder.load_file('Student/student_dashboard.kv')
        Builder.load_file('Teacher/teacher_register.kv')
        Builder.load_file('Teacher/teacher_login.kv')
        Builder.load_file('Teacher/teacher_create.kv')
        Builder.load_file('Teacher/teacher_scanner.kv')

        # Initialize the ScreenManager
        self.sm = ScreenManager()
        self.sm.add_widget(WelcomeScreen(name='welcome'))
        self.sm.add_widget(StudentRegister(name='student_register'))
        self.sm.add_widget(StudentLogin(name='student_login'))
        self.sm.add_widget(StudentDashboard(name='student_dashboard'))
        self.sm.add_widget(TeacherRegister(name='teacher_register'))
        self.sm.add_widget(TeacherLogin(name='teacher_login'))
        self.sm.add_widget(TeacherCreate(name='teacher_create'))
        self.sm.add_widget(TeacherScanner(name='teacher_scanner'))


        # if os.path.exists('login_state.txt'):
        #     self.sm.current = 'student_dashboard'
        #
        # else:
        #     self.sm.current = 'welcome'

        if os.path.exists('login_teacher.txt'):
            self.sm.current = 'teacher_create'

        else:
            self.sm.current = 'welcome'

        return self.sm

    def insert_student_data(self, name_input, id_input, email_input, password_input):
        # Database connection parameters
        cnx = mysql.connector.Connect(
            host="localhost",
            user="root",
            passwd="boss2412",
            database="attendanceapp"
        )
        cursor = cnx.cursor()

        # Insert data into the database
        query = "INSERT INTO student (name, college_id, email, password) VALUES (%s, %s, %s, %s)"
        values = (name_input, id_input, email_input, password_input)
        cursor.execute(query, values)

        # Commit transaction
        cnx.commit()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

    def generate_qr_code(self, name_input, id_input, email_input):
        info = f"{name_input},{id_input},{email_input}"

        qr = QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(info)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to the assets directory
        assets_dir = 'assets'
        if not os.path.exists(assets_dir):
            os.makedirs(assets_dir)
        safe_college_id = "".join(c for c in id_input if c.isalnum() or c in ('.', '_'))
        img_path = os.path.join(assets_dir, f'{safe_college_id}.png')
        img.save(img_path)

        print(f"QR code saved to {img_path}")

    def insert_teacher_data(self, name_input, id_input, subject_input, email_input, password_input):
        # Database connection parameters
        cnx = mysql.connector.Connect(
            host="localhost",
            user="root",
            passwd="boss2412",
            database="attendanceapp"
        )
        cursor = cnx.cursor()

        # Insert data into the database
        query = "INSERT INTO teacher (name, college_id, subject, email, password) VALUES (%s, %s, %s, %s, %s)"
        values = (name_input, id_input, subject_input, email_input, password_input)
        cursor.execute(query, values)

        # Commit the transaction
        cnx.commit()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

    def go_to_teacher_scanner_screen(self):
        self.sm.current = 'teacher_scanner'

    def login_user(self, email, password):
        user_data = login(email, password)
        if user_data:
            print("Login successful")
            self.sm.current = 'student_dashboard'
            self.populate_dashboard(user_data)
            with open('login_state.txt', 'w') as file:
                file.write('Logged in')
        else:
            print("Login failed")

    def login_teacher(self, email, password):
        user_data = login1(email, password)
        if user_data:
            print("Login successful")
            self.sm.current = 'teacher_create'
            with open('login_teacher.txt', 'w') as file:
                file.write('Logged in')
        else:
            print("Login failed")

    def populate_dashboard(self, user_data):

        dashboard_screen = self.sm.get_screen('student_dashboard')
        user_data_list = dashboard_screen.ids.user_data_list
        user_data_list.clear_widgets()
        for column_name, value in user_data.items():
            if column_name != 'password':
                user_data_list.add_widget(
                    TwoLineListItem(text=column_name, secondary_text=str(value))
                )
        if 'college_id' in user_data:
            image_path = f"assets/{user_data['college_id']}.png"
            image = Image(source=image_path, size_hint=(None, None), size=(300, 300))
            image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            user_data_list.add_widget(image)

    def logout(self):
        if os.path.exists('login_state.txt'):
            os.remove('login_state.txt')
        self.sm.current = 'welcome'

    def logout1(self):
        if os.path.exists('login_teacher.txt'):
            os.remove('login_teacher.txt')
        self.sm.current = 'welcome'


if __name__ == '__main__':
    MainApp().run()
