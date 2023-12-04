from weather_emails import gmail, weather

import sqlite3
import database
import ui
from models import User

DATABASE_FILE = "weather.sqlite"
SUBJECT = 'Weather forecast for you'


def main():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    database.create_table_if_not_exist(conn, cursor)
    option = ui.get_user_option()
    if option == "delete":
        print("DELETE option selected")
        email = input("Enter email adress: ")
        user = User(email = email)
        database.delete_user(conn, cursor, user)

    elif option == "create":
        print("CREATE option selected")
        name = input("Enter user name: ")
        city = input("Enter city name: ")
        weather_fields = input("Enter weather component: ")
        email = input("Enter email adress: ")
        user = User(name = name, city = city, weather_fields=weather_fields, email=email)
        database.post_user(conn, cursor, user)
        
    elif option == "update":
        print("UPDATE option selected") # TODO
        user_name = input("Enter user name: ")
        field_to_change = input("Enter field to change: ")
        new_value = input("Enter new value: ")
        database.patch_user(conn, cursor, field_to_change, new_value, user_name)
    elif option == "send_email":
        print("SEND_EMAIL option selected")
        users = database.get_users(conn, cursor)
        if not users:
            print("No users in database")
            return
        creds = gmail.get_credentials()
        for user in users: 
            message = weather.prepare_message(user)
            
            if not message:                   
                message = f'Good morning. \n\nDear {user[0]} you did not choose correct weather component.'

            message_id = gmail.send_email(creds, message, user[3], SUBJECT)
            if message_id is None:
                print("Message not send")
            else:
                print("Message send")


if __name__ == "__main__":
    main()
