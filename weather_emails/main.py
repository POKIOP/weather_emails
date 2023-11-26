from weather_emails import gmail, weather
from dataclasses import dataclass
import sqlite3
import database
import ui

# https://realpython.com/python-data-classes/

@dataclass
class User:
    name: str
    city: str
    weather_fields: str
    email: str



DATABASE_FILE = "weather.sqlite"
SUBJECT = 'Weather forecast for you'


def main():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    database.create_table_if_not_exist(conn, cursor)
    option = ui.get_user_option()
    if option == "delete":
        print("DELETE option selected")
        user_name = input("Enter email adress: ")
        user = database.delete_user(conn, cursor, user_name)
        if not user:
            print("No user in database")
            return
    elif option == "create":
        print("CREATE option selected")
        user_name = input("Enter user name: ")
        city = input("Enter city name: ")
        weather_fields = input("Enter weather component: ")
        email = input("Enter email adress: ")
        user = database.post_user(conn, cursor, user_name, city, weather_fields, email)
        print(user)
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

    # @dataclass jak zastosowac do grupowania na : imie , miasto ????                  
            
            message = weather.prepare_message(user[0], user[2], user[1])
            if not message:                   
                message = f'Good morning. \n\nDear {user[0]} you did not choose correct weather component.'

            message_id = gmail.send_email(creds, message, user[3], SUBJECT)
            if message_id is None:
                print("Message not send")
            else:
                print("Message send")



if __name__ == "__main__":
    main()
