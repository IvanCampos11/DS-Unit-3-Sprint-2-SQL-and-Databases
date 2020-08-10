import sqlite3


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


TOTAL_UNIQUE_CHARACTERS = """SELECT * FROM charactercreator_character;
SELECT count(*) from charactercreator_character;
SELECT count(distinct name) FROM charactercreator_character;"""

TOTAL_FIGHTER = """SELECT count(*) FROM charactercreator_fighter;"""
TOTAL_CLERIC = """SELECT count(*) FROM charactercreator_cleric;"""
TOTAL_MAGE = """SELECT count(*) FROM charactercreator_mage;"""
TOTAL_THIEF = """SELECT count(*) FROM charactercreator_thief;"""
TOTAL_NECROMANCER = """SELECT count(*) FROM charactercreator_necromancer;"""
TOTAL_ITEMS = """SELECT count(*) FROM armory_item;"""
TOTAL_WEAPON_ITEMS = """SELECT count(*) FROM armory_weapon;"""


if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()
    results = execute_query(curs, TOTAL_FIGHTER)
    results2 = execute_query(curs, TOTAL_CLERIC)
    results3 = execute_query(curs, TOTAL_MAGE)
    results4 = execute_query(curs, TOTAL_THIEF)
    results5 = execute_query(curs, TOTAL_NECROMANCER)
    results6 = execute_query(curs, TOTAL_ITEMS)
    results7 = execute_query(curs, TOTAL_WEAPON_ITEMS)
    print('total fighters: ', results)
    print('total clerics: ', results2)
    print('total mages: ', results3)
    print('total thiefs: ', results4)
    print('total necromancers: ', results5)
    print('total items: ', results6)
    print('total weapons: ', results7)
