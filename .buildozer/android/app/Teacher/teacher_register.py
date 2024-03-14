from kivy.uix.screenmanager import Screen
import mysql.connector


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

class TeacherRegister(Screen):
    pass
