#polaczyc plik weather i gmail zeby zbieralo informacje i wysylalo emaila
# wiecej parametrow pogodowych - zmiany w email contetnt

from weather_emails import gmail, weather
import sqlite3
import database

CITY_NAME = "North Berwick"
DATABASE_FILE = "weather.sqlite"
EMAIL_RECIPIENT = 'jkstycz91@gmail.com'
NAME = "John"
CREATE_TABLE_QUERRY = "CREATE TABLE users (name VARCHAR, city VARCHAR, weather_fields VARCHAR)"
SUBJECT = 'Temperature today'
WEATHER_FIELDS = "temperature"


def main():
    with sqlite3.connect(DATABASE_FILE) as con:
        cur = con.cursor()
        database.execute_query(con, CREATE_TABLE_QUERRY, cur)
        database.post_user(con, cur, NAME, CITY_NAME, WEATHER_FIELDS)


        


#     temperature = weather.get_city_temperature(CITY_NAME)
#     pressure = weather.get_city_pressure(CITY_NAME)
#     creds = gmail.get_credentials()
#     email_content= f'Good morning {NAME},\n\nToday at {CITY_NAME} is {temperature} C degrees and {pressure} hPa.'
#     message_id = gmail.send_email(creds, email_content, EMAIL_RECIPIENT, SUBJECT)
    
#     print(message_id)




if __name__ == "__main__":
    main()
