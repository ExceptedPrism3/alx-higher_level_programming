#!/usr/bin/python3
''' script that lists all states from the database hbtn_0e_0_usa: '''

import MySQLdb
import sys

if __name__ == '__main__':
    connection = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            database=sys.argv[3])
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM states ORDER BY states.id ASC;')

    states = cursor.fetchall()
    for state in states:
        print(state)
