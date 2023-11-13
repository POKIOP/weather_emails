import sqlite3

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

def post_user(conn, cur, name, city, weather_fields, email):
    querry = f'INSERT INTO users(name, city, weather_fields, email) values ("{name}", "{city}", "{weather_fields}", "{email}")'
    execute_query(conn, querry, cur)
    

def get_user(conn, cur, email):
    querry = f'SELECT * FROM users WHERE email = "{email}"'
    user = execute_query(conn, querry, cur)
    return user[0]

def get_users(conn, cur):
    querry = f'SELECT * FROM users'
    users = execute_query(conn, querry, cur)
    return users


def delete_user(conn, cur, email):
    querry = f'DELETE FROM users WHERE email = "{email}"'
    user = execute_query(conn, querry, cur)
    return user


def patch_user(conn, cur, field_to_change, new_value, user_name):
    querry = f"""UPDATE users SET "{field_to_change}" = "{new_value}" WHERE name = "{user_name}" """
    # querry = f"""UPDATE users SET weather_fields = "{weather_component}" WHERE weather_fields = "{current_weather_component}" """
    execute_query(conn, querry, cur)

def create_table_if_not_exist(conn, cur):
    cur.execute(""" SELECT count(name) FROM sqlite_master WHERE type="table" AND name="users" """)
    if cur.fetchone()[0]==1:
        print('Table already exists.')
    else:
        execute_query(conn, CREATE_TABLE_QUERRY, cur)
