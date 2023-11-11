#polaczyc plik weather i gmail zeby zbieralo informacje i wysylalo emaila
# wiecej parametrow pogodowych - zmiany w email contetnt
# https://builtin.com/data-science/sqlite

from weather_emails import gmail, weather
import sqlite3
import database
import ui


DATABASE_FILE = "weather.sqlite"
# EMAIL_RECIPIENT = 'jkstycz91@gmail.com'

SUBJECT = 'Weather forecast for you'



def main():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    database.create_table_if_not_exist(conn, cursor)
    option = ui.get_user_option()
    if option == "delete":
        print("DELETE option selected")
        user_name = input("Enter email adress: ")
        database.delete_user(conn, cursor, user_name)
    elif option == "create":
        print("CREATE option selected")
        user_name = input("Enter user name: ")
        city = input("Enter city name: ")
        weather_fields = input("Enter weather component: ")
        email = input("Enter email adress: ")
        database.post_user(conn, cursor, user_name, city, weather_fields, email)
    elif option == "update":
        print("UPDATE option selected")
        city_name = input("Enter new city name: ")
        current_city_name = input("Enter city name: ")
        database.patch_user(conn, cursor, city_name, current_city_name)
    elif option == "send_email":
        print("SEND_EMAIL option selected")
        users = database.get_users(conn, cursor)
        for user in users:
            city= (user[1])
            tempreture = weather.get_city_temperature(city)
            pressure = weather.get_city_pressure(city)
            weather_component = (user[2])
            email = (user[3])
            
    
            creds = gmail.get_credentials()
            if weather_component == "tempreture":
                email_content= f'Good morning {user[0]},\n\nToday at {city} is {tempreture} C degrees.'
            elif weather_component == "pressure":
                email_content= f'Good morning {user[0]},\n\nToday at {city} is {pressure} hPa.'        
            message_id = gmail.send_email(creds, email_content, email, SUBJECT)
            
            print(message_id)




if __name__ == "__main__":
    main()
