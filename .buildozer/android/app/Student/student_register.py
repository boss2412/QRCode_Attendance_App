import qrcode
from kivy.uix.screenmanager import Screen
import mysql.connector
from qrcode.main import QRCode
import os


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


class StudentRegister(Screen):
    pass
