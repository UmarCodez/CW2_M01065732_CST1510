import sqlite3

def get_connection():
    return sqlite3.connect('DATA/intelligence_platform.db', check_same_thread=False)

#create_user_table(conn)
#migrate_users(conn)
# print(get_all_users(conn))