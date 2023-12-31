import sqlite3
from models import User

CREATE_TABLE_QUERRY = "CREATE TABLE users (name VARCHAR, city VARCHAR, weather_fields VARCHAR, email VARCHAR PRIMARY KEY)"


def execute_query(conn, querry, cur):
    cur.execute(querry)
    response = cur.fetchall()
    conn.commit()
    return response

def connect_to_database():
    conn = sqlite3.connect('database.sqlite')
    cur = conn.cursor()
    conn.close()

def post_user(conn, cur, user):
    querry = f'INSERT INTO users(name, city, weather_fields, email) values ("{user.name}", "{user.city}", "{user.weather_fields}", "{user.email}")'
    execute_query(conn, querry, cur)
    
def get_user(conn, cur, user):
    querry = f'SELECT * FROM users WHERE email = "{user.email}"'
    user = execute_query(conn, querry, cur)[0]
    return User(name=user[0], city=user[1], weather_fields=user[2], email=user[3])

def get_all_users(conn, cur):
    querry = 'SELECT * FROM users'
    users = execute_query(conn, querry, cur)
    return [User(name=user[0], city=user[1], weather_fields=user[2], email=user[3]) for user in users]

def delete_user(conn, cur, user):
    querry = f'DELETE FROM users WHERE email = "{user.email}"'
    execute_query(conn, querry, cur)
    
def patch_user(conn, cur, field_to_change, new_value, user):
    querry = f"""UPDATE users SET "{field_to_change}" = "{new_value}" WHERE name = "{user.name}" """
    execute_query(conn, querry, cur)

def create_table_if_not_exist(conn, cur):
    cur.execute(""" SELECT count(name) FROM sqlite_master WHERE type="table" AND name="users" """)
    if cur.fetchone()[0]==1:
        print('Table already exists.')
    else:
        execute_query(conn, CREATE_TABLE_QUERRY, cur)
