from weather_emails import gmail, weather

import sqlite3
import database
from models import User


DATABASE_FILE = "weather.sqlite"
SUBJECT = 'Weather forecast for you'

def delete(conn, cursor):
    print("DELETE option selected")
    email = input("Enter email adress: ")
    user = User(email = email)
    database.delete_user(conn, cursor, user)

def create(conn, cursor):
    print("CREATE option selected")
    name = input("Enter user name: ")
    city = input("Enter city name: ")
    weather_fields = input("Enter weather component: ")
    email = input("Enter email adress: ")
    user = User(name = name, city = city, weather_fields=weather_fields, email=email)
    database.post_user(conn, cursor, user)

def update(conn, cursor):
    print("UPDATE option selected")
    user_name = input("Enter user name: ")
    field_to_change = input("Enter field to change: ")
    new_value = input("Enter new value: ")
    user = User(name = user_name, **{field_to_change:new_value})
    database.patch_user(conn, cursor, field_to_change, new_value, user)

def send_email(conn, cursor):
    print("SEND_EMAIL option selected")
    users = database.get_users(conn, cursor)
    if not users:
        print("No users in database")
        return
    creds = gmail.get_credentials()
    for user in users: 
        message = weather.prepare_message(user)
        if not message:                   
            message = f'Good morning. \n\nDear {user.name} you did not choose correct weather component.'
        message_id = gmail.send_email(creds, message, user.email, SUBJECT)
        if message_id is None:
            print("Message not send")
        else:
            print("Message send")

def main():
    options = {"1":delete, "2":create, "3":update, "4":send_email }
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    database.create_table_if_not_exist(conn, cursor)
    user_ch = input("Enter your option: ")
    user_choice = options[user_ch]
    user_choice(conn, cursor)
    
    
if __name__ == "__main__":
    main()
