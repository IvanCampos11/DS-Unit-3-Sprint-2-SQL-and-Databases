import psycopg2

dbname = 'ksevjtjp'
user = 'ksevjtjp'
password = 'GyTszUzFv35lkitHMGxMHqoF9sU2ahIk'
host = 'isilo.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
pg_curs = pg_conn.cursor()


def execute_query(cursor, query):
    pg_curs.execute(query)
    return pg_curs.fetchall()


did_not_survive = 'SELECT count(survived) FROM titanic WHERE survived = 0;'
survived = 'SELECT count(survived) FROM titanic WHERE survived = 1;'
class_one = 'SELECT count(Pclass) FROM titanic WHERE Pclass = 1;'
class_two = 'SELECT count(Pclass) FROM titanic WHERE Pclass = 2;'
class_three = 'SELECT count(Pclass) FROM titanic WHERE Pclass = 3;'

dead_class_one = 'SELECT count(Pclass) FROM titanic WHERE Pclass = 1 AND survived = 0;'
alive_class_one = 'SELECT count(Pclass) FROM titanic WHERE Pclass = 1 AND survived = 1;'
dead_class_two = 'SELECT count(Pclass) FROM titanic WHERE Pclass = 2 AND survived = 0;'
alive_class_two = 'SELECT count(Pclass) FROM titanic WHERE Pclass = 2 AND survived = 1;'
dead_class_three = 'SELECT count(Pclass) FROM titanic WHERE Pclass = 3 AND survived = 0;'
alive_class_three = 'SELECT count(Pclass) FROM titanic WHERE Pclass = 3 AND survived = 1;'

average_survived_age = 'SELECT avg(age) FROM titanic WHERE survived = 1;'
average_dead_age = 'SELECT avg(age) FROM titanic WHERE survived = 0;'

average_dead_age_class_one = 'SELECT avg(age) FROM titanic WHERE survived = 0 AND Pclass = 1;'
average_alive_age_class_one = 'SELECT avg(age) FROM titanic WHERE survived = 1 AND Pclass = 1;'
average_dead_age_class_two = 'SELECT avg(age) FROM titanic WHERE survived = 0 AND Pclass = 2;'
average_alive_age_class_two = 'SELECT avg(age) FROM titanic WHERE survived = 1 AND Pclass = 2;'
average_dead_age_class_three = 'SELECT avg(age) FROM titanic WHERE survived = 0 AND Pclass = 3;'
average_alive_age_class_three = 'SELECT avg(age) FROM titanic WHERE survived = 1 AND Pclass = 3;'


results = execute_query(pg_curs, did_not_survive)
results2 = execute_query(pg_curs, survived)


results3 = execute_query(pg_curs, class_one)
results4 = execute_query(pg_curs, class_two)
results5 = execute_query(pg_curs, class_three)


results6 = execute_query(pg_curs, dead_class_one)
results7 = execute_query(pg_curs, alive_class_one)
results8 = execute_query(pg_curs, dead_class_two)
results9 = execute_query(pg_curs, alive_class_two)
results10 = execute_query(pg_curs, dead_class_three)
results11 = execute_query(pg_curs, alive_class_three)


results12 = execute_query(pg_curs, average_survived_age)
results13 = execute_query(pg_curs, average_dead_age)


result14 = execute_query(pg_curs, average_dead_age_class_one)
result15 = execute_query(pg_curs, average_dead_age_class_one)
result16 = execute_query(pg_curs, average_dead_age_class_two)
result17 = execute_query(pg_curs, average_dead_age_class_two)
result18 = execute_query(pg_curs, average_dead_age_class_three)
result19 = execute_query(pg_curs, average_dead_age_class_three)

if __name__ == "__main__":
    print(' ')
    print('-------------------------------------------------')
    print(' ')
    print(results[0][0], 'people did not survive the titanic.')
    print(results2[0][0], 'people survived the titanic.')
    print(' ')
    print('-------------------------------------------------')
    print(' ')
    print('there are', results3[0][0], 'people in class 1.')
    print(results6[0][0], 'of which died and with an average age of', result14[0][0],
          'while', results7[0][0], 'survived with an average age of', result15[0][0])

    print(' ')
    print('there are', results4[0][0], 'people in class 2.')
    print(results8[0][0], 'of which died and with an average age of', result16[0][0],
          'while', results9[0][0], 'survived with an average age of', result17[0][0])

    print(' ')
    print('there are', results5[0][0], 'people in class 3.')
    print(results10[0][0], 'of which died and with an average age of', result18[0][0],
          'while', results11[0][0], 'survived with an average age of', result19[0][0])

    print(' ')
    print('-------------------------------------------------')
    print(' ')
    print('the average age for the survivers:', results12[0][0])
    print('the average age for the dead passengers:', results13[0][0])
    print(' ')
    print('-------------------------------------------------')
    print(' ')

    # the rest of the questions are repetitive and i know
    # i have a good understanding of today's assignment.
    # I made it into a somewhat pretty format so
    # i hope that will make up for it.
