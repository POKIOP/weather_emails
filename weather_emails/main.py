#polaczyc plik weather i gmail zeby zbieralo informacje i wysylalo emaila
# wiecej parametrow pogodowych - zmiany w email contetnt
# https://builtin.com/data-science/sqlite

from weather_emails import gmail, weather
import sqlite3
import database
import ui


DATABASE_FILE = "weather.sqlite"
EMAIL_RECIPIENT = 'jkstycz91@gmail.com'

SUBJECT = 'Temperature today'



def main():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    database.create_table_if_not_exist(conn, cursor)
    option = ui.get_user_option()
    if option == "delete":
        user_name = input("Enter user name: ")
        database.delete_user(conn, cursor, user_name)
    elif option == "create":
        user_name = input("Enter user name: ")
        city = input("Enter city name: ")
        weather_fields = input("Enter weather component: ")
        email = input("Enter email adress: ")
        database.post_user(conn, cursor, user_name, city, weather_fields, email)
    elif option == "update":
        city_name = input("Enter new city name: ")
        current_city_name = input("Enter city name: ")
        database.patch_user(conn, cursor, city_name, current_city_name)
    # users = database.get_users(conn, cursor)
    # for user in users:
        
    #     tempereture = weather.get_city_temperature(user[1])
        
    # # pressure = weather.get_city_pressure(user[1])
    #     creds = gmail.get_credentials()
    #     email_content= f'Good morning {user[0]},\n\nToday at {user[1]} is {tempereture} C degrees.'
    #     message_id = gmail.send_email(creds, email_content, EMAIL_RECIPIENT, SUBJECT)
        
    #     print(message_id)




if __name__ == "__main__":
    main()
