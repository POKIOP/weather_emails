from weather_emails import gmail, weather
import sqlite3
import database
import ui


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
        weather_field1 = input("Enter weather component no 1: ")
        weather_field2 = input("Enter weather component no 2: ")
        email = input("Enter email adress: ")
        user = database.post_user(conn, cursor, user_name, city, weather_field1, weather_field2, email)
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
        for user in users: 
            temperature = weather.get_city_temperature(user[1])
            pressure = weather.get_city_pressure(user[1])
            humidity = weather.get_city_humidity(user[1])
            weather_component1 = user[2]
            weather_component2 = user[3]
            creds = gmail.get_credentials()
            if weather_component1 == "temperature" and weather_component2 == "pressure":
                email_content = f'Good morning {user[0]},\n\nToday at {user[1]} is {temperature} C degrees, pressure is: {pressure} hPa.'
            elif weather_component1 == "pressure":
                email_content = f'Good morning {user[0]},\n\nToday at {user[1]} is {pressure} hPa.'  
            elif weather_component1 == "humidity":
                email_content = f'Good morning {user[0]},\n\nToday at {user[1]} is {humidity} % of humidity.'           
            else:
                email_content = f'Good morning. \n\nDear {user[0]} you not chosen correct weather component.'
            message_id = gmail.send_email(creds, email_content, user[4], SUBJECT)
            if message_id is None:
                print("Message not send")
            else:
                print("Message send")



if __name__ == "__main__":
    main()
