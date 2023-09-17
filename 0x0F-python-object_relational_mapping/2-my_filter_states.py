#!/usr/bin/python3
"""
takes in an argument and displays all values in the states
itable of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = ("SELECT * FROM states "
             "WHERE BINARY name = '{}' ".format(sys.argv[4]))
    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
