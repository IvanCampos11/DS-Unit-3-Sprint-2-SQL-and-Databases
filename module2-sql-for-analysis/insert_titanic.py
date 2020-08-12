import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

url = 'https://raw.githubusercontent.com/IvanCampos11/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv'

titanic = pd.read_csv(url).rename({
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
)
"""


if __name__ == "__main__":

    titanic = pd.read_csv(url).rename({
        "Siblings/Spouces Aboard": "Siblings_Spouses_Aboard",
        "Parents/Children Aboard": "Parents_Children_Aboard",
    }, axis=1)
    titanic['Name'] = titanic['Name'].str.replace("'", "")

    pg_curs.execute(create_titanic_table)
    pg_conn.commit()
    execute_values(pg_curs, """
    INSERT INTO titanic
    (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard,Parents_Children_Aboard,Fare)
    VALUES %s;
    """, [tuple(row) for row in titanic.values])
    pg_conn.commit()
    pg_curs.close()
    pg_conn.close()
