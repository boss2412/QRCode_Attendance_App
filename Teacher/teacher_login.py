from kivy.uix.screenmanager import Screen
import mysql.connector


def create_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="boss2412",
        database="attendanceapp"
    )
    return connection


def login1(email_input, password_input):
    connection = create_db_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM teacher WHERE email = %s AND password = %s"
    cursor.execute(query, (email_input, password_input))
    result = cursor.fetchone()
    connection.close()
    if result:
        # Convert the result tuple into a dictionary
        user_data = dict(zip([column[0] for column in cursor.description], result))
        return user_data
    else:
        return None


class TeacherLogin(Screen):
    pass
