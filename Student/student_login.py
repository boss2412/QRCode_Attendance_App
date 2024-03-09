from kivy.uix.screenmanager import Screen
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="boss2412",
)


class StudentLogin(Screen):
    pass
