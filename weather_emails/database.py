import sqlite3

CREATE_TABLE_QUERRY = "CREATE TABLE users (name VARCHAR, city VARCHAR, weather_fields VARCHAR)"


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
    

def get_user(conn, cur, user_name):
    querry = f'SELECT * FROM name WHERE name = {user_name}'
    execute_query(conn, querry, cur)


def delete_user(conn, cur, user_name):
    querry = f'DELETE FROM name WHERE name = {user_name}'
    execute_query(conn, querry, cur)


def patch_user(conn, cur, city_name, current_city_name):
    querry = f"""UPDATE users SET city = {city_name} WHERE name = {current_city_name} """
    execute_query(conn, querry, cur)

def create_table_if_not_exist(conn, cur):
    cur.execute(""" SELECT count(name) FROM sqlite_master WHERE type="table" AND name="users" """)
    if cur.fetchone()[0]==1:
        print('Table already exists.')
    else:
        execute_query(conn, CREATE_TABLE_QUERRY, cur)
