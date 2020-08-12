import pymongo
import sqlite3

password = 'e'
dbname = 'test'

connection = ('mongodb+srv://e:' + password +
              '@cluster0.1di8a.mongodb.net/' + dbname +
              '?retryWrites=true&w=majority')
client = pymongo.MongoClient(connection)
db = client.test

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

get_characters = 'SELECT * FROM charactercreator_character;'
characters = sl_curs.execute(get_characters).fetchall()

num = 0


if __name__ == "__main__":
    characters = sl_curs.execute(get_characters).fetchall()
    while num < 302:
        rpg_doc = {
            'doc_type': 'rpg_character',
            'sql_key': characters[num][0],
            'name': characters[num][1],
            'level': characters[num][2],
            'exp': characters[num][3],
            'hp': characters[num][4],
            'strength': characters[num][5],
            'intelligence': characters[num][6],
            'dexterity': characters[num][7],
            'wisdom': characters[num][8]
        }
        db.test.insert_one(rpg_doc)
        num = num + 1
