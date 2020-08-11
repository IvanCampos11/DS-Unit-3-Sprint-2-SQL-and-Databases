import sqlite3


def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


TOTAL_UNIQUE_CHARACTERS = """SELECT count(distinct name) FROM charactercreator_character;"""

TOTAL_FIGHTER = """SELECT count(*) FROM charactercreator_fighter;"""
TOTAL_CLERIC = """SELECT count(*) FROM charactercreator_cleric;"""
TOTAL_MAGE = """SELECT count(*) FROM charactercreator_mage;"""
TOTAL_THIEF = """SELECT count(*) FROM charactercreator_thief;"""
TOTAL_NECROMANCER = """SELECT count(*) FROM charactercreator_necromancer;"""
TOTAL_ITEMS = """SELECT count(*) FROM armory_item;"""
TOTAL_WEAPON_ITEMS = """SELECT count(*) FROM armory_weapon;"""
AVERAGE_ITEMS_PER_CHARACTER = """SELECT avg((SELECT count(character_id)
FROM charactercreator_character_inventory
GROUP BY character_id)) average_items
FROM charactercreator_character_inventory
"""
AVERAGE_WEAPONS_PER_CHARACTER = """SELECT avg((SELECT count(character_id) FROM armory_weapon
INNER JOIN charactercreator_character_inventory
on item_ptr_id = item_id
GROUP BY item_ptr_id))
FROM armory_weapon
"""
WEAPONS_PER_CHARACTER = """SELECT count(item_ptr_id)
FROM armory_weapon, 
charactercreator_character_inventory
WHERE item_ptr_id = item_id
GROUP BY item_ptr_id
LIMIT 20;
"""
ITEMS_PER_CHARACTER = """SELECT count(cci.item_id)First20ItemsCount
FROM armory_item AS ai,
charactercreator_character_inventory as cci
WHERE ai.item_id = cci.item_id
GROUP BY cci.item_id
LIMIT 20;
"""


if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()
    results = execute_query(curs, TOTAL_UNIQUE_CHARACTERS)
    results1 = execute_query(curs, TOTAL_FIGHTER)
    results2 = execute_query(curs, TOTAL_CLERIC)
    results3 = execute_query(curs, TOTAL_MAGE)
    results4 = execute_query(curs, TOTAL_THIEF)
    results5 = execute_query(curs, TOTAL_NECROMANCER)
    results6 = execute_query(curs, TOTAL_ITEMS)
    results7 = execute_query(curs, TOTAL_WEAPON_ITEMS)
    results8 = execute_query(curs, AVERAGE_ITEMS_PER_CHARACTER)
    results9 = execute_query(curs, AVERAGE_WEAPONS_PER_CHARACTER)
    results10 = execute_query(curs, WEAPONS_PER_CHARACTER)
    results11 = execute_query(curs, ITEMS_PER_CHARACTER)
    print(' ')
    print('Total Unique Characters:', results[0][0])
    print(' ')
    print('Total Fighters:', results1[0][0])
    print('Total Clerics:', results2[0][0])
    print('Total Mages:', results3[0][0])
    print('Total Thiefs:', results4[0][0])
    print('Total Necromancers:', results5[0][0])
    print(' ')
    print('Total Items:', results6[0][0])
    print('Total Weapons:', results7[0][0])
    print(' ')
    print('On Average there are:', results8[0][0], 'Items Per Character')
    print('On Average there are:', results9[0][0], 'Weapons Per Character')
