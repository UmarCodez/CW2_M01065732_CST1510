import sqlite3
import pandas as pd

def migrate_cyber_incidents(conn):   
    data = pd.read_csv('DATA/cyber_incidents.csv')
    data.to_sql('cyber_incidents', conn)

def get_all_cyber_incidents():
    conn = sqlite3.connect('DATA/intelligence_platform.db', check_same_thread=False)
    sql = 'SELECT * FROM cyber_incidents'
    data = pd.read_sql(sql, conn)
    conn.close()
    return data

#def get_all_cyber_incidents(conn):
    #sql = 'SELECT * FROM cyber_incidents'
    #data = pd.read_sql(sql, conn)
    #conn.close()
    #return(data)