#!/usr/bin/env python3

# This is a script that lists all states from the database
import MySQLdb
import sys

if __name__ == "__main__":
    my_host = "localhost"
    port = 3306
    my_user = sys.argv[1]
    my_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host=my_host, port=port, user=my_user,
                         passwd=my_password, db=db_name)

    cursor = db.cursor()

    states = "SELECT states.id, states.name FROM states ORDER BY states.id ASC"

    cursor.execute(states)
    result = cursor.fetchall()

    for res in result:
        print(res)

    cursor.close()
    db.close()
