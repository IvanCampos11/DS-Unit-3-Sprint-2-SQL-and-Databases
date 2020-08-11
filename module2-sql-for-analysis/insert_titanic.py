import pandas as pd
import psycopg2

titanic = pd.read_csv('titanic.csv').rename({
    "Siblings/Spouces Aboard": "Siblings_Spouses_Aboard",
    "Parents/Children Aboard": "Parents_Children_Aboard",
}, axis=1)

titanic['Name'] = titanic['Name'].str.replace("'", "")

dbname = 'ksevjtjp'
user = 'ksevjtjp'
password = 'GyTszUzFv35lkitHMGxMHqoF9sU2ahIk'
host = 'isilo.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()

create_titanic_table = """
DROP TABLE IF EXISTS titanic;
CREATE TABLE titanic (
  Survived INT,
  Pclass INT,
  Name VARCHAR,
  Sex VARCHAR,
  Age FLOAT,
  Siblings_Spouses_Aboard INT,
  Parents_Children_Aboard INT,
  Fare FLOAT
);
"""

if __name__ == "__main__":
    pg_curs.execute(create_titanic_table)
    pg_conn.commit()
    for character in titanic:
        insert_character = """
          INSERT INTO charactercreator_character
          (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard)
          VALUES """ + str(titanic[1:]) + ";"
        pg_curs.execute(insert_character)
    pg_conn.commit()
    pg_curs.close()
    pg_conn.close()
