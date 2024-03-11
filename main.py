import qrcode
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from qrcode.main import QRCode

from Student.student_login import StudentLogin
from Teacher.teacher_register import TeacherRegister
from Student.student_register import StudentRegister, insert_student_data, generate_qr_code
from Teacher.teacher_login import TeacherLogin
from welcome_screen import WelcomeScreen
from kivy.core.window import Window
from kivy.core.text import LabelBase
import mysql.connector
import os


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
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = None

    def build(self):
        # Load the KV files
        Builder.load_file('welcome_screen.kv')
        Builder.load_file('Student/student_login.kv')
        Builder.load_file('Teacher/teacher_login.kv')
        Builder.load_file('Teacher/teacher_register.kv')
        Builder.load_file('Student/student_register.kv')

        # Initialize the ScreenManager
        self.sm = ScreenManager()
        self.sm.add_widget(WelcomeScreen(name='welcome'))
        self.sm.add_widget(StudentLogin(name='student_login'))
        self.sm.add_widget(TeacherLogin(name='teacher_login'))
        self.sm.add_widget(TeacherRegister(name='teacher_register'))
        self.sm.add_widget(StudentRegister(name='student_register'))
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

        # Commit the transaction
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

if __name__ == '__main__':
    MainApp().run()
