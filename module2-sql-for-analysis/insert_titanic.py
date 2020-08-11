import pandas as pd
import psycopg2

df = pd.read_csv('titanic.csv')


dbname = 'ksevjtjp'
user = 'ksevjtjp'
password = 'GyTszUzFv35lkitHMGxMHqoF9sU2ahIk'
host = 'isilo.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()
