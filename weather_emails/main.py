#polaczyc plik weather i gmail zeby zbieralo informacje i wysylalo emaila
# wiecej parametrow pogodowych - zmiany w email contetnt
# https://builtin.com/data-science/sqlite

from weather_emails import gmail, weather
import sqlite3
import database
import ui

CITY_NAME = "New York"
DATABASE_FILE = "weather.sqlite"
EMAIL_RECIPIENT = 'jkstycz91@gmail.com'
NAME = "James"
SUBJECT = 'Temperature today'
WEATHER_FIELDS = "temperature"


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
        database.post_user(conn, cursor, user_name, city, weather_fields)
    elif option == "update":
        city_name = input("Enter city name: ")
        current_city_name = input("Enter new city name: ")
        database.patch_user(conn, cursor, city_name, current_city_name)

    


    # temperature = weather.get_city_temperature(CITY_NAME)
    # pressure = weather.get_city_pressure(CITY_NAME)
    # creds = gmail.get_credentials()
    # email_content= f'Good morning {NAME},\n\nToday at {CITY_NAME} is {temperature} C degrees and {pressure} hPa.'
    # message_id = gmail.send_email(creds, email_content, EMAIL_RECIPIENT, SUBJECT)
    
    # print(message_id)




if __name__ == "__main__":
    main()