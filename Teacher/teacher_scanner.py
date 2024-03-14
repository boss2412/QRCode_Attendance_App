from kivy.uix.screenmanager import Screen
import cv2
from pyzbar.pyzbar import decode
import mysql.connector
import pandas as pd


scan_flag = True


def scan_qr_code():
    cap = cv2.VideoCapture(0)

    while scan_flag :
        ret, frame = cap.read()
        decoded_objects = decode(frame)

        for obj in decoded_objects:
            data = obj.data.decode("utf-8")
            print("QR Code Data:", data)
            # Assuming data is in the format "name,college_id,email"
            name, college_id, email = data.split(',')
            insert_into_db(name, college_id, email)

        cv2.imshow('QR Code Scanner', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def insert_into_db(name, college_id, email):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='attendanceapp',
            user='root',
            password='boss2412'
        )

        cursor = connection.cursor()
        query = "INSERT IGNORE INTO attendance (name, college_id, email) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, college_id, email))
        connection.commit()
        print("Data inserted successfully")

    except mysql.connector.Error as error:
        print("Failed to insert data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def xlsx():
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="boss2412",
        database="attendanceapp"
    )

    # Query to select data from MySQL table
    query = "SELECT * FROM attendance"

    # Execute query and fetch data into a pandas DataFrame
    df = pd.read_sql(query, conn)

    # Close the MySQL connection
    conn.close()

    # Write DataFrame to Excel file
    output_file = "attendance.xlsx"
    df.to_excel(output_file, index=False)

    print(f"Data has been exported to {output_file}")


class TeacherScanner(Screen):
    pass
