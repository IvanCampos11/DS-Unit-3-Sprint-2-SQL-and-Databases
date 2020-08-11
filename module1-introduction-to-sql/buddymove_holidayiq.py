import sqlite3
import pandas as pd


def connect_to_db(db_name='buddymove_holidayiq.sqlite3'):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


# df = pd.read_csv('buddymove_holidayiq.csv')
# df.to_sql('buddymove_holidayiq', connect_to_db())

DATAFRAME = "SELECT * FROM buddymove_holidayiq"
NAT_AND_SHOP_OVER = """SELECT count(Nature) NatureOver100
 FROM  buddymove_holidayiq
 WHERE Nature > 100
 AND Shopping > 100;"""
 

if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()
    # execute_query(curs, DATAFRAME)
    results = execute_query(curs, NAT_AND_SHOP_OVER[0][0])
    print('Number of people who reviewed over 100 in shopping and nature:', results)
