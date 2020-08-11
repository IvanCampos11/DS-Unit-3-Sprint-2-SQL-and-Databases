import psycopg2
import sqlite3

dbname = 'ksevjtjp'
user = 'ksevjtjp'
password = 'GyTszUzFv35lkitHMGxMHqoF9sU2ahIk'
host = 'isilo.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)

pg_curs = pg_conn.cursor()

create_table_statement = """
CREATE TABLE test_table (
  id SERIAL PRIMARY KEY,
  name varchar(40) NOT NULL,
  data JSONB
);
"""
insert_statement = """
INSERT INTO test_table (name, data) VALUES
(
  'Zaphod Beeblebrox',
  '{"key": "value", "key2": true}'::JSONB
)
"""

get_characters = "SELECT * FROM charactercreator_character;"
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

create_character_table = """
CREATE TABLE charactercreator_character (
  character_id SERIAL PRIMARY KEY,
  name VARCHAR(30),
  level INT,
  exp INT,
  hp INT,
  strength INT,
  intelligence INT,
  dexterity INT,
  wisdom INT
);
"""


if __name__ == "__main__":
    pg_curs.execute(create_table_statement)
    pg_conn.commit()
    pg_curs.execute(insert_statement)
    pg_conn.commit()

    sl_curs.execute(get_characters)
    characters = sl_curs.fetchall()
    sl_curs.execute('PRAGMA table_info(charactercreator_character);')
    sl_curs.fetchall()
    pg_curs.execute(create_character_table)
    pg_conn.commit()
    for character in characters:
        insert_character = """
          INSERT INTO charactercreator_character
          (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
          VALUES """ + str(character[1:]) + ";"
        pg_curs.execute(insert_character)
    pg_conn.commit()
    pg_curs.close()
    pg_conn.close()
    sl_curs.close()
    sl_conn.close()
