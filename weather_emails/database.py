import sqlite3

def execute_query(conn, querry, cur):
    cur.execute(querry)
    conn.commit()

def connect_to_database():
    conn = sqlite3.connect('database.sqlite')
    cur = conn.cursor()
    conn.close()

def post_user(conn, cur, name, city, weather_fields):
    querry = f'INSERT INTO users(name, city, weather_fields) values ("{name}", "{city}", "{weather_fields}")'
    execute_query(conn, querry, cur)
    

def get_user(conn, cur):
    user_name = print(input("Enter user name: "))
    querry = f'SELECT * FROM name WHERE name = {user_name}'
    execute_query(conn, querry, cur)


def delete_user(conn, cur):
    user_name = print(input("Enter user name: "))
    querry = f'DELETE * FROM name WHERE name = {user_name}'
    execute_query(conn, querry, cur)


def patch_user(conn, cur):
    querry = f'UPDATE users SET name = "Tom" WHERE name = "John"'
    execute_query(conn, querry, cur)